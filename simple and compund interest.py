def calcom(principal , interest, tenure):
    for i in range(1,tenure):
        finalamount = principal*(1+(interest/100))**tenure-1
    return finalamount

def calsim(principal , interest, tenure):
    finalamount = principal+((principal*interest*tenure)/100)
    return finalamount


c=calcom(1000,10,2)
print(c)
d=calsim(1000,10,2)
print(d)