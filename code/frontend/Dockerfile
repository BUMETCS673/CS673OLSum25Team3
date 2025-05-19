FROM node:18-alpine as builder

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm ci

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Output stage - this stage is just for copying the build output
FROM alpine:latest

# Create a directory for the build output
WORKDIR /build-output

# Copy only the built files from the builder stage
COPY --from=builder /app/dist ./dist

# This image doesn't need to run anything
# It's just a way to pass the build output to other images
