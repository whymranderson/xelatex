#a, b, c, d = symbols('a, b, c, d', real=True)
#>>> nonlinsolve([a**2 + a, a - b], [a, b])
#{(-1, -1), (0, 0)}
#>>> nonlinsolve([x*y - 1, x - 2], x, y)
#{(2, 1/2)}

from sympy import *
a,b,c,d,r1 = symbols('a b c d r1')
nonlinsolve([r1*(a+b+c)-a*b*c,
             r2*(b+c+d)-b*c*d,
             r3*(c+d+a)-c*d*a,
             r4*(d+a+b)-d*a*b,], [b,c,d,r4])
2.4655255439081647
2.05025946403542
1.7580102453709943
nonlinsolve([2.4655255*(3.0+b+c)-3.0*b*c,
             2.0502594*(b+c+d)-b*c*d,
             1.7580102*(c+d+3.0)-c*d*3.0,
             r4*(d+3.0+b)-d*3.0*b,], [b,c,d,r4])
# doesn't work!

e=Poly(r2**2*(r1**2*(a+c)*(a*c-r3**2)+c*(a*c-r1**2)*(a*c-r3**2)+r3**2*(a+c)*(a*c-r1**2))-r1**2*(a+c)*r3**2*(a+c)*c)
e.subs(r1,)
