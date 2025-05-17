# GetActive Local Development Database

This directory contains the MySQL database configuration for local development. The database container will automatically execute the `01-init.sql` script upon startup to create and initialize database tables.

## Quick Start

### 1. Build Database Container

```bash
# Execute in the database directory
docker build -t getactive-db .
```

### 2. Start Database Container

```bash
docker run -d \
  --name getactive-db \
  -p 3306:3306 \
  getactive-db
```

## Database Configuration

- Database Name: `getactive`
- Username: `root`
- Password: `password`
- Port: `3306`

## Modifying Database Schema

If your feature requires changes to the database schema (adding, removing, or modifying tables/columns), simply:

1. Edit the `01-init.sql` file
2. Add or modify the corresponding SQL statements
3. Rebuild and restart the database container:
   ```bash
   # Stop and remove the old container
   docker rm -f getactive-db
   
   # Rebuild and start
   docker build -t getactive-db .
   docker run -d --name getactive-db -p 3306:3306 getactive-db
   ```

## Connecting with MySQL Workbench

1. Open MySQL Workbench
2. Create a new connection:
   - Hostname: `localhost`
   - Port: `3306`
   - Username: `root`
   - Password: `password`

## Important Notes

1. This is a development environment database, not for production use
2. Schema changes require container rebuild
3. Container data is temporary and will be lost when container is removed
4. Add Docker volume if data persistence is needed
5. Ensure port 3306 is not in use

## Troubleshooting

If you encounter issues:

1. Port Conflict
   ```bash
   # Check if port 3306 is in use
   lsof -i :3306
   ```

2. Container Won't Start
   ```bash
   # View detailed logs
   docker logs getactive-db
   ```

3. Cannot Connect to Database
   - Verify container is running
   - Check port mapping
   - Review firewall settings
