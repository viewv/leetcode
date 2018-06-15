#include <iostream>

using namespace std;

class Array
{
  private:
    int a;
    int b;

  public:
    //注意下面的函数声明为友元函数，这是因为重载<<很可能需要访问私有数据，这时候要使用友元函数才可以访问
    friend std::ostream &operator<<(std::ostream &out, const Array &array);
    //注意下面的函数中不是常引用，如果是常引用将会导致无法输入数据！
    friend std::istream &operator>>(std::istream &in, Array &array);
    Array(int A, int B); //构造函数
    ~Array() {}          //析构函数
};

Array::Array(int A = 0, int B = 0)
{
    a = A;
    b = B;
}

//对<<的重载，这个地方比较难记忆，重载输入输出函数还是与普通的输入输出函数不太一样
ostream &operator<<(std::ostream &out, const Array &array)
{
    out << "Number A: " << array.a
        << " Number B: " << array.b << endl;
    return out;
}

istream &operator>>(std::istream &in, Array &array)
{
    in >> array.a >> array.b;
    return in;
}

//自定义模板类
template <class T>
T abs(T x)
{
    return x < 0 ? -x : x;
}

//自定义模板类
template <class T>
void outputarray(const T *array, int count)
{
    for (int i = 0; i < count; i++)
    {
        cout << array[i] << " ";
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    int x = -5;
    float y = -3.1;
    cout << abs(x) << "|" << abs(y) << endl;
    Array *array = new Array[5](); //new 之后必须手动加()才可以实现调用构造函数来初始化
    outputarray(array, 5);
    cin >> array[3]; //这里使用>>重载
    cout << array[3];
    return 0;
}
