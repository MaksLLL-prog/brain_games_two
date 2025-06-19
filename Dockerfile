FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml .
COPY brain_games/ brain_games/

RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync && \
    uv build

RUN pip install --force-reinstall dist/*.whl

RUN ls -la /usr/local/bin/brain-games

ENTRYPOINT ["python", "-m", "brain_games.scripts.brain_games"]