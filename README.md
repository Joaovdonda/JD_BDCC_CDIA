# Lavoura Inteligente

API REST para rastreabilidade agrícola: cadastro de talhões e controle dos lotes colhidos em cada um, alinhado ao contexto de conformidade da EUDR (European Union Deforestation Regulation).

## Modelo de dados

```
Talhao 1 ────── N Lote
```

### Talhao

| Campo | Tipo | Observação |
|---|---|---|
| identificador | CharField | único, ex.: `TALHAO_8F23` |
| produtor | CharField | |
| fazenda | CharField | |
| geojson | JSONField | opcional, polígono do talhão |
| status | CharField | `APROVADO`, `REVISAO` ou `BLOQUEADO` |
| data_cadastro | DateTimeField | preenchido automaticamente |

### Lote

| Campo | Tipo | Observação |
|---|---|---|
| talhao | ForeignKey | referência ao `Talhao` |
| codigo | CharField | único |
| peso_kg | DecimalField | peso do lote na balança |
| status | CharField | `APROVADO`, `SUSPEITO` ou `BLOQUEADO` |
| motivo | TextField | opcional |
| data_recepcao | DateTimeField | preenchido automaticamente |

## Endpoints

| Método | Rota | Ação |
|---|---|---|
| GET, POST | `/api/talhoes/` | listar e criar talhões |
| GET, PUT, PATCH, DELETE | `/api/talhoes/{id}/` | detalhar, alterar e remover um talhão |
| GET, POST | `/api/lotes/` | listar e criar lotes |
| GET, PUT, PATCH, DELETE | `/api/lotes/{id}/` | detalhar, alterar e remover um lote |
| GET | `/` | health check do Elastic Beanstalk |
| | `/admin/` | painel administrativo do Django |

## Stack

- Python 3.12
- Django 6.0
- Django REST Framework
- SQLite
- Gunicorn
- AWS Elastic Beanstalk

## Rodando localmente

```bash
python -m pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # opcional, para acessar o /admin/
python manage.py runserver
```

A API fica em `http://127.0.0.1:8000/api/`.

## Deploy no Elastic Beanstalk

A configuração de deploy já está pronta em `.ebextensions/django.config`, que roda `migrate`, cria o superusuário (via variáveis `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` configuradas no ambiente) e roda `collectstatic` a cada deploy.

### Publicando

1. Gere o `app.zip` com o conteúdo do projeto (sem `.venv`, `db.sqlite3` e `__pycache__`)
2. No console do Elastic Beanstalk, envie o `app.zip` em **Upload and deploy**
