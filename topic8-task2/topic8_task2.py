import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]: 
    """
    Генерує дійсні числа з текстового рядка.
    
    Функція знаходить усі цілі та дійсні числа в тексті за допомогою
    регулярного виразу та повертає їх як генератор float значень.
    
    Args:
        text (str): Вхідний текстовий рядок для пошуку чисел.
        
    Yields:
        float: Знайдені числа у форматі float.
    """
    #Регулярний вираз для пошуку дійсних чисел
    pattern = r"\b\d+\.?\d*\b"
    #Всі співпадіння в тексті
    matches = re.finditer(pattern, text)
    #Повертає кожне знайдене число як float по одному, не припиняючи своєї роботи до самого кінця
    for match in matches:
        yield float(match.group())

#Обчислює загальну суму всіх чисел у тексті, використовуючи генератор
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]):
    #Повертає об'єкт-генератор
    number_generator = func(text)
    #sum() приймає генератор
    total_sum = sum(number_generator)
    return total_sum

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    # Виведе: Загальний дохід: 1351.46
