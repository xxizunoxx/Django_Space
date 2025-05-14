# 🚀 Django Space

Uma aplicação web desenvolvida com Django que exibe uma galeria de imagens espaciais com título, legenda e descrição. Ideal para quem quer explorar imagens do universo com uma interface simples e funcional.

## 🌌 Funcionalidades

- 📸 Cadastro de imagens com:
  - Nome
  - Legenda
  - Descrição
  - Foto
- 🖼️ Exibição de imagens em galeria com layout HTML responsivo
- 🔍 Filtro e organização das imagens por conteúdo
- 💾 Armazenamento local de imagens estáticas

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/) 3.x
- [Django](https://www.djangoproject.com/) 4.x
- HTML5, CSS3 e JavaScript
- SQLite3 (banco de dados padrão do Django)

## 📁 Estrutura do Projeto

Django_Space/
├── galeria/ # Aplicação principal
│ ├── models.py # Modelo Fotografia
│ ├── views.py # Lógica de exibição
│ ├── urls.py # Rotas da aplicação
│ └── templates/ # Templates HTML
│ └── galeria/
├── static/ # Arquivos estáticos (CSS, JS, imagens)
├── db.sqlite3 # Banco de dados SQLite
├── manage.py # Comando de gerenciamento do Django
└── requirements.txt # Dependências do projeto


## 🧪 Como Rodar Localmente

### 1. Clone o repositório
git clone https://github.com/xxizunoxx/Django_Space.git
cd Django_Space

### 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Execute as migrações
python manage.py migrate

### 5. Inicie o servidor
python manage.py runserver



