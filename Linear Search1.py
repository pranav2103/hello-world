arr={10,20,30,80,90,50,110,11011,11,300,130}
x=110
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
        return -1
print(search)
