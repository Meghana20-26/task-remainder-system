import json

FILE_NAME = "tasks.json" 

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_name, description, deadline, email):
    tasks = load_tasks()

    new_task = {
        "task":task_name,
        "description":description,
        "deadline":deadline,
        "email":email
    }

    tasks.append(new_task)

    save_tasks(tasks)

def get_tasks():
    return load_tasks()                    