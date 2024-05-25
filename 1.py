# "Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
# "Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
# Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
# Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
# Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".

# !pip install pulp
import pulp

model = pulp.LpProblem("Maximaze_product", pulp.LpMaximize)  # Максимізація

limonad = pulp.LpVariable('Limonad', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit juice', lowBound=0, cat='Integer')

# Цільова функція
model += limonad + fruit_juice, "Total products"  # Максимізувати 

# Обмеження
model += 2 * limonad + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * limonad <= 50, "Sugar Constraint"
model += 1 * limonad <= 30, "Lemon Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

model.solve()

# статус розв'язку
status = pulp.LpStatus[model.status]
print("Status:", status)

for variable in model.variables():
    print(f"{variable.name} = {variable.varValue}")
# Вартість цільової функції
print(f"Total: = {pulp.value(model.objective)}")


if status == "Optimal":
    print(f"\nВраховуючи обмеження максимально можливо виробити напоїв: {int(limonad.varValue + fruit_juice.varValue)}")
    print("З них:")
    print(f"   Лимонаду: {int(limonad.varValue)}")
    print(f"   Фруктового соку: {int(fruit_juice.varValue)}")
          