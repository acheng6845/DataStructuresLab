class suffixTrie:
    class _Node:
        def __init__(self, e):
            self.element = e
            self.children = {}
        def draw(self, x, y, start=None):
            global S, C
            #tb = TextBox(self.element, x, y)
            if not C:
                tb = TextBox(S[self.element], x, y)
                tb.draw()
                maxx = x
                for c in self.children:
                    maxx, tc = self.children[c].draw(maxx, y+50)
                    tb.drawLineToOtherBoxBelow(tc)
                return (maxx+tb.width(), tb)
            else:
                if len(self.children) == 1:
                    if start is None:
                        start = self.element
                    for c in self.children:
                        return self.children[c].draw(x, y, start)
                else:
                    if start is not None:
                        tb = TextBox(S[start:self.element+1], x, y)
                    else:
                        tb = TextBox(S[self.element], x, y)
                    tb.draw()
                    maxx = x
                    for c in self.children:
                        maxx, tc = self.children[c].draw(tb.width()+maxx, y+50)
                        tb.drawLineToOtherBoxBelow(tc)
                    return (maxx+tb.width(), tb)
                    
                
    def __init__(self, s):
        self.root = self._Node("")
        for i in range(len(s)-1,-1,-1):
            n = self.root
            for j in range(i, len(s)):
                if s[j] not in n.children:
                    #n.children[s[j]] = self._Node(s[j])
                    n.children[s[j]] = self._Node(j)
                n = n.children[s[j]]
    def draw(self, x=0, y=0, n=None, p=None):
        if n is None:
            n = self.root
        tb = TextBox(n.element, x, y)
        tb.draw()
        for c in n.children:
            (x, tc) = n.children[c].draw(x+5,y+50)
            tb.drawLineToOtherBoxBelow(tc)
        #tb = TextBox(n.element, x+n.x, y)
        #tb.draw()
        #if len(n.children) != 0:
        #    num = 0
        #    for c in n.children:
        #        tc = self.draw(x+tb.width()+num, y+tb.height()+10, n.children[c], tb)
        #        num += 50
        #        tb.drawLineToOtherBoxBelow(tc)
        #return tb

class TextBox:
    TEXTSIZE = 30
    
    def __init__(self, text, x=0, y=0):
        self._text, self._x, self._y = str(text), x, y
        
    def replaceText(self,text):
        self._text = text
        
    def setLocation(self, x, y):
        self._x, self._y = x, y
        
    def draw(self):
        textAlign(LEFT, TOP)
        textSize(TextBox.TEXTSIZE)
        rectMode(CORNER)
        fill(255)
        stroke(0)
        strokeWeight(1)
        rect(self._x, self._y, self.width(), self.height())
        fill(0)
        text(self._text, self._x + textWidth(" ") // 2, self._y - textDescent() //2)
    
    def width(self):
        textSize(TextBox.TEXTSIZE)
        return textWidth(self._text + " ")
    
    def height(self):
        textSize(TextBox.TEXTSIZE)
        return textAscent() + textDescent()
    
    def drawLineToOtherBoxBelow(self, otherBox):
        stroke(0)
        textSize(TextBox.TEXTSIZE)
        strokeWeight(1)
        line(self._x + self.width() / 2, self._y + self.height(), otherBox._x + otherBox.width() /2, otherBox._y)

def setup():
    global S, C
    S = "hih$"
    C = False
    size(1600, 1000)
    pixelDensity(displayDensity())
    noLoop()
    
def keyPressed():
    global S, C
    #if key=='0':
    if key==u'\x08':
        S=S[:-1]
    elif key==TAB:
        C= not C
    elif key != 65535:
        S+=key
    redraw()
    
def draw():
    background(200,150,200)
    TextBox(S,10,10).draw()
    st=suffixTrie(S)
    # n = st.root
    # for c in n.children:
    #     print(n.children[c].element)
    #     for d in n.children[c].children:
    #         print(n.children[c].children[d].element)
    #         for e in n.children[c].children[d].children:
    #             print(n.children[c].children[d].children[e].element)
    #             for f in n.children[c].children[d].children[e].children:
    #                 print(n.children[c].children[d].children[e].children[f].element)
    #                 for g in n.children[c].children[d].children[e].children[f].children:
    #                     print(n.children[c].children[d].children[e].children[f].children[g].element
    st.draw(50,100)