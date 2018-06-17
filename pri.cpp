#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

// template <class T>
// T getPower(T x, T y)
// {

//     if (y == 0)
//     {
//         return 1;
//     }

//     else if (y == 1)
//     {
//         return x;
//     }
//     else
//     {
//         return x * getPower(x, y - 1);
//     }
//     // T ans = 1;
//     // for (T i = 0; i < y; i++)
//     // {
//     //     ans = ans * x;
//     // }
//     // return ans;
// }

// int main(int argc, char const *argv[])
// {
//     int x, y;
//     cin >> x >> y;
//     cout << getPower(x, y) << endl;
//     return 0;
// }

// class Student
// {
//   private:
//     int num;
//     string name;
//     int age;
//     int score;

//   public:
//     Student(int Num, string Name, int Age, int Score);
//     ~Student();
//     int getscore();
//     bool operator<(const Student &stu)
//     {
//         return (score > stu.score);
//     }
//     friend istream &operator>>(istream &in, Student &stu);
//     // friend bool compare(const Student &a, const Student &b);
//     friend ostream &operator<<(ostream &out, Student &stu);
// };

// Student::Student(int Num = 0, string Name = "", int Age = 0, int Score = 0)
// {
//     num = Num;
//     name = Name;
//     age = Age;
//     score = Score;
// }

// Student::~Student()
// {
// }

// int Student::getscore()
// {
//     return score;
// }

// istream &operator>>(istream &in, Student &stu)
// {
//     cout << "Please Input info num name age score: ";
//     in >> stu.num >> stu.name >> stu.age >> stu.score;
//     return in;
// }

// ostream &operator<<(ostream &out, Student &stu)
// {
//     out << "Num: " << stu.num << " Name: " << stu.name << " Age: " << stu.age << " Score: " << stu.score;
//     return out;
// }

// // bool compare(const Student &a, const Student &b)
// // {
// //     if (a.score > b.score)
// //     {
// //         return true;
// //     }
// //     return false;
// // }

// int main(int argc, char const *argv[])
// {
//     int n;
//     float sum = 0;
//     cout << "How Many Student?" << endl;
//     cin >> n;
//     vector<Student> arrofstudent(n);
//     for (int i = 0; i < n; i++)
//     {
//         cin >> arrofstudent[i];
//     }
//     sort(arrofstudent.begin(), arrofstudent.end());
//     for (int i = 0; i < n; i++)
//     {
//         cout << arrofstudent[i] << endl;
//         sum += arrofstudent[i].getscore();
//     }
//     cout << "Average Score Of Student: " << sum / n << endl;
//     return 0;
// }

template <class T>
class Circle
{
  private:
    T r;

  public:
    Circle(T R = 0) : r(R){};
    ~Circle(){};
};


int main(int argc, char const *argv[])
{

    return 0;
}
