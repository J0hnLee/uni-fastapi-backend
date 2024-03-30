# 
FROM python:3.11-alpine

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code
# 将主机上的代码目录挂载到容器内的 /code 目录
VOLUME ./:/code


# 将容器的端口映射到主机的端口
EXPOSE 8001
RUN chmod +x start.sh

# 
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload" ]
CMD ["./start.sh"]