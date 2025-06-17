 
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

You will need to have another email account ready (not the one you sign up with), along with it's [app password](https://support.google.com/accounts/answer/185833?hl=en), in order for MFA/Reset password to work.
They will need to be set in the .env file. The .env file can be provided for the purposes of the demo.

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
