FROM 755674844232.dkr.ecr.us-east-1.amazonaws.com/spark/emr-6.7.0 AS base

USER root

RUN yum install -y maven
RUN mvn install:install-file \
   -Dfile=/usr/lib/spark/jars/spark-sql_2.12-3.2.1-amzn-0.jar \
   -DgroupId=org.apache.spark \
   -DartifactId=spark-sql_2.12 \
   -Dversion=3.2.1-amzn-0 \
   -Dpackaging=jar \
   -DgeneratePom=true

WORKDIR /app
COPY . .

RUN mvn package

FROM scratch AS export
COPY --from=base /app/target/simple-project-1.0.jar /