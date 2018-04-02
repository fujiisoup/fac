from pfac.atom import *
from pfac import fac
import os

# by uncommenting the following line and the one at the end of this file,
# this script will be converted to the input file for the SFAC interface.
#fac.ConvertToSFAC('fe.sf')

asym = 'Li'

# generate atomic data for H-like to He-like ions.
nele = range(1, 3)
atomic_data(nele, asym, iprint=1, dir='./')

#fac.CloseSFAC()
