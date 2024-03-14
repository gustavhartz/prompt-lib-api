#!/bin/bash

# Load environment variables
source ../.env

# Directory containing seed scripts
SEEDS_DIR=seeds

echo "Seeding database..."

for file in $SEEDS_DIR/*.sql
do
    echo "Seeding: $file"
    psql -h $DB_HOST -U $DB_USER -d $DB_NAME -p $DB_PORT -a -f $file
done

echo "Database seeded."
