# Brain Games

### 🔧 Установка необходимых инструментов

**Сначала установите uv и скопируйте репозиторий:**
```bash
gh repo clone MaksLLL-prog/brain_games_two
pip install uv

- Потом приступайте к дальнейшем шагам:

cd brain_games_two
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

### Лицензия: MIT
```bash
Распространяется под лицензией MIT. См. файл LICENSE.
```

### Этот README:
- Краткий и информативный
- Содержит все необходимые команды
- Четко разделяет способы установки
- Перечисляет все доступные игры
- Включает инструкции для разработчиков

### Примеры игр с помощью Asciinema:

1. Проверка на чётность
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)
2. Калькулятор
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)
3. Наибольший общий делитель
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)
4. Арифметическая прогрессия
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)
5. Простое ли число?
[![asciicast](https://asciinema.org/a/XXXXXX.svg)](https://asciinema.org/a/XXXXXX)