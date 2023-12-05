FROM php:8.1.24-cli-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        wget && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    mkdir -p /opt/conda && \
    ~/miniconda.sh -b -u -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda init bash

ENV PATH="/opt/conda/bin:$PATH"

RUN git clone https://github.com/swoole/phpy.git /app/phpy

WORKDIR /app/phpy
RUN sed -i 's@anaconda3@conda@' config.m4

RUN docker-php-source extract && \
    phpize && \
    ./configure && \
    make install && \
    docker-php-ext-enable phpy && \
    docker-php-source delete

RUN php -m | grep -i phpy

CMD [ "bash" ]
