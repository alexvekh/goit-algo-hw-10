import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
from monte_carlo_simulation3 import monte_carlo_simulation, f

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# ------- Монте Карло ----------------------------------------
# Верхня і нижня межа, як видно на графіку, це по x. Знаходимо контрольні точки для визначення прямокутника
b_x = b
b_y = f(b)  # 4 (2, 4)

# розмір прямокутника
num_samples = 1500
S, inside_points, outside_points = monte_carlo_simulation(b_x, b_y, num_samples) # (a, b, num_samples)

print("Площа за методом Монте-Карло", S)

# ------- Перевірка ------------------------------------------
# Обчислення площі scipy QUAD
result, error = spi.quad(f, a, b)
print("Теоретична площа (scipy.integrate.quad): ", result)

# ------- Графік ----------------------------------------------
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
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Додавання точок до графіка
if inside_points:
    inside_x, inside_y = zip(*inside_points)
    ax.scatter(inside_x, inside_y, color='green', s=1, label='Inside points')
if outside_points:
    outside_x, outside_y = zip(*outside_points)
    ax.scatter(outside_x, outside_y, color='red', s=1, label='Outside points')

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
plt.legend()
plt.show()