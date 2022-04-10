"""
calca.drt
---
Direction and forces calculating
---

There aren't too much to explain so let's just see some examples.

Examples
---
    >>> import calca.drt
    >>> calca.drt.vec(8,9)
    ... # Real and imaginal: 8 + 9j
    >>> F = calca.drt.force(5,(3,4))
    ... # This means you have a speed '5' and each time, you go in angle of (3, 4)
    >>> F.push()
    (3.0000000000000004, 3.9999999999999996)
    ... # This is the result(not exact), you went 3 in x and 4 in y.
    """
from calca.overall import*
def hypot(x:'float|int',y:'float|int')->float:return math.sqrt(x**2+y**2)
class tuping():
    """Gets a tuple-like object that can add, sub, mul, div."""
    def __init__(self,*inp:tuple)->None:
        self.inp=list(inp)
        self.__repr__=self.__str__
    def __add__(self,num:tuple):
        result=tuping()
        for val in self.inp:result.append(val+num[self.inp.index(val)])
        return result
    def __sub__(self,num:tuple)->None:
        result=tuping()
        for val in self.inp:result.append(val-num[self.inp.index(val)])
        return result
    def __mul__(self,num:'int|float')->None:
        result=tuping()
        for val in self.inp:result.append(val*num)
        return result
    def __div__(self,num:'int|float')->None:
        result=tuping()
        for val in self.inp:result.append(val/num)
        return result
    def __str__(self):return "tuping("+str(self.inp)[1:-1]+")"
    def __getitem__(self,_n:int)->object:return self.inp[_n]
    def __setitem__(self,_n:int,_o:object)->None:self.inp[_n]=_o
    def tuplify(self)->tuple:return tuple(self.inp)
    def append(self,_o:object):self.inp.append(_o)
    def copy(self):return self.inp.copy()
class vec():
    """Gets a vector, can be added to other vectors."""
    def __init__(self,real:'float|int',ima:'float|int'):
        self.vec=tuping(real,ima)
        self.__repr__=self.__str__
    def __str__(self):return "vec("+str(self[0])+","+str(self[1])+")"
    def __getitem__(self,_n:int)->object:return self.vec[_n]
    def __add__(self,_o):return vec(*(self.vec+_o.vec))
    def tuplify(self)->tuple:return self.vec.tuplify()
    def aaxis(self):return math.atan(self[1],self[0])
    def copy(self):return vec(self.vec[0],self.vec[1])
class force():
    """Based on vectors, push every time to get a result."""
    def __init__(self,speed:'float|int',dir:tuple)->None:
        self.angle=aaxis(*dir)
        self.speed=speed
        pushv=self.push()
        self.vec=vec(pushv[0],pushv[1])
        self.__repr__=self.__str__
        self.dir=dir
    def reaxis(self,dir:tuple)->None:
        self.angle=aaxis(*dir)
        pushv=self.push()
        self.vec=vec(pushv[0],pushv[1])
        del self.compiled
    def sp(self,val:'float|int',add:bool=True)->None:
        if add:self.speed+=val
        else:self.speed=val
    def __str__(self):return "force("+str(self.speed)+","+str(self.dir)+")"
    def push(self)->tuple:
        if self.angle is not None:
            if not hasattr(self,"compiled"):self.compiled=cspeed(self.speed,self.angle)
            return self.compiled
        else:return (0,0)
    def __lt__(self,f:'int|float')->bool:return self.speed < f
    def __gt__(self,f:'int|float')->bool:return self.speed > f
    def __mul__(self,F):
        vals=(self.vec+F.vec).tuplify()
        return force(hypot(vals[0],vals[1]),vals)
    def copy(self):return force(self.speed,self.dir)
def cspeed(speed:'int|float'=1,angle:int=0)->None:
    """Convert speed and angle to specific tuple object."""
    y=math.sin(angle)*speed
    x=math.cos(angle)*speed
    return (x,y)
def aaxis(x:'float|int',y:'float|int')->float:
    try:
        result=math.atan(y/x)
        if result == 0:return symbol(x)*90-90
        return result
    except ZeroDivisionError:return symbol(y)*90
def combine(forces:'tuple[force]'):
    Fr=force(0,(0,0))
    for F in forces:Fr=Fr*F
    return Fr