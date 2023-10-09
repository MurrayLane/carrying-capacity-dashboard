FROM tomcat:8.5

EXPOSE 8080

COPY source/ /usr/local/tomcat/
RUN rm -rf /usr/local/tomcat/webapps.dist
