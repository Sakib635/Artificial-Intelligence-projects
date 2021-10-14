

f = open("input.txt","r")
n=int(f.readline())
m=int(f.readline())
print(n)
graph = {i:[] for i in range(n)}

for i in range(m):
   u,v=map(int,f.readline().split())
   graph[u].append(v)
print(graph)