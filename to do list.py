import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "tasks.csv")

class Task():
    def __init__(self, task_name, description, priority):
        self.task_name = task_name
        self.description = description
        self.priority =  priority


class ToDoList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully")

    def remove_task(self, index): # i'm trying to remove the task by its object
        if not self.tasks:
            print('There is no task to remove')
            print('                          ')
            return
        def priority_value(task):
            priority_order = {"high": 1, "medium": 2, "low": 3}
            return priority_order.get(task.priority.lower(), 4)

        sorted_tasks = sorted(self.tasks, key = priority_value)
        
        if 0 <= index < len(sorted_tasks):
            task_to_remove = sorted_tasks[index]
            self.tasks.remove(task_to_remove)   
            print(f"Task '{task_to_remove.task_name}' removed.")
            self.save_to_file(csv_path)

        else:
            print("Invalid task number.")
            print('                    ')

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            print('                     ')
            return
        
        def priority_value(task):
            priority_order = {"high": 1, "medium": 2, "low": 3}
            return priority_order.get(task.priority.lower(), 4)

        sorted_tasks = sorted(self.tasks, key = priority_value)
        
        for i, task in enumerate(sorted_tasks, start=1):
            print(f"{i}. {task.task_name} | {task.description} | Priority: {task.priority}")
            print('                          ')

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(f"{task.task_name},{task.description},{task.priority}\n")
        
        print(f"Saving {len(self.tasks)} tasks to file...")
        print("Tasks are now saved to file.")
        print('                          ')

    def load_from_file(self, filename):
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        task_name, description, priority = parts
                        task = Task(task_name, description, priority)
                        self.tasks.append(task)
            print("Tasks loaded from file.")
            print('                          ')
        
        except FileNotFoundError:
            print("No previous task file found.")
            print('                          ')

what_to_do = ToDoList()

answer = input("Do you want to make a new list of tasks?(y/n) ").strip().lower()

if answer == "y":
    with open(csv_path, "w", encoding="utf-8") as f:
        pass 
    print("Your new list of tasks is ready.")

elif answer == "n":
    what_to_do.load_from_file(csv_path)
    print("Editing your previous list of tasks.")

else:
    print('Your choice is invalid, please try typing y/n.')
    exit()


print('Welcome to your own To Do List!')
while True:
    print('Please select your choice from down below: ')
    print('                          ')
    print('[Adding a task : 1 |Removing a task :2 |Show the tasks :3\nSave to file :4 |Load from file :5 |Exit the menu :6\nChange your choice :0]')
    print('                          ')
    
    choice = input('Please enter your choice : (1,2,3,4,5,6) ')   
    
    if choice == '1':
        name = input('Please enter your task name : ')
        description = input('Please enter description : ')
        priority = input('Please enter task priority from high to low : ')
        task = Task(name, description, priority)
        what_to_do.add_task(task)
    
    elif choice == '2':
        if not what_to_do.tasks:
            print('No task to remove.')
            print('Try adding a new task.')
            name = input('Please enter your task name : ')
            description = input('Please enter description : ')
            priority = input('Please enter task priority from high to low : ') 
            task = Task(name, description, priority)
            what_to_do.add_task(task)
        else:    
            what_to_do.show_tasks()
            index = int(input('please enter the number of task you wanna remove : ')) - 1
            what_to_do.remove_task(index)

    elif choice == '3':
        what_to_do.show_tasks()

    elif choice == '4':
        what_to_do.save_to_file(csv_path)

    elif choice == '5':
        what_to_do.load_from_file(csv_path)

    elif choice == '6':
        print('Exiting from the menu...Thank you and Goodbye!')
        break

    elif choice == '0':
        continue

    else:
        print('Your choice is invalid, please enter a number from the list!')

