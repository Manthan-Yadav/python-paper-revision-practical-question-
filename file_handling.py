# # file write 
# f=open("data.txt","w")
# f.write("hello everone manthan this side\n")
# f.close

# # file read
# f=open("data.txt","r")
# data=f.read()
# print(data)
# f.close

# # file append
# f=open("data.txt","a")
# f.write("this line is appen\n")
# f.close

# # insert in file 
# f=open("data.txt","r")
# lines=f.readlines()
# f.close()
# lines.insert(1,"this line is inserted\n")
# f=open("data.txt","a")
# f.writelines(lines)
# f.close()

# # delete a line 
# f=open("data.txt","r")
# lines=f.readlines()
# f.close()
# lines.remove("this line is inserted")
# f=open("data.txt","w")
# f.writelines(lines)
# f.close()

# # update file
# f=open("data.txt","r")
# data=f.read()
# f.close()
# data=data.replace("hello world","hello python")
# f=open("data.txt","w")
# f.write(data)
# f.close()

# binary file create
import pickle
# data=[12,13,14,15]
# f=open ("data.dat","wb")
# pickle.dump(data,f)
# f.close()

# # read binary file 
# f=open("data.dat","rb")
# data=pickle.load(f)
# print(data)
# f.close()

# # append ninary file 
# f=open("data.dat","rb")
# data=pickle.load(f)
# f.close()

# data.append("sita")
# f=open("data.dat","wb")
# pickle.dump(data,f)
# f.close()

# # update binary file 
# f=open("data.dat","rb")
# data=pickle.load(f)
# f.close()
# data[1]="krishna"
# f=open("data.dat","wb")
# pickle.dump(data,f)
# f.close()

# # delete binary file
# f=open("data.dat","rb")
# data=pickle.load(f)
# f.close()
# data.remove(12)
# f=open("data.dat","wb")
# pickle.dump(data,f)
# f.close()

# reading csv file 
