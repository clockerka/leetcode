import random
lst1 = sorted([random.randint(-1000, 1000) for p in range(50)])
lst2 = sorted([random.randint(-1000, 1000) for m in range(50)])
def merge_sorted_lists(list1, list2):
    len_sum = len(list1) + len(list2)
    merged_list = [0] * len_sum
    index_lst1 = 0
    index_lst2 = 0
    index_merged_list = 0
    for q in range(len_sum):
        if index_lst1 < len(list1) and (index_lst2 >= len(list2) or list1[index_lst1] < list2[index_lst2]):
            merged_list[index_merged_list] = list1[index_lst1]
            index_lst1 += 1
        else:
            merged_list[index_merged_list] = list2[index_lst2]
            index_lst2 += 1
        index_merged_list += 1
    return merged_list
print("первый список: ", lst1)
print("второй список: ", lst2)
result = merge_sorted_lists(lst1, lst2)
print(result)