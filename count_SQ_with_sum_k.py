def print_count_SQ_with_sum_k(i:int,arr:list,sum:int,s:int,res:list):

    if(i == len(arr)):
        if(s == sum):
            return 1
        else:
            return 0
    
    res.append(arr[i])
    s+=arr[i]

    l = print_count_SQ_with_sum_k(i+1,arr,sum,s,res)
    res.pop()
    s-=arr[i]

    r = print_count_SQ_with_sum_k(i+1,arr,sum,s,res)

    return l+r

if __name__ == "__main__":
    arr=[1,2,1]
    sum=2
    s = 0
    res=[]
    
    print(print_count_SQ_with_sum_k(0,arr,sum,s,res))