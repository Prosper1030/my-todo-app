import function
import FreeSimpleGUI as sg

lable = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todo(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window('My to do app',
                   layout=[[lable],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, value = window.read()
    print(event, value)
    match event:
        case "Add":
            todos = function.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            function.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"]
            todos = function.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todo(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_complete = value["todos"][0]
            todos = function.get_todo()
            todos.remove(todo_complete)
            function.write_todo(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=value["todos"][0].strip("\n"))
        case sg.WIN_CLOSED:
            break
window.close()