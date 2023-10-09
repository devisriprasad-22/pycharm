todos = []

while True:
    user_action = input("type add, show ,edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo:") + "\n"
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index+1}.{item}"
                print(row)
        case 'exit':
            break
        case 'edit':
            number = int(input("enter the todo number:"))
            number = number - 1
            new_todo = input("enter a new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("enter the todo to complete:"))
            todos.pop(number-1)
        case whatever:
            print("you've entered an unknown command")
print(todos)
print("Bye!")