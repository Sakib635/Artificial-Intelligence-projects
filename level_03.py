#Level 3: [2 Point]

#Graph implementation
f = open("input_level03.txt","r")
positions=int(f.readline())
number_connections=int(f.readline())

graph = {i:[] for i in range(positions)}

for i in range(number_connections):
   key,value=map(int,f.readline().split())
   graph[value].append(key)

#taking all the necessary inputs
s=int(f.readline())  # ’x’-Lina’s position
n=int(f.readline())  # ‘k’- number of participants

k=[] # list of positions of participants
for j in range(n):
    k.append(int(f.readline()))


#BFS implemented
visited={}
distance={}
queue=[]

for node in graph.keys():
    visited[node]=False
    distance[node]=float('inf')

source=s
visited[source]=True
distance[source]=0
queue.append(source)

while len(queue)>0:
    u=queue.pop(0)
 
    for v in graph[u]:
        if not visited[v]: 
           visited[v]=True
        
           distance[v]=distance[u]+1
           queue.append(v) 

min_path=float('inf')
for i in range(n):
    min_path=min(min_path,distance[k[i]])

print("Level 3: [2 Point]")
print("Minimum number of moves the winner needed to go to ‘x’ is:  ",min_path)