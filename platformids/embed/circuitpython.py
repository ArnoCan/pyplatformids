# -*- coding: utf-8 -*-
"""CircuitPython releases.
"""
from __future__ import absolute_import

from platformids import _debug, _verbose
from platformids import rte2num, num2rte, num2pretty, custom_dist

from platformids.embed.micropython import RTE_MICROPYTHON 


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_CIRCUITPYTHON = RTE_MICROPYTHON + custom_dist.add_enum()  #: implementation/distribution variants


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'circuitpython':      RTE_CIRCUITPYTHON,
        RTE_CIRCUITPYTHON:    RTE_CIRCUITPYTHON,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_CIRCUITPYTHON:    'circuitpython',
    }
)


#: mapping for pretty print
num2pretty.update(
    {
        RTE_CIRCUITPYTHON:    'CircuitPython',
    }
)



# if not isJython:
#     try:
#         osname = os.name
#     except AttributeError:
#         try:
#             # CirctuiPython, MicroPython
#             osname = sys.implementation.name  # @UndefinedVariable
#             if osname in ('circuitpython', 'micropython', ):
#                 sys.stderr.write('use special module for: ' + str(osname))
#                 sys.exit()
#         except:
#             sys.stderr.write('platform is not supported')
#             sys.exit()
# 
#     if PYV35Plus:
#         PlatformIDsFileCheck = (FileNotFoundError,)  # @UndefinedVariable
#     
#     else:
#         PlatformIDsFileCheck = (Exception,)
# 
# else:
#     osname = os._name  # @UndefinedVariable  # set to the platform name
#     PlatformIDsFileCheck = (IOError,)  # @UndefinedVariable


