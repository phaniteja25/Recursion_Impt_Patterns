def print_one_sq_with_sum_k(i:int,arr:list,sum:int,s:int,res:list):
    #base condition

    if(i==len(arr)):
        if(sum==s):
            print(res)
            return True
        else:
            return False
    #taking the element in the current index
    res.append(arr[i])
    s+=arr[i]

    if(print_one_sq_with_sum_k(i+1,arr,sum,s,res) == True):
        return True
    res.pop()
    s-=arr[i]

    if(print_one_sq_with_sum_k(i+1,arr,sum,s,res) == True):
        return True
    
    return False



    




if __name__ == "__main__":
    arr=[1,2,1]
    sum=2
    s = 0
    res=[]
    
    print_one_sq_with_sum_k(0,arr,sum,s,res)