import math
try:
    opp=input("Enter the Opposite side of the triangle\n-> ")
    x=int(opp)
    adj=input("Enter the Adjacent side of the triangle\n-> ")
    y=int(adj)
    print("Sides of the triangle entered are\n-> ",x,"and",y)
except:
    print("Enter Correct Side of the Triangle")
try:
    z=math.sqrt(x**2 + y**2)
    print("Hypotenuse of the triangle is :  ",z)
    fun=input("Enter the Trigonometric function for which you want to find the angle\n-> ")
    if fun=='sin':
        sintheta=x/z
        stheta=math.asin(sintheta)
        scon=math.degrees(stheta)
        print("Sine angle is",math.ceil(scon))
    elif fun=='cos':
        costheta=y/z
        ctheta=math.acos(costheta)
        ccon=math.degrees(ctheta)
        print("Cosine angle is",math.ceil(ccon))
    elif fun=='tan':
        tantheta=x/y
        ttheta=math.atan(tantheta)
        tcon=math.degrees(ttheta)
        print("Tangent angle is",math.ceil(tcon))
    else:
        print("Sorry,only Sine, Cosine and Tangent angles can be calculated")
except:
    print("Dont play with Python and Put actual value for the correct results. Thankyou")
quit()
