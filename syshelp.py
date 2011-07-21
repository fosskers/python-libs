# file:    syshelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   Help with system tasks.

import sys

def get_args(oper='EXACTLY', num=1):
    '''Checks args on the command line and returns them if valid.
    Examples of use:
      get_args()  # Looks for exactly 1 arg.
      get_args('EXACTLY', 2)  # Looks for exactly 2 args.
      get_args('AT_LEAST', 0)  # Will accept any number of args.
      get_args('AT_LEAST', 2)  # Looks for two or more args.
      '''
    comps = {'EXACTLY': '!=', 'AT_LEAST': '<'}
    if oper not in comps:
        print('Bad comparison code -> {0}'.format(oper))
        return
    if eval('len(sys.argv) {0} num + 1'.format(comps[oper])):  # +1 for filename
        print('Bad number of args ->', sys.argv[1:])
        return
    return sys.argv[1:] if len(sys.argv) > 1 else []
