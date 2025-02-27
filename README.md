# Python Demo

```
mkdir -p container
cd container
```

Fork & Clone this Repo

```
cd docker_python_mycalc_demo
```

## Build an Image

(default it uses Dockerfile, but can customized with -f parameter)

```bash
podman build -t mycalc .
```

or

```bash
docker build -t mycalc .
```

## Run the container using the Image


```bash
podman run --rm --name gccalc mycalc
```

or

```bash
docker run --rm --name gccalc mycalc
```