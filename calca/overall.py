"""Import and define wide-used functions and module
---
See more at calca
---"""
import math,fractions,sys,os
from fractions import Fraction
from typing import NoReturn,Iterable,Any
fr=fractions.Fraction
class CalcaQuit(Exception):...
def rbystr(_f:float,digits:int=0):
    """Gives the rounded number to _f.
Works by string"""
    _f=str(_f).split('.')
    if digits <= 0:
        try:
            if digits!=0:
                if int(_f[0][digits]) >= 5:add=10**abs(digits)
                else:add=0
                if digits<-1:return int(_f[0][:digits])*10**abs(digits)+add
                else:return int(_f[0][:digits])*10+add
            else:
                try:
                    if int(_f[1][0]) >= 5:add=1
                    else:add=0
                except:add=0
                return int(_f[0])+add
        except IndexError:return 0
    else:
        try:
            if int(_f[1][digits]) >= 5:add=add=0.1**abs(digits)
            else:add=0
        except IndexError:add=0
        try:return round(float('.'.join((_f[0],_f[1][:digits])))+add,digits)
        except IndexError:return float('.'.join((_f[0],_f[1])))
def symbol(_num:'float|int')->int:
    """Gets the symbol a of number."""
    try:return int(_num // abs(_num))
    except ZeroDivisionError:return 0
def viewhelp(name:str="calca"):
    """View the helps to calca.
    >>> calca.viewhelp("drt")
    ... # Is equivalent to:
    >>> help(calca.drt)"""
    if isinstance(name,str):
        try:help(sys.modules["calca."+name])
        except KeyError:
            if name.startswith("calca"):
                try:help(sys.modules[name])
                except KeyError:print("No helps available")
            else:print("No helps available")
    else:help("calca")
def NoInstance(*args,**kwargs)->NoReturn:
    """What a instance-less type do when you try to create an instance."""
    raise TypeError("No instance can be made by class.")
def InstanceLess(cls:type):
    """Involve a class without an instance"""
    cls.__init__=cls.__new__=NoInstance
    return cls