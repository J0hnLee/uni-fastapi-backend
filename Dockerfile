
FROM python:3.11-alpine


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt





#CMD ["fastapi", "run", "app/main.py", "--port", "80"]


# COPY . /code
COPY ./app /app

# 将主机上的代码目录挂载到容器内的 /code 目录
VOLUME [./app]


# 将容器的端口映射到主机的端口
EXPOSE 8000
RUN chmod +x ./start.sh

# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload" ]
CMD ["./start.sh"]

