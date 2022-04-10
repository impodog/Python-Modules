from calca.overall import*


_G=globals()

def browse(___var___:object)->'str|NoReturn':
    """Gets the name of a specific variant.\n
    Only browses surfaces in globals."""
    for k,v in _G.items():
        if v is ___var___:return k
    raise NameError("Value %s not existing in global surface."%(___var___))

def Get(_name:str)->'object|NoReturn':
    """Gets the object of a name.\n
    Only browses surfaces in globals."""
    try:return _G[_name]
    except KeyError:raise NameError("Name %s not existing in global surface."%(_name))
def Set(_name:str,_object:object,inside:dict=_G)->None:
    """Sets the name to an object.\n"""
    inside[_name]=_object