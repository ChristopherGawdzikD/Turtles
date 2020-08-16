from turtle import*

def getAudiLogo():
    # Will make audi logo
    for i in range(4):
        for x in ["grey"]:
            color(x)
            pensize(5)
            circle(50)
            forward(60)


print(getAudiLogo())