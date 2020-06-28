def jacobi(first_eq, second_eq, third_eq, n=100):
    """
        Iterative method for solving linear equations
        https://en.wikipedia.org/wiki/Jacobi_method
    """

    a11 = first_eq[0]
    a12 = first_eq[1]
    a13 = first_eq[2]
    b1 = first_eq[3]
    a21 = second_eq[0]
    a22 = second_eq[1]
    a23 = second_eq[2]
    b2 = second_eq[3]
    a31 = third_eq[0]
    a32 = third_eq[1]
    a33 = third_eq[2]
    b3 = third_eq[3]

    # Initial values
    x= 0
    y = 0
    z = 0
    xs = []
    ys = []
    zs = []
    ns = []

    for i in range(n):
        oldx = x
        oldy = y
        oldz = z
        x = (1/a11) * (b1 - a12*oldy - a13*oldz)
        y = (1/a22) * (b2 - a21*oldx - a23*oldz)
        z = (1/a33) * (b3 - a31*oldx - a32*oldy)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        ns.append(i)

    return {'n': ns, 'x': xs, 'y': ys, 'z': zs}
