# Working with File
with open('INI5.txt','r') as open_file:
    num_line = 0
    for line in open_file:
        num_line += 1
        if num_line % 2 == 0 or num_line % 2 == 1:
            line = open_file.readline()
            with open('INI5_2.txt','a') as new_file:
                new_file.write(line)
        else:
            continue


