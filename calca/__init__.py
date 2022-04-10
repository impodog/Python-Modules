"""Calculate common ADVANCED!
------
See help() to get avalible imports.(Or 'import calca' to import all initial modules)

Initial Modules
------
    - calca.drt : Direction Force calculating
    - calca.factoring : Prime numbers and prime factors
    - calca.numeries : Sqrt and an array of numbers
    - calca.screening : Calculate screen resolution
    - calca.sets : Sets and giving more classes
    - calca.text : Text operate, spliting calculate
    - calca.unicode : Unicode and shift on keyboard


Not in initial because they're either too slow or not necessary
------
    - calca.point : Simulate pointers
    - calca.pysp : Python space browsing and adding
    - calca.run : Running threads
    - calca.console : Easy terminal prints

Useful
------
    >>> from calca.notinitial import*
    ... #This imports all the not initial modules
    >>> from calca.support import*
    ... #This shows the support message
    >>> calca.viewhelp("drt") #Or like 'calca.viewhelp("calca.drt")'
    ... #Run python help() to see the module in calca


------
Update logs
------


Main update (v0.1)
------
    - More modules : 'run', 'console'(Not initial)
    - InstanceLess decorator
    - Unordered type
    
v0.1.0 updates
------
    - (.0)
        - More modules : 'run', 'console'(Not initial)
        - InstanceLess decorator
        - Moved 'point' and 'pysp' away from initial modules
        - More contents in 'sets'(unordered)
        - Fixed bugs
    - (.1) New function 'text.mltsplit'
    - (.2) Fixed the numeries.sqrt problem
    - (.3) 
        - More fixes to the numeries calculating
        - Comparing between numeries
    
New/Fixed things in the 0.1.0.3 compared to the last one.
------
    - More fixes to the numeries calculating
    - Comparing between numeries"""
__version__="0.1.0.3"
from calca.overall import*
from calca.drt import*
from calca.factoring import*
from calca.screening import*
from calca.numeries import*
from calca.unicode import*
from calca.text import*
from calca.sets import*