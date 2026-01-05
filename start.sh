#!/bin/sh
set -e

# clasp 인증 복원
mkdir -p /root
echo "$CLASPRC_JSON" > /root/.clasprc.json
chmod 600 /root/.clasprc.json

# 디버그 (한번만 확인용)
which clasp
clasp --version

# 서버 실행
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}

