import random

# Generate 6 random unique numbers and a bonus number
numbers = random.sample(range(1, 50), 6)
bonus = random.randint(1, 49)

# Print the numbers with a message
print("Here are this week's lucky numbers:")
for i, num in enumerate(numbers):
    print(num, end=' ')
print("(Bonus: {})".format(bonus))
