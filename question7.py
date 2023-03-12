# write  a python script   to calculate average of three numbers.entered  by the user
num1,num2,num3=[int(i) for i in  input("enter   three numbers sep by comma").split(",")]
avg=(num1+num2+num3)/3
print("average is {}".format(avg))