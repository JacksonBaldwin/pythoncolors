def printc(text,color='default',underline=False,bold=False): #\033[93m
    color_dict = {'purple':'95m','lightblue':'94m','cyan':'96m','lightgreen':'92m','orange':'93m',
                  'red':'91m','green':'32m','default':'0m','white':'37m','black':'30m','darkpurple':'35m','yellow':'103m',
                  'blackbackground':'100m','redbackground':'101m','greenbackground':'102m','orangebackground':'103m',
                  'lightbluebackground':'104m','purplebackground':'105m','cyanbackground':'106m','whitebackground':'107m'}
    cl = '\033['
    if underline:
        cl += '4;'
    if bold:
        cl += '1;'
    
    cl += color_dict[color]
    print(cl+text+'\033[0m') #print text and return terminal to normal text

printc('python terminal colors!','green',False,True)
printc("using the printc function, you can make your text whatever color you'd like!",'lightblue',True)
printc('you can also make your text underlined and bold','purple',True,True)