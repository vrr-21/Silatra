from os import listdir, system
from os.path import isfile

digit1 = 0

newDataPath = "./training-images/Digits_Kartik/"+str(digit1)+"/Right_Hand/Normal/"

files = listdir(newDataPath)
files.sort()
# print(files)

mergeDataPath = "./training-images/Digits/"+str(digit1)+"/Right_Hand/Normal/"

newCount = len(listdir(mergeDataPath)) + 1

print(newCount," images present in "+mergeDataPath)

print("To start transfer, you need to manually edit the program")




for file1 in files:
    system("cp "+newDataPath+file1+" "+mergeDataPath+str(newCount)+".png")
    newCount+=1
print("\nCopied files from "+newDataPath+" to "+mergeDataPath)