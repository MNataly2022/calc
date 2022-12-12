import view
from logger import log
import model


@log
def start():
    """Стартовая функция"""
    view.greatings()
    while True:
        exp = view.input_exp()
        if exp == "exit":
            break
        view.print_answer(model.calc(exp))
