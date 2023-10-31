FROM python:3.12

RUN apt-get update && apt-get install -y vim

WORKDIR /app

VOLUME ["/app"]

CMD ["/bin/bash"]