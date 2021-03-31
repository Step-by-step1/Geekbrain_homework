num_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_to_read = open("exercise_4.txt")
new_file = open("exercise_4_new.txt", "w")
new_file.writelines([line.replace(line.split()[0], num_dict[line.split()[0]]) for line in file_to_read.readlines()])
file_to_read.close()
new_file.close()

