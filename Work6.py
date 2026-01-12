import random

# Generate a 3-digit code (0–9)
code_3_digit = [random.randint(0, 9) for _ in range(3)]

# Generate a 4-digit code (1–6)
code_4_digit = [random.randint(1, 6) for _ in range(4)]

# Print results
print("3-digit combination lock code:")
print("".join(map(str, code_3_digit)))

print("4-digit combination lock code:")
print("".join(map(str, code_4_digit)))
