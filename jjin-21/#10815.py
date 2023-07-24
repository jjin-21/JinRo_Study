#10815

N = int(input())
num_set = set(map(int, input().split()))
M = int(input())
card_ls = list(map(int, input().split()))

result = []
for card in card_ls:
    if card in num_set:
        result.append(1)
    else:
        result.append(0)
print(*result)