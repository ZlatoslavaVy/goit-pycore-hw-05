def caching_fibonacci():
    # Словник для кешування
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1    
        elif n in cache:
            return cache[n]
        if n not in cache:    
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    return fibonacci


# Блок, що не дає запускатись прикладам при імпорті модуля в інший файл
if __name__ == "__main__":
# Отримуємо функцію fibonacci
    fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610
