FROM python:3.9

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Chrome WebDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libgconf-2-4

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE \
    && wget https://chromedriver.storage.googleapis.com/`cat LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin/chromedriver \
    && chmod +x /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip \
    && rm LATEST_RELEASE

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /usr/src/app

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
