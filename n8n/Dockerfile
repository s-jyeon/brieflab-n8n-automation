FROM n8nio/n8n:latest

# 루트 권한으로 전환
USER root

# 필수 패키지 설치 및 가상환경 설정
RUN apk update && \
    apk add --no-cache python3 py3-pip bash curl unzip ca-certificates && \
    python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip install --upgrade pip && \
    pip install gsutil && \
    chown -R node:node /venv
# 서비스 계정 키 복사
COPY brieflab_service_account.json /home/node/.n8n/brieflab_service_account.json

# 환경변수 설정
ENV PATH="/venv/bin:$PATH"
ENV GOOGLE_APPLICATION_CREDENTIALS="/home/node/.n8n/brieflab_service_account.json"

USER node
