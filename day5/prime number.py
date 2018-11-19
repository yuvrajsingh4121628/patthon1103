counter = 2
while counter < 1000 :
     i = 1
     while i < counter :
         #print "i=1", i
         i = i + 1
         if (counter % i) == 0:
             break
            #print "counter",counter

        
     if i ==counter :
         print"prime number=",counter
     counter = counter + 1
         
