FROM 755674844232.dkr.ecr.us-east-1.amazonaws.com/spark/emr-6.7.0 AS base

USER root

RUN yum install -y maven

WORKDIR /app
RUN chown hadoop /app

USER hadoop

# This required a bit of guess and chekc - spark-sql require catalyst and core
RUN for package in spark-sql spark-catalyst spark-core; do \
   mvn install:install-file \
      -Dfile=/usr/lib/spark/jars/${package}_2.12-3.2.1-amzn-0.jar \
      -DgroupId=org.apache.spark \
      -DartifactId=${package}_2.12 \
      -Dversion=3.2.1 \
      -Dpackaging=jar \
      -DgeneratePom=false; \
   done

COPY --chown=hadoop:hadoop src ./src
COPY --chown=hadoop:hadoop pom.xml .

FROM base AS package
RUN mvn package

FROM base AS test
RUN mvn test

FROM scratch AS export
COPY --from=package /app/target/simple-project-1.0.jar /