
ARG CONDA_VER=4.4.10
ARG OS_TYPE=x86_64
ARG PY_VER=3.6.8


FROM sickcodes/docker-osx:high-sierra

### system packages 
#RUN apt-get update && apt-get install -yq curl wget jq vim bzip2 libglib2.0-0
#RUN apt-get install -y binutils libc6 libc-bin 

### use the above args during building
ARG CONDA_VER
ARG OS_TYPE

### install miniconda to /miniconda
#RUN curl -LO "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-MacOSX-${OS_TYPE}.sh"
#RUN bash Miniconda3-${CONDA_VER}-MacOSX-${OS_TYPE}.sh -p /miniconda -b
#RUN rm Miniconda3-${CONDA_VER}-MacOSX-${OS_TYPE}.sh
#ENV PATH=/miniconda/bin:${PATH}
#RUN conda update -y conda



