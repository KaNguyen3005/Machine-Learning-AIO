import math

def is_int(n):
    return isinstance(n, int)

def is_num(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def sigmoid_func(x):
    return 1 / (1 + math.exp(-x))

def ReLU(x):
    return max(0, x)

def ELU(x):
    if x <= 0:
        return 0.01*(math.exp(x) - 1)
    else:
        return x

def activate_func():
    x = input('x: ')
    func_name = input('func_name: ')
    if not is_num(x):
        print('x must be a number')
        return
    x = float(x)
    match func_name:
        case 'sigmoid':
            print(f'{func_name}: f({x}) = {sigmoid_func(x)}')
        case 'relu':
            print(f'{func_name}: f({x}) = {ReLU(x)}')
        case 'elu':
            print(f'{func_name}: f({x}) = {ELU(x)}')
        case _:
            print(f'{func_name} is not supported')

def cal_f1_score(tp, fp, fn):
    if not is_int(tp):
        print('tp must be int')
        return
    if not is_int(fp):
        print('tp must be int')
        return
    if not is_int(fn):
        print('tp must be int')
        return
    if tp < 0 or fp < 0 or fn < 0:
        print('tp and fp and fn must be int')
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'precision: {precision}')
    print(f'recall: {recall}')
    print(f'f1-score: {f1_score}')


# cal_f1_score(2.1,3,0)
activate_func()