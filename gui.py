import function
import FreeSimpleGUI as sg
import time
import os


if not os.path.exists("todo.txt"):
   with open("todo.txt", "w") as file:
       pass

sg.theme("black")
clock = sg.Text("", key="clock")
lable = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todo(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My to do app',
                   layout=[[clock],
                           [lable],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 14))
while True:
    now = time.strftime('%b %d, %Y %H:%M:%S')
    event, value = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == "Exit":   # 檢查窗口關閉事件
        break
    window["clock"].update(value=now)
    match event:
        case "Add":
            todos = function.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            function.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"]
                todos = function.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 14))
        case "Complete":
            try:
                todo_complete = value["todos"][0]
                todos = function.get_todo()
                todos.remove(todo_complete)
                function.write_todo(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 14))
        case "todos":
            window["todo"].update(value=value["todos"][0].strip("\n"))
window.close()