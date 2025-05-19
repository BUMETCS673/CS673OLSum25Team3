FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git  \
    sqlite3 libsqlite3-dev libpq-dev libffi-dev libssl-dev \
    nodejs npm

# Create a user and group to run the application
RUN groupadd -g 10000 mymedic && \
    useradd -u 10000 -g mymedic -m mymedic

# Copy the application code and fix user permissions
COPY --chown=mymedic:mymedic mymedic-backend/ /home/mymedic/mymedic-backend/
COPY --chown=mymedic:mymedic mymedic-frontend/ /home/mymedic/mymedic-frontend/
RUN chown -R mymedic:mymedic /home/mymedic/
RUN chmod -R u+w /home/mymedic/

# Set environment variables
ENV DEFAULT_RECEIVER_IP="host.docker.internal" \
    DEFAULT_SENDER_IP="0.0.0.0" \
    DEFAULT_CLIENT_PORT=5000 \
    DEFAULT_BACKEND_PORT=5001 \
    DEFAULT_FRONTEND_PORT=5002 \
    DEFAULT_DB_PORT=5003

# Set the working directory and user
WORKDIR /home/mymedic
USER mymedic

# Create a virtual environment and install dependencies for backend
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    cd mymedic-backend && \
    pip install -e .

# Expose the application port, where data is sent to the client
EXPOSE 5000

# Start the application
CMD ["bash", "-c", ". venv/bin/activate && run-mymedic"]
