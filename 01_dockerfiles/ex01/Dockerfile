FROM debian

ENV TS3SERVER_LICENSE accept

RUN apt update -y \
    && apt install -y wget bzip2 \
    && wget https://files.teamspeak-services.com/releases/server/3.8.0/teamspeak3-server_linux_amd64-3.8.0.tar.bz2 \
    && tar xfv teamspeak3-server_linux_amd64-3.8.0.tar.bz2 

WORKDIR /teamspeak3-server_linux_amd64

EXPOSE 9987/udp 10011 30033

ENTRYPOINT sh ts3server_minimal_runscript.sh

# docker build -t ex01 .
# docker container run --rm -p 9987:9987/udp -p 10011:10011 -p 30033:30033 ex01
# loging with ip:9987
# teamspeak client will ask for priviledge key, it's in the server log "token=..."
