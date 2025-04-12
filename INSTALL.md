### Installation Instructions
We provide a [`Dockerfile`](/Dockerfile) which installs all necessary dependencies to reproduce the results of AlphaTrans. Please download [Docker](https://www.docker.com/), and then execute the following to create a docker image and execute the container in interactive mode:

```
docker build --no-cache -t alphatrans .
docker run -it alphatrans bash
```
> [!NOTE]
> If you are using MacOS with an Apple chip, please consider adding `--platform=linux/amd64` in `docker build`.
