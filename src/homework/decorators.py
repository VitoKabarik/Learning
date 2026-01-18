from functools import wraps


def log(filename = ''):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if filename:
                with open(filename, 'a') as file:
                    try:
                        result = function(*args, **kwargs)
                    except Exception as err_mess:
                        file.write(f'{function.__name__} error: {err_mess}. Inputs: {args}, {kwargs}\n')
                    else:
                        file.write(f'{function.__name__} ok.\n')
                        return result
            else:
                try:
                    result = function(*args, **kwargs)
                except Exception as err_mess:
                    print(f'{function.__name__} error: {err_mess}. Inputs: {args}, {kwargs}')
                else:
                    print(f'{function.__name__} ok')
                    return result
        return wrapper
    return decorator
