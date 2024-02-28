real_part1 = float(input("Enter the real part of the first complex number: "))
imag_part1 = float(input("Enter the imaginary part of the first complex number: "))
real_part2 = float(input("Enter the real part of the second complex number: "))
imag_part2 = float(input("Enter the imaginary part of the second complex number: "))
z1 = complex(real_part1, imag_part1)
z2 = complex(real_part2, imag_part2)
result = z1 + z2
print("Addition is:", result)
