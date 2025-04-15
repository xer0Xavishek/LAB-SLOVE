def convert_min(time_str):

    hrs = int(time_str.split(":")[0]) 
    mints = int(time_str.split(":")[1])  
    return hrs * 60 + mints 

def trainSort(n, data):
    trains = []  
    
    for index, line in enumerate(data):
        
        bars = line.split()
        t_name = bars[0]  
        dest = bars[4]  
        d_time = bars[-1]  
        mints = convert_min(d_time)  
        trains.append((t_name, dest, mints, index, line))  
 
    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):
            
            if (trains[j][0] < trains[min_idx][0]) or \
               (trains[j][0] == trains[min_idx][0] and trains[j][2] > trains[min_idx][2]) or \
               (trains[j][0] == trains[min_idx][0] and trains[j][2] == trains[min_idx][2] and trains[j][3] < trains[min_idx][3]):
                min_idx = j
    


        if min_idx != i:
            trains[i], trains[min_idx] = trains[min_idx], trains[i]



    for train in trains:
        print(train[4]) 

n = int(input())
data = [input() for i in range(n)]
trainSort(n, data)
