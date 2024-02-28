numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = [float(num) for num in numbers.split()]
print("List of floats:", numbers_list)
average = sum(numbers_list) / len(numbers_list)
print("Average:", average)