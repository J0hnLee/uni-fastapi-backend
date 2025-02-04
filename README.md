# uni-fastapi-backend

# 啟動
```fastapi dev main.py```

# docker
```docker build -t unifastapibackend:latest .```
``` docker run -it -p 8000:8000 -v ./app:/app unifastapibackend:latest```
## 標記
``` docker tag unifastapibackend:latest 12cloud/unifastapibackend:latest```
## push
```docker push 12cloud/unifastapibackend:latest```

# 當無法連線時調整VPC的組態(security group)
