def print_models(unprint,complete):
    """打印模型"""
    while unprint:
        cur = unprint.pop()
        print('printing model:' + cur)
        complete.append(cur)
def show_models(model):
    print('show all models:')
    for m in model:
        print(m)
