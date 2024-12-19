
# To-Do List Application

## **Descrição do Projeto**
Este projeto implementa uma lista de tarefas interativa usando Python. Ele oferece funcionalidades como adicionar, listar, concluir e excluir tarefas, além de exportar tarefas concluídas para arquivos CSV e exibir uma barra de progresso.

## **Funcionalidades**

1. **Adicionar tarefas**:
   - Permite adicionar uma nova tarefa com registro da data.

2. **Listar tarefas**:
   - Exibe todas as tarefas (pendentes e concluídas), juntamente com suas datas.

3. **Concluir tarefas**:
   - Marca uma tarefa como concluída e registra a data de conclusão.

4. **Excluir tarefas**:
   - Remove uma tarefa da lista.

5. **Exportar tarefas concluídas**:
   - Exporta tarefas concluídas em um intervalo de datas para um arquivo CSV.

6. **Barra de progresso**:
   - Exibe o progresso de conclusão das tarefas em formato de barra e percentual.

## **Tecnologias Usadas**
- **Linguagem**: Python 3
- **Persistência de Dados**: Arquivo JSON
- **Exportação de Dados**: Arquivo CSV

## **Como Rodar o Projeto**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/to-do-list.git
   cd to-do-list
   ```

2. **Instale as dependências**:
   - Este projeto não possui dependências externas além do Python 3.

3. **Execute a aplicação**:
   ```bash
   python main.py
   ```

## **Comandos Disponíveis**

### **Menu Interativo**
Ao executar o programa, você verá o menu com as seguintes opções:

```
=== To-Do List ===
1. Adicionar nova tarefa
2. Listar tarefas
3. Marcar tarefa como concluída
4. Excluir tarefa
5. Exportar tarefas concluídas (CSV)
6. Mostrar progresso
7. Sair
```

- Escolha o número correspondente à funcionalidade desejada e siga as instruções na tela.

### **Exportar Tarefas Concluídas**
Para exportar tarefas concluídas em um intervalo de datas, use a opção `5`. Informe as datas no formato `YYYY-MM-DD`.

### **Barra de Progresso**
A opção `6` exibe uma barra de progresso mostrando o percentual de tarefas concluídas em relação ao total de tarefas.

## **Estrutura de Arquivos**

```
to_do_list/
├── main.py           # Código principal da aplicação
├── tasks.json        # Arquivo que armazena as tarefas
├── README.md         # Documentação do projeto
└── completed_tasks_<start_date>_to_<end_date>.csv # Arquivos CSV gerados
```

## **Exemplo de Uso**

### Adicionar uma tarefa
```
Escolha uma opção: 1
Digite a nova tarefa: Comprar mantimentos
Tarefa 'Comprar mantimentos' adicionada com sucesso!
```

### Listar tarefas
```
Escolha uma opção: 2

Tarefas:
1. Comprar mantimentos - [Pendente] - 2023-12-18
```

### Exportar tarefas concluídas
```
Escolha uma opção: 5
Digite a data inicial (YYYY-MM-DD): 2023-12-01
Digite a data final (YYYY-MM-DD): 2023-12-18
Tarefas concluídas exportadas para 'completed_tasks_2023-12-01_to_2023-12-18.csv' com sucesso!
```

## **Melhorias Futuras**
- Implementar categorias para as tarefas.
- Adicionar suporte para notificações automáticas.
- Criar uma interface gráfica (GUI) com frameworks como Tkinter ou PyQt.

## **Licença**
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo.

## **Contribuição**
Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações: `git checkout -b minha-nova-feature`
3. Envie suas alterações: `git push origin minha-nova-feature`
4. Abra um Pull Request.

## **Autor**
Este projeto foi desenvolvido por MPSPG.
