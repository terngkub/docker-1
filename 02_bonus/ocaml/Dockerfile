FROM ubuntu:18.04

RUN apt update
RUN apt install -y make
RUN apt install -y ocaml

WORKDIR /app
COPY app .

RUN make

CMD ["./tic_tac_toe"]

# docker build -t tic-tac-toe .
# docker run -it --rm tic-tac-toe