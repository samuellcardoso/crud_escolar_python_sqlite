# Sistema Escolar em Python * SQLite

Esse projeto e um **CRUD escolar** desenvolvido em Python, utilizando **SQLite** como banco de dados.
Ele permite cadastrar, atualizar, excluir, buscar, listar e exportar dados de alunos de forma simples e interativa.

## Funcionalidades
- **Cadastrar aluno**: insere novos registros no banco de dados.
- **Atualizar dados**: altera a idade de um aluno existente.
- **Excluir aluno**: remove registros pelo nome.
- **Buscar aluno**: pesquisa alunos pelo nome (busca parcial com `LiKE`).
- **Listar alunos**: exibe todos os alunos cadastrados.
- **Menu interativo**: interface de linha de comando para navegar entre as opcoes.

## Tecnologias utilizadas
- [Python 3](https://www/python.org/)
- [SQLite](https://www.sqlite.org/index.html)
- Modulos padrao:
    -`sqlite`
    -`csv`
    -`datetime`

## Como executar
Clone este repositorio:
```bash
git clone https://github.com/samuellcardoso/crud_escolar_python_sqlite
```
Acesse a pasta do projeto:
```bash
cd crud_escolar_python_sqlite
```
Execute o sistema
```bash
python main.py
```

## Exportacao de dados
Os registros podem ser exportados para CSV.
O arquivo e salvo na pasta **crud_escolar/** com o nome no formato:
```bash
alunos_YYYY-MM-DD_HH_MM_SS.csv
```

## Observacoes
- O banco de dados e criado automaticamente no arquivo **escola.db**.
- O sistema valida entradas para evitar erros (somente letras em nomes e numeros em idade).
- Este projeto e ideal para estudos de integracao entre Python e bancos de dados relacionais.
