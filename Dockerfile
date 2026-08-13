FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

COPY pyproject.toml .
COPY server.py .
COPY aliss_client.py .

RUN uv sync

EXPOSE 8080

CMD ["sh", "-c", "uv run python -c 'import fastmcp; print(\"INSTALLED FASTMCP:\", fastmcp.__version__)' && uv run server.py"]
