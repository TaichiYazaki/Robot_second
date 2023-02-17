import os
import termcolor

print(termcolor.colored(__file__, "red"))
print(os.path.abspath(__file__))
print(termcolor.colored(os.path.dirname(os.path.abspath(__file__)), "red"))
