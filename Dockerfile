FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED=1
ENV FASTMCP_STATELESS_HTTP=true
ENV FASTMCP_STREAMABLE_HTTP_PATH=/mcp

RUN uv sync

EXPOSE 8080

CMD ["uv", "run", "server.py"]
