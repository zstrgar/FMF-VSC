# Something is wrong!
# If only there would be a way for us to solve this mistery...


def bisection(l, x):
    """ Returns the index of the last element smaller than x. """
    if len(l) == 0:
        return 0
    else:
        middle = len(l) // 2
        l1 = l[:middle]
        l2 = l[middle:]
        if l[middle] >= x:  # Element is in the first half
            return bisection(l1, x)
        else:  # Element is in the second half
            return middle + bisection(l2, x)

# test_bisection = bisection([0, 2, 4, 6, 8, 10, 12], 7)
# print(test_bisection)


def is_ordered(l):
    # We use the bisection. Please don't do this at home.
    for k in range(len(l)):
        # Ordered if the k-1 first elements are smaller than the element on k
        if k != bisection(l[:k-1], l[k]):
            return False
    return True

# test_ordered = is_ordered([1, 2, 3, 4, 5])
# print(test_ordered)


def id_matrix(n):
    M = [[0]*n]*n  # Make empty matrix
    for i in range(n):
        M[i][i] = 1
    return M

# test_matrix = id_matrix(5)
# print(test_matrix)


def exp(n, m):
    """
    Calculates m ^ n.
    """
    if n == 1:
        # m ^ 1  = m
        return m
    else:
        # m ^ n = m * m ^ (n-1)
        return m * exp(m, n - 1)

# exp_test = exp(4, 4)  # 4 ^ 4 is 256
# print(exp_test)