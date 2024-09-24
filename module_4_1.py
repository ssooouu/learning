from fake_math import divide as fake
from true_math import divide as true

result1 = fake(69, 3)
result2 = fake(3, 0)
result3 = true(49, 7)
result4 = true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
