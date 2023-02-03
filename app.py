#Write a function, parallel(), that, when called, outputs the outputs the effective resistance of a network of 2 or more resistors connected in parallel. 
# The function should be able to accept a list of numbers of any length.

def parallel(resistor_list):
    size=len(resistor_list)
    if (size >=2):
        sum=0
        paralsum=0

    for i in resistor_list : 
        sum += 1/i
        paralsum+(1/sum)
        print('%2f' %paralsum, "ohms")
        return 0

parallel([100,789,990])


def potential_divider(voltage_supply,resistor_value):
    total_res= sum(resistor_value)

    voltage_drop =[voltage_supply *(resistor/total_res) 
for resistor in resistor_value]

    for x in range(len(resistor_value)):
        print(f"the voltage drop across R{x+1}= {voltage_drop[x]} V")

potential_divider (8,[ 4000,2000])



def temperature_check(temp,condition):
    if condition == "C":
        if temp <35:
            print("the patient is hypothermic")
        elif temp >40:
            print ("the patient is hyperthermic")
        else:
            print(" the patient's temperature is normal")
    elif condition == "F":
        if temp <95:
            print ("the Patient is hypothermic")
        elif temp >104:
            print("the patient is hyperthermic")
        else:
            print ("the patient's temperature is normal")
    else:
        print("not valid")

temperature_check(37 ,"C")
 

           

