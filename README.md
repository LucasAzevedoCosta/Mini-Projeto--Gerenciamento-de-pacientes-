# 🏥 Gerenciamento de Pacientes

Este projeto consiste em um sistema web desenvolvido com Django para gerenciamento de informações de pacientes. Ele permite cadastrar, atualizar, remover e visualizar dados dos pacientes, sendo ideal para clínicas, consultórios médicos ou qualquer aplicação que precise gerenciar registros de saúde.

## 🚀 Tecnologias Utilizadas

- 🐍 Python
- 🌐 Django
- 🗄️ SQLite
- 🎨 HTML, CSS (Django Templates)

## 📦 Configuração do Ambiente

### ✅ Pré-requisitos
Certifique-se de ter o **Python** instalado na sua máquina.

### 📥 Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/gerenciamento-pacientes.git
   cd gerenciamento-pacientes
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

Execute o seguinte comando para iniciar o servidor:
```sh
python manage.py runserver
```
A aplicação estará disponível em `http://127.0.0.1:8000/`.

## 🛠️ Estrutura do Projeto

| Pasta/Arquivo     | Descrição |
|-------------------|-----------|
| 📜 `manage.py`    | Gerenciador do Django. |
| 📜 `requirements.txt` | Lista de dependências do projeto. |
| 🗄️ `db.sqlite3`   | Banco de dados local (SQLite). |
| 📜 `.gitignore`   | Arquivos e pastas ignorados no repositório. |
| 📂 `core/`        | Configurações principais do projeto. |
| 📂 `pacientes/`   | Aplicação de gerenciamento de pacientes. |
| 📂 `templates/`   | Templates HTML para renderização das páginas. |


---
