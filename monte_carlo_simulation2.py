import random

def f(x):
    return x ** 2

def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині області під кривою."""
    return y <= f(x)

def monte_carlo_simulation(a, b, num_samples):
    """Виконує експеримент методом Монте-Карло та повертає середню площу та точки."""
    points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(num_samples)]
    inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]
    outside_points = [point for point in points if not is_inside(a, b, point[0], point[1])]

    M = len(inside_points)
    N = len(points)
    area = (M / N) * (a * b)

    return area, inside_points, outside_points