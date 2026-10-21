l = [10,20,30]
l.append(40); l.insert(1,15);l.extend([50,60])
print(l)
l.remove(20);print(l.pop(),l.pop(0));print(l)
l.sort();l.reverse();print(l)
print(l.index(30),l.count(30),l[1:3])
l[0] = 99
print([x * 2 for x in range(5)])
print([x for x in range(10)if x % 2 == 0])
