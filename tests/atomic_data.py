from pfac.atom import atomic_data
from pfac import fac
import os

# by uncommenting the following line and the one at the end of this file,
# this script will be converted to the input file for the SFAC interface.
# fac.ConvertToSFAC('Li.sf')

asym = 'Li'

# generate atomic data for H-like to Na-like ions.
if not os.path.exists('data'):
    os.mkdir('data')

nele = list(range(1, 3))
atomic_data(nele, asym, iprint=1, dir='data/')

# fac.CloseSFAC()