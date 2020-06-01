# Sheet explaining this in folder



def koch(n):
    'returns turtle directions for drawing curve Koch(n)'

    if n == 0:  # base case
        return 'F' # Always the first direction

    # print("before:",n)

    tmp = koch(n-1) # recursive step: get directions for Koch(n-1),  use them to construct directions for Koch(n)
    # will return 'full_instructions' as tmp when moving out of recursions
    # print("after:",n)
    # print('tmp: ',tmp)
    full_instructions = tmp + 'L' + tmp + 'R' + tmp + 'L' + tmp
    print(full_instructions)
    return full_instructions



from turtle import Screen, Turtle

def drawkoch(n):
    # draws nth Koch curve using instructions from function koch(n)

    s = Screen()    # create screen
    t = Turtle()    # create turtle
    directions = koch(n)        # obtain directions to draw Koch(n)

    t.speed(10)



    for move in directions:
        if move == 'F':
            t.forward(300/3**n)
        if move == 'L':
            t.lt(60)
        if move == 'R':
            t.rt(120)
    s.exitonclick()


usr_number = int(input("What level of detail would you like your Koch's Curve? "))
drawkoch(usr_number)


