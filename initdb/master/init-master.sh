#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create replication user and slot
echo "Creating replication user and slot..."
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<EOSQL
DO \$\$
DECLARE
    slave_user TEXT;
    slave_password TEXT;
BEGIN
    slave_user := current_setting('postgres.slave.user');
    slave_password := current_setting('postgres.slave.password');

    -- Create replication user
    EXECUTE format(
        'CREATE USER %I WITH REPLICATION LOGIN ENCRYPTED PASSWORD %L',
        slave_user,
        slave_password
    );

    -- Create replication slot
    PERFORM pg_create_physical_replication_slot('replication_slot');
END;
\$\$;
EOSQL


cp -r /var/lib/postgresql/certs/* /var/lib/postgresql/certs_export/
