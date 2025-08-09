# Print the pattern 
row = int(input("Enter the num of rows :"))
for i in range(1, row+1):
    for j in range (1, 2*i):
        print("*", end="")
    print()    # This is used to print in next line