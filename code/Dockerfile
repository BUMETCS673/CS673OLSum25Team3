FROM python:3.13-alpine

RUN apk update && apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev nginx su-exec

RUN mkdir -p /app /sqlite /var/run/nginx
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY nginx.conf /etc/nginx/nginx.conf

RUN adduser -D -u 1001 user \
 && chown -R user:user /app /sqlite \
 && chmod +x /app/docker-entrypoint.sh /app/docker-cmd.sh

EXPOSE 80 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["/app/docker-cmd.sh"]
