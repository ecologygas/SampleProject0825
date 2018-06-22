data = list(map(int,input().split()))
d = data[0]
n = data[1]
d = 100**d
if(n==100):
	print(d*(n+1))
else:
	print(d*n)