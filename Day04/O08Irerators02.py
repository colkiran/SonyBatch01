
lst1 = ['a', 'b', 'c', 'd', 'e']

iterObj = iter(lst1)

while(True):
    try:
        elem = iterObj.__next__()
        print(elem, end=" ")
    except StopIteration:
        break

