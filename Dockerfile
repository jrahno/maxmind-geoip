FROM debian:bullseye

USER root

# Set Environment Variables
ENV DEBIAN_FRONTEND noninteractive

# install basic components
RUN apt-get -y update -qq && apt-get -y install wget curl python3 pip

# download & install geoip deb package
RUN wget https://github.com/maxmind/geoipupdate/releases/download/v7.0.1/geoipupdate_7.0.1_linux_amd64.deb
RUN dpkg -i geoipupdate_7.0.1_linux_amd64.deb

# copy api script to image
COPY geoip /geoip
COPY api.sh /
COPY geoip_update /etc/cron.d/
COPY geoip/GeoIP.conf /etc/

# update geoip DB
RUN /usr/bin/geoipupdate -d /geoip/

# prepare python env
RUN cd /geoip
RUN pip install pipenv
RUN pipenv --python 3.9
RUN pipenv install flask geoip2

EXPOSE 5000/tcp

ENTRYPOINT ["/api.sh"]