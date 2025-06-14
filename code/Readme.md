 
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
---

### 3. Build the Docker Image

```bash
docker build -t mymedic .
```

---

### 4. Run the Server

#### Running Tests
```bash
docker run --rm mymedic pytest -v tests/
```

#### Run in Development Mode

```bash
docker compose -f docker-compose-dev.yml up -d
```

#### Run in Production Mode

```bash
docker compose up -d
```

This binds the local website code into the container and serves it at `http://127.0.0.1:8080`.
