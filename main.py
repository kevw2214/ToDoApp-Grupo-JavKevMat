from task_model import TaskModel

def main():
    task = TaskModel ("Estudiar para el examen")
    print (f"Tarea creada: {task.get_task_name()}")
    task.set_done()
    print (f"Tarea completada: {task.is_done()}")
    task.remove_task()
    print (f"Tarea eliminada: {task.get_task_name()}")
    print("Bienvenido a ToDoApp")

if __name__ == "__main__":
    main()