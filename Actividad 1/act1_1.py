from statistics import median
def devolver_distintos(int1 : int, int2 : int, int3 : int ):
    my_list = list([int1, int2, int3])

    if sum(my_list) > 15:
        return max(my_list)
    elif sum(my_list) < 10:
        return min(my_list)
    else:
        # for i in my_list:
        #     if max(my_list) != i and min(my_list) != i:
        #         return i
        return median(my_list)    
                
print(devolver_distintos(4,2,8))



