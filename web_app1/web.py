import streamlit as st
import function


def add_todo():
    new_todo = st.session_state["new_todo"]+"\n"
    if new_todo in todos:
        st.warning("This todo already exist!")
    else:
        todos.append(new_todo)
        function.write_todo(todos)
    st.session_state["new_todo"] = ""   # 清空輸入欄

todos = function.get_todo()

st.title("My todo app")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    todo_key = f"{todo}_{index}"   # 建立唯一key
    checkbox = st.checkbox(todo, key=todo_key)
    if checkbox:
        todos.pop(index)
        function.write_todo(todos)
        del st.session_state[todo_key]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

