
# API de Gerenciamento de Tarefas

Projeto desenvolvido para a disciplina de Manutenção de Software da Universidade Federal Rural do Semi-Árido (UFERSA).

A aplicação consiste em uma API REST para gerenciamento de tarefas e categorias, desenvolvida com Django REST Framework e banco de dados SQLite.

## 1. Tecnologias utilizadas

- Python 3.11
- Django 4.2.3
- Django REST Framework
- SQLite
- Git e GitHub
- Coverage.py

## 2. Entidades

### Categoria

Representa uma classificação para organizar tarefas.

Atributos:
- id: identificador da categoria
- nome: nome único da categoria
- descricao: descrição opcional

### Tarefa

Representa uma atividade a ser realizada.

Atributos:
- id: identificador da tarefa
- titulo: título da atividade
- descricao: descrição opcional
- prazo: data limite
- status: pendente, andamento ou concluida
- categoria: referência à categoria

### Relacionamento

Uma categoria pode possuir várias tarefas, mas cada tarefa pertence a uma categoria.

O relacionamento foi implementado utilizando ForeignKey do Django ORM.

## 3. Funcionalidades

A API permite:

- Cadastrar categorias e tarefas
- Consultar categorias e tarefas
- Atualizar informações cadastradas
- Excluir registros
- Organizar tarefas por categorias
- Validar prazos das tarefas
- Impedir a exclusão de categorias com tarefas associadas

## 4. Endpoints REST

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /api/categorias/ | Listar categorias |
| POST | /api/categorias/ | Criar categoria |
| GET | /api/categorias/{id}/ | Consultar categoria |
| PUT/PATCH | /api/categorias/{id}/ | Atualizar categoria |
| DELETE | /api/categorias/{id}/ | Excluir categoria |
| GET | /api/tarefas/ | Listar tarefas |
| POST | /api/tarefas/ | Criar tarefa |
| GET | /api/tarefas/{id}/ | Consultar tarefa |
| PUT/PATCH | /api/tarefas/{id}/ | Atualizar tarefa |
| DELETE | /api/tarefas/{id}/ | Excluir tarefa |

## 5. Regras de negócio

### Validação de prazo

O sistema impede o cadastro de tarefas com prazo anterior à data atual.

Quando um prazo inválido é informado, a API retorna HTTP 400 Bad Request.

### Proteção de categorias

Uma categoria que possui tarefas associadas não pode ser excluída.

Essa regra utiliza models.PROTECT e tratamento de ProtectedError.

Quando a exclusão é impedida, a API retorna HTTP 409 Conflict.

## 6. Instalação e execução

### Clonar o repositório

```bash
git clone https://github.com/LudmilaMonteiro/api-gerenciamento-tarefas.git
cd api-gerenciamento-tarefas
```

### Criar o ambiente virtual

```bash
python -m venv venv
```

### Ativar o ambiente virtual

No Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

### Instalar dependências

```bash
python -m pip install -r requirements.txt
```

### Aplicar as migrações

```bash
python manage.py migrate
```

### Iniciar o servidor

```bash
python manage.py runserver
```

A API poderá ser acessada em:

http://127.0.0.1:8000/api/tarefas/

http://127.0.0.1:8000/api/categorias/

## 7. Testes automatizados

Foram implementados seis testes utilizando APITestCase do Django REST Framework.

Os testes verificam:

1. Cadastro de tarefas
2. Consulta de tarefas
3. Atualização de tarefas
4. Exclusão de tarefas
5. Validação de prazos inválidos
6. Proteção contra exclusão de categorias com tarefas associadas

Para executar:

```bash
python manage.py test tarefas
```

Resultado obtido: 6 testes executados com sucesso.

## 8. Métricas de manutenção

Foram analisadas duas métricas:

### Quantidade de linhas de código

157 linhas, considerando os arquivos Python do aplicativo tarefas, incluindo testes e excluindo migrações e arquivos de cache.

### Cobertura de testes

97% de cobertura, com 104 de 107 instruções executadas.

Para reproduzir a medição, instale o Coverage:

```bash
python -m pip install coverage
```

Execute:

```bash
python -m coverage run --source=tarefas manage.py test tarefas
python -m coverage report -m
```

## 9. Utilização de Inteligência Artificial

O ChatGPT foi utilizado como ferramenta de apoio ao desenvolvimento e à manutenção.

Foi solicitada uma sugestão para melhorar os testes automatizados e a integridade dos dados.

A melhoria implementada consistiu no tratamento da tentativa de exclusão de categorias que possuem tarefas associadas.

A solução foi validada por meio de um novo teste automatizado, com resultado positivo.

## 10. Gerenciamento de configuração

O desenvolvimento foi controlado utilizando Git e GitHub.

A branch feature/gerenciamento-tarefas foi utilizada para implementar a API, os testes e as melhorias.

Foram realizados commits descritivos para registrar a evolução do projeto.

## 11. Projeto original

Este trabalho foi desenvolvido a partir do Django Quick Project, disponibilizado pela equipe LISA da UFERSA.

Repositório original:

https://github.com/lisa-ufersa/django-quickproject

O projeto base foi adaptado para implementar a API de Gerenciamento de Tarefas.
