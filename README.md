# Sistema de Gestão de Estoque (SGE)

Este é um sistema de gestão de estoque desenvolvido em Django para auxiliar no controle de produtos, categorias, marcas, fornecedores, entradas e saídas de estoque.

## Funcionalidades

- **Autenticação de Usuários**: Controle de acesso ao sistema.
- **Gerenciamento de Produtos**: Cadastro e manutenção de informações dos produtos.
- **Gerenciamento de Categorias**: Organização dos produtos por categorias.
- **Gerenciamento de Marcas**: Cadastro e manutenção de marcas dos produtos.
- **Gerenciamento de Fornecedores**: Cadastro e manutenção de informações dos fornecedores.
- **Controle de Entradas e Saídas**: Registro de movimentações de estoque.
- **Gerenciamento de Permissões**: Controle detalhado de permissões de usuários.

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS
- JavaScript

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/MarcioLucas22/sge-django.git
   cd sge-django  # Acesse o diretório do projeto
   ```

2. **Crie um ambiente virtual e ative-o**:

   ```bash
   python -m venv venv  # Cria um ambiente virtual
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate` para ativá-lo
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt  # Instala todas as bibliotecas necessárias
   ```

4. **Configure as variáveis de ambiente**:

   Renomeie o arquivo `.env.example` para `.env` e ajuste as configurações conforme necessário. Isso garante que as credenciais e configurações sensíveis estejam corretas.

5. **Aplique as migrações**:

   ```bash
   python manage.py migrate  # Aplica as mudanças no banco de dados
   ```

6. **Crie um superusuário**:

   ```bash
   python manage.py createsuperuser  # Permite criar um usuário administrador para acessar o painel
   ```

7. **Inicie o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver  # Inicia o servidor localmente na porta 8000
   ```

8. **Acesse o sistema**:

   Abra o navegador e vá para `http://localhost:8000/` para interagir com a aplicação.

## Uso

- **Login**: Acesse o sistema com a conta de superusuário criada.
- **Gerenciamento**: Utilize as seções disponíveis para gerenciar produtos, categorias, marcas, fornecedores, entradas e saídas de estoque.
- **Permissões do Administrador**: O administrador pode gerenciar usuários e definir permissões para cada um, controlando quem pode visualizar, editar e excluir registros dentro do sistema.
