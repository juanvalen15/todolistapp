user_prompt = "Type add, show, or exit:"
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
            for item in todos:
                print(item)
        case 'exit':
            break
        case whatever:
            print("Incorrect command!")

print('Bye!')


