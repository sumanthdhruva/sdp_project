n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (i - 1) + "* " * (n - i + 1))
for i in range(1, n):
    print(" " * (n - i - 1) + "* " * (i + 1))
