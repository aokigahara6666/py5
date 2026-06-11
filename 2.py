import random
import math
import statistics

numbers = [random.randint(1, 100) for _ in range(100)]

mean_val = statistics.mean(numbers)
median_val = statistics.median(numbers)
stdev_val = statistics.stdev(numbers)
sqrt_sum = round(math.sqrt(sum(numbers)), 2)

print(f"Среднее: {mean_val}, Медиана: {median_val}, Стандартное отклонение: {round(stdev_val, 2)}, Корень из суммы: {sqrt_sum}")