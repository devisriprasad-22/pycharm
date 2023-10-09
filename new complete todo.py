while True:
    user_action = input("type add, show ,edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo:") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}.{item}"
                print(row)
        case 'edit':
            number = int(input("enter the todo number:"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            print('here is existing ', todos)

            new_todo = input("enter a new todo:")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print('here is how it will be', todos)
        case 'complete':
            number = int(input("enter the todo to complete:"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)

        case 'whatever':
            print("you've entered an unknown command")
        case 'exit':
            break
print(todos)
print("Bye!")