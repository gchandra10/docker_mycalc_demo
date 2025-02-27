# Python Demo

```
mkdir -p container
cd container
```

Fork & Clone this Repo

```
cd docker_mycalc_demo
```

## Build an Image

(default it uses Dockerfile, but can customized with -f parameter)

```bash
podman build -t docker_mycalc_demo .
```

or

```bash
docker build -t docker_mycalc_demo .
```

## Run the container using the Image


```bash
podman run --rm --name gccalc mycalc
```

or

```bash
docker run --rm --name gccalc mycalc
```