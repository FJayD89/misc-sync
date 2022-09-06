# tlacitka

def action1():
    buttons = 'ABD'
    return buttons

def action2():
    buttons = 'ACD'
    return buttons

def action3():
    buttons = 'A'
    buttons += 'C'*5
    buttons += 'D'
    return buttons

def action4():
    buttons = 'A'
    buttons += action2()
    buttons += 'D'
    return buttons

def action5():
    buttons = 'A'
    buttons += action3()
    buttons += 'C'
    buttons += action1()*5
    buttons += 'D'
    return buttons

def action6():
    buttons = 'A'
    buttons += action5()
    buttons += 'C'
    buttons += 'B'*5
    buttons += action4()*5
    buttons += 'D'
    
    
    return buttons



actions = {
1:action1(),
2:action2(),
3:action3(),
4:action4(),
5:action5(),
6:action6()
    }
print(actions[int(input())])
