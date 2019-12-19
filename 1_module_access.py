
# Importing modules from start i.e from package
import pckg.m1
import pckg.m2

# Accessing code from these modules
pckg.m1.f1m1()
pckg.m2.f1m2()

# Other way to do above is by aliasing to reduce the length of module usage
import pckg.m1 as alias_m1
import pckg.m2 as alias_m2
# Accessing code
alias_m1.f1m1()
alias_m2.f1m2()

# Import only modules
from pckg import m1
from pckg import m2
# Now access the code
m1.f1m1()
m2.f1m2()

# Import specific code from the modules
from pckg.m1 import f1m1
from pckg.m2 import f1m2
# Accessing them now
f1m1()
f1m2()

