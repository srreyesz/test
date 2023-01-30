def create_strings_from_characters(frequencies, string1, string2):

    lis_string1 = []
    lis_string2 = []

    

    for elem_s1 in string1:
        if elem_s1 in frequencies and frequencies[elem_s1] >= 1:
            lis_string1.append(elem_s1)
            frequencies[elem_s1] -= 1
    
    
    lis_string1 = "".join(lis_string1)

    if lis_string1 != string1:
        for elem in lis_string1:
            if elem in frequencies:
                frequencies[elem] += 1
    

    for elem_s2 in string2:
        if elem_s2 in frequencies and frequencies[elem_s2] >= 1:
            lis_string2.append(elem_s2)
            frequencies[elem_s2] -= 1

    lis_string2 = "".join(lis_string2)

    print(string1, string2, lis_string1, lis_string2)

    if lis_string1 == string1 and lis_string2 == string2:
        return 2

    if lis_string1 == string1 or lis_string2 == string2:
        return 1
    
    return 0  
    
def pairs_sum_to_target(list1, list2, target):
    lst_final = []
    for index1 in range(len(list1)):
        for index2 in range(len(list2)):
            if list1[index1] + list2[index2] == target:
                lst = [index1, index2]
                lst_final.append(lst)  
       
    
    return lst_final


z = "hacer un pull request"