def func_1(type_='max'):
    def func_2(lst):
        return eval(f'{type_}(lst)')

    return func_2