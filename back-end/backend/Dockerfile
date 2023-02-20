FROM openjdk:17-jdk-alpine
VOLUME /tmp
# 포트
EXPOSE 8081
FROM openjdk:11
ARG JAR_FILE=target/inburger.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
