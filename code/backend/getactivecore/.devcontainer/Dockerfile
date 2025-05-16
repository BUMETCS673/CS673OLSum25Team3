# Base image with Java, Node.js, and Gradle
FROM mcr.microsoft.com/devcontainers/java:1-17-bullseye

# Install Node.js (16.x or LTS)
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Install yarn (optional)
# RUN npm install -g yarn

# Install gradle
ENV GRADLE_VERSION=8.5
RUN wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -P /tmp && \
    unzip -d /opt/gradle /tmp/gradle-${GRADLE_VERSION}-bin.zip && \
    ln -s /opt/gradle/gradle-${GRADLE_VERSION}/bin/gradle /usr/bin/gradle

# Verify Gradle
RUN gradle --version

# Create a non-root user
# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

# Set default working directory
WORKDIR /workspace
