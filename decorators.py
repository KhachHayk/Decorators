from _datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.now().strftime('%d-%m-%Y время %H:%M:%S')
        old_func_name = old_function.__name__
        res = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'Время вызова функции - {call_time},\n'
                       f'имя функции - {old_func_name},\n'
                       f'аргументы функции - {args, kwargs},\n'
                       f'значение функции - {res}\n')
        return res
    return new_function


def logger2(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.now().strftime('%d-%m-%Y время %H:%M:%S')
            old_func_name = old_function.__name__
            res = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'Время вызова функции - {call_time},\n'
                           f'имя функции - {old_func_name},\n'
                           f'аргументы функции - {args, kwargs},\n'
                           f'значение функции - {res}. \n\n'
                           f'\n')
            return res
        return new_function
    return __logger
