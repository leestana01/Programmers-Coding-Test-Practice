solution = lambda n, arr1, arr2 : [bin(i|j)[2:].replace('1','#').replace('0',' ') if len(bin(i|j)[2:]) == n else ('0'*(n-len(bin(i|j)[2:])) + bin(i|j)[2:]).replace('1','#').replace('0',' ') for i,j in zip(arr1,arr2)]
