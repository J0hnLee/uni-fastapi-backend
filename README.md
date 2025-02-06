# uni-fastapi-backend

## start up without docker

```bash 
fastapi dev main.py
```


## Quick Setup

1. Install Docker and Docker-Compose

- [Docker Install documentation](https://docs.docker.com/install/)
- [Docker-Compose Install documentation](https://docs.docker.com/compose/install/)
  
1.1 if you only use docker:
```bash
    docker build -t unifastapibackend:latest .
    docker run -it -p 8000:8000 -v ./app:/app unifastapibackend:latest
```
1.2
```bash
 docker tag unifastapibackend:latest 12cloud/unifastapibackend:latest
```
1.3 push
```bash
docker push 12cloud/unifastapibackend:latest
```


TODO: rewrite docker-compose.yaml file
2. Create a docker-compose.yml file similar to this:

```yml
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80'
      - '81:81'
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
```

This is the bare minimum configuration required. See the [documentation](https://nginxproxymanager.com/setup/) for more.

3. Bring up your stack by running

```bash
docker-compose up -d

# If using docker-compose-plugin
docker compose up -d

```
TODO: rearrange
4. Log in to the Admin UI

When your docker container is running, connect to it on port `81` for the admin interface.
Sometimes this can take a little bit because of the entropy of keys.

[http://127.0.0.1:81](http://127.0.0.1:81)

Default Admin User:
```
Email:    admin@example.com
Password: changeme
```

Immediately after logging in with this default user you will be asked to modify your details and change your password.

## Trouble shooting
### Deploy on AWS fargate
   - 當無法連線時調整VPC的組態(security group)