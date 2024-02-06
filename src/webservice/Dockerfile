FROM golang:1.21-alpine AS build
WORKDIR /app

COPY . .
RUN go mod download

RUN CGO_ENABLED=0 GOOS=linux go build -o /build ./cmd/main.go

FROM alpine:3 AS release
WORKDIR /app

RUN apk add tesseract-ocr

COPY /config.toml .
COPY --from=build /build ./build

EXPOSE 8080

ENTRYPOINT [ "/app/build" ]