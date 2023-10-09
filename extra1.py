todos= []

while True:
    user_action = input("type add, show or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case whatever:
            print("you've entered an unknown command")
print(todos)
print("Bye!")