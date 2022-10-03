# Derive from image
FROM python:3.9.5-slim

# Create a work directory in the Docker image that
# all the files will be created in
WORKDIR /api

# NOTE: To check available versions of a package
#       apt-cache madison <package>
#
# Install dependent libraries for software to work
RUN apt-get update -y
RUN apt-get install -y nodejs=10.24.0~dfsg-1~deb10u1
RUN apt-get install -y npm=5.8.0+ds6-4+deb10u2

# Install Sphinx
# and install third party theme "Read the docs"
RUN pip install sphinx
RUN pip install sphinx_rtd_theme

# Install flake8 and nose2 for linting and unit tests
RUN pip install flake8
RUN pip install nose2
