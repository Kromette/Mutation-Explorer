#!/bin/bash

set -e

# Configuration PostgreSQL Docker
HOST="127.0.0.1"
PORT="5432"
USER="fireprot"
DATABASE="fireprotdb"
PASSWORD="fireprot"

# Chemin du dump FireProtDB
DUMP_FILE="/Users/aline/Documents/Mutation-Explorer/data/raw/fireprotdb_dump_2025_09_22/01_fireprotdb_2025-09-20.sql"

echo "======================================"
echo "Restauration FireProtDB"
echo "======================================"

# Vérification du fichier dump
if [ ! -f "$DUMP_FILE" ]; then
    echo "Erreur : dump introuvable :"
    echo "$DUMP_FILE"
    exit 1
fi

echo "Dump trouvé :"
echo "$DUMP_FILE"

# Test connexion PostgreSQL
echo ""
echo "Test connexion PostgreSQL..."

PGPASSWORD=$PASSWORD psql \
    -h $HOST \
    -p $PORT \
    -U $USER \
    -d $DATABASE \
    -c "SELECT version();"

echo ""
echo "Début restauration..."

PGPASSWORD=$PASSWORD psql \
    -h $HOST \
    -p $PORT \
    -U $USER \
    -d $DATABASE \
    -v ON_ERROR_STOP=1 \
    -f "$DUMP_FILE"

echo ""
echo "Restauration terminée."

echo ""
echo "Vérification des tables..."

PGPASSWORD=$PASSWORD psql \
    -h $HOST \
    -p $PORT \
    -U $USER \
    -d $DATABASE \
    -c "\dt"

echo ""
echo "FireProtDB est prête."