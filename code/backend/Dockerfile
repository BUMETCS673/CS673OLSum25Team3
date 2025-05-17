# Start from a Java image
FROM eclipse-temurin:17-jdk as builder

# Set working directory inside 
WORKDIR /app

# Copy Gradle wrapper and build files
COPY getactivecore/gradlew getactivecore/build.gradle getactivecore/settings.gradle /app/
COPY getactivecore/gradle /app/gradle
RUN ./gradlew --no-daemon bootJar || return 0  # build fails if no source yet

# Copy source
COPY getactivecore/src /app/src

# Build the application
RUN ./gradlew clean bootJar --no-daemon


# ---- runtime image ----
FROM eclipse-temurin:17-jdk

WORKDIR /app

# Copy the built JAR from the builder
COPY --from=builder /app/build/libs/*.jar app.jar

# Port the server listens at
EXPOSE 3232

CMD ["java", "-jar", "app.jar"]
