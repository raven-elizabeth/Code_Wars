def binary_array_to_number(arr):
    binary_value = ""
    for i in arr:
        binary_value += str(i) # Convert int to string in order to concatenate
    binary = bin(int(binary_value))
    print(binary)
    print(int(binary))
    
    
print(binary_array_to_number([0, 0, 0, 1]))