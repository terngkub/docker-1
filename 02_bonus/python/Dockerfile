FROM ubuntu:18.04

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
ENV DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN apt install -y tzdata
RUN apt install -y python3-tk

WORKDIR /npuzzle
COPY npuzzle .

ENTRYPOINT ["python3", "main.py"]

# docker build -t npuzzle .
# docker run -it --rm npuzzle -f puzzles/3s