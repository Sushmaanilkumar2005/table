# Multiplication tables from 2 to n
# Range between 1 and 11

n = int(input("Enter the last number: "))

for i in range(2, n + 1):
    print("\nMultiplication Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)