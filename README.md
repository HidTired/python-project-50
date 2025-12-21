### Hexlet tests and linter status:
[![Actions Status](https://github.com/HidTired/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/HidTired/python-project-50/actions)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=HidTired_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=HidTired_python-project-50)

# Проект - Вычислитель отличий
 gendiff - это утилита командной строки, предназначенная для сравнения двух конфигурационных файлов и отображения различий между ними.
 
  Она полезна разработчикам и администраторам для анализа изменений конфигурации, мониторинга состояния системы или отслеживания обновлений настроек приложений.

# Требования:

[Python 3.13 +] - (https://www.python.org/downloads/)


[UV 0.5.11 +] - (https://astral.sh)


# Пример использования пакета

## Клонируем репозиторий на ваше устройство:

git clone git@github.com:https://github.com/HidTired/python-project-50.git

## Переходим в директорию проекта:

cd python-project-50

## Устанавливаем необходимые зависимости:

uv build

uv tool install dist/*.whl

### Данный репозиторий поддерживает файлы формата:


- JSON (.json)
- YAML (.yaml, .yml)


# Запуск:


Поместите два файла, которые вы хотите сравнить в папку tests/test_data.


Замените file1.json и file2.json на названия ваших файлов и воспользуйтесь командой:


uv run gendiff tests/test_data/file1 tests/test_data/file2 


## Важно:

Стандартный вызов форматирует 'stylish'

Для вызова другого формата используйте 'json' или 'plain' , указывайте с флагом -f


Указывайте не только названия файла, но и его формат.

# Командные строки для вызова разных форматтеров:

## Формат по умолчанию (stylish):

uv run gendiff tests/test_data/file1 tests/test_data/file2  


## Формат JSON:
uv run gendiff -f json tests/test_data/file1 tests/test_data/file2 



## Формат PLAIN:
uv run gendiff -f plain tests/test_data/file1 tests/test_data/file2 



# Демонстрация:
[![asciicast](https://asciinema.org/a/dNSO2CIu2QdLVAScxrkHIh7ix.svg)](https://asciinema.org/a/dNSO2CIu2QdLVAScxrkHIh7ix)
[![asciicast](https://asciinema.org/a/mqyXgntnl0fBL9Pju9Nw8Hp2P.svg)](https://asciinema.org/a/mqyXgntnl0fBL9Pju9Nw8Hp2P)