# Biblioteca — Django Full Stack Lab

Sistema de cadastro e consulta de acervo de uma biblioteca, desenvolvido nas Aulas 4 e 5 da disciplina **Laboratório de Programação Full Stack** (Universidade de Vassouras).

## Funcionalidades

- Cadastro de livros com título, autor, ano, tipo e categoria
- Tipo de acervo: **Físico** ou **Digital**
- Categoria pela Classificação Decimal de Dewey (000 a 900)
- Pesquisa por título ou autor, tipo e categoria (combináveis)
- Painel administrativo (Django Admin) com filtros e busca

## Tecnologias

- Python 3.11
- Django 5.2
- PostgreSQL
- python-dotenv

## Como executar

1. Clone o repositório e entre na pasta:

   ```bash
   git clone <url-do-repositorio>
   cd biblioteca_fs_lab
   ```

2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie o banco `biblioteca_db` no PostgreSQL.

5. Copie o `.env.example` para `.env` e preencha com seus dados:

   ```
   DB_NAME=biblioteca_db
   DB_USER=postgres
   DB_PASSWORD=sua_senha
   DB_HOST=localhost
   SECRET_KEY=uma-chave-secreta
   ```

6. Aplique as migrações e crie um administrador:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

7. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

## Rotas

| Endereço | Página |
|---|---|
| `/livros/` | Lista do acervo com pesquisa |
| `/livros/novo/` | Cadastro de livro |
| `/admin/` | Painel administrativo |

## Estrutura

```
biblioteca/         configurações do projeto (settings, urls)
acervo/             app do acervo
  models.py         model Livro, com tipo e categoria
  forms.py          LivroForm (cadastro) e BuscaForm (pesquisa)
  views.py          lista com filtros e cadastro
  templates/acervo/ base.html, lista.html, form.html
  static/acervo/    estilo.css
```