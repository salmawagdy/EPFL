def convert():
    celsius= input("Enter a temp in Celsius ")
    fehrenheit= (float(celsius)*9/5)+32
    return str(celsius)+"degrees Celsius are  "+str(fehrenheit)

print(convert())
