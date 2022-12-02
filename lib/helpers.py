from lib.config import DEBUG_MODE, TEST_MODE

def log(string):
    global DEBUG_MODE
    if DEBUG_MODE:
        print(string)
        

def get_input(fname):
    in_str = ''
    dir = "test" if TEST_MODE else "inputs"
    fname = f"./{dir}/{fname}"
    with open(fname, 'r') as f:
        in_str = f.read()

    return in_str.strip('\n')


def get_ints_by_lines(fname):
    in_str = get_input(fname)
    return [
        int(line.strip('\n')) for line in in_str.split('\n') if line
    ]


def get_strings_by_lines(fname):
    in_str = get_input(fname)
    return [
        line.strip('\n') for line in in_str.split('\n') if line
    ]
