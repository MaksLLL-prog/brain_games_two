## 🔧 Установка (локальная)

**Требования:**
- Python 3.10+
- Пакетный менеджер `uv`

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/ваш-username/brain-games.git
cd brain-games

# 2. Установите зависимости
uv sync

# 3. Соберите пакет
uv build

# 4. Установите игры в систему
uv tool install --force dist/*.whl



### 2. Установка (Docker)
```markdown
## 🐳 Установка (Docker)

**Требования:**
- Установленный Docker

```bash
# 1. Соберите образ
docker build -t brain-games .

# 2. Запустите контейнер
docker run -it brain-games


### 3. Запуск игр (локальный)
```markdown
## 🎮 Запуск игр (локальный)

```bash
# Основное меню
brain-games

# Конкретные игры:
brain-even       # Проверка на четность
brain-calc       # Арифметические вычисления
brain-gcd        # Наибольший общий делитель
brain-prime      # Простые числа
brain-progression # Арифметическая прогрессия



### 4. Запуск игр (Docker)
```markdown
## 🐳 Запуск игр (Docker)

```bash
# Запуск с выбором игры
docker run -it brain-games brain-even

# Или войти в контейнер для доступа ко всем играм
docker run -it brain-games sh
> brain-calc


### 5. Удаление
```markdown
## 🗑️ Удаление

**Локальная установка:**
```bash
uv tool uninstall brain-games

docker rmi brain-games
docker system prune


### 6. Разработка
```markdown
## 💻 Разработка

```bash
# Установка для разработки
uv sync --editable

# Запуск тестов
uv run pytest tests/

# Сборка пакета
uv build

# Проверка стиля кода
uv run ruff check brain_games


Каждая секция:
1. Имеет понятный заголовок с иконкой
2. Четко разделяет локальную и Docker-установку
3. Содержит готовые команды для копирования
4. Указаны требования для каждого способа
5. Добавлен раздел для разработчиков


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