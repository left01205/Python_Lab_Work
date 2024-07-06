file1 = open("file1.txt", "r")


content = file1.read()


file1.close()


file2 = open("file2.txt", "w")

content="good morning Vietnam"
file2.write(content)


file2.close()


file3 = open("file3.txt", "a")


file3.write("This is some additional content.")

file3.close()


with open("file1.txt", "r") as source_file:
    with open("file4.txt", "w") as destination_file:
        for line in source_file:
            destination_file.write(line)
