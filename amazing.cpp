#include <iostream>

using namespace std;

class nComplex; //前向声明

class Complex
{
  private:
    double real;
    double imag;

  public:
    Complex(double r = 0.0, double i = 0.0) : real(r), imag(i)
    {
    } //这其实是一个内联函数，为了简单就直接放在类内了，是隐式声明类内函数
    ~Complex() {}
    Complex(const Complex &obj);
    void display() const;
    friend nComplex; //声明为友元类
    //下面的函数都是常引用函数
    Complex operator+(const Complex &a);
    Complex operator-(const Complex &a);
    Complex operator*(const Complex &a);
    Complex &operator++();
    Complex operator++(int);
    //重载<<使用友元函数
    friend ostream &operator<<(ostream &out, const Complex &a);
    //注意下面都函数是在重载>>，这个时候不可以使用常引用，使用常引用会使对象无法被修改，导致无法传入参数，陷入死循环
    friend istream &operator>>(istream &in, Complex &a);
    Complex &operator[](int);
};

class nComplex : public Complex
{
  private:
    double vsum;

  public:
    nComplex(double r = 0, double u = 0, double v = 0) : Complex(r, u), vsum(v) {}
    double sum(const Complex &a);
};

double nComplex::sum(const Complex &a)
{
    return (a.real + a.imag);
}

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

Complex Complex::operator*(const Complex &a)
{
    return Complex(real * a.real, imag * a.imag);
}

Complex &Complex::operator[](int index)
{
}

ostream &operator<<(ostream &out, const Complex &a)
{
    if (a.imag < 0)
    {
        out << a.real << a.real << "i";
    }
    else if (a.imag > 0)
    {
        out << a.real << "+" << a.imag << "i";
    }
    else
    {
        cout << a.real;
    }
    return out;
}

istream &operator>>(istream &in, Complex &a)
{
    cout << "Input a Complex Number as x(real) x(imag)";
    in >> a.real >> a.imag;
    return in;
}

int main(int argc, char const *argv[])
{
    Complex e;
    Complex a(9, 5);
    Complex b(3, 2);
    cout << "a*b=";
    Complex g(a * b);
    g.display();
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
    cout << "a= " << a << endl;
    cout << "++ ++ a=";
    (++++a).display();
    cout << "In Fact a is change into" << endl;
    a.display();
    cout << "--------------------------" << endl;
    cout << "use << to show information" << endl;
    cout << "a=" << a << endl;
    cout << "b=" << b << endl;
    Complex z(b - a);
    cout << "b-a=" << z << endl;
    cout << "--------------------------" << endl;
    Complex arrayofcomplex[10];
    cout << arrayofcomplex[1] << endl;
    int index;
    cout << "--------------------------" << endl;
    cout << "Enter Index (<10)" << endl;
    cin >> index;
    cout << "Enter The Complex Number" << endl;
    cin >> arrayofcomplex[index];
    cout << "You Just Enter: ";
    cout << arrayofcomplex[index] << endl;
    cout << "--------------------------" << endl;
    nComplex sumComplex(2.0, 3.0, 5.0);
    cout << sumComplex << endl;
    cout << "--------------------------" << endl;
    return 0;
}
