diag = lambda m, n: [] if m == [] else \
    (m[0][0],) + (m[1][1],) + (m[2][2],)

diag1 = lambda m, n: [] if m == [] else \
    m[0][0] + diag((m[n][n],), n + 1)