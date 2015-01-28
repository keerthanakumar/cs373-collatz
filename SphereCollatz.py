#!/usr/bin/env python3

# -------
# imports
# -------

import sys

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ----------
# get_cycles
# ----------

def get_cycles (n) :
    """
    n the number within 1 and 1000000 to calculate the cycles
    return the number of cycles taken from n to 1 following problem 
    """
    c = 1
    while (n > 1) :
        if (n % 2) == 0:
            n = n >> 1
            c += 1
        else:
            n = n + (n >> 1) + 1
            c += 2
    return c

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    maxcycles = 1
    if (i > j) :
        i, j = j, i        
    for n in range(i, j+1) :
        c = get_cycles(n)
        if maxcycles < c :
            maxcycles = c
    return maxcycles

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)
