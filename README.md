### Hexlet tests and linter status:
[![Actions Status](https://github.com/HidTired/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/HidTired/python-project-50/actions)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=HidTired_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=HidTired_python-project-50)

# gendiff - инструмент командной строки для поиска различий между двумя файлами

## Пример использования пакета

# Клонируем репозиторий на ваше устройство:

git clone https://github.com/HidTired/python-project-50.git

# Переходим в директорию проекта:

cd python-project-50

# Устанавливаем необходимые зависимости:

uv build

uv tool install dist/*.whl

### Данный репозиторий поддерживает файлы формата:


- JSON (.json)
- YAML (.yaml, .yml)


# Запуск:

Поместите два файла, которые вы хотите сравнить в папку tests/test_data.

Замените file1.json и file2.json на названия ваших файлов и воспользуйтесь командой:

uv run gendiff tests/test_data/<file1> tests/test_data/<file2>


## Важно:

Стандартный вызов форматирует 'stylish'
Для вызова другого формата используйте 'json' или 'plain' , указывайте с флагом -f ,


# Командные строки для вызова разных форматтеров:

## Формат по умолчанию (stylish):

uv run gendiff tests/test_data/<file1> tests/test_data/<file2>  - указывайте не только названия файла, но и его формат


## Формат JSON:
uv run gendiff -f json tests/test_data/<file1> tests/test_data/<file2> - указывайте не только названия файла, но и его формат



## Формат PLAIN:
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file2> - указывайте не только названия файла, но и его формат



# Демонстрация:
(Тут скоро будут аскинемы)