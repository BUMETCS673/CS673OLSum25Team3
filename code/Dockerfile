FROM python:3.13-alpine

RUN apk update \
 && apk add --no-cache \
      gcc musl-dev python3-dev libffi-dev openssl-dev \
      nginx su-exec

RUN mkdir -p /usr/src/mymedic /sqlite /var/run/nginx
WORKDIR /usr/src/mymedic

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

RUN adduser -D -u 1001 user \
 && chown -R user:user /usr/src/mymedic /sqlite \
 && chmod +x /usr/src/mymedic/docker-entrypoint.sh \
              /usr/src/mymedic/docker-cmd.sh

EXPOSE 80 8000

ENTRYPOINT ["/usr/src/mymedic/docker-entrypoint.sh"]
CMD ["/usr/src/mymedic/docker-cmd.sh"]
