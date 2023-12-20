FROM php:8.2.13-cli-bullseye
LABEL authors="Heelie"

RUN sed -i 's#http://deb.debian.org#https://mirrors.aliyun.com#g' /etc/apt/sources.list
RUN apt update && apt install -y python3 python3-dev

WORKDIR /opt
COPY . /opt/phpy

# 编译安装
RUN cd /opt/phpy && docker-php-source extract && \
    phpize && \
    ./configure --with-python-dir=/usr && \
    make && make install && \
    docker-php-ext-enable phpy && \
    docker-php-source delete

CMD ["bash"]

