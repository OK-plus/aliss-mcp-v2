FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

COPY pyproject.toml .
COPY server.py .
COPY aliss_client.py .

RUN uv sync

EXPOSE 8080

CMD ["uv", "run", "server.py"]
