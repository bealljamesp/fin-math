class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.c = complex(real, imaginary)
        
    def __add__(self, no):
        _ = self.c + no.c
        return Complex(_.real, _.imag)
            
    def __sub__(self, no):
        _ = self.c - no.c
        return Complex(_.real, _.imag)
        
    def __mul__(self, no):
        _ = self.c * no.c
        return Complex(_.real, _.imag)
    
    def __truediv__(self, no):
        _ = self.c / no.c
        return Complex(_.real, _.imag)
        
    def mod(self):
        _ = abs(self.c)
        return Complex(_.real, _.imag)

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

    