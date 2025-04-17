user_prompt = "Type add, show, edit, complete, or exit:"
todo_prompt = "Enter a todo:"
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    if 'show' in user_action:
        with open('files/todos.txt') as file:
            todos = file.readlines()

        for list_index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{list_index + 1}-{item}"
            print(row)

    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open('files/todos.txt','r') as file:
            todos = file.readlines()

        new_todo = input(todo_prompt)
        todos[number] = new_todo + '\n'

        with open('files/todos.txt','w') as file:
            file.writelines(todos)

    if 'complete' in user_action:
        number = int(input("Number of the todo to : "))
        index  = number - 1

        with open('files/todos.txt','r') as file:
            todos = file.readlines()

        todo_to_remove = todos[index]
        todos.pop(index)

        with open('files/todos.txt','w') as file:
            file.writelines(todos)

        print(f"Todo {todo_to_remove.strip('\n')} was removed from the list.")

    if 'exit' in user_action:
        break


print('Bye!')


