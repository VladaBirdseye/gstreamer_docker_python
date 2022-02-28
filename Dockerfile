FROM nvidia/cuda:11.5.0-devel-ubuntu18.04
EXPOSE 8081
WORKDIR /opt/build

RUN apt-get update -y 
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Belgrade
RUN apt-get install -y tzdata
RUN apt install -y build-essential
RUN apt install -y python3.8 
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN apt install -y python3-venv
RUN apt-get install -y gstreamer-1.0
RUN apt-get install -y gstreamer1.0-dev 
RUN apt-get install -y git autoconf automake libtool

RUN apt-get install -y python3-gi
RUN apt-get install -y libgirepository1.0-dev
RUN apt-get install -y libcairo2-dev gir1.2-gstreamer-1.0
RUN apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
RUN apt-get install -y git autoconf automake libtool
RUN apt install -y software-properties-common
RUN apt-get update
RUN apt-get install -y python-gst-1.0
RUN apt-get install -y gstreamer1.0-tools gstreamer1.0-alsa gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
RUN apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-good1.0-dev libgstreamer-plugins-bad1.0-dev
RUN pip install pycairo
RUN pip install PyGObject
ENV QT_X11_NO_MITSHM=1
RUN apt-get update && \
    apt-get install -y libqt5gui5 && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
        build-essential \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libopenjp2-7-dev \
        libavformat-dev \
        libpq-dev \
        qt5-default
RUN apt-get install libxkbcommon-x11-0
RUN apt install libsm6
RUN apt-get install libxcb-xinerama0

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        python3-dev \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev \
	libgtk2.0-dev \
	qtbase5-dev \
	libqt5opengl5-dev \
	libassimp-dev \
        python-opengl \
	x11vnc \
	xvfb \
	fluxbox \
	wmctrl \
	swig3.0 \
	python-numpy \
	zlib1g-dev \
	xorg-dev \
	libboost-all-dev \
	libsdl2-dev \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN apt-get install python3-venv
ENV QT_DEBUG_PLUGINS=1
RUN pip3 install pycairo
RUN pip3 install PyGObject
RUN pip3 install opencv-python
RUN pip3 install git+https://github.com/jackersson/gstreamer-python.git

RUN python -c "import gi; gi.require_version('Gst', '1.0'); \
gi.require_version('GstApp', '1.0'); \
gi.require_version('GstVideo', '1.0'); \
gi.require_version('GstBase', '1.0')"

