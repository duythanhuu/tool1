# A Python program to demonstrate working of
# findall()
import re
import re
from pathlib import Path
import os.path
from os import path
import os

# Python code to convert string to list
def Convert(string):
    li = list(string.split("\""))
    return li
  

# Python program to convert a list to string 
# Function to convert  
def VlistToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += "\"Valid variant " + ele + "\"\n"
    
    # return string  
    return str1  

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

# input #=================================================================================================================================================
print("\nEnter txt base path: ")
txtpath = input()
# txtpath = r"C:\Users\duyze\OneDrive\Desktop\_workspace\capture2text\RE.txt"
while path.exists(txtpath) == False:
    print("\nNot found the txt path above ...\n\nPlease Enter right txt path again: ")
    txtpath = input()
try:
    print("\nStarting...\n")

    txtfile = open(txtpath).read()

    #results = re.findall("Bosch.*: \t", txtfile)


    ####################################################################################
    temp1 = listToString(re.findall("\d+[(]\d+[)]", txtfile))    

    temp2 = re.sub("[(]\d+[)]", "\"", temp1)[:-1]
    list3 = Convert(temp2)
    list4 = []
    for i in list3:
        if i not in list4:
            list4.append(i)

    temp5 = VlistToString (list4) + "\n\--------------------------------------------\n"
    # print(temp5)
    

    ####################################################################################
    # str1 = listToString(re.sub("BoschVarCode: \tVar\d+[(]1[)]\t - CustomerVarCode[(]BYTE[)]: \t", "\"", txtfile))
    str1 = listToString(re.sub("BoschVarCode.*[(]1[)].*CustomerVarCode[(]BYTE[)]: \t", "\"", txtfile))
    str1 = listToString(re.sub("BoschVarCode.*CustomerVarCode[(]BYTE[)]: \t", "", str1))
    str1 = listToString(re.sub("\n\"", "\"\n\"", str1)) + "\""
    # print(str1)
    
    sss = temp5 + str1
    # print(sss)

    stubFile = open("_result.txt",'w')
    stubFile.write(sss)
    stubFile.close()
    
    print("\n\nTool run completed ...\n")
    
except ValueError as outputError:
    print(outputError)  

os.system("pause")