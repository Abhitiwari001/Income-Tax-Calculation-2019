#!/usr/bin/python3

def sixty(age,z):
    tax=0
    if z<=250000:
        pass
    elif 250000<=z and z<=500000:
        tax=5/100 * (z-250000)
        if z<=350000:
            tax=tax-2500
            if tax<0:
                tax=0
        cess=tax*0.04
        tax+=cess
     
    elif 500000<=z and z<=1000000:
        tax += (0.05*(250000))
        tax += (0.2 * (z-500000))
        cess = 0.04*tax
        tax += cess

    elif z>1000000:
        tax += (0.05*(250000))
        tax += (0.2 * (500000))
        tax += (0.3*(z-1000000))
        cess = tax * 0.04
        tax += cess
    print("tax is :{}".format(tax))

def sixtyeight(age,z):
    tax=0
    if z<=300000:
        pass
    elif z>=300000 and z<500000:
        tax=5/100 * (z-300000)
        if z<=350000:
            tax=tax-2500
            if tax<0:
                tax=0
        cess=0.04*tax
        tax+=cess
        
    elif z>=500000 and z<=1000000:
        tax += (0.05*(200000))
        tax += (0.2*(z-500000))
        cess = 0.04*tax
        tax += cess
    elif z>1000000:
        tax += (0.05*(200000))
        tax += (0.2*(500000))
        tax += (0.3*(z-1000000))
        cess = 0.04*tax
        tax += cess
    print("Tax is :{}".format(tax))

def aboveeighty(age,z):
    tax=0
    if z<=500000:
        pass
    elif 500000<z<1000000:
        tax=(0.2*(z-500000))
        if z<=350000:
            tax=tax-2500
            if tax<0:
                tax=0
        cess=tax*0.04
        tax+=cess
    elif z>=1000000:
        tax += (0.2*(500000));
        tax += (0.3 * (z-1000000));
        cess = 0.04*tax;
        tax += cess;
    
    print("Tax is :{}".format(tax))

if __name__=="__main__":
    #Salary

    salary=int(input("Salary:"))

    #income from other resources

    extra=int(input("Income from other Resources:"))
    #total salary

    total=salary+extra

    #deductions

    #print("Enter deductions\n")

    #d80C=int(input("80C (PF,PPF,Insurance Premium):"))

    #med=int(input("80D (Medical Insurance Premium):"))

    #bi=int(input("80TTA(Bank Account Interest):"))

    deductions=int(input("Enter Total Deductions"))
    #deductions=d80C+med+bi

    #total deductions

    print("Total Deductions are:{}".format(deductions))

    #Gross taxable income

    gross=total-deductions

    print("Gross Taxable Income:{}".format(gross))

    earning=input("Are you Salaried Answer in Y/N:")

    z=gross
    #if person is earning
    if earning=="yes" or earning=="Y":
        p=40000
        z=gross - p
    print("Now Gross Taxable Income for EMPLOYERS OR PENSIONER -{}".format(z))
    age=int(input("Enter Your Age"))
    if age<60:
        sixty(age,z)
    elif 60<=age<80:
        sixtyeight(age,z)
    else:
        aboveeighty(age,salary,z)
 






