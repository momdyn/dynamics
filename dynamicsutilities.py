from sympy import *
from sympy.physics.mechanics import *
from IPython.display import display, Latex

"""
Uses `IPython.display` to show formatted equation with an equals sign between terms given `str` or `Symbol`-like arguments.

Example
-------
>> # String-formatted argument
>> arg1 = r'\boldsymbol{r}'
>>
>> # Sympy-formatted argument
>> N = ReferenceFrame('N')
>> x, y = symbols('x, y')
>> arg2 = x*N.x + y*N.y
>>
>> # Formatted equation
>> dtex(arg1, arg2)
"""
def dtex(*args):
    tex = ''
    for arg in args:
        if isinstance(arg, str):
            # Handle string arguments
            tex += f'${arg}$ $\, = \,$ '
        else:
            # Handle SymPy arguments
            tex += f'${mlatex(arg)}$ $\, = \,$ '
    
    # Trim off the last equals sign
    tex = tex[:-10]  
    display(Latex(tex))
