my_student =open("student",'wt')
i=1
while i<=13:
    Name =raw_input("Enter the student of name{}".format(i))
    my_student.write(Name+'\n')
    i=i+1
my_student.close()
        
