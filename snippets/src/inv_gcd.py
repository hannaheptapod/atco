def inv_gcd(a, b):
    a %= b
    if a == 0: return b, 0
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        u = s // t

        s -= t * u
        m0 -= m1 * u

        s, t = t, s
        m0, m1 = m1, m0

    if m0 < 0: m0 += b // s
    return s, m0
