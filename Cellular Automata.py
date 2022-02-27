import numpy as np

stateArray=[("***"),("** "), ("* *"), ("*  "), (" **"), (" * "),("  *"), ("   ")]
value=[]

def arrayRules():
    match value:
        case "***":
            print(" ")
        case "** ":
            print(" ")
        case "* *":
            print(" ")
        case "*  ":
            print("*")
        case " **":
            print("*")
        case " * ":
            print("*")
        case "  *":
            print("*")
        case "   ":
            print(" ")
