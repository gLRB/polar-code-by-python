def SGA(x):
    y = None
    if x >= 0 and x < 0.036:
        y = 0.00206 * x - 0.36 * (x ** 2) + 18.68 * (x ** 3)
    else:
        if x >= 0.036 and x < 0.05:
            y = -0.001288 + 0.05 * x
        else:
            if x >= 0.05 and x < 0.92:
                y = 0.0159 * x + 0.37 * (x ** 2) - 0.112 * (x ** 3)
            else:
                if x >= 0.92 and x < 8:
                    y = 0.367 * x + 0.075 * (x ** 2) - 0.0035 * (x ** 3) - 0.18
                else:
                    y = -2.211 + 0.9848 * x
    return y