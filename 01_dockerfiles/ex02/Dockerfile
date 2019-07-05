FROM ruby

RUN apt update
RUN apt install -y nodejs
RUN gem install rails

ONBUILD COPY  app /opt/app
ONBUILD WORKDIR /opt/app

ONBUILD RUN bundle install
ONBUILD RUN bundle exec rake db:migrate
ONBUILD RUN bundle exec rake db:seed

# docker build -t ft-rails:onbuild .
# cd test
# docker build -t ex02 .
# docker run --rm ex02
