# Brain Games 🧠🎮

Набор консольных математических игр для тренировки мозга

## 📦 Установка

### Локальная установка
```bash
# 1. Клонируйте репозиторий
git clone https://github.com/ваш-username/brain-games.git
cd brain-games

# 2. Установите зависимости (требуется Python 3.10+)
uv sync

# 3. Установите пакет
uv tool install --force dist/*.whl
Установка через Docker
bash
docker build -t brain-games .
docker run -it brain-games
🎮 Доступные игры
Команда	Описание
brain-games	Главное меню
brain-even	Определение четности числа
brain-calc	Арифметические вычисления
brain-gcd	Наибольший общий делитель
brain-prime	Проверка на простое число
brain-progression	Поиск пропущенного числа в прогрессии
🛠 Разработка
Структура проекта
text
brain_games/
├── game_logic/    # Логика игр
├── scripts/       # Точки входа
├── constants.py   # Тексты и сообщения
└── cli.py         # Интерфейс пользователя
Сборка проекта
bash
uv build
Запуск тестов
bash
pytest tests/
📝 Требования
Python 3.10+

Пакетный менеджер uv

Docker (опционально)

🤝 Как внести вклад
Форкните репозиторий

Создайте ветку (git checkout -b feature/AmazingFeature)

Закоммитьте изменения (git commit -m 'Add some AmazingFeature')

Запушьте в ветку (git push origin feature/AmazingFeature)

Откройте Pull Request

📜 Лицензия
Распространяется под лицензией MIT. См. файл LICENSE.


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