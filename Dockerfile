FROM python:3.12-slim

WORKDIR /nazarenko

COPY . /nazarenko

ENV STUDENT_SURNAME=Nazarenko

CMD ["/bin/bash"]