def check():
    opentab=tuple('({[')
    closetab=tuple('))}]')
    map=dict(zip(opentab,closetab))
    print(map)
    
check()