def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
def choose(l, k):
    return list(choose_iter(l, k))

def fullcombination(l):
    for i in range(1,len(l)+1):
        print (choose(l,i))

print(len(choose('efghqwoeiruasdlfkjhasdaksjdhf', 3)))
fullcombination('abc')
fullcombination('12345')
