
my_file = open("a.txt","rt")
my_file1= open("c.txt","wt")
for i in my_file:
    my_file1.write(i)
my_file.close()
my_file1.close()

