# 베이스 이미지를 설정합니다.
FROM python:3.8-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 필요한 패키지들을 설치합니다.
COPY requirements.txt .
RUN pip install -r requirements.txt

# appuser 사용자를 생성합니다.
RUN useradd -m appuser

# /app 디렉터리의 소유자를 appuser로 변경합니다.
RUN chown -R appuser:appuser /app

# appuser 사용자를 사용합니다.
USER appuser

# 애플리케이션 파일들을 복사합니다.
COPY . .

# 애플리케이션을 실행합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
