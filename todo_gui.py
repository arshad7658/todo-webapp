import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("To-Do List")
st.subheader("Remember your tasks efficiently.")

st.write("Increase your productivity.")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Write a new todo....",
              key="new_todo", on_change=add_todo)
