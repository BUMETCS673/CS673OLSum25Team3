
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

Edit `.env` with appropriate development values as needed. Do not commit your `.env` file.

---

### 3. Build the Docker Image

```bash
docker build -t mymedic:master .
```

---

### 4. Apply Migrations

```bash
docker run -it --rm -v sqlite:/sqlite mymedic:master python manage.py migrate
```

---

### 5. Create a Superuser (optional)

```bash
docker run -it --rm -v sqlite:/sqlite mymedic:master python manage.py createsuperuser
```

---

### 6. Run the Development Server

```bash
docker run -it --rm -p 8000:8000 -v sqlite:/sqlite -v %cd%\website:/usr/src/website mymedic:master python manage.py runserver 0.0.0.0:8000
```

This binds the local website code into the container and serves it at `http://localhost:8000`.

---

### 7. Run Tests

```bash
docker run --rm mymedic:master ./pytest.sh
```

---
