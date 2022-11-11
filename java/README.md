# Java Build Dependency with EMR Spark Artifacts

You can use the EMR on EKS container image to build a Java project against EMR artifacts.

## Overview

This example uses EMR 6.7.0 in us-east-1 - make sure you login to ECR for the [account and region you are using](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/docker-custom-images-tag.html) before proceeding.

```shell
aws ecr get-login-password --region us-east-1 \
        | docker login \
            --username AWS \
            --password-stdin \
            755674844232.dkr.ecr.us-east-1.amazonaws.com
```

Make sure you specify the `amzn` artifact (`3.2.1-amzn-0`) in your `pom.xml`. The included [`Dockerfile`](./Dockerfile) installs the local jar files before doing a `mvn package`.

## Building

The following command will build and copy your jar file to the `dist/` directory.

> **Note** `DOCKER_BUILDKIT` ensures that Docker BuildKit backend is enabled in order for the `--output` flag to work.

```shell
DOCKER_BUILDKIT=1 docker build --output dist .
```