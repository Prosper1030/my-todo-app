import function
import FreeSimpleGUI as sg

lable = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter do", key="todo")
add_button = sg.Button("Add")
window = sg.Window('My to do app',
                   layout=[[lable], [input_box, add_button]],
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
        case sg.WIN_CLOSED:
            break
window.close()