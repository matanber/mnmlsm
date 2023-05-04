FROM python:3.10-alpine

WORKDIR /app

# Install dependecies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN apk add chromium

# Use global chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

COPY challenge .

EXPOSE 8005

ENTRYPOINT ["python3"]
CMD ["mnmlsm.py"]
