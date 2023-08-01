res=[]
for m in range(int(input())):
    tmp=0
    K,N,M=map(int,input().split())
    li=list(map(int,input().split()))+[N]
    gap=[1 for i in range(M) if li[i+1]-li[i]>K]
    gage,idx=K,0
    if gap: #충전소 사이 거리가 K보다 먼경우, 
        res.append(tmp)
        continue

    while idx<N:
        if gage==0 and idx not in li: #현재, 연료가 없고 현재위치에 충전소가 없는경우
            idx-=1  # 후진
        elif gage==0 and idx in li: # 현재, 연료가 없고 현재위치에 충전소가 있는 경우
            gage=K # 풀충전
            tmp+=1 #충전소 경유 +1 
        else:
            idx+=1 #연료가 있는경우, 한칸전진
            gage-=1 # 연료 -1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s"%(i+1,res[i]))