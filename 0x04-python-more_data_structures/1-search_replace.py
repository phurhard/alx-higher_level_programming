def search_replace(my_list, search, replace):
    new_list = []
    for elements in my_list:
        if elements == search:
            elements = replace
        new_list.append(elements)
    return new_list
