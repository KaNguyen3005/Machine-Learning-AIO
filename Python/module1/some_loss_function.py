def mae(samples):
    if len(samples) == 0: return 0
    n = len(samples)
    res = 0
    for i in range(0, n):
        y = samples[i][0]
        y0 = samples[i][1]
        res += abs(y - y0)
    return res / n

def mse(samples):
    if len(samples) == 0: return 0
    n = len(samples)
    res = 0
    for i in range(0, n):
        y = samples[i][0]
        y0 = samples[i][1]
        res += (y - y0)*(y - y0)
    return res / n

def loss_func():
    n = input("number of samples: ")
    samples = []
    for i in range(0, n):
        y = input(f'target {i}-th: ')
        y0 = input(f'predict {i}-th: ')
        samples.append([y,y0])
    for y, y0 in samples:
        if not y.isnumberic() or not y0.isnumberic():
            print("samples must be integers")
            return

    func_name = input('loss function: ')
    res = -1
    match func_name:
        case 'mae':
            res = mae(samples)
        case 'mse':
            res = mse(samples)
    print(res)

loss_func()