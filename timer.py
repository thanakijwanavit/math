#!/usr/bin/env python3
import timeit
print("your function took %s seconds" % timeit.Timer('for i in range(10): oct(i)').timeit())
