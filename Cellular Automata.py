import numpy as np

#stateArray=[("***"),("** "), ("* *"), ("*  "), (" **"), (" * "),("  *"), ("   ")]
#value=[]

realArray=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "] 

tempArray=realArray

#case = "   " 
for len(realArray)
    print(realArray)
    for position in realArray
        print(realArray)
        
        test = ""
        
        if position == 0
           test+=(realArray[len(realArray)-1])
           test+=(realArray[0])
           test+=(realArray[2])
           continue
        elif position == (len(realArray)-1)
           test+=(realArray[len(realArray)-2])
           test+=(realArray[len(realArray)-1])
           test+=(realArray[0])
           continue
        else
            case+=realArray[position-1]
            case+=realArray[position]
            case+=realArray[postition+1]
        
        match value:
        case "***":
            tempArray[position] = " "
        case "** ":
            tempArray[position] = " "
        case "* *":
            tempArray[position] = " "
        case "*  ":
            tempArray[position] = "*"
        case " **":
            tempArray[position] = "*"
        case " * ":
            tempArray[position] = "*"
        case "  *":
            tempArray[position] = "*"
        case "   ":
            tempArray[position] = " "
            
            
    realArray = tempArray

#def arrayRules():
#    match value:
#        case "***":
#            print(" ")
#       case "** ":
#            print(" ")
#        case "* *":
#            print(" ")
#        case "*  ":
#            print("*")
#        case " **":
#            print("*")
#        case " * ":
#            print("*")
#        case "  *":
#            print("*")
#        case "   ":
#            print(" ")
