from function import get_todo, write_todo
import time

now = time.strftime('%b %d, %Y:%M:%S')
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todo()
        todos.append(todo)
        write_todo(todos)
    elif user_action.startswith("show"):
        todos = get_todo()
        for index,item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            numbers = int(user_action[5:])
            numbers -= 1
            todos = get_todo()
            new_tudo = input("Enter new todo: ")
            todos[numbers] = new_tudo + "\n"
            write_todo(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todo()
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todo(todos)
            print(f"Todo {todo_to_remove} was removed from list.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("wrong command")
print("bye")

