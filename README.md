# grep command-line utility

## Description

Analogue of grep command-line utility in Python. It searches files in a 
specified directory for lines containing a specified substring.


### CLI description
```
usage: mygrep [-h] path substring

Search files in the specified directory for lines containing a specified substring.

positional arguments:
  path        directory to search files in
  substring   substring to search in files

optional arguments:
  -h, --help  show this help message and exit

```

## Usage

Assume there are 2 files in the working directory:

`$ cat f1.py`

```python
print("Hello, world!")
```

`$ cat f2.txt`

```
hello
world
```

`$ mygrep . "Hello"`

```
f1.py line=1: print("Hello, world!")
```

`$ mygrep . world`

```
f1.py line=1: print("Hello, world!")
f2.txt line=2: world
```

### Create virtual environment
```
make venv
```
### Install utility
```
python setup.py install
```
### Run tests
```
make test
```
