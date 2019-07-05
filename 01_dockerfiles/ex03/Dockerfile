FROM ubuntu

# install dependencies
RUN apt update -y
RUN apt install -y ca-certificates curl openssh-server postfix tzdata

# install gitlab
RUN curl -LO https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh \
    && bash script.deb.sh \
    && rm script.deb.sh
RUN apt install -y gitlab-ce

# gitlab, nginx and sshd settings
RUN printf "external_url 'https://gitlab.example.com'\nnginx['redirect_http_to_https'] = true\nnginx['ssl_certificate'] = '/etc/gitlab/ssl/gitlab.example.com.crt'\nnginx['ssl_certificate_key'] = '/etc/gitlab/ssl/gitlab.example.com.key'" > /etc/gitlab/gitlab.rb
RUN echo "AuthorizedKeysFile	/var/opt/gitlab/.ssh/authorized_keys" >> /etc/ssh/sshd_config

# create ssl certificate
RUN mkdir -p /etc/gitlab/ssl \
    && chmod 700 /etc/gitlab/ssl
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/gitlab/ssl/gitlab.example.com.key -out /etc/gitlab/ssl/gitlab.example.com.crt -subj "/C=FR/CN=gitlab.example.com"

# reconfigure gitlab
RUN (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure

EXPOSE 80 443 22

ENTRYPOINT (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure && service ssh start && tail -f /dev/null