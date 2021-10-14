graph = {
  '0' : ['1','2','3'],
  '1' : ['4'],
  '2' : [],
  '3' : ['5','6'],
  '4' : ['7','8'],
  '5' : [],
  '6' : [],
  '7' : [],
  '8' : []
}

color={}
parent={}
traversal_time={}
DFS_output=[]

for node in graph.keys():
    color[node]='W'
    parent[node]=None
    traversal_time[node]=[-1,-1]

#print(color)
time=0

def DFS(u):
    global time
    color[u]='G'
    traversal_time[u][0]=time
    time+=1
    DFS_output.append(u)

    for v in graph[u]:
        if color[v]=='W':
            parent[v]=u
            DFS(v)
    
    color[u]='B'
    traversal_time[u][1]=time
    time+=1

DFS('0')
print(DFS_output)
#print(parent)
print(traversal_time)
#print('')
for node in graph.keys():
    print(node, "-->",traversal_time[node])
