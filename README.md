## docker for exporting calimera software

1. build docker once
2. edit only path to `calimera/src/` folder
3. run pyinstaller in this docker to create a executable calimera app


---
### ubuntu (>=16.04)
```sh
docker build -t calimera_ubuntu https://raw.githubusercontent.com/loipf/calimera_docker_export/main/linux/Dockerfile

docker run --rm -v "/path/to/calimera/src/:/code/src" -v "${PWD}:/code/dist/" calimera_ubuntu
```




---
possible improvements:

- add version date to output name
- ubuntu: maybe change permissions since output file is limited to root [https://vsupalov.com/docker-shared-permissions/]



---
edited from:
https://gist.github.com/pangyuteng/f5b00fe63ac31a27be00c56996197597
https://github.com/cdrx/docker-pyinstaller/blob/master/Dockerfile-py3-win64


