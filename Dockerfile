# 베이스 이미지 선택
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 복사
COPY requirements.txt /app/requirements.txt

# 패키지 설치
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 앱 코드 복사
COPY main.py /app/

# Uvicorn을 실행하기 위한 기본 명령어'
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
