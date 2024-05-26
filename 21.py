import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

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
Sq = b * f(b)  # b * b_y
print('Площа прямокутної області генерації точок', Sq)

def is_inside(a, b, x, y):  #  b_x, b_y
    """Перевіряє, чи знаходиться точка (x, y) всередині області під кривою."""
    return y <= f(x)

# Генерація випадкових точок
num_samples = 1500
points = [(random.uniform(a, b), random.uniform(0, b_y)) for _ in range(num_samples)]

# Відбір точок, що знаходяться всередині області
inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]
outside_points = [point for point in points if not is_inside(a, b, point[0], point[1])]

# Кількість усіх точок та точок всередині
N = len(points)
M = len(inside_points)


print(f"Згенеровано {N} точок, з них попали в зону під криву {M} точок")

# Площа за методом Монте-Карло
Sm = (M / N) * (b_x * b_y)  # Площа за методом Монте-Карло

print("Площа за методом Монте-Карло", Sm)

# ------- Перевірка ------------------------------------------
# Обчислення площі scipy QUAD
result, error = spi.quad(f, a, b)
print("Теоретична площа: ", result)

print(f"Різниця: {abs(result - Sm)}, Відхилення: {abs((result - Sm)/result) * 100}%")
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
