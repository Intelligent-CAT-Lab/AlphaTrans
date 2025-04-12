## Hardware Requirements
The docker image created by our tool occupies about 10 GB of disk space. The tool further requires interacting with an LLM (e.g., GPT or open-source model hosted by ollama, vLLM). Please see the instructions in our README for more details on how to interact with LLMs. You might need GPUs to host open-source LLMs locally, or API KEY to access LLMs remotely.

## Software Requirements
We provide a [`Dockerfile`](/Dockerfile) to build a Docker image with all the dependencies required to run our tool. Simply download [Docker](https://www.docker.com/) first and build the image using the command in [`INSTALL.md`](INSTALL.md). Moreover, we recommend using a Unix-based system (Linux or MacOS) to run the tool.
