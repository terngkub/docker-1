FROM golang:1.12

WORKDIR /app
COPY app .

RUN go build -o app

CMD ["./app"]

# docker build -t go-v1.12 .
# docker run --rm go-v1.12