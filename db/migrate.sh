#!/bin/bash

# Load environment variables
source ../.env

# Directory containing migration scripts
MIGRATIONS_DIR=migrations

echo "Running migrations..."

for file in $MIGRATIONS_DIR/*.sql
do
    echo "Applying migration: $file"
    psql PGPASSOWRD=$DB_PASSWORD -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -a -f $file
done

echo "Migrations completed."
