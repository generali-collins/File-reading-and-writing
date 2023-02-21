# Collins Wanga

# How to read and write in a file

# Creating a file
file_one = open("myfile.txt", "w")
A = ["Welcome to Formula 1 \n", "I love car racing\n", "The greatest sport ever\n"]

# Writing data to a file
file_one.write("Hola! \n")
file_one.writelines(A)
file_one.close() 

file_one = open("myfile.txt", "r+")

print("The output of my read function is ")
print(file_one.read())
print()


