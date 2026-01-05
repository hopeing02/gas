FROM python:3.11-slim

# 필수 패키지
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    git \
    && rm -rf /var/lib/apt/lists/*

# Node 20 설치 (clasp 필수)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# clasp 설치
RUN npm install -g @google/clasp

# PATH 보장
ENV PATH="/usr/local/bin:${PATH}"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# start.sh 복사
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]

