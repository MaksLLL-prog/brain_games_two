lint:
	uv run ruff check brain_games

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl


clean:
	rm -rf *.egg-info dist build __pycache__