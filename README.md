# todeolho

Exemplo simples de monitorias agendadas utilizando Python 3.11.

## Como usar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o agendador:

```bash
python -m todeolho.main
```

As tarefas registradas executam a cada minuto. Edite os módulos em
`todeolho/tasks/` para adicionar novas monitorias.

### Variáveis de ambiente

Alguns monitores utilizam variáveis de ambiente para definir parâmetros:

- `API_URL`, `DB_CONN`, `DB_QUERY` – utilizados pela tarefa `api_db_compare` para
  comparar resultados de uma API com o banco PostgreSQL.
- `HTTP_URL` – endpoint utilizado pelo monitor `http_monitor`.

Caso haja divergência entre a API e o banco, será emitido um alerta via log.

## Testes

```bash
pytest
```
