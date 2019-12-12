import copy


def create_adjacency_mx(raw_graph,adjacency_mx_size):
    adjacency_mx=[[0]*adjacency_mx_size for i in range(adjacency_mx_size)]
    adress_rows = raw_graph[1::2]

    for i in range(len(adress_rows)) :
        #adjacency_mx[i][i] = 1
        for j in adress_rows[i].split(',') :
            adjacency_mx[i][int(j)-1] = 1
    return(adjacency_mx)

def check_for_strongbound(adjacency_mx,adjacency_mx_size):
    for i in range(adjacency_mx_size) :
        for j in range(adjacency_mx_size) :
            if (adjacency_mx[i][j]!=adjacency_mx[j][i]) : return False
    return True

def check_for_cycles(adjacency_mx,adjacency_mx_size):
    if not (check_for_strongbound(adjacency_mx, adjacency_mx_size)) : print('Graph is oriented')

def depth_check(cur_build, adjacency_mx, adjacency_mx_size):
    for i in range(adjacency_mx_size) :
        if adjacency_mx[int(cur_build[-1])-1][i] == 1 :  
            perm_adjacency_mx = copy.deepcopy(adjacency_mx) #OHRENET` ESLI BI NE DOPER SHO TUT SSILKA VMESTO KOPII PEREDAVALAS` NA OBJEKT DROPNUL BI NAHUI ETU ZADACHU
            perm_adjacency_mx[i][int(cur_build[-1])-1] = 0
            perm_adjacency_mx[int(cur_build[-1])-1][i] = 0
            traf_cur_build = copy.deepcopy(cur_build)
            depth_check(traf_cur_build+str(i+1),perm_adjacency_mx,adjacency_mx_size)
        f = open('traverselits.txt', 'a+')
        f.writelines(cur_build+'\n')
        f.close

def process_traverses(traverse):
    dict_ = {} 
    for letter in traverse: 
        if letter not in dict_.keys(): 
            dict_[letter] = 1 
        else: 
            dict_[letter] += 1 
            
    for i in dict_:
        if dict_.get(i)>1 :
            return(traverse[traverse.find(str(i)):traverse.rfind(str(i))+1])




        





finp = open('tsk2_input.txt')
f = open('traverselits.txt','w')
f.close()
adjacency_mx_size = 0
raw_graph = []
for lines in finp :
    adjacency_mx_size += 1
    raw_graph += lines.strip('\n').split(':')



print (raw_graph)

admx=create_adjacency_mx(raw_graph, adjacency_mx_size)
for i in admx : print (i)
print(check_for_strongbound(admx,adjacency_mx_size))

depth_check('1',admx, adjacency_mx_size)
traverselist = ''

trav = open('traverselits.txt', 'r')

travlist = []
for lines in trav:
    trav_ = process_traverses(lines)
    if travlist is None : travlist += trav_
    if travlist.count(trav_) == 0 : travlist.append(trav_) 
print (travlist)
    


