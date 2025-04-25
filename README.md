# 📚 Sistema de Distribuição de Grupos - UERR

Este é um sistema web desenvolvido em Django para auxiliar os professores da Universidade Estadual de Roraima (UERR) na criação e organização de grupos de trabalho, com alocação automática de alunos, sorteio da ordem de apresentação e gerenciamento do cronograma.

## 🛠️ Funcionalidades

- Cadastro de temas com data e horário de apresentação
- Cadastro de alunos com matrícula única
- Alocação automática dos alunos em grupos
- Sorteio da ordem de apresentação dos grupos
- Horário mínimo de 15 minutos por grupo
- Remanejamento manual de alunos entre grupos
- Interface para visualização de grupos e apresentações
- Totalmente em português 🇧🇷

## ⚙️ Tecnologias

- Python 3
- Django 4.x
- Bootstrap 5
- SQLite (desenvolvimento)

## ▶️ Como rodar o projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Crie e ative um ambiente virtual (opcional mas recomendado)
python -m venv venv
venv\Scripts\activate  # no Windows

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário para acessar o admin
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

📂 Organização do Projeto
core/ – app principal com models, views e templates

templates/core/ – arquivos HTML da aplicação

static/ – arquivos estáticos como CSS e JS (se necessário)

📅 Status
🚧 Projeto em desenvolvimento.

👥 Contribuidores
Cauã Silva

link do projeto: https://github.com/cauasilva2003/ProgWeb
