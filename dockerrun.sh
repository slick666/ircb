#!/usr/bin/env bash

# Wait for postgres to become available
until nc -z postgres 5432; do
    echo "$(date) - waiting for postgres..."
    sleep 1
done

/usr/local/bin/ircb runserver
