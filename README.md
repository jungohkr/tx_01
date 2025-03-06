# tx_01
연습용 사이트 제작공간
초기 셋팅 단순 켜지기만 하는 구조.
포트 충돌 작동 테스트!


##### 1. **프로젝트 프로젝트 구조** :
``` tree
/study_project/
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── tasks.py
│   └── models.py
├── nginx/
│   └── nginx.conf
```


##### 2. **파일 내용** :

- **docker-compose.yml** :
```yaml
version: '3.8'

services:
  app:
    build: ./app
    command: uvicorn main:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    depends_on:
      - redis
      - postgres

  celery:
    build: ./app
    command: celery -A tasks worker --loglevel=info
    depends_on:
      - redis
      - postgres

  postgres:
    image: postgres:latest
    environment:
      POSTGRES_USER: study_user
      POSTGRES_PASSWORD: your_password
      POSTGRES_DB: study_db
    volumes:
      - pg_data:/var/lib/postgresql/data

  redis:
    image: redis:latest

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app

volumes:
  pg_data:

```

- **/app/Dockerfile** :

```dockerfile
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


```

- **/app/requirements.txt** :
```text
fastapi==0.68.0
uvicorn==0.14.0
sqlalchemy==1.4.22
psycopg2-binary==2.9.1
redis==3.5.3
celery==5.1.2

```

- **/app/main.py** :
``` python
from fastapi import FastAPI
from models import Problem, engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

- **/app/models.py** :

```python
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("postgresql://study_user:your_password@postgres:5432/study_db")

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True)
    topic = Column(String(255))
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")
```

-  **/nginx/nginx.conf** :
```nginx
events {}

http {
    server {
        listen 80;
        
        location / {
            proxy_pass http://app:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        # 로그 설정 추가
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;
    
```


  ##### 4. **데이터베이스** 필요 시:
-  PostgreSQL 테이블 생성:
	- 테이블
		- docker exec -it study_project-postgres-1 psql -U study_user -d study_db
```sql
CREATE TABLE problems (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(255),
    question TEXT,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


##### 5. 빌드.
```
# 도커 이미지를 빌드합니다.
docker build -t myapp .

# 도커 컨테이너를 실행합니다.
docker run -p 8000:8000 myapp

```
