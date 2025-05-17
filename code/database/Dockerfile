FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=getactive

COPY 01-init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
  CMD mysqladmin ping -h localhost -u root -p${MYSQL_ROOT_PASSWORD} || exit 1
