FILEPATH = "todo.txt"


def get_todo(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r', encoding="utf-8") as f:  # 加上encoding解碼
        todos_local = f.readlines()
    return todos_local


def write_todo(todos_arg, filepath=FILEPATH):
    """Write the to do item in the text file."""
    with open(filepath, 'w', encoding="utf-8") as f:
        f.writelines(todos_arg)