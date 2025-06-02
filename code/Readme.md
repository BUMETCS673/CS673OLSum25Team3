
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

####Windows:
```bash
docker run -it --rm -p 8000:8000 -v sqlite:/sqlite -v %cd%\website:/usr/src/website mymedic:master python manage.py runserver 0.0.0.0:8000
```

####MacOS:
```bash
docker run -it --rm -p 8000:8000 -v sqlite:/sqlite -v $(pwd)/website:/usr/src/website mymedic:master python manage.py runserver 0.0.0.0:8000
```

This binds the local website code into the container and serves it at `http://127.0.0.1:8080`.

---

### 7. Run Tests

```bash
docker run --rm mymedic:master pytest -v tests/

```

---
