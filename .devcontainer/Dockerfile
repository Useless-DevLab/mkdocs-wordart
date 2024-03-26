FROM debian:11

ARG TASK_VERSION=3.32.0

USER root

### Task (https://taskfile.dev/) ###
RUN wget -P /tmp https://github.com/go-task/task/releases/download/v$TASK_VERSION/task_linux_amd64.deb && \
    dpkg -i /tmp/task_linux_amd64.deb && \
    rm -f /tmp/task_linux_amd64.deb
