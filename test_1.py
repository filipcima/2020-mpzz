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
