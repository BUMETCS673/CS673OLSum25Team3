# Directory Contents
This folder contains all source code and test code.

# MyMedic Container Usage
Once cloned to your machine, run `docker compose up` to create the containers and 
volume. The volume is used to store the persistent data for the database. The
frontend and backend run in one container (mymedic-app) and command line access to
the database is maintained with the database container (mymedic-db)

Once the docker containers are running, you may access the MyMedic App frontend at
`https://localhost:8080`

