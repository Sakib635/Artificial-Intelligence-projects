#TASK-1: Level 1: [1 Point]

#Graph implementation
f = open("input_level01.txt","r")
positions=int(f.readline())
number_connections=int(f.readline())

graph = {i:[] for i in range(positions)}

for i in range(number_connections):
   key,value=map(int,f.readline().split())
   graph[key].append(value)

destination=f.readline()

#BFS implemented
visited={}
distance={}
queue=[]

for node in graph.keys():
    visited[node]=False
    distance[node]=-1

source=0
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

print("Level 1: [1 Point]")
print("Minimum number of moves Nora needs to go to ‘x’-> ",distance[int(destination)])