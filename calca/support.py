import calca.console
supporttext="""
Calca is fully made by Python code and helps calculating.
Go to http://dogsocute.icu/module/calca to see more information.
See also http://dogsocute.icu, more games and calca support!
Help texts can be called by calca.(overall.)viewhelp(module)

Thank you all for download this!
Hopes that it will be better!

Original developed by Dogs.
There aren't any copyrights!
I like dogs, as usual."""

calca.console.clear()
supportlist=supporttext.split(' ')
for i in range(1,len(supportlist)+1):
    print(*supportlist[:i])
    hits=''.join(supportlist[i:]).count('\n')
    input(hits*'\n'+"Hit Return:")
    calca.console.clear()
print(supporttext)