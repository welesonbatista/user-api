# Setup de Ambiente Python (FastAPI)

## 1. Criar Ambiente Virtual

```bash
python -m venv .venv
```

---

# 2. Ativar Ambiente Virtual

## Windows (PowerShell)

```bash
.\.venv\Scripts\Activate.ps1
```

## Windows (CMD)

```bash
.\.venv\Scripts\activate
```

## Linux / Mac

```bash
source .venv/bin/activate
```

---

# 3. Selecionar Interpretador no VS Code

No comando do **:contentReference[oaicite:0]{index=0}**:

```
Python: Select Interpreter
```

Selecionar:

```
.venv/Scripts/python.exe
```

---

# 4. Instalar Dependências do Projeto

Instalação das bibliotecas principais:

```bash
pip install fastapi uvicorn sqlalchemy aiosqlite
```

Instalação de ferramentas de qualidade e testes:

```bash
pip install pylint pytest pytest-asyncio
```

---

# 5. Gerar Arquivo de Dependências

```bash
pip freeze > requirements.txt
```

---

# 6. Executar API

Executar aplicação com **:contentReference[oaicite:1]{index=1}** (servidor ASGI usado com **:contentReference[oaicite:2]{index=2}**):

```bash
uvicorn main:app --reload
```

---

# 7. Executar Testes

Rodar testes com **:contentReference[oaicite:3]{index=3}**:

```bash
pytest -s -v
```

---

# 8. Testar conexão SQLite manualmente

```python
import sqlite3

conn = sqlite3.connect("schema.db")
conn.close()
```

---

# 9. Configuração do Pylint

Arquivo `.pylintrc`:

```ini
disable=
C0116,
C0015,
C0114,
C0209,
E0115
```

---

# 10. Instalação Garantida no Ambiente Virtual

Forma recomendada para garantir que os pacotes sejam instalados no Python correto:

```bash
python -m pip install fastapi
python -m pip install uvicorn
python -m pip install sqlalchemy
python -m pip install aiosqlite
python -m pip install pylint
python -m pip install pytest
python -m pip install pytest-asyncio
```

Ou instalar tudo de uma vez:

```bash
python -m pip install fastapi uvicorn sqlalchemy aiosqlite pylint pytest pytest-asyncio
```

pytest -m -v
