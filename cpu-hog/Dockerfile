FROM alpine:latest

CMD while true; do for i in $(seq 1 10000); do test $(factor $i | wc -w) -eq 2 && echo $i; done; done
