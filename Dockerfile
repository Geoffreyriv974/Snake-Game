FROM ubuntu:latest
LABEL authors="geoffrey"

ENTRYPOINT ["top", "-b"]