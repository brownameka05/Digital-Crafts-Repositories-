

class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority


tasks = []

while True:


    title = input("Enter task title or q to quit:")
#this doesn't quit the app this breaks the loop
    if(title == "q"):
        break
    priority = input("Enter priority:")

    task = Task(title,priority)

    tasks.append(task)


    print(len(tasks))


for task in tasks:
    print(task.title)
    print(task.priority)

print("----THANKS FOR USING THE APP!-----")
