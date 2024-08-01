def print_all_subsequences(i:int,arr:list,res:list):

    #base case

    if(i==len(arr)):
        print(res)
        return
    #take the element present in the current position
    res.append(arr[i])
    print_all_subsequences(i+1,arr,res)
    #remove the previously taken element
    res.pop()
    print_all_subsequences(i+1,arr,res)


if __name__ == "__main__":
    arr = [1,2,3]
    res=[]
    print_all_subsequences(0,arr,res)
    
    