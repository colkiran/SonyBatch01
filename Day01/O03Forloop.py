
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 31):
    # if i > 20:
    #     break           # stop the iteration
    if i % 2 == 1:
        continue            # skip the current iteration
    print(i, end=" ")
else:
    print("\nCompleted generating numbers")
