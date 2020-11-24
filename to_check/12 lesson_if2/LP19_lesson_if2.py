
def myfunc(str1,str2):
    if type(str1) is not str or type(str2) is not str:
        return 0
    if str1 == str2:
        return 1
    if len(str1)>len(str2):
        return 2
    if str2=='learn':
        return 3


#dataset0
print(myfunc(0,"string"))
print(myfunc("string",True))
print("\n")
#dataset1
print(myfunc("string","string"))
#dataset2
print(myfunc("string1","string"))
#dataset3
print(myfunc("d","learn"))




