### https://gist.github.com/pangyuteng/f5b00fe63ac31a27be00c56996197597

ARG UBUNTU_VER=16.04
ARG CONDA_VER=4.4.10
ARG OS_TYPE=x86_64
ARG PY_VER=3.6.8

FROM ubuntu:${UBUNTU_VER}

### system packages 
RUN apt-get update && apt-get install -yq curl wget jq vim bzip2 
RUN apt-get install -y binutils libc6 libc-bin

### Use the above args during building https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG CONDA_VER
ARG OS_TYPE

### install miniconda to /miniconda
RUN curl -LO "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh"
RUN bash Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh -p /miniconda -b
RUN rm Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

ARG PY_VER
### install packages from conda and downgrade py (optional)
RUN conda install -c anaconda -y python=${PY_VER}

RUN pip install scipy==1.3.0 \ 
	statsmodels==0.10.0 \ 
	matplotlib==3.1.2 \ 
	pandas==0.23.4 \ 
	seaborn==0.9.0 \ 
	numpy==1.15.0 \ 
	pingouin==0.2.7 \ 
	pygam==0.8.0 \ 
	PyQt5==5.13.2 \
	pyinstaller==3.5

RUN mkdir /code
WORKDIR /code

### download code here ? naaa
# wget https://ascgitlab.helmholtz-muenchen.de/computationaldiscovery/calimeradev/calimera/-/archive/master/calimera-master.tar.gz?path=src


#exec pyinstaller $@

ENTRYPOINT [ "pyinstaller" ]






