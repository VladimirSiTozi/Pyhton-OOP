from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if task_name == t.name:
                t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared_tasks = 0
        task_to_clear = []
        for t in self.tasks:
            if t.completed:
                task_to_clear.append(t)
                cleared_tasks += 1
        for t_to_clear in task_to_clear:
            self.tasks.remove(t_to_clear)
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self):
        result = [f'Section {self.name}:']
        for t in self.tasks:
            result.append(t.details())
        return '\n'.join(result)




# task = Task("Make bed", "27/05/2020")
# print(task.details())
# print(task.add_comment('comment1'))
# print(task.add_comment('comment2'))
# print(task.comments)
# print(task.edit_comment(0, 'comment0'))
# print(task.details())
# section = Section('section1')
# section2 = Section('section2')
# print(section.add_task(task))
# print(section.tasks)
# print(section.complete_task('task'))


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("27/05/2020"))
# print(task.change_name("Go to University"))
# task.add_comment("Don't forget laptop")
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.edit_comment(99, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# print(section.add_task(second_task))
# print(section.add_task(second_task))
# print(section.complete_task('Make bed'))
# print(section.complete_task('M121ake bed'))
# print(section.view_section())
# print(section.clean_section())
# print(section.view_section())