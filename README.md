# Docker Dashboard

This program was written with the intent of helping folks get up and running
with docker containers and is designed to work with Docker Desktop.  

- Running containers
- Building containers
- Removing containers
- Using volumes to persist data
- Using multi-stage builds to separate build-time and runtime dependencies

## Getting Started

If you wish to run the program, you can use the following command after installing Docker Desktop:

```bash
docker-compose up --build
```

Once it has started, you can open your browser to [http://localhost](http://localhost:5001).

## Development

This project has a `docker-compose.yml` file, which will start the mkdocs application on your
local machine and help you see changes instantly.

```bash
docker compose up
```