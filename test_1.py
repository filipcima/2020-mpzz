from collections import defaultdict

# Mappings
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


def injection(R, A):
    if not mapping(R, A):
        raise Exception(f"Relation R={R} on set {A} isn't mapping.")

    set_b = [b for (a, b) in R]

    occurances_b = defaultdict(lambda: 0)
    for item in set_b:
        occurances_b[item] += 1

    return all([i == 0 or i == 1 for i in occurances_b.values()])


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

# Relations
def reflexive(R, A):
    """Returns True if a relation R on set A is reflexive, False otherwise."""
    for a in A:
        if (a, a) not in R:
            return False
    
    return True


def irreflexive(R, A):
    """Returns True if a relation R on set A is irreflexive, False otherwise."""
    for a in A:
        if (a, a) in R:
            return False
    
    return True


def symmetric(R, A=None):
    """Returns True if a relation R on set A is symmetric, False otherwise."""
    for a, b in R:
        if (b, a) not in R:
            return False
    
    return True


def asymmetric(R, A):
    """Returns True if a relation R on set A is asymmetric, False otherwise."""
    for (a, b) in R:
        if (b, a) in R:
            return False
    
    for x in A:
        if (x, x) in R:
            return False

    return True


def antisymmetric(R, A):
    """Returns True if a relation R on set A is antisymmetric, False otherwise."""

    for (a, b) in R:
        if a == b:
            continue

        if (b, a) in R:
            return False

    return True


def transitive(R, A):
    """Returns True if a relation R on set A is transitive, False otherwise."""
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    
    return True

# Relace

# Pokud nemas na pocitaci python, pouzij https://repl.it/languages/python3
# A = Mnozina, do ktere patri relace R
# R = Relace z mnoziny A

A = ["a", "b", "c"]
R = [("a", "a"), ("b", "b"), ("c", "c")]

print(f"Properties for relation R={R} on set A={A}\n")

print(f"Is reflexive: {reflexive(R, A)}")
print(f"Is irreflexive: {irreflexive(R, A)}")
print(f"Is symmetric: {symmetric(R, A)}")
print(f"Is asymmetric: {asymmetric(R, A)}")
print(f"Is antisymmetric: {antisymmetric(R, A)}")
print(f"Is transitive: {transitive(R, A)}")


# Zobrazeni
A1 = [1, 2, 3]
R1 = [(1, 2), (2, 3), (3, 1)]

print(f"\n\nProperties for mapping R1={R} on set A1={A}\n")

print(f"Is mapping: {mapping(R1, A1)}")
print(f"Is injection: {injection(R1, A1)}")
print(f"Is surjection: {surjection(R1, A1)}")
print(f"Is bijection: {bijection(R1, A1)}")