#include <iostream>

using namespace std;

class Complex
{
  private:
    double real;
    double imag;

  public:
    Complex(double r = 0.0, double i = 0.0) : real(r), imag(i)
    {
    }
    ~Complex() {}
    Complex(const Complex &obj);
    void display() const;
    Complex operator+(const Complex &a);
    Complex operator-(const Complex &a);
    Complex &operator++();
    Complex operator++(int);
};

Complex::Complex(const Complex &obj)
{
    real = obj.real;
    imag = obj.imag;
}

void Complex::display() const
{
    if (imag > 0)
    {
        cout << real << "+" << imag << "i" << endl;
    }
    else if (imag == 0)
    {
        cout << real << endl;
    }
    else
    {
        cout << real << imag << "i" << endl;
    }
}

Complex Complex::operator+(const Complex &a)
{
    return Complex(real + a.real, imag + a.imag);
}

Complex Complex::operator-(const Complex &a)
{
    return Complex(real - a.real, imag - a.imag);
}

Complex &Complex::operator++()
{
    real++;
    imag++;
    return *this;
}

Complex Complex::operator++(int)
{
    Complex old = *this;
    ++(*this);
    return old;
}

int main(int argc, char const *argv[])
{
    Complex e;
    Complex a(9, 5);
    Complex b(3, 10);
    cout << "a+b=";
    Complex c(a + b);
    c.display();
    cout << "a-b=";
    Complex d(a - b);
    d.display();
    cout << "a-b=e,e=";
    e = d;
    e.display();
    cout << "a=";
    a.display();
    cout << "b=";
    b.display();
    cout << "c=";
    c.display();
    cout << "d=";
    d.display();
    cout << "e=";
    e.display();
    cout << "++a=";
    (++a).display();
    cout << "a++=";
    (a++).display();
    cout << "In Fact a is change into" << endl;
    a.display();
    return 0;
}
