"""Interface to ioLab bbox

This is currently a simple import of the ioLab python library
That needs to be installed - it is included in the Standalone distributions
of PsychoPy as of version 1.62.01.

usage::
    from psychopy.hardware import ioLab
    
for examples see the demos menu of the PsychoPy Coder or go to the URL above.

--------
"""
# Part of the PsychoPy library
# Copyright (C) 2010 Jonathan Peirce
# Distributed under the terms of the GNU General Public License (GPL).

from psychopy import log
try:
    from ioLabs import *
except:
    msg="""Failed to import the ioLab library. If you're using your own copy of 
python (not the Standalone distribution of PsychoPy) then try installing it with:
    > easy_install ioLab
    
"""
    log.error(msg)