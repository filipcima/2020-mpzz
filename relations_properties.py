def reflexive(R, A):
    """Returns True if a relation R on set A is reflexive, False otherwise."""
    for a in A:
        if (a, a) not in R:
            return False
    
    return True


def test__reflexive():    
    A = [1, 2, 3]

    cases = [
        ([(1, 2), (2, 1)], A, False),
        ([(1, 1), (1, 2), (2, 1), (1, 3)], A, False),
        ([(2, 2)], A, False),
        ([(2, 1)], A, False),
        ([], A, False),
        ([(1, 1), (2, 2), (3, 3)], A, True),
        ([(1, 1), (2, 2), (3, 3), (1, 3)], A, True),
    ]

    for R, A, expected_output in cases:
        assert reflexive(R, A) == expected_output


def irreflexive(R, A):
    """Returns True if a relation R on set A is irreflexive, False otherwise."""
    for a in A:
        if (a, a) in R:
            return False
    
    return True


def test__irreflexive():    
    A = [1, 2, 3]

    cases = [
        ([(1, 2), (2, 1)], A, True),
        ([(1, 1), (1, 2), (2, 1), (1, 3)], A, False),
        ([(2, 2)], A, False),
        ([(2, 1)], A, True),
        ([], A, True),
        ([(1, 1), (2, 2), (3, 3)], A, False),
        ([(1, 1), (2, 2), (3, 3), (1, 3)], A, False),
    ]

    for R, A, expected_output in cases:
        assert irreflexive(R, A) == expected_output



def symmetric(R):
    """Returns True if a relation R on set A is symmetric, False otherwise."""
    for a, b in R:
        if (b, a) not in R:
            return False
    
    return True

def test__symmetric():    
    cases = [
        ([(1, 2), (2, 1)], True),
        ([(1, 1), (1, 2), (2, 1), (1, 3)], False),
        ([(2, 2)], True),
        ([(2, 1)], False),
        ([], True),
        ([(1, 2), (1, 3), (2, 1), (3, 1), (2, 3), (3, 2), (1, 1), (2, 2), (3, 3)], True),
    ]

    for R, expected_output in cases:
        assert symmetric(R) == expected_output



def asymmetric(R, A):
    """Returns True if a relation R on set A is asymmetric, False otherwise."""
    for (a, b) in R:
        if (b, a) in R:
            return False
    
    for x in A:
        if (x, x) in R:
            return False

    return True


def test__asymmetric():
    A = [1, 2, 3]
    
    cases = [
        ([(1, 2), (2, 3)], A, True),
        ([(1, 1), (1, 2), (2, 3)], A, False),
        ([(2, 2)], A, False),
        ([(2, 1)], A, True),
        ([], A, True),
        ([(2, 1), (1, 2)], A, False),
    ]

    for R, A, expected_output in cases:
        assert asymmetric(R, A) == expected_output


def antisymmetric(R, A):
    for (a, b) in R:
        if a == b:
            continue

        if (b, a) in R:
            return False

    return True


def test__antisymmetric():
    A = [1, 2, 3]
    
    cases = [
        ([(1, 2), (2, 3)], A, True),
        ([(1, 1), (1, 2), (2, 3)], A, True),
        ([(2, 2)], A, True),
        ([(2, 1)], A, True),
        ([], A, True),
        ([(1, 1), (1, 2), (2, 1)], A, False)
    ]

    for R, A, expected_output in cases:
        assert antisymmetric(R, A) == expected_output


def transitive(R, A):
    """Returns True if a relation R on set A is transitive, False otherwise."""
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    
    return True


def test__transitive():
    A = [1, 2, 3]
    
    cases = [
        ([(1, 2), (2, 3)], A, False),
        ([(1, 1), (1, 2), (2, 3), (1, 3)], A, True),
        ([(2, 2)], A, True),
        ([(2, 1)], A, True),
        ([], A, True),
        ([(1, 3), (1, 2), (2, 3), (4, 4), (4, 3)], [1, 2, 3, 4], True)
    ]

    for R, A, expected_output in cases:
        assert transitive(R, A) == expected_output
