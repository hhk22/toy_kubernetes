
## Architecture

![Architecture](https://github.com/hhk22/toy_kubernetes/images/k8s_architecture.png)

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

## Mysql 배포

k8s에서 배포 database배포.

```
kubectl apply -f mysql/secret.yaml
kubectl apply -f mysql/pv.yaml
kubectl apply -f mysql/pvc.yaml
kubectl apply -f mysql/deployment.yaml
```

## Kubernetes에서 nfs-volume 설정

```
sudo apt-get update
sudo apt-get install -y nfs-common nfs-kernel-server rpcbind portmap

sudo mkdir /mnt/nfs_shared
sudo chmod 777 /mnt/nfs_shared

sudo echo '/mnt/nfs_shared 192.168.1.0/24(rw,sync,no_subtree_check)' >> /etc/exports

sudo systemctl restart nfs-kernel-server

kubectl apply -f nfs-volume/

```

## Kubernetes에서 Api 배포

개인 Repo에 해당 docker image들이 배포되어있어야함.  
nfs-volume이 배포 되어있어야함. 

### docker login 

```
docker login  # k8s machine.
```

```
kubectl apply -f secret.yaml
kubectl apply -f scraper.yaml
kubectl apply -f gpt.yaml
kubectl apply -f text_preprocessor.yaml
```


## Test

```
curl http://0.0.0.0?url=<scraper_url>

...
<A few sceonds later>
...

ls -al /nfs_shared/dynamic-vol/gpt_results
>> json file (gpt result)

```