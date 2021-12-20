FROM ubuntu:latest

RUN set -ex \
  	&& sed -i -e "s%http://archive.ubuntu.com/ubuntu/%http://no.archive.ubuntu.com/ubuntu/%g" /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y \
 			python3-pip \
 			python3-dev \
 			build-essential \
 	&& apt-get clean \
 	&& rm -rf /var/lib/apt/lists/* \
 	&& pip install --upgrade pip

ENV APPPATH /opt/myflaskapp
COPY . $APPPATH
WORKDIR $APPPATH
RUN pip install .
WORKDIR $APPPATH/app
ENTRYPOINT ["python3"]
CMD ["src/app.py"]