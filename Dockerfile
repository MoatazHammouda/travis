# Dockerfiles MUST begin with a FROM command, which specifies a base image, can be OS specific/language-specific.
FROM python:3.8-alpine
LABEL maintainer="moahammo@cisco.com"

RUN pip install --upgrade pip &&\
    pip install flask

WORKDIR /src

EXPOSE 5000/TCP

ENTRYPOINT ["python"]
CMD ["start.py"]