user_prompt = "Type add, show, edit, or exit:"
todo_prompt = "Enter a todo:"
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input(todo_prompt)
            todos.append(todo)
        case 'show':
            for list_index, item in enumerate(todos):
                print(list_index, item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            existing_todo = todos[number]
            new_todo = input(todo_prompt)
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("Incorrect command!")

print('Bye!')


