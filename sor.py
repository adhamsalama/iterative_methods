def sor(first_eq, second_eq, third_eq, w, n=30):
    """
        Iterative method for solving linear equations
        https://en.wikipedia.org/wiki/Successive_over-relaxation
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
        x = (1-w)*x + (w/a11) * (b1 - a12*y - a13*z)
        y = (1-w)*y + (w/a22) * (b2 - a21*x - a23*z)
        z = (1-w)*z + (w/a33) * (b3 - a31*x - a32*y)
        xs.append(x)
        ys.append(y)
        zs.append(z)
        ns.append(i)

    return {'n': ns, 'x': xs, 'y': ys, 'z': zs}
