```markdown
# Brain Games

### Установка (локальная)
```bash
git clone https://github.com/ваш-username/brain-games.git
cd brain-games
uv sync
uv build
uv tool install --force dist/*.whl
```

### Установка (Docker)
```bash
docker build -t brain-games .
docker run -it brain-games
```

### Доступные игры
```bash
brain-games      # Главное меню
brain-even       # Четность числа
brain-calc       # Калькулятор
brain-gcd        # Наибольший делитель
brain-prime      # Простые числа
brain-progression # Прогрессии
```

### Удаление
```bash
uv tool uninstall brain-games  # Локально
docker rmi brain-games        # Docker
```

### Разработка
```bash
uv sync --editable
uv run pytest tests/
uv build
```

> Лицензия: MIT
```

Этот README:
- Краткий и информативный
- Содержит все необходимые команды
- Четко разделяет способы установки
- Перечисляет все доступные игры
- Включает инструкции для разработчиков

## Проверка на чётность
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Калькулятор
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Наибольший общий делитель
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Арифметическая прогрессия
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)

## Простое ли число?
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)