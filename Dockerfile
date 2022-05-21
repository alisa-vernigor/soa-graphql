FROM python:latest

RUN apt-get update
RUN pip install 'strawberry-graphql[debug-server]'

WORKDIR /soa-graphql

COPY schema.py ./

EXPOSE 8000

CMD ["/bin/bash",  "-c", "strawberry server schema"]