# Java Build Dependency with EMR Spark Artifacts

You can use the EMR on EKS container image to build a Java project against EMR artifacts.

This particular example shows adding `spark-sql` dependencies to your maven repo to address a Spark SQL regresion.

## Overview

This example uses EMR 6.7.0 in us-east-1 - make sure you login to ECR for the [account and region you are using](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-tag.html) before proceeding.

```shell
aws ecr get-login-password --region us-east-1 \
        | docker login \
            --username AWS \
            --password-stdin \
            755674844232.dkr.ecr.us-east-1.amazonaws.com
```

The included [`Dockerfile`](./Dockerfile) replaces the standard artifacts using local jars.

## Testing

Tests can be run by building the `test` target.

```shell
docker build -t emr-java-demo/test . --target test
```

By providing the `-t` flag, you can run a shell with the resulting image if you need.

```shell
docker run --rm -it emr-java-demo/test /bin/bash    
```

## Building

The following command will build and copy your jar file to the `dist/` directory.

> **Note** `DOCKER_BUILDKIT` ensures that Docker BuildKit backend is enabled in order for the `--output` flag to work.

```shell
DOCKER_BUILDKIT=1 docker build --output dist .
```