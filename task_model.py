# task_model.py
class TaskModel:
    def __init__(self, task_id, task_name, status):
      
        self.task_name = task_name

    def get_task_name(self):
        return self.task_name