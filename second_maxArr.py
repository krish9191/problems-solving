if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    x= list(set(arr))
    for item in x:
        for j in range(1,len(x)):
            if x[j] <= x[j-1]:
                x[j-1],x[j]=x[j],x[j-1]



    print(x[len(x)-2])
