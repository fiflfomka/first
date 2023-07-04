
N = int(input())
l = (input().split())
for i in range(N):
	l[i] = int(l[i])
l = [0,0] + l
sums = l.copy()
for i in range(2,N+2):
	sums[i] = max( l[i-1], l[i-2] ) + l[i]
print(sums[-1])
