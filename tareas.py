import os
os.system('cls' if os.name == 'nt' else 'clear')

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.users = {}
        self.current_user = None

        """Registra un nuevo usuario con un nombre de usuario y contraseña."""
    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("Usuario ya existe.")
        self.users[username] = User(username, password)        
        print(f"User '{username}' Correctamente registrado.")

    def login_user(self, username, password):
        """Conecta un usuario con su usuario y contraseña."""
        if username not in self.users:
            raise ValueError("usuario no existe.")
        if self.users[username].password != password:
            raise ValueError("Contraseña incorrecta.")
        self.current_user = self.users[username]
        print(f"User '{username}' Conectado correctamente.")


    """Desconecta el usuario actual."""
    def logout_user(self):
        
        if self.current_user:
            print(f"User '{self.current_user.username}' Correctamente desconectado.")
            self.current_user = None
        else:
            print("Ningún usuario esta conectado.")

    """Añade una tarea al usuario conectado."""
    def add_task(self, task_description):
        
        if not self.current_user:
            raise ValueError("No usuario conectado.")
        if not task_description:
            raise ValueError("La tarea no puede quedar vacia.")
        task = Task(task_description)
        self.current_user.tasks.append(task)
        print(f"Task '{task_description}' added successfully for user '{self.current_user.username}'.")

    """Visualiza tareas para el usuario conectado."""
    def view_tasks(self):
        
        if not self.current_user:
            raise ValueError("No hay usuario conectado.")
        if not self.current_user.tasks:
            print("No hay tareas disponibles.")
            return
        print(f"Daily Tasks for {self.current_user.username}:")
        for i, task in enumerate(self.current_user.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{i}. {task.description} [{status}]")

    def remove_task(self, task_number):
        """Removes a task by its number for the currently logged-in user."""
        if not self.current_user:
            raise ValueError("No user is logged in.")
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.current_user.tasks):
                raise IndexError("Invalid task number.")
            removed_task = self.current_user.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.description}' removed successfully for user '{self.current_user.username}'.")
        except ValueError:
            print("Task number must be an integer.")
        except IndexError as e:
            print(e)

    def mark_task_completed(self, task_number):
        """Marca una tarea como completada para el actual usuario conectado."""
        if not self.current_user:
            raise ValueError("Ningún usuario conectado.")
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.current_user.tasks):
                raise IndexError("Invalid task number.")
            self.current_user.tasks[task_number - 1].completed = True
            print(f"Task '{self.current_user.tasks[task_number - 1].description}' marked as completed for user '{self.current_user.username}'.")
        except ValueError:
            print("El número de la tarea debe ser un número entero.")
        except IndexError as e:
            print(e)

    def modify_task(self, task_number, new_description):
        """Modifies the description of a task by its number for the currently logged-in user."""
        if not self.current_user:
            raise ValueError("No user is logged in.")
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.current_user.tasks):
                raise IndexError("Invalid task number.")
            if not new_description:
                raise ValueError("New task description cannot be empty.")
            self.current_user.tasks[task_number - 1].description = new_description
            print(f"Task {task_number} modified successfully for user '{self.current_user.username}'.")
        except ValueError as e:
            print(e)
        except IndexError as e:
            print(e)

    def main(self):
        """Bucle principal para interactuar con las tareas y el sistema de usuarios."""
        while True:
            if not self.current_user:
                print("\n-------------------------------------------------------")
                print("\nControl de entrada de usuarios - Organizador de Tareas:")
                print("1. Registrar Usuario")
                print("2. Login Usuario")
                print("3. Salida")
                print("\n-------------------------------------------------------")
                choice = input("Elige una opción: ")
                if choice == '1':
                    username = input("Introduce nombre de usuario: ")
                    password = input("Introduce contraseña: ")
                    try:
                        self.register_user(username, password)
                    except ValueError as e:
                        print(e)
                elif choice == '2':
                    username = input("Introduce nombre de usuario: ")
                    password = input("Introduce contraseña: ")
                    try:
                        self.login_user(username, password)
                    except ValueError as e:
                        print(e)
                elif choice == '3':
                    print("Saliendo del programa. ¡Adios!")
                    break
                else:
                    print("Opción Invalida. Intentalo otra vez.")
            else:
                print("\nOrganizador de Tareas:")
                print("\n----------------------------------------")
                print("1. Añadir Tarea")
                print("2. Ver Tareas")
                print("3. Eliminar Tareas")
                print("4. Marcar tarea como completada")
                print("5. Modificar tarea")
                print("6. Desconectar Usuario")
                print("\n----------------------------------------")
                choice = input("Elige una opción: ")
                if choice == '1':
                    task_description = input("Introduce la tarea: ")
                    try:
                        self.add_task(task_description)
                    except ValueError as e:
                        print(e)
                elif choice == '2':
                    try:
                        self.view_tasks()
                    except ValueError as e:
                        print(e)
                elif choice == '3':
                    task_number = input("Introduce el número de la tarea para eliminar: ")
                    try:
                        self.remove_task(task_number)
                    except ValueError as e:
                        print(e)
                elif choice == '4':
                    task_number = input("Introduce el número de la tarea para marcarla como completada: ")
                    try:
                        self.mark_task_completed(task_number)
                    except ValueError as e:
                        print(e)
                elif choice == '5':
                    task_number = input("Introduce el número de la tarea para modificar: ")
                    new_description = input("Introduce la nueva descripción de la tarea:")
                    try:
                        self.modify_task(task_number, new_description)
                    except ValueError as e:
                        print(e)
                elif choice == '6':
                    self.logout_user()
                else:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.main()
