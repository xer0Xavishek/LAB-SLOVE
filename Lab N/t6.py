def sortingAgain(n, st_id, st_mks):

    students = [(st_id[i], st_mks[i]) for i in range(n)]  
    swaps = 0  

    for i in range(n):
        max_i = i
        for j in range(i + 1, n):
            if (students[j][1] > students[max_i][1]) or \
               (students[j][1] == students[max_i][1] and students[j][0] < students[max_i][0]):
                max_i = j
        
        
        if max_i != i:
            students[i], students[max_i] = students[max_i], students[i]
            swaps += 1  
    
    print(f"Minimum swaps: {swaps}")
    for student in students:
        print(f"ID: {student[0]} Mark: {student[1]}")

n = int(input())
st_id = [int(i) for i in input().split()]
st_mks = [int(i) for i in input().split()]
sortingAgain(n, st_id, st_mks)
