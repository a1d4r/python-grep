# Аналог утилиты `grep`

## Описание

Аналог утилиты `grep`, которая выполняет поиск указанной подстроки во всеx файлах указанной директории и всех её поддиректорий.

```
usage: mygrep [-h] path substring

Search files in the specified directory for lines containing a specified substring.

positional arguments:
  path        directory to search files in
  substring   substring to search in files

optional arguments:
  -h, --help  show this help message and exit

```

### Примеры вызова

Пусть в текущей директории есть два файла:
`>> cat f1.py`

```python
print("Hello, world!")
```

`>> cat f2.txt`

```
hello
world
```

Вызов: `mygrep . "Hello"`

Результат:

```
f1.py line=1: print("Hello, world!")
```

Вызов: `mygrep . world`

Результат:

```
f1.py line=1: print("Hello, world!")
f2.txt line=2: world
```

### Установка виртуального окружения
```
make venv
```
### Установка утилиты
```
python setup.py install
```
### Запуск тестов
```
make test
```
