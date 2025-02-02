user_prompt = "Add a new member: "
user_input = input(user_prompt)  + "\n"

membersList = []

file = open('/Users/juan/PycharmProjects/todolistapp/files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(user_input)

file = open('/Users/juan/PycharmProjects/todolistapp/files/members.txt', 'w')
file.writelines(members)