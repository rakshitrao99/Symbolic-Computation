# DECLARATION:
#While most of the important part of the code has been done in the class.
#I have just added the concept of  subtraction, multiplication, division and exponentiation to the given class 'expr'.
#While I tried my best to work out the assignment myself but a few times I got struck. In that case I first tried to google the problem
#and then I have a good discussion with my friend,Sourav Kumar. But at the end, I all the codes are completely implemented by me.

#THOUGHT PROCESS:
#In order to keep things simple, I have considered  a very simple symbolic-differentiation program that handles expressions that are build up
#using the operations of addition and multiplication with two arguments. 
#Differentiation of any such expression can be carried out by applying the following reduction rules:
#1.)  dc/dx=0  where 'c' a constant or a variable different from x
#2.)  dx/dx=1
#3.)  (d(u+v))/dx=du/dx+dv/dx
#4.)  (d(uv))/dx=u(dv/dx)+v(du/dx)




class expr:
        
    def __init__(self,S,Null = None):
        if (Null):
            self.expr = Null
        else:
            (e,n) = self.parse(S)
            self.expr = e
    class Node:
        def __init__(self,data):
            self.left = None
            self.right = None
            self.data = data
            
        def toString(self):
            if (self.left and self.right):
                left = self.left.toString()
                right = self.right.toString()
                operation = self.data
                return "(" + left + " " + operation + " " + right + ")"
            else:
                return self.data

        def prettyprint(self):
            s = self.expr.toString()
            print(s)
                
        def parse(self,S):
            l = len(S)
            if (S[0] == "("):
                (left,n) =  self.parse(S[1:l-2])
                operation = S[n+1]
                (right,m) = self.parse(S[n+2:l-1])
                expr = self.Node(operation)
                expr.left = left
                expr.right = right
                return (expr,n+m+3)
        
            elif S[0].isdigit():
                i = 0
                while ((i < l) and (S[i].isdigit() or (S[i] == "."))):
                    i = i+1
                    num = S[0:i]
                    expr = self.Node(num)
                    return (expr,i)
            elif S[0].isalpha():
                i = 0
                while ((i < l) and S[i].isalpha()):
                    i = i+1
                    var = S[0:i]
                    expr = self.Node(var)
                    return (expr,i)
            else:
                return Exception("Invalid input")

    def constant(self):
        if self.expr.data[0].isdigit():
            return True
        else:
            return False

    def variable(self):
        if self.expr.data[0].isalpha():
            return True
        else:
            return False

    def samevariable(self,x):
        if (self.expr.data == x):
            return True
        else:
            return False

    def addition(self):
        if (self.expr.data == '+'):
            return True
        else:
            return False
    def multiplication(self):                              
        if(self.expr.data=='*'):
            return True
        else:
            return False

    def division(self):                                          
        if(self.expr.data=="/"):
            return True
        else:
            return False
    def exponentiation(self):                                  
        if(self.expr.data=="^"):
            return True
        else:
            return False
    def difference(self):                                 
        if(self.expr.data=="-"):
            return True
        else:
            return False                            


    def addend(self):
        left = self.expr.left
        return expr("",left)

    def augend(self):
        right = self.expr.right
        return expr("",right)

    def makeproduct(self,e1,e2):
        e=self.Node("*")
        e.left=e1.expr
        e.right=e2.expr
        return expr("",e)

    def makedivision(self,e1,e2):
        e=self.Node("/")
        e.left=e1.expr
        e.right=e2.expr
        return expr("",e)

    def makepower(self,e1,e2):
        e=self.Node("^")
        e.left=e1.expr
        e.right=e2.expr
        return expr("",e)

    def makesum(self,e1,e2):
        e = self.Node("+")
        e.left = e1.expr
        e.right = e2.expr
        return expr("",e)
        
    def makedifference(self,e1,e2):
        e = self.Node("-")
        e.left = e1.expr
        e.right = e2.expr
        return expr("",e)

    def deriv(self,x):
        if self.constant():
            return expr("0.0")
        
        elif self.variable():
            if self.samevariable(x):
                return expr("1.0")
            else:
                return expr("0.0")
        
        elif self.addition():
            e1 = self.addend()
            e2 = self.augend()
            return self.makesum(e1.deriv(x),e2.deriv(x))

        elif self.exponentiation():
            e1 = self.addend()
            e2 = self.augend()
            return self.makeproduct(e2,self.makepower(e1,self.makedifference(e2,expr("1"))))
        
        elif self.division():
            e1 = self.addend()
            e2 = self.augend()
            return self.makedivision((self.makedifference(self.makeproduct(e1.deriv(x),e2),self.makeproduct(e2.deriv(x),e1))),self.makeproduct(e2,e2))
        
        elif self.multiplication():
            e1 = self.addend()
            e2 = self.augend()
            return self.makesum(self.makeproduct(e1.deriv(x),e2),self.makeproduct(e2.deriv(x),e1))
        
        elif self.difference():
            e1 = self.addend()
            e2 = self.augend()
            return self.makedifference(e1.deriv(x),e2.deriv(x))    
        
        else:
            raise Exception("DontKnowWhatToDo!")
                

a = input("Enter an expression:")
e = expr(a)
e.prettyprint()
f = e.deriv('x')
f.prettyprint()
    
