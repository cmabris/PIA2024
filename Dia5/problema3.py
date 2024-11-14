def ceros_repetidos(*args):
    if len(args) < 2:
        return False
    for i in range(1, len(args)):
        if args[i] == 0 and args[i-1] == 0:
            return True
    return False

def ceros_repetidos_v2(*args):
    i = 1
    while i<len(args) and (args[i] == 0 and args[i-1]):
        i += 1
    if i == len(args):
        return False
    return True
