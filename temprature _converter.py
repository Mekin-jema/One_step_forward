input=36.50
output=[]
def tempreture_converter(input):
    kelvin=input+273.15
    fahreheit=input*1.8+32.00
    output.append(kelvin)
    output.append(fahreheit)
    return output
result=tempreture_converter(input)
print(result)