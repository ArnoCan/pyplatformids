from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"

import unittest

from platformids import num2rte

import platformids.embed.micropython
import platformids.embed.circuitpython


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None
        platformids.num2rte.strict_check = True
        platformids.rte2num.strict_check = True

    def testCase010(self):
        self.assertEqual(
            num2rte[platformids.embed.micropython.RTE_MICROPYTHON], 
            'micropython'
            )

    def testCase020(self):
        self.assertEqual(
            num2rte[platformids.embed.circuitpython.RTE_CIRCUITPYTHON], 
            'circuitpython'
            )


if __name__ == '__main__':
    unittest.main()
    
    
    
    