 
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

### 3. Run the Server

#### Run in Production Mode

```bash
docker compose up --build
```

This binds the local website code into the container and serves it at `http://localhost:8080`.