def minTime(machines, goal):
    # Intialise time, items equal to 0. 
    t = 0  
    while (1): 
      
        items = 0
  
        # Calculating items at each second 
        for i in range(len(machines)): 
            items += (t // machines[i]) 
  
        # If items equal to m return time. 
        if (items >= goal): 
            return t 
  
        t += 1 # Increment time 
