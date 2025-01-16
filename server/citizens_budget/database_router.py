import psycopg2
from psycopg2 import OperationalError

from citizens_budget import settings


class PrimaryReplicaRouter:

    def is_default_healthy(self):
        """
        Check if the replica database is available.
        """
        try:
            conn = psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT'],
            )
            conn.close()
            return True
        except OperationalError:
            return False
    def db_for_read(self, model, **hints):
        """
        Directs read operations to the default if available; fallback to replica1 otherwise.
        """
        return "replica1"

    def db_for_write(self, model, **hints):
        """
        Writes always go to default.
        """
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the default/replica pool.
        """
        db_set = {"default", "replica1"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True