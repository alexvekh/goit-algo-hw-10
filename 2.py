import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random
from monte_carlo_simulation import monte_carlo_simulation

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа


# ------- Монте Карло ----------------------------------------
# Верхня і нижня межа, як видно на графікуб це по x. Знаходимо контрольні точки для визначення прямокутника
a_x = a
a_y = f(a)  # 0 (0, 0)
b_x = b
b_y = f(b)  # 4 (2, 4)

# розмір прямокутника
# Sq = b * f(b)  # or b * b_y
num_experiments = 100
S = monte_carlo_simulation(b_x, b_y, num_experiments) # (a, b, num_experiments)

print("Площа за методом Монте-Карло", S)


# ------- Перевірка ------------------------------------------
# Обчислення площі scipy QUAD
result, error = spi.quad(f, a, b)
print("Теоретична площа (scipy.integrate.quad): ", result)
print(f"Проведено {num_experiments} серій генерацій точок")
print(f"Різниця: {abs(result - S)}, Відхилення: {abs((result - S)/result) * 100}%")


# ------- Графік області (без візуалізації точок) ------------
# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='green', alpha=0.3)
ax.fill_between(ix, iy, b_y, color='red', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

