import function
import FreeSimpleGUI as sg

lable = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter do")
add_button = sg.Button("Add")
window = sg.Window('My to do app', layout=[[lable], [input_box ,add_button]])
window.read()
window.close()