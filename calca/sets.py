"""calca.sets
---
Set operation
---

usage
---
    >>> import calca.sets
    >>> calca.sets.reverse({1:2,7:5})
    {2:1,5:7}
    >>> A=calca.sets.unordered((3,1,2,3,4,2,3,3,3))
    >>> A[3]
    ... #This is the count of '3'
    5
    >>> A[2]=100
    ... #Change number of '2' to '100'
    >>> A.remove(2,95)
    ... #Remove 95 of '2'
    >>> A
    unordered([1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4,])
    """
from calca.overall import*
def reverse(D:dict)->dict:
    """Reverse the dict."""
    result={}
    for k,v in D.items():result[v]=k
    return result

class unordered():
    """Get an unordered list.
__getitem__ and __setitem__: item is the number of sth."""
    def __init__(self,iterable:Iterable):
        if isinstance(iterable,dict):self._count=iterable
        else:
            self._count=dict()
            for obj in set(iterable):self._count[obj]=iterable.count(obj)
    @property
    def count(self)->dict:return self._count
    def __getitem__(self,_o:object)->int:return self._count[_o]
    def append(self,_o:object,_n:int=1)->None:
        """Append sth into the object."""
        try:self._count[_o]+=_n
        except:self._count[_o]=_n
    def __setitem__(self,_o:object,_n:int)->None:self._count[_o]=_n
    def __delitem__(self,_o:object):del self._count[_o]
    def remove(self,_o:object,_n:int=1)->'None|NoReturn':
        """Remove sth from the object.
_n is the number to remove."""
        if self._count.get(_o) is not None:
            if self._count.get(_o) <= _n:del self[_o]
            else:self[_o]-=_n
        else:raise ValueError("Non-existing object to remove.")
    def __str__(self)->str:
        result='unordered(['
        for k,v in self._count.items():result+=(str(k)+', ')*v
        result=result[:-1]+'])'
        return result
    def __repr__(self)->str:return self.__str__()