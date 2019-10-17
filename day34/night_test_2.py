def sort_list(lst):
    if len(lst) <= 1:
        return lst
    key = lst[0]
    lst_s = [x for x in lst if x < key]
    lst_b = [x for x in lst if x > key]
    lst_eq = [x for x in lst if x == key]
    return sort_list(lst_s) + lst_eq + sort_list(lst_b)

lst = [80, 90, 121, 34, 56, 90 , 73, 98, 12, 43]

values = sort_list(lst)
print(values)











































