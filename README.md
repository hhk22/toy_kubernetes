
## API 배포

Local서 다음과같이 Image를 빌드하고, 개인 dockerHub repo에 배포한다.  
추후, Kubernetes에서 docker login을 하고 해당 이미지를 가지고 pod를 배포한다. 

### scraper 배포

```
docker build -t hyeonghwan/mini-project-api:latest . -f dockerfiles/dockerFile_api

docker login

docker push hyeonghwan/mini-project-api:latest
```

### text preprocessor 배포

```
docker build -t hyeonghwan/mini-project-mini-project-text-preprocessor:latest . -f dockerfiles/dockerFile_text

docker login

docker push hyeonghwan/mini-project-mini-project-text-preprocessor:latest
```

### chatgpt 배포

```
docker build -t hyeonghwan/mini-project-gpt:latest . -f dockerfiles/dockerFile_gpt

docker login

docker push hyeonghwan/mini-project-gpt:latest
```