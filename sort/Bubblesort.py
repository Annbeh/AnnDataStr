

def bubblesort (alist):
    for num in range(len(alist)):
        for i in range(num-1):
            if alist[i]> alist[i+1]:
                
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
alist = [2,56,2,1,36,69,98]
bubblesort(alist)
print(alist)
