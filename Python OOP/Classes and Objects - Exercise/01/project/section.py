from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if task.name == new_task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                cleared_tasks += 1
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"

        for task in self.tasks:
            result += f"{task.details()}\n"
        return result