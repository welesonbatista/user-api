# Comandos Python e Configuração

## Ambiente Virtual

```bash
python3 -m venv venv
.venv/bin/activate
.\venv\Scripts\Activate
. venv\Scripts\Activate.ps1
```

## Seleção de Interpretador

```bash
python: Select interpreter
```

## Instalação de Pacotes

```bash
pip install pylint
pip install fastapi
pip install uvicorn
```

## Geração de Dependências

```bash
pip freeze > requirements.txt
```

## Configuração Pylint (disable)

```ini
disable=
C0116, # Used when a module, class, method or function has no docstring or it is
C0015, # Used when a docstring is missing or empty. This is used when the docstring
C0114, # Used when an inline option has no effect on the message
C0209, # Used when a logging format string is not a string literal. This can potentially lead to security issues if the format string is constructed from user input.
E0115, # Used when a method is missing a required argument, which is usually 'self' for instance methods and 'cls' for class methods.
```
>>> import sqlite3
>>> conn = sqlite3.connect("schema.db")
>>> conn.close()
>>> exit()