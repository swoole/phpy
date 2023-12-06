FROM php:8.3.0-fpm
LABEL authors="Heelie"

WORKDIR /opt
ADD . .

# 安装依赖
RUN sed -i 's#http://deb.debian.org#https://mirrors.aliyun.com#g' /etc/apt/sources.list.d/debian.sources && \
    apt update && apt install -y python3 python3-dev

# 编译安装
RUN docker-php-source extract && \
    phpize && \
    ./configure --with-python-dir=/usr && \
    make && make install && \
    docker-php-ext-enable phpy && \
    docker-php-source delete

CMD ["bash"]

