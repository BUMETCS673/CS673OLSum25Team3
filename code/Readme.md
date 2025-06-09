
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

Edit `.env` and add a DJANGO_SECRET_KEY generated from [Django Secret Key Generator](https://djecrety.ir/), and also the email settings if you plan to use email features, which is necessary for password reset functionality.

---

### 3. Build the Docker Image and create the SQLite volume

```bash
docker build -t mymedic:master . 
``` 

```bash
docker volume create sqlite-data
```

---

### 4. Run the Development Server

#### Windows:
```bash
docker run --rm --env-file .env -v "%cd%":/app -v sqlite-data:/sqlite -p 8080:80 mymedic:master
```

#### MacOS:
```bash
docker run --rm --env-file .env -v "$(pwd)":/app -v sqlite-data:/sqlite -p 8080:80 mymedic:master
```

This binds the local website code into the container and serves it at `http://localhost:8080`.

---

### 5. Run the Development Server (Through Docker Compose)

```bash
docker compose up --build
```

This version of the code is designed to run without the Django debug server, and has set up Gunicorn as the WSGI server. It is suitable for production use, but can also be used for development purposes.

What’s New: I’ve overhauled the entire user authentication and deployment workflow: login bugs are fixed and responses now include a clear "role" flag; I introduced a ProviderProfile model and full signup flow for healthcare providers (in addition to patients); password resets send real email links (console backend in DEBUG, SMTP in production); signup and reset forms have stronger validation; the validate-token endpoint now returns role information so the frontend can branch UI accordingly; all statics are served by Nginx instead of the dev server; and the Docker setup is simplified into a production-ready Gunicorn + Nginx container (with an optional Compose multi-container configuration).

---
