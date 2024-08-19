import streamlit as st
import function


def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function.write_todo(todos)


todos = function.get_todo()
st.title("My todo app")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")