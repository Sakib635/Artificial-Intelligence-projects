#Level 2: [2 Points]

#Graph implementation
f = open("input_level02.txt","r")
positions=int(f.readline())
number_connections=int(f.readline())

graph = {i:[] for i in range(positions)}

for i in range(number_connections):
   key,value=map(int,f.readline().split())
   graph[key].append(value)


#taking all the necessary inputs
destination=int(f.readline()) # Lina’s position
source_1=int(f.readline())    # Nora’s position
source_2=int(f.readline()   ) # Lara’s position


def BFS(s):

    visited={}
    distance={}
    queue=[]

    for node in graph.keys():
        visited[node]=False
        distance[node]=-1

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

    return int(distance[int(destination)])
    


Nora_moves=BFS(source_1)
lara_moves=BFS(source_2)

print("Level 2: [2 Points]")
print("Nora can go to ‘x’ with ",Nora_moves, " moves")
print("Lara can go to ‘x’ with ",lara_moves, " moves")

winner=min(Nora_moves,lara_moves)

if (winner==lara_moves):
    if (winner==-1):
        print("Lara can not reach, winner is Nora")
    else:    
        print("Winner is Lara")
else:
    if (winner==-1):
        print("Nora can not reach, winner is Lara")
    else:    
        print("Winner is Nora")
