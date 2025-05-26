docker build -t mymedic:master .

docker run -it --rm -v sqlite:/sqlite mymedic:master python manage.py createsuperuser

docker run -it --rm -v sqlite:/sqlite mymedic:master python manage.py runserver 0.0.0.0:8000

docker run -it --rm -p 8000:8000 -v sqlite:/sqlite -v %cd%\website:/usr/src/website mymedic:master python manage.py runserver 0.0.0.0:8000

docker run --rm mymedic:master ./pytest.sh