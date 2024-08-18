def get_todo(filepath="todo.txt"):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as f:
        todos_local = f.readlines()
    return todos_local


def write_todo(todos_arg, filepath="todo.txt"):
    """Write the to do item in the text file."""
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)