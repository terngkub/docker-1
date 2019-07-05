FROM ubuntu:18.04

RUN apt update
RUN apt install -y vim
RUN apt install -y zsh
RUN apt install -y curl
RUN apt install -y git
RUN sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

CMD ["zsh"]

# docker build -t ubuntu-base .
# docker run -it --rm ubuntu-base