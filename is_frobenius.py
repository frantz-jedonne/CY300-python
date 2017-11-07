def is_frobenius(lst):
    if len(lst) == 1:
            if len(lst[0]) == 1:
                if lst[0][0] == 1:
                    return True
                else: 
                    return False
    for row in lst:
        if len(row) != len(lst):
            return False   

    for i,r in enumerate(lst):
            if r[i] != 1:
                return False
            for item in r[i+1:]:
                if item != 0:
                    return False
    iList = []
    for i,r in enumerate(lst): 
        for item in r[:i]:
            if item != 0 and r.index(item) != i:
                index = r.index(item)
                iList.append(index)
    for val in iList:
        if val != iList[0]:
            return False
    return True


    if __name__ == '__main__':
        
        lst = input("Enter a Matrix as a list of lists where there rows are nested lists")

        is_frobenius(lst)