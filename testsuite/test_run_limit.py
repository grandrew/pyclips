# test_fact.py

"""\
TESTS:

RunWithLimit
EnvRunWithLimit
"""

import clips
import unittest

from test_00 import ctestcase


class ctc_Fact(ctestcase):
    """test Fact objects"""

    def test_RunWithLimit(self):
        """Testing: Run(limit)"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            e.Assert("(num 1)")
            e.BuildRule("inctest", "?f <- (num ?x)", "(retract ?f) (assert (num (+ ?x 1)))")
            e.Run(100)


# end.