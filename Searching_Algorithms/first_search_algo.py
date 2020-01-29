grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right


def neihbours(curr_node,r,c,delta=delta):
    neihbours_list = []
    for e in delta:
        r_val = curr_node[0]+e[0]
        c_val = curr_node[1]+e[1]
        if ((r_val>=0 and r_val<=r) and (c_val>=0 and c_val<=c)):
            neihbours_list.append((r_val,c_val))
    return neihbours_list




def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    open_set = set()
    open_list =[]
    open_set_costs = []
    closed_set = set()
    expansion_list = []
    #make the init node as start
    node = tuple(init)
    #get the  shape of grid
    r = len(grid)-1
    c = len(grid[0])-1
    
    #update the initial cost function to cost
    updated_cost = 0
    min_idx = 0
    min_cost = 0
    #adding the init node to open set  along with generate its cost.  
    open_set.add(node)
    open_list.append(node)
    open_set_costs.append(updated_cost)
    while node != tuple(goal):

        expansion_list = neihbours(node,r,c)
        del open_set_costs[min_idx]
        #update the closed set 
        closed_set.add(node)
        #update the open set 
        open_set.discard(node)
        del open_list[min_idx]
        #update the cost of current iteration.
        #updated_cost += cost
        updated_cost = min_cost+cost
        for e in expansion_list:
            if((e not in closed_set) and (e not in open_set)and (grid[e[0]][e[1]] !=1) ):                
                open_set_costs.append(updated_cost)
                open_set.add(e) 
                open_list.append(e)
        print(open_list,' ',open_set_costs)
        #print(node,' ',expansion_list)
        ##Updates for the next loop
        min_cost = min(open_set_costs)
        min_idx = open_set_costs.index(min_cost)
        node = open_list[min_idx]
    return open_list

open_list = search(grid,init,goal,cost)
