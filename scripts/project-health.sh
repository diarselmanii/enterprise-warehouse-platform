#!/bin/bash

set -euo pipefail

PROJECT_NAME="Enterprise Warehouse Platform"
PROJECT_DIR="$HOME/enterprise-warehouse-platform"
APP_ENV="development"

echo "========================================="
echo "$PROJECT_NAME"
echo "PROJECT HEALTH CHECK"
echo "========================================="

echo "Environment: $APP_ENV"
echo "Project path: $PROJECT_DIR"

echo ""
echo "Checking project directories..."

for directory in app/api app/worker app/database app/tests docker infrastructure/terraform kubernetes helm scripts docs
do
    if [ -d "$PROJECT_DIR/$directory" ]; then
	echo "[OK] $directory exists"
    else
	echo "[ERROR] $directory is missing"
    fi
done

echo ""
echo "Checking project files..."

for file in README.md .gitignore docker-compose.yaml
do
    if [ -f "$PROJECT_DIR/$file" ]; then
	echo "[OK] $file exists"
    else
	echo "[ERROR] $file is missing"
    fi
done

echo ""
echo "Project health check completed!"




















