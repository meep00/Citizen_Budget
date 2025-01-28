#!/bin/sh

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

PGPASSWORD=${POSTGRES_PASSWORD} pg_dump -h master -U ${POSTGRES_USER} ${POSTGRES_DB} > /backups/backup_$DATE.sql

echo "Backup created: /backups/backup_$DATE.sql"
