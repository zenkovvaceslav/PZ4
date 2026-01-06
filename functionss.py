import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_nested_list(lst):
    total = 0
    
    for element in lst:
        if isinstance(element, (int, float)):
            total += element
        elif isinstance(element, list):
            total += sum_nested_list(element)
    
    return total

def main():
    logger.info("старт")
    
    n = 50
    
    logger.info(f"запуск итеративной функции для n={n}")
    start_time = time.time()
    result_iter = fibonacci_iterative(n)
    end_time = time.time()
    time_iter = end_time - start_time
    
    logger.info(f"итеративная функция завершена за {time_iter:.6f} секунд")
    print(f"итеративная функция: F({n}) = {result_iter}")
    print(f"время выполнения: {time_iter:.6f} секунд")
    

    n_small = 35
    
    logger.info(f"запуск рекурсивной функции для n={n_small}")
    start_time = time.time()
    result_rec_small = fibonacci_recursive(n_small)
    end_time = time.time()
    time_rec_small = end_time - start_time
    
    logger.info(f"рекурсивная функция завершена за {time_rec_small:.6f} секунд")
    print(f"рекурсивная функция: F({n_small}) = {result_rec_small}")
    print(f"время выполнения: {time_rec_small:.6f} секунд")
    
    start_time = time.time()
    result_iter_small = fibonacci_iterative(n_small)
    end_time = time.time()
    time_iter_small = end_time - start_time
    
    print(f"итеративная функция для n={n_small}: {time_iter_small:.6f} секунд")
    print(f"разница во времени для n={n_small}: {time_rec_small/time_iter_small:.2f} раз")

    test_list = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]
    
    logger.info(f"запуск функции подсчета суммы для списка: {test_list}")
    start_time = time.time()
    total_sum = sum_nested_list(test_list)
    end_time = time.time()
    time_sum = end_time - start_time
    
    logger.info(f"функция подсчета суммы завершена за {time_sum:.6f} секунд")
    print(f"сумма элементов списка {test_list}")
    print(f"результат: {total_sum}")
    print(f"время выполнения: {time_sum:.6f} секунд")
    
    manual_sum = 1 + 2 + 3 + 4 + 5 + 6 + (-1) + (-5) + 0
    print(f"проверка расчета: {manual_sum}")
    print(f"результат верен: {total_sum == manual_sum}")
    
    logger.info("программа завершена")

if __name__ == "__main__":
    main()