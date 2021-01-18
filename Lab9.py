# Yong He
# 500570639

# ***INSTRUCTIONS***
# Failure to follow the instructions will result in a mark of 0 on the lab, with no exceptions
# Do not edit the code ANYWHERE other than where indicated
# The code which you write should not produce any additional output
# When running your file, the only output should be the output from the tests, which are already provided
# Submit your file with the name Lab9.py
# Insert your name and your student number as comments where indicated at the beginning of the file

# In this lab, you will be writing an function to find the minimum spanning tree in a graph
# Graphs will be input as an list of edges. Each edge will be a tuple of the form (u,v,w)
# Where u and v represent the endpoints of an edge, and w represents the cost of that edge
# The function will also take as input n, the number of vertices in the graph
# The graph is undirected(you can travel from u to v or from v to u)
# Your function should output a list of edges from the original graph which form the minumum spanning tree
# You may write helper functions if needed

# Complete the following function
def minimum_spanning_tree(graph, n):
    result = []
    lengths = alllengths(graph)
    for cost in lengths:
        for i in graph:
            if i[2] == cost:
                checkconnection(result,i)

    return result[0]
# Add helper functions here if needed
def alllengths (graph):
    result = []
    for i in graph:
        if i[2] not in result:
            result.append(i[2])
    result.sort()
    return result
def checkconnection(list1, list2):
    appended = False
    index = 0
    whereappended = 0
    if len(list1) == 0:
        list1.append([list2])
        return
    for lis in list1:
        counter = 0
        count1 = 0
        count2 = 0
        for tup in lis:
            temp = [tup[0],tup[1]]
            #print("Comparing {} to {} and {} to {}".format(list2[0],temp, list2[1],temp))
            if (list2[0] in temp or list2[1] in temp):
                counter+=1
                if list2[0] in temp:
                    count1 +=1
                if list2[1] in temp:
                    count2 +=1
        rejected = False
        check1 = False
        if appended == True and ((count1 == 0 and count2 != 0) or (count1 != 0 and count2 == 0)):
            for i in list1[whereappended]:
                for e in list1[index]:
                    temp2 = [i[0],i[1]]
                    if e[0] in temp2:
                        check1 = True
                    if e[1] in temp2 and check1 == True:
                        rejected = True
            if rejected == False:
                list1[whereappended].extend(list1[index])
                list1[index] = [(None,None,None)]
        if ((count1 == 0 and count2 != 0) or (count1 != 0 and count2 == 0)) and appended == False:
            lis.append(list2)
            appended = True
            whereappended = index
        

        index +=1
    if appended == False:
        list1.append([list2])
    

            

# DO NOT EDIT THE CODE BELOW THIS LINE

def print_graph(graph):
    k = 0
    for e in graph:
        k += e[2]
    print("Minimum Spanning Tree")
    print("---------------------")
    print("Weight:\t" + str(k))
    print("Edges:")
    print(graph)
    print("#####################\n\n")


g1 = [
    (0,1,2),
    (0,2,2),
    (1,2,1)
]

g2 = [
    (0,1,4),
    (0,2,3),
    (0,3,2),
    (0,4,7),
    (1,3,3),
    (2,3,1),
]

g3 = [
    (0,1,4),
    (0,2,3),
    (0,5,7),
    (2,3,4),
    (1,3,2),
    (2,4,7),
    (4,5,4),
    (5,9,1),
    (8,9,3),
    (5,8,2),
    (1,7,10),
    (5,6,5),
    (6,7,2),
    (7,8,1),
]

mst1 = minimum_spanning_tree(g1, 3)
print_graph(mst1) # Expeted Weight: 3

mst2 = minimum_spanning_tree(g2, 5)
print_graph(mst2) # Expeted Weight: 13

mst3 = minimum_spanning_tree(g3, 10)
print_graph(mst3) # Expeted Weight: 26
