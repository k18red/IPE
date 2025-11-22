# CRUD Flask + MySQL (HTML)

## 1) Preparar MySQL
No MySQL, rode:

```sql
SOURCE schema.sql;
```
ou copie o conteúdo do `schema.sql` e execute (cria DB `exemplo_flask` e a tabela `produtos`).

## 2) Preparar ambiente (Windows)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set FLASK_APP=app.py
# opcional: setar credenciais se diferentes
# set DB_HOST=localhost
# set DB_USER=root
# set DB_PASS=123456
# set DB_NAME=exemplo_flask
# set DB_PORT=3306
python app.py
```

Abra: http://127.0.0.1:5000/

## 3) Variáveis de ambiente (opcional)
- DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT
