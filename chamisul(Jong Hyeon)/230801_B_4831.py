for m in range(int(input())):
    K,N,M=map(int,input().split())
    li=list(map(int,input().split()))+[N]
    idx,res=0,0
    while idx<N:
        res+=1
        t=[i for i in range(idx+1,idx+K+1) if i in li]
        if t:
            idx=t[-1]
        else:
            res=1
            break
    print(f'#{m+1} {res-1}')