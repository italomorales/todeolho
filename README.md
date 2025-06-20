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

As tarefas registradas executam a cada minuto. Edite os módulos em `todeolho/tasks/` para adicionar novas monitorias.

## Testes

```bash
pytest
```
