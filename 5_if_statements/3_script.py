age = 28

# 'if-elif' chain to test one condition
if age < 2:
    life_stage = 'baby'
elif age < 4:
    life_stage = 'toddler'
elif age < 13:
    life_stage = 'kid'
elif age < 20:
    life_stage = 'teenager'
elif age < 65:
    life_stage = 'adult'
elif age >= 65:
    life_stage = 'elder'

print(f"you are a {life_stage}")

# notes
    # 'else' can ommitted for more accuracy in a chain 