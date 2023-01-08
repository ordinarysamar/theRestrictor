import curses

screen = curses.initscr()
curses.curs_set(0)
screen.nodelay(True)


NORMAL = '[ ] _'
SELECTED = '[X] _'


def consolePrint(xcord:int , ycord:int , text:str , options = 0):
    screen.addstr(ycord , xcord , text , options)
    screen.refresh()

def templateParser(template:str , ele:str ) -> str :
    template = template.split('_')
    template.insert(1 , ele)
    return (''.join(template))

def optionsRender(xcord:int , ycord:int , optionList:list , title:str , highlightIndex : int | None = None ) :
    consolePrint(xcord , ycord , f' {title} ')
    if highlightIndex != None : 
            consolePrint(
                xcord , 
                ycord + 2 + highlightIndex , 
                templateParser(SELECTED , optionList[highlightIndex]) , 
                options = curses.color_pair(1)
            )
    
    for ele in optionList:
        if optionList.index(ele) != highlightIndex :
            consolePrint(xcord , ycord + 2 + optionList.index(ele) , templateParser(NORMAL , ele))
        
