
graph = {
  '0' : ['1','2','3'],
  '1' : ['3', '4'],
  '2' : ['3'],
  '3' : ['5','6'],
  '4' : ['7','8'],
  '5' : ['6',],
  '6' : ['7'],
  '7' : ['8'],
  '8' : []
}
visited={}
distance={}
parent={}
BFSlist=[]
queue=[]

for node in graph.keys():
    visited[node]=False
    parent[node]=None
    distance[node]=-1

source='0'
visited[source]=True
distance[source]=0
queue.append(source)

while len(queue)>0:
    u=queue.pop(0)
    BFSlist.append(u)
    for v in graph[u]:
        if not visited[v]:  #if not true, 
           visited[v]=True
           parent[v]=u
           distance[v]=distance[u]+1
           queue.append(v) 


print(graph)

