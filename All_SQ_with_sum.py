def print_sq_with_sum(i:int,arr:list,sum:int,res:list,s:int):

    if(i == len(arr)):
        if(sum == s):
            print(res)
        return
    
    #taking the current index element
    res.append(arr[i])
    s += arr[i]
    print_sq_with_sum(i+1,arr,sum,res,s)
    #removing the previously added element
    res.pop()
    s-=arr[i]
    print_sq_with_sum(i+1,arr,sum,res,s)



    

if __name__ =="__main__":
    arr=  [1,3,2]
    sum = 2
    res=[]

    print_sq_with_sum(0,arr,sum,res,0)
