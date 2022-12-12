from logger import log
@log

def greatings():
    '''Вывод приветствия'''

    print('Привествуем вас в нашем Калькуляторе')

@log
def input_exp():
    '''Запрос даных'''

    return input('Введите выражение (или exit для выхода): ')


@log
def print_answer(result):
    '''Вывод результата'''

    print(f'результат = {result}')
