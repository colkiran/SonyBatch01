
fruits = [
    ('apple', 285),
    ('orange', 80),
    ('pineapple', 60),
    ("grapes", 120),
    ('gauva', 110),
    ('banana', 70),
    ('mango', 240),
    ('strawberry', 385)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit for fruit in fruits]
print(price)
print("-" * 60)

price = [(fruit[0], fruit[1]) for fruit in fruits]
print(f'price :{price}')
print("-" * 60)

price = [fruit[1] for fruit in fruits]
print(price)
print("-" * 60)

price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit  in fruits if fruit[1] > 100]
print(f'price :{price}')
