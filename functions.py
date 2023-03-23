Filepath='lesson6.txt'
def get_todos(filepath=Filepath):
    """ get file text and open it """
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos_arg,filepath=Filepath):
    """ write in a data in a file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
