# Continuous Integration (CI) Workflow

This document describes the automated CI workflow for the GetActive project.

## Overview

Our CI pipeline runs automatically on every push and pull request to any branch. It performs integrated testing across both backend and frontend components to ensure code quality and functionality.

## Workflow Steps

1. **Environment Setup**
   - Runs on Ubuntu latest
   - Spins up a MySQL 8.0 database service for testing

2. **Database Initialization**
   - Initializes the MySQL database with required schema and test data

3. **Backend Testing & Deployment**
   - Sets up JDK 17 and Gradle
   - Runs backend unit tests with connection to the test database
   - Builds the backend application (excluding tests)
   - Starts the backend service and verifies health check endpoint

4. **Frontend Testing**
   - Sets up Node.js 18 with npm caching
   - Installs frontend dependencies
   - Runs frontend unit tests

## Running Locally

To run the CI workflow locally before pushing:

1. After cloning the repository, please run the following command to enable the project's Git hooks:`chmod +x .githooks/pre-commit && git config core.hooksPath .githooks`
2. Start a MySQL database: `cd ./code/database && docker build -t getactive-db . && docker run -d --name getactive-mysql -p 3306:3306 getactive-db`
3. Database management tool: MySQLWorkbench. username: root, password: password
4. Run backend tests: `./gradlew test`
5. Build backend: `./gradlew build -x test`
6. Start backend service: `java -jar build/libs/getactivecore-0.0.1-SNAPSHOT.jar` and verify health check at http://localhost:3232/v1/health
7. Run frontend tests: `npm run test`

## Troubleshooting

If the CI workflow fails:
- Check backend logs for service startup issues
- Verify database connection settings
- Ensure all tests pass locally before pushing

## GitHub Actions Configuration

The detailed configuration can be found in `.github/workflows/ci.yml`.