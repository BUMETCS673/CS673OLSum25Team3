 
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/BUMETCS673/CS673OLSum25Team3.git
cd CS673OLSum25Team3
```

---

### 2. Copy and Configure the Environment File

```bash
cp .env.example .env
```

Edit `.env` and add a DJANGO_SECRET_KEY generated from [Django Secret Key Generator](https://djecrety.ir/).
Add the email and app passwords for the Gmail account.

---

### 3. Run the Server

If Docker gives an error about permissions for executing docker-cmd or docker-entrypoint, run the following command to fix it:

```bash
chmod +x docker-cmd.sh
chmod +x docker-entrypoint.sh
```

#### Run in Production Mode

```bash
docker compose up --build --force-recreate
```

This binds the local website code into the container and serves it at `http://localhost:8080`.

#### To remove old containers and images, run:

```bash
docker compose down -v --remove-orphans
```

---