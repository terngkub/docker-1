FROM ubuntu:18.04

# install dependencies
RUN apt update -y
RUN apt install -y ca-certificates curl openssh-server postfix tzdata

# install gitlab
RUN curl -LO https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh \
    && bash script.deb.sh \
    && rm script.deb.sh
RUN apt install -y gitlab-ce

# gitlab, nginx and sshd settings
# https://docs.gitlab.com/omnibus/settings/nginx.html
RUN printf "external_url 'https://192.168.99.100'\nnginx['redirect_http_to_https'] = true\nnginx['ssl_certificate'] = '/etc/gitlab/ssl/gitlab.example.com.crt'\nnginx['ssl_certificate_key'] = '/etc/gitlab/ssl/gitlab.example.com.key'" > /etc/gitlab/gitlab.rb
RUN echo "AuthorizedKeysFile	/var/opt/gitlab/.ssh/authorized_keys" >> /etc/ssh/sshd_config

# create ssl certificate
RUN mkdir -p /etc/gitlab/ssl \
    && chmod 700 /etc/gitlab/ssl
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/gitlab/ssl/gitlab.example.com.key -out /etc/gitlab/ssl/gitlab.example.com.crt -subj "/C=FR/CN=gitlab.example.com" && openssl rsa -in /etc/gitlab/ssl/gitlab.example.com.key -out /etc/gitlab/ssl/gitlab.example.com.key

EXPOSE 80 443 22

ENTRYPOINT (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure && service ssh start && tail -f /dev/null

# docker build -t ex03 .
# docker container run -p 80:80 -p 443:443 -p 8022:22 --name gitlab ex03

# access site
# https://192.168.99.100
# http://192.168.99.100 will be redirect to https

# test ssh
# 1. log in and create project
# 2. add ssh key to gitlab
#    in host: ssh ~/.ssh/id_rsa.pub
# 3. git clone ssh://git@192.168.99.100:8022/root/project

# test https
# 1. disable git certificate verify to don't have to copy certificate to host 
#    git config --global http.sslVerify false
# 2. git clone https://192.168.99.100/root/project
# 3. re-enable certificate verification
#    git config --global http.sslVerify true
