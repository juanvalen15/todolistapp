user_prompt = "Type add or show:"
todo_prompt = "Enter a todo:"
todos = []

while True:
    user_action = input(user_prompt)

    match user_action:
        case 'add':
            todo = input(todo_prompt)
            todos.append(todo)
        case 'show':
            print(todos)


