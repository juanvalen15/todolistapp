user_prompt = "Type add, show, edit, complete, or exit:"
todo_prompt = "Enter a todo:"
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(todo_prompt) + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todos.txt') as file:
                todos = file.readlines()

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


