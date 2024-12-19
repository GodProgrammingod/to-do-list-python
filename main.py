# File: main.py

import json
import os
import sys
import csv
from datetime import datetime

class ToDoList:
    def __init__(self, filename="tasks.json"):
        """Initialize the To-Do List with optional file persistence."""
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from a file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to a file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except OSError:
            print("Erro ao salvar as tarefas. Verifique as permissões do sistema de arquivos.")
    
    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False, "date": datetime.now().strftime("%Y-%m-%d")})
        self.save_tasks()
        print(f"Tarefa '{task}' adicionada com sucesso!")
    
    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
            return
        print("\nTarefas:\n")
        for i, task in enumerate(self.tasks, 1):
            status = "Concluída" if task['completed'] else "Pendente"
            print(f"{i}. {task['task']} - [{status}] - {task['date']}")
    
    def complete_task(self, task_number):
        """Mark a task as completed."""
        try:
            index = task_number - 1
            self.tasks[index]['completed'] = True
            self.tasks[index]['completed_date'] = datetime.now().strftime("%Y-%m-%d")
            self.save_tasks()
            print(f"Tarefa '{self.tasks[index]['task']}' marcada como concluída!")
        except (IndexError, ValueError):
            print("Tarefa inválida. Por favor, tente novamente.")
    
    def delete_task(self, task_number):
        """Delete a task from the list."""
        try:
            index = task_number - 1
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Tarefa '{removed_task['task']}' removida com sucesso!")
        except (IndexError, ValueError):
            print("Tarefa inválida. Por favor, tente novamente.")

    def export_completed_tasks_csv(self, start_date, end_date):
        """Export completed tasks within a date range to CSV."""
        output_file = f"completed_tasks_{start_date}_to_{end_date}.csv"
        try:
            with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['Task', 'Completion Date']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for task in self.tasks:
                    if task['completed'] and start_date <= task['completed_date'] <= end_date:
                        writer.writerow({'Task': task['task'], 'Completion Date': task['completed_date']})
            print(f"Tarefas concluídas exportadas para '{output_file}' com sucesso!")
        except Exception as e:
            print(f"Erro ao exportar tarefas: {e}")

    def show_completion_progress(self):
        """Show a completion progress bar and percentage."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        if total_tasks == 0:
            print("Nenhuma tarefa para exibir progresso.")
            return
        percent_complete = (completed_tasks / total_tasks) * 100
        bar_length = 20
        completed_length = int(bar_length * completed_tasks // total_tasks)
        progress_bar = f"[{'#' * completed_length}{'-' * (bar_length - completed_length)}]"
        print(f"\nProgresso: {progress_bar} {percent_complete:.2f}% Concluído\n")

def show_menu():
    """Display the main menu of the application."""
    print("""
    === To-Do List ===
    1. Adicionar nova tarefa
    2. Listar tarefas
    3. Marcar tarefa como concluída
    4. Excluir tarefa
    5. Exportar tarefas concluídas (CSV)
    6. Mostrar progresso
    7. Sair
    """)

def main():
    todo_list = ToDoList()
    while True:
        show_menu()
        try:
            choice = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if choice == 1:
            task = input("Digite a nova tarefa: ")
            todo_list.add_task(task)
        elif choice == 2:
            todo_list.list_tasks()
        elif choice == 3:
            try:
                task_number = int(input("Digite o número da tarefa a ser concluída: "))
                todo_list.complete_task(task_number)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif choice == 4:
            try:
                task_number = int(input("Digite o número da tarefa a ser excluída: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif choice == 5:
            start_date = input("Digite a data inicial (YYYY-MM-DD): ")
            end_date = input("Digite a data final (YYYY-MM-DD): ")
            todo_list.export_completed_tasks_csv(start_date, end_date)
        elif choice == 6:
            todo_list.show_completion_progress()
        elif choice == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
