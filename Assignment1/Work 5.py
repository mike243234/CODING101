POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

talent = float(input('Input talent:'))
pounds = float(input('Input pounds:'))
lots = float(input('Input lots:'))

#convert everything to lots
total_lots = (talent * POUNDS_PER_TALENT * LOTS_PER_POUND) \
             + (pounds * LOTS_PER_POUND) \
             + lots

# Convert lots to grams
total_grams = total_lots * GRAMS_PER_LOT

# Convert grams to kilograms and remaining grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

#result
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
