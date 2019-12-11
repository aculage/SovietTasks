def create_adjacency_mx(raw_graph,adjacency_mx_size):
    adjacency_mx=[[0]*adjacency_mx_size for i in range(adjacency_mx_size)]
    adress_rows = raw_graph[1::2]

    for i in range(len(adress_rows)) :
        adjacency_mx[i][i] = 1
        for j in adress_rows[i].split(',') :
            adjacency_mx[i][int(j)-1] = 1
    return(adjacency_mx)

def check_for_strongbound(adjacency_mx,adjacency_mx_size):
    for i in range(adjacency_mx_size) :
        for j in range(adjacency_mx_size) :
            if (adjacency_mx[i][j]!=adjacency_mx[j][i]) : return False
    return True



finp = open('tsk2_input.txt')

adjacency_mx_size = 0
raw_graph = []
for lines in finp :
    adjacency_mx_size += 1
    raw_graph += lines.strip('\n').split(':')



print (raw_graph)

admx=create_adjacency_mx(raw_graph, adjacency_mx_size)
for i in admx : print (i)
print(check_for_strongbound(admx,adjacency_mx_size))

