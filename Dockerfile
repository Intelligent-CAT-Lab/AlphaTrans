FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    git \
    wget \
    curl \
    zip \
    unzip \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN arch=$(uname -m) && \
    if [ "$arch" = "x86_64" ]; then \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"; \
    elif [ "$arch" = "aarch64" ]; then \
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh"; \
    else \
    echo "Unsupported architecture: $arch"; \
    exit 1; \
    fi && \
    wget $MINICONDA_URL -O miniconda.sh && \
    mkdir -p /root/.conda && \
    bash miniconda.sh -b -p /root/miniconda3 && \
    rm -f miniconda.sh

ENV PATH="/root/miniconda3/bin:${PATH}"

RUN pip3 install --upgrade pip

WORKDIR /home

RUN git clone https://github.com/Intelligent-CAT-Lab/AlphaTrans.git

WORKDIR /home/AlphaTrans

SHELL ["/bin/bash", "-c"]

RUN conda init bash

RUN echo "source /root/.bashrc && conda activate alphatrans" > /etc/profile.d/conda.sh && \
    echo "conda activate alphatrans" >> ~/.bashrc

RUN conda env create -f environment.yml

RUN bash setup.sh install_graal

RUN echo "OPENAI_API_KEY=" >> .env
RUN echo "VLLM_API_KEY=" >> .env
RUN echo "VLLM_API_URL=" >> .env

RUN mkdir -p /home/AlphaTrans/misc/sitter-libs
RUN git clone https://github.com/tree-sitter/tree-sitter-java.git /home/AlphaTrans/misc/sitter-libs/java
RUN git clone https://github.com/tree-sitter/py-tree-sitter /home/AlphaTrans/misc/sitter-libs/python
