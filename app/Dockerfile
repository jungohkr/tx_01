# 베이스 이미지를 설정합니다.
FROM python:3.8-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 필요한 빌드 도구 설치
RUN apt-get update && apt-get install -y gcc musl-dev

# 필요한 패키지들을 설치합니다.
COPY requirements.txt .
RUN pip install -r requirements.txt

# 사용자 추가
RUN useradd -m appuser

# 파일 권한 설정
RUN chown -R appuser:appuser /app

# appuser로 변경
USER appuser

# 애플리케이션 파일 복사
COPY . .

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

