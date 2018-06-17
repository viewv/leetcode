#include <iostream>
#include <cassert>
using namespace std;

template <class T>
class Array
{
  private:
    T *list;  //T类型指针，用于存放动态分配的数组内存首地址
    int size; //数组大小（元素个数）
  public:
    Array(int sz = 50);       //构造函数
    Array(const Array<T> &a); //复制构造函数
    ~Array();                 //析构函数

    Array<T> &operator=(const Array<T> &rhs); //重载=使数组对象可以整体赋值

    template <class S>
    friend ostream &operator<<(ostream &out, const Array<S> &rhs);
    template <class K>
    friend istream &operator>>(istream &in, Array<K> &rhs);

    Array<T> &operator+(const Array<int> &b);
    Array<T> &operator-(const Array<int> &b);

    T &operator[](int i); //重载[] ,使Array对象可以起到C++普通数组的作用
    //const T &operator[](int i) const; //“[]”运算符针对const的重载
    operator T *() const;       //重载到T*类型的转换，使Array对象可以起到C++普通数组的作用
    operator const T *() const; //到T*类型转换操作符针对const的重载

    int getsize() const; //取数组的大小
    void resize(int sz); //修改数组的大小
};

//构造函数
template <class T>
Array<T>::Array(int sz)
{
    assert(sz >= 0);    //sz为数组大小，为非负数
    size = sz;          //将元素个数赋值给变量size
    list = new T[size]; //动态分配size个T类型的元素空间
}

//析构函数
template <class T>
Array<T>::~Array()
{
    delete[] list;
}

template <class S>
ostream &operator<<(ostream &out, const Array<S> &rhs)
{
    int SIZE = rhs.getsize();
    for (int i = 0; i < SIZE; i++)
    {
        out << rhs.list[i] << " ";
    }
    return out;
}

template <class K>
istream &operator>>(istream &in, Array<K> &rhs)
{
    for (int i = 0; i < rhs.getsize(); i++)
    {
        in >> rhs[i];
    }
    return in;
}

//复制构造函数
template <class T>
Array<T>::Array(const Array<T> &a)
{
    size = a.size;
    list = new T[size];
    for (int i = 0; i < size; i++)
        list[i] = a.list[i];
}

//重载“=”运算符，将对象rhs赋值给本对象，实现对象之间的整体赋值
template <class T>
Array<T> &Array<T>::operator=(const Array<T> &rhs)
{
    if (&rhs != this)
    {
        if (size != rhs.size)
        {
            delete[] list;
            size = rhs.size;
            list = new T[size];
        }
        for (int i = 0; i < size; i++)
            list[i] = rhs.list[i];
    }
    return *this;
}

//重载+和-
template <class T>
Array<T> &Array<T>::operator+(const Array<int> &b)
{
    if (&b != this)
    {
        if (size != b.size)
            return *this;

        else
        {
            Array<int> c(size); //将c的内容
            for (int i = 0; i < size; i++)
            {
                c.list[i] = list[i] + b.list[i];
            }
            return c;
        }
    }
}

template <class T>
Array<T> &Array<T>::operator-(const Array<int> &b)
{
    if (&b != this)
    {
        if (size != b.size)
            return *this;

        else
        {
            Array<int> c(size); //将c的内容
            for (int i = 0; i < size; i++)
            {
                c.list[i] = list[i] - b.list[i];
            }
            return c;
        }
    }
}

//重载下标运算符，实现与普通数组一样通过下标访问元素，并且具有越界检查功能
/*template <class T>
const T &Array<T>::operator[](int n) const
{
    assert(n >= 0 && n < size);
    return list[n];
}*/

template <class T>
Array<T>::operator const T *() const
{
    return list;
}

//取用当前数组的大小
template <class T>
int Array<T>::getsize() const
{
    return size;
}

//将数组大小修改为sz
template <class T>
void Array<T>::resize(int sz)
{
    assert(sz >= 0);
    if (sz == size)
        return;
    T *newList = new T[sz];
    int n = (sz < size) ? sz : size;
    for (int i = 0; i < n; i++)
        newList[i] = list[i];
    delete[] list;
    list = newList;
    size = sz;
}

template <class T>
Array<T>::operator T *() const
{
    return list;
}

template <class T>
T &Array<T>::operator[](int i)
{
    assert(i >= 0 && i < size);
    return list[i];
}

int main()
{
    Array<int> a(5);
    Array<int> b(5);
    cout << "please input a and b:" << endl;
    cout << "a :";
    cin >> a;
    cout << "b :";
    cin >> b;
    Array<int> c = b;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "c = " << c << endl;
    cout << c.getsize() << endl;
    c.resize(10);
    cout << c.getsize() << endl;
    return 0;
}
