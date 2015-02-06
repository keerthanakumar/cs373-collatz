#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycles

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s   = "1    10\n"
        i,j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_3 (self) :
        s   = "10 1\n"
        i,j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)

    def test_read_4 (self) :
        s   = "1 10 100\n"
        i,j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    # ------
    # cycles
    # ------

    def test_cycles_1 (self) :
        n = 1
        r = get_cycles(n)
        self.assertEqual(r, 1)

    def test_cycles_2 (self) :
        n = 9
        r = get_cycles(n)
        self.assertEqual(r, 20)

    def test_cycles_3 (self) :
        n = 27
        r = get_cycles(n)
        self.assertEqual(r, 112)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_7 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print_3 (self):
        w = StringIO()
        collatz_print(w, 10000, -100000, 0)
        self.assertEqual(w.getvalue(), "10000 -100000 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("16492 688777\n10 1\n450 99\n1 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "16492 688777 509\n10 1 20\n450 99 144\n1 1000 179\n")

    def test_solve_3 (self) :
        r = StringIO("2 99\n3 1\n22 22\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "2 99 119\n3 1 8\n22 22 16\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
