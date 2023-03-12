# write  a python script to calculate simple interest
amount=float(input("enter  the amount"))
rate=int(input("enter the rate of the interest"))
time=float(input("enter the time  in years"))
interest=(amount*rate*time)/100
print("interest is {}".format(interest))
