def list_function(a, b):
    for item in a:
        if item in b:
            print("True")
            break


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 6, 7, 8]
list_function(list1, list2)
