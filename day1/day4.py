import sqlite3
conn =sqlite3.connect("zoo")
c=conn.cursor()

#c.execute("""create table zoo
 #           (id integer,
  #          first text,
   #         last text,
    #        pay integer)
     #        """)
     


zoo = open("F:/Database/zoo/zoo.csv","rt")
read_zoo=zoo.readlines()

print read_zoo

