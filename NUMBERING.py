todos= []

while True:
    user_action = input("type add, show ,edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo:")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index}.{item}"
                print(row)
        case 'exit':
            breakad
        case 'edit':
            number = int(input("enter the todo number:"))
            number = number - 1
            new_todo = input("enter a new todo:")
            todos[number] = new_todo
        case whatever:
            print("you've entered an unknown command")
print(todos)
print("Bye!")