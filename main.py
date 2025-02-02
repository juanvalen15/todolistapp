user_prompt = "Type add, show, edit, complete, or exit:"
todo_prompt = "Enter a todo:"
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(todo_prompt) + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            file = open('files/todos.txt')
            todos = file.readlines()
            file.close()

            for list_index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{list_index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            existing_todo = todos[number]

            new_todo = input(todo_prompt)
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to : "))
            todos.pop(number)
        case 'exit':
            break
        case _:
            print("Incorrect command!")

print('Bye!')


