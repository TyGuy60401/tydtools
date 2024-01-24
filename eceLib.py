import sys

def volt_divide(vin: float, rs: list):
    """Return a list containing the voltages across each resistor in the list rs
    
    Parameters
    ----------
    vin:    Voltage to be divided
    rs: List of resistors that are dividing the voltage vin
    
    Returns
    -------
    vs: List of divided voltages corresponding to the resistors in rs
    """
    rtot = sum(rs)
    vs = []
    for r in rs:
        vs.append(vin * r / rtot)
    return vs
    

def calc2Para(res1: float, res2: float):
    """
    Deprecated. Used to calculate the value of two 
    resistors or inductors in parallel.
    Use parallel() instead.
    """
    return (res1*res2)/(res1 + res2)

def parallel(*vs):
    """Return the parallel equivalent value of the values passed"""
    sum = 0
    for v in vs:
        sum += 1/v
    return 1/sum


def opampSum():
    voltDict = {}
    getInput = True
    i = 0
    Rf = float(input("Enter a resistance for Rf: "))

    while getInput:
        voltage = input("Enter a voltage (end for end) ")
        if voltage == "end".lower():
            getInput = False
        else:
            resistance = float(input("Enter a resistance: "))
            voltage = float(voltage)
            
            dictString = str(i)
            voltDict[dictString] = [voltage, resistance]
            i += 1
            print(voltDict)
    
    if len(voltDict) > 0:
        sumInside = 0
        for ii in range(len(voltDict)):
            sumInside += voltDict[ii][0]/voltDict[ii][1]
        ans = -Rf * (sumInside)
        print("Answer is: ")
        print(ans)
        print("  ---  ")
    

if __name__ == '__main__':
    # Testing the parallel function
    vList = []
    for arg in sys.argv[1:]:
        vList.append(float(arg))
    print(parallel(vList))

