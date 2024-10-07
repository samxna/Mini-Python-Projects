# Samina Ahmed | 220023354 | 04/2023
# IN0007 Lab 2 Assessment | Q1

# Open the file in write mode
file = open("self.txt", "w")

# Write the questions and answers to the file
file.write("What is your name?\n")
file.write("Samina\n")
file.write("What is your favourite food?\n")
file.write("Sunday roast\n")
file.write("What is your favourite holiday destination?\n")
file.write("Dubai\n")

# Close the file
file.close()

# # Open the file in read mode and print its content
# file = open("self.txt", "r")
# print(file.read())
# file.close()

# def count_lines(filename):
#     """
#     This function takes a filename as input and returns the number of lines in the file.
#     """
#     with open(filename, "r") as file:
#         lines = file.readlines()
#         return len(lines)

# # # Defining the parameter for the input to get an output from the above functions. 
# # filename = "self.txt"

# print("\n")
# print("No. of lines =", count_lines(filename))

def print_even_lines(filename):
    """
    This function takes a filename as input and prints all the even lines (i.e. answers) from the file.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(1, len(lines), 2): 
            print(lines[i].strip())


# Defining the parameter for the input to get an output from the above functions. 
filename = "self.txt"

print("\n")
print_even_lines(filename)


