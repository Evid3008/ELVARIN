FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y ffmpeg curl gnupg ca-certificates git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "BrandrdXMusic"]
