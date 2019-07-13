FROM ruby

RUN apt update
RUN apt install -y nodejs
RUN gem install rails

ONBUILD COPY  app /opt/app
ONBUILD WORKDIR /opt/app

ONBUILD RUN bundle install
ONBUILD RUN bundle exec rake db:migrate
ONBUILD RUN bundle exec rake db:seed

# docker build -t ft-rails:on-build .
# cd test
# docker build -t ex02 .
# docker run --rm -it -p 3000:3000 ex02
# access the site with ip:3000
