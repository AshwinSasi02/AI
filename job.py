def printJobs(arr,t):
    n=len(arr)

    arr.sort(key=lambda x:x[1],reverse=True)   #sorting

    result= [False]*t    #slots

    jobs= ['0']*t       #job list
    profit=0
    for i in range(n):            #job selection
        for j in range(min(t-1,arr[i][1]-1),-1,-1):

            if result[j] is False:
                result[j]=True
                profit+=arr[i][2]
                jobs[j]=arr[i][0]
                break
    print(jobs)
    print("Profit= ", profit)
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

print("Following is maximum profit sequence of jobs")

printJobs(arr, 3)