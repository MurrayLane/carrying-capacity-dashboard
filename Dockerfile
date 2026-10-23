# Stage 1: compile the servlet and assemble ROOT.war
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /build
COPY pom.xml .
RUN mvn -q -B dependency:go-offline
COPY src ./src
RUN mvn -q -B package

# Stage 2: run it on the official Tomcat 9 image
FROM tomcat:9.0-jre21-temurin
# Default webapps (docs, examples, manager) are not wanted; the dashboard is served at /
RUN rm -rf /usr/local/tomcat/webapps/* /usr/local/tomcat/webapps.dist
COPY --from=build /build/target/ROOT.war /usr/local/tomcat/webapps/ROOT.war
ENV JAVA_OPTS="-XX:MaxRAMPercentage=75"
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=5s --start-period=40s \
  CMD curl -fsS http://localhost:8080/ > /dev/null || exit 1
