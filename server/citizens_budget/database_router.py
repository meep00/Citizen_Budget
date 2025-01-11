import psycopg2
from psycopg2 import OperationalError

from citizens_budget import settings


class PrimaryReplicaRouter:

    def is_primary_healthy(self):
        """
        Check if the replica database is available.
        """
        try:
            conn = psycopg2.connect(
                dbname=settings.DATABASES['primary']['NAME'],
                user=settings.DATABASES['primary']['USER'],
                password=settings.DATABASES['primary']['PASSWORD'],
                host=settings.DATABASES['primary']['HOST'],
                port=settings.DATABASES['primary']['PORT'],
            )
            conn.close()
            return True
        except OperationalError:
            return False
    def db_for_read(self, model, **hints):
        """
        Directs read operations to the primary if available; fallback to replica1 otherwise.
        """
        if self.is_primary_healthy():
            return 'primary'
        else:
            return 'replica1'

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return "primary"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {"primary", "replica1"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True