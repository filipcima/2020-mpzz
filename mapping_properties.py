from collections import defaultdict


# mapping([("a", "a"), ("b", "a"), ("b", "b"), ("c", "b"), ("c", "c"), ("d", "c"), ("d", "d")], ("a","b","c","d")) == False
# mapping([("a", "a"), ("b", "a"), ("c", "b"), ("d", "b")], ("a","b","c","d")) == True
def mapping(R, A):
    set_a = [a for (a, b) in R]
    
    for a in A:
        if a not in set_a:
            return False

    occurances_a = defaultdict(lambda: 0)
    for item in set_a:
        occurances_a[item] += 1

    for i in occurances_a.values():
        if i > 1 or i == 0:
            return False

    return True


# injection([(1,1), (2, 2), (3, 5)], (1,2,3)) == True
# injection([(1,1), (2, 3), (3, 2)], (1,2,3)) == True
# injection([(1,1), (2, 3), (3, 1)], (1,2,3)) == False
def injection(R, A):
    if not mapping(R, A):
        raise Exception(f"Relation R={R} on set {A} isn't mapping.")

    set_b = [b for (a, b) in R]

    occurances_b = defaultdict(lambda: 0)
    for item in set_b:
        occurances_b[item] += 1

    return all([i == 0 or i == 1 for i in occurances_b.values()])


# surjection([(1,1), (2, 2), (3, 2)], (1,2,3)) == True
# surjection([(1,1), (2, 2), (3, 1)], (1,2,3)) == False
def surjection(R, A):
    if not mapping(R, A):
        raise Exception(f"Relation R={R} on set {A} isn't mapping.")

    set_b = [b for (a, b) in R]

    occurances_b = defaultdict(lambda: 0)
    for i in A:
        occurances_b[i] = 0

    for item in set_b:
        occurances_b[item] += 1

    return all([i >= 1 for i in occurances_b.values()])


# bijection([(1,1), (2, 3), (3, 2)], (1,2,3)) == True
def bijection(R, A):
    if not mapping(R, A):
        raise Exception(f"Relation R={R} on set {A} isn't mapping.")

    set_a = [b for (a, b) in R]
    set_b = [b for (a, b) in R]

    if not len(set_a) == len(set_b):
        return False
    
    inj = injection(R, A)
    sur = surjection(R, A)

    if inj and sur:
        return True

    return False
