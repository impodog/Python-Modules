"""
calca.console
---
Provides the terminal shortcuts and operations.
---

Examples
---
    >>> import calca.console
    >>> calca.console.clear() 
    ... #Clear the console(Not counted)
    >>> calca.console.Terminal 
    ... #Terminal operations (It is a type, do not create any instances)
    
    >>> calca.console.Terminal.puts("I like dogs.")
    ... #This is to put the string in terminal and put it into memory
    
    >>> calca.console.Terminal.clear()
    ... #Confusion: ONLY Terminal.clear() puts Memory into ACTUAL Memory and you can putmem(). NOT clear()
    
    >>> calca.console.Terminal.putmem()
    ... #So now you shall see:
    //
        I like dogs.
    //
"""
import os,platform,sys
from calca.overall import*
cslength,cswidth=os.get_terminal_size()
system=platform.system()
def clear():
    if system == 'Windows':os.system("cls")
    else:os.system("clear")
PutLen=0
Mem=""
Solid=""
ForMem=""
@InstanceLess
class Terminal:
    """Terminal operations"""
    @classmethod
    def center(cls,string:str,_fillchar:str=' ')->str:
        """Center a string like the original method does but in this case, the middle of the terminal"""
        return string.center(cslength,_fillchar)
    @classmethod
    def rjust(cls,string:str,_fillchar:str=' ')->str:
        """Left justify a string like the original method does but in this case, the right of the terminal"""
        return string.rjust(cslength,_fillchar)
    @classmethod
    def eraseline():
        """Erase the length of a line"""
        print('\b'*cslength,end='',flush=True)
    @classmethod
    def recputs(cls,string:Any):
        """Puts chars in terminal. This DOES count into Puts Length and Memory"""
        global PutLen,Mem
        string=str(string);PutLen+=len(string);Mem+=string;print(string,end="")
    @classmethod
    def puts(cls,string:Any):
        """Puts chars in terminal. This DOES count into Puts Length BUT NOT Memory"""
        global PutLen,Mem
        string=str(string);PutLen+=len(string);print(string,end="")
    @classmethod
    def eraseputs(cls):
        """Erase the Puts Length"""
        global PutLen
        print('\b'*PutLen,end='',flush=True)
    @classmethod
    def clear(cls):
        """Clear the console. The putmem() ONLY works AFTER Terminal.clear()"""
        global ForMem,Mem
        clear();ForMem=Solid+Mem;Mem=""
    @classmethod
    def putmem(cls):
        """Put the Memory onto terminal. This method ONLY works AFTER Terminal.clear()"""
        global ForMem
        Terminal.puts(ForMem)
    @classmethod
    def record(cls,string:Any):
        """Record a memory instantly without using puts() to put. The putmem() ONLY works AFTER Terminal.clear()"""
        global Mem
        string=str(string);Mem+=string
    @classmethod
    def solidrecord(cls,string:Any):
        """This records a Solid string that never changes into Memory(Before soft memory). The putmem() ONLY works AFTER Terminal.clear()"""
        global Solid
        string=str(string);Solid=string
class T(Terminal):...