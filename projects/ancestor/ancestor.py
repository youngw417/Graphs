"""
create a list to hold list of path to ancestor
use queue class, enqueue starting_node in list in form of list
while q > o
get the first enqueued item and saved to path
get the last element
get the neigbors for the item

if no a ances
   add it to final list

for all ances
add each ances to path saved to the list
enqueue the copy of list

check the length of final
get the highest length of array
if the multiple highest length, get the highest value of the last item
and return it


"""
from util import Queue

def get_parents(me, ancestors):
    parents = []
    for i in range(len(ancestors)):
        if ancestors[i][1] == me:
            parents.append(ancestors[i][0])

    return parents

def get_earlist_ancestor(path):  # path = [[1, 2, 5], [2, 4, 6], [3, 6]]
    max_ancestor_list = []
    highest = max([ len(x) for x in path]) # find the max length of list
    for i in range(len(path)):
        if len(path[i]) == highest:  
            # in case of multiple lists with the same highest length, put those into max_ancestor
            max_ancestor_list.append(path[i])
    ancestor = min([x[-1] for x in max_ancestor_list]) # compare the last element and get the lowest
    return ancestor


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue([starting_node])
    path_to_ans = []
    while q.size() > 0:
        # [1, 2, 4]
        path = q.dequeue()
        cur = path[-1]
 
        parents = get_parents(cur, ancestors)
    
        if not parents:  # if no parents with no parents, put the final path in the list
        # if there is no parent for starting node, it will append as [[4]] in path_to_ans
            path_to_ans.append(path)

        else:
            for each in parents:
                new_path = path + [each]
                q.enqueue(new_path)
    if len(path_to_ans) == 1 and len(path_to_ans[0]) == 1: 
        # if there is no parents in starting node as in [[4]]
        return -1          

    return get_earlist_ancestor(path_to_ans)



if __name__ == "__main__":

# mypath =[[2,3,6], [[2,4]], [3,4,5]]

# final =  get_earlist_ancestor(mypath)
# print('final', final)

    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(ancestors, 5))
    print(get_parents(5, ancestors))