#import numpy as np

#stateArray=[("***"),("** "), ("* *"), ("*  "), (" **"), (" * "),("  *"), ("   ")]
#value=[]

realArray=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "] 

tempArray=realArray

#case = "   " 
for i in range(len(realArray)):
    for x in range(len(realArray)):
        print(realArray[x], end="")
        
    for position in range(len(realArray)):
        #print(realArray)
        
        test = ""
        
        if position == 0:
           test+=(realArray[len(realArray)-1])
           test+=(realArray[0])
           test+=(realArray[2])
           continue
        elif position == (len(realArray)-1):
           test+=(realArray[len(realArray)-2])
           test+=(realArray[len(realArray)-1])
           test+=(realArray[0])
           continue
        else:
            test+=realArray[position-1]
            test+=realArray[position]
            test+=realArray[position+1]
        
        # match value:
        # case "***":
        #     tempArray[position] = " "
        # case "** ":
        #     tempArray[position] = " "
        # case "* *":
        #     tempArray[position] = " "
        # case "*  ":
        #     tempArray[position] = "*"
        # case " **":
        #     tempArray[position] = "*"
        # case " * ":
        #     tempArray[position] = "*"
        # case "  *":
        #     tempArray[position] = "*"
        # case "   ":
        #     tempArray[position] = " "
            
            
    realArray = tempArray
    print("\n")

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
