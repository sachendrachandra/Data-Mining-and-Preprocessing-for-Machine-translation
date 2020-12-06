import re
import os
ll=-2147483648
for file in os.listdir("/home/sachendra/TSE/T2/pythonFiles"):
    path="/home/sachendra/TSE/T2/pythonFiles/"+str(file)
    print(path)
    # try:

    with open (path) as myfile:
        try:

            data=myfile.read()   
            l=re.split("def",data) 
             
            print(len(l))
            for i in range(1,len(l)):
                l[i]='def'+l[i]

            for s in l[1:]: 
                t=s.split('\n')   
                with open("/home/sachendra/TSE/split2/{}.py".format(ll),"w") as f:
                    f.write(s) 
                ll=ll+1
        except:
            print("error")


