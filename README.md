## docker for exporting calimera software

1. install docker [https://docs.docker.com/get-docker/]
2. build docker once
3. edit only path to `calimera/src/` folder
(4. run pyinstaller in this docker to create a executable calimera app)

---

## download images from dockerhub and 

### windows
```sh
docker build -t calimera_win https://raw.githubusercontent.com/loipf/calimera_docker_export/main/win/Dockerfile

docker run --rm -v "/path/to/calimera/src/:/code/src" -v "${PWD}:/code/dist/" calimera_win
```






---

# oldschool manual way

### windows
```sh
docker build -t calimera_win https://raw.githubusercontent.com/loipf/calimera_docker_export/main/win/Dockerfile

docker run --rm -v "/path/to/calimera/src/:/code/src" -v "${PWD}:/code/dist/" calimera_win
```



### ubuntu (>=20.04)
```sh
docker build -t calimera_ubuntu https://raw.githubusercontent.com/loipf/calimera_docker_export/main/linux/Dockerfile

docker run --rm -v "/path/to/calimera/src/:/code/src" -v "${PWD}:/code/dist/" calimera_ubuntu
```

---

### manual configuration in case of error:
```sh
### move in docker environment
docker run -it --rm -v "/path/to/calimera/src/:/code/src" -v "${PWD}:/code/dist/" --entrypoint /bin/bash calimera_win

## run pyinstaller within docker:
pyinstaller win_pyinstaller_export.spec
```




---
possible improvements:

- add version date to output name
- remove `console=True` argument in `.spec` files for export - only for easier debugging
- ubuntu: maybe change permissions since output file is limited to root [https://vsupalov.com/docker-shared-permissions/]
- error `standard_init_linux.go:211: exec user process caused "exec format error"` can occur with different architectures, fix
`docker buildx build --platform=linux/amd64 -t <image-name> .`



---
edited from:  
https://gist.github.com/pangyuteng/f5b00fe63ac31a27be00c56996197597  
https://github.com/cdrx/docker-pyinstaller/blob/master/Dockerfile-py3-win64  

