# Django Rest Framework em 30 Minutos

Django Rest Framework, é um framework que facilita a criação de APIs REST usando o Django. Para reaquecer as habilidade em Python!!

## Para utilização

1. `venv\scripts\activate` - windows <br>
    `source venv/scripts/activate` - linux/mac

2. `cd api` - pasta do projeto

3. `py manage.py runserver` - rodar o server

4. acesse `http://localhost:3000/`

## Endpoints

O Django Rest Framework já disponibiliza pra gente com poucas linhas de código para um CRUD completo

### GET
* `/clientes/` - retorna a lista de clientes
* `/clientes/{id}/` - retorna um cliente pelo ID

### POST
*`/clientes/` - envia a requisição de criação pelo `request body`(nome, endereco, idade) e retorna o cliente criado

### PUT
*`/clientes/{id}/` - faz uma alteração completa de um cliente em especifico com o `request body` (nome, endereco, idade) e retorna esse cliente alterado

### PATCH
*`/clientes/{id}/` - faz uma alteração de um campo de um determinado cliente com a `request body` sendo algum dos campos presentes(nome, endereco e idade)[também pode altera-lo por completo como o PUT] e retorna esse cliente alterado.

### DELETE
*`/clientes/{id}/` - deleta um cliente em especifico

<em>OBS: Não esqueça da `/` no final da URL</em>

Fonte: [Aprendendo Django Rest em 30 Minutos - Gregory Pacheco](https://www.youtube.com/watch?v=gFsIGJR5R8I)


