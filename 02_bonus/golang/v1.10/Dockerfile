FROM golang:1.10

WORKDIR /go/src/app
COPY app .

RUN go get -d -v ./...
RUN go install -v ./...

CMD ["app"]

# docker build -t go-v1.10 .
# docker run --rm go-v1.10