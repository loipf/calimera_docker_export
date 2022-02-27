
ARG UBUNTU_VER=16.04
ARG CONDA_VER=4.4.10
ARG OS_TYPE=x86_64
ARG PY_VER=3.6.8


FROM ubuntu:${UBUNTU_VER}

### system packages 
RUN apt-get update && apt-get install -yq curl wget jq vim bzip2 libglib2.0-0
RUN apt-get install -y binutils libc6 libc-bin 

### use the above args during building
ARG CONDA_VER
ARG OS_TYPE

### install miniconda to /miniconda
RUN curl -LO "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh"
RUN bash Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh -p /miniconda -b
RUN rm Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda


### install packages from conda and downgrade py (optional)
ARG PY_VER
RUN conda install -c anaconda -y python=${PY_VER}
RUN apt-get install -y python3-pyqt5


### install calimera packages
RUN pip install -r https://ascgitlab.helmholtz-muenchen.de/computationaldiscovery/calimeradev/calimera/-/raw/master/docs/py_packages_requirements.txt


### post process pingouin package problems
WORKDIR /miniconda/lib/python3.6/site-packages/pingouin
RUN rm plotting.py
RUN rm -r datasets
RUN sed -i "/\b\(plotting\|datasets\)\b/d" __init__.py 
WORKDIR /


RUN mkdir /code
WORKDIR /code

RUN wget https://raw.githubusercontent.com/loipf/calimera_docker_export/main/linux/linux_pyinstaller_export.spec


ENTRYPOINT [ "pyinstaller", "linux_pyinstaller_export.spec" ]



