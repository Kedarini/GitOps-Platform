FROM ghcr.io/astral-sh/uv:latest AS uv

FROM python:3-12-slim

WORKDIR /app

COPY --from=uv /uv /uvx /bin/

RUN uv sync --frozen --no-dev --no-install-project

COPY . .

EXPOSE 5000

CMD ["/app/.venv/bin/python", "app.py"]