import os


def mkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def parseable_int(s):
    # https://stackoverflow.com/a/1267145/5277189
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_subsequent_int(string, start_index):
    if(not len(string)):
        return
    index = start_index
    found = False
    parse_started = False
    value = '0'
    while not found:
        if (parseable_int(string[index])):
            parse_started = True
            value += string[index]
        else:
            if parse_started:
                found = True
        index += 1
        if (index > len(string) - 1):
            break
    return int(value)
