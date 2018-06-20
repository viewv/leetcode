// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <string>

// using namespace std;

//!Below is problem 1
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

//!Below is problem 2
// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <string>

// using namespace std;
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

//// bool compare(const Student &a, const Student &b)
//// {
////     if (a.score > b.score)
////     {
////         return true;
////     }
////     return false;
//// }

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

//!Below is Problm 3
// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <string>

// using namespace std;
// template <class T>
// class Circle
// {
//   private:
//     T r;

//   public:
//     const T PI = 3.14;
//     Circle(T R = 0) : r(R){};
//     ~Circle(){};
//     T getArea()
//     {
//         return (PI * r * r);
//     }
// };

// int main(int argc, char const *argv[])
// {
//     Circle<float> small(3.0);
//     Circle<int> big(7);
//     cout << "Small Circle's Area: " << small.getArea() << endl;
//     cout << "Big Circle's Area: " << big.getArea() << endl;
//     return 0;
// }

//todo:Finish Problem 4
//!Below is the emam of computer science (co.)
//*I finish it!

// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <string>

// using namespace std;

// class Birthday
// {
//   private:
//     int year;
//     int month;
//     int date;

//   public:
//     Birthday(int y = 0, int m = 0, int d = 0) : year(y), month(m), date(d) {}
//     friend ostream &operator<<(ostream &out, const Birthday &a);
//     friend istream &operator>>(istream &in, Birthday &a);
//     friend bool operator<(const Birthday &a, const Birthday &b);
// };

// bool operator<(const Birthday &a, const Birthday &b)
// {
//     if (a.year > b.year)
//     {
//         return true;
//     }
//     else
//     {
//         if (a.year == b.year)
//         {
//             if (a.month > b.month)
//             {
//                 return true;
//             }

//             else
//             {
//                 if (a.month == b.month)
//                 {
//                     if (a.date > b.date)
//                     {
//                         return true;
//                     }
//                 }
//             }
//         }
//     }
//     return false;
// }

// ostream &operator<<(ostream &out, const Birthday &a)
// {
//     out << a.year << "/" << a.month << "/" << a.date;
//     return out;
// }

// istream &operator>>(istream &in, Birthday &a)
// {
//     cout << "Year: ";
//     in >> a.year;
//     cout << "Month: ";
//     in >> a.month;
//     cout << "Date: ";
//     in >> a.date;
// }

// class Employee
// {
//   private:
//     string num;
//     string name;
//     int gender;
//     Birthday birthday;

//   public:
//     friend Birthday;
//     Employee(string nu, string na, int gen, int y, int m, int d int f,int h,int area);
//     ~Employee() {}
//     friend ostream &operator<<(ostream &out, const Employee &a);
//     friend istream &operator>>(istream &in, Employee &a);
//     friend bool comp(const Employee &a, const Employee &b);
//     int getgender();
// };

// int Employee::getgender()
// {
//     return gender;
// }

// bool comp(const Employee &a, const Employee &b)
// {
//     if (a.birthday < b.birthday)
//     {
//         return false;
//     }
//     else
//     {
//         return true;
//     }
// }

// Employee::Employee(string nu = "", string na = "", int gen = 0, int y = 0, int m = 0, int d = 0)
//     : birthday(y, m, d)
// {
//     num = nu;
//     name = na;
//     gender = gen;
// }

// ostream &operator<<(ostream &out, const Employee &a)
// {
//     out << "Num: " << a.num << "\tName: " << a.name << "\tGender: "
//         << a.gender << "\tBirthday: " << a.birthday;
//     return out;
// }

// istream &operator>>(istream &in, Employee &a)
// {
//     cout << "Num: ";
//     in >> a.num;
//     cout << "Name: ";
//     in >> a.name;
//     cout << "Gender(0 or 1): ";
//     in >> a.gender;
//     cout << "Birthday-\n";
//     in >> a.birthday;
// }

// int main(int argc, char const *argv[])
// {
//     int n;
//     int sum = 0;
//     cout << "How Many Employees in This Company? ";
//     cin >> n;
//     vector<Employee> employee(n);
//     cout << "Please Input Data!" << endl;
//     for (int i = 0; i < n; i++)
//     {
//         cout << i + 1 << ": " << endl;
//         cin >> employee[i];
//     }
//     sort(employee.begin(), employee.end(), comp);
//     cout << "Sorted" << endl;
//     for (int i = 0; i < n; i++)
//     {
//         cout << employee[i] << endl;
//         sum += employee[i].getgender();
//     }
//     cout << "Male: " << sum << " Female: " << n - sum << endl;
//     return 0;
// }

//!Problem 4
//*Remember This Algorithm @Function computeArea
//Todo Remember @Function computeArea!

// #include <iostream>
// #include <vector>
// #include <algorithm>
// #include <string>

// using namespace std;
// class Point
// {
// private:
//   float x;
//   float y;

// public:
//   Point(float A = 0, float B = 0) : x(A), y(B) {}
//   ~Point() {}

//   friend istream &operator>>(istream &in, Point &p);
//   friend ostream &operator<<(ostream &out, const Point &p);
//   friend bool comp(const Point &a, const Point &b);
//   friend float computeArea(Point ar, Point al, Point br, Point bl);
// };

// // int computeArea(int A, int B, int C, int D, int E, int F, int G, int H)
// // {
// //   int sum = (C - A) * (D - B) + (H - F) * (G - E);
// //   if (E >= C || F >= D || B >= H || A >= G)
// //     return sum;
// //   return sum - ((min(G, C) - max(A, E)) * (min(D, H) - max(B, F)));
// // }

// bool comp(const Point &a, const Point &b)
// {
//   if (a.x <= b.x)
//   {
//     if (a.y <= b.y)
//     {
//       return true;
//     }
//   }
//   return false;
// }

// //!Important Algorithm!

// float computeArea(Point ar, Point al, Point br, Point bl)
// {
//   float A = ar.x;
//   float B = ar.y;
//   float C = al.x;
//   float D = al.y;
//   float E = br.x;
//   float F = br.y;
//   float G = bl.x;
//   float H = bl.y;
//   float sum = (C - A) * (D - B) + (H - F) * (G - E);
//   if (E > C || F > D || B > H || A > G)
//   {
//     return -1;
//   }

//   else if (E == C || F == D || B == H || A == G)
//   {
//     return 0.0;
//   }
//   else
//   {
//     return ((min(G, C) - max(A, E)) * (min(D, H) - max(B, F)));
//   }
// }

// istream &operator>>(istream &in, Point &p)
// {
//   cout << "Input x y" << endl;
//   in >> p.x >> p.y;
//   return in;
// }

// ostream &operator<<(ostream &out, const Point &p)
// {
//   out << "(" << p.x << "," << p.y << ")" << endl;
//   return out;
// }

// // Todo: One Day Use This Class To Finish This Problem
// // class Rect
// // {
// // private:
// //   Point a;
// //   Point b;
// //   Point c;
// //   Point d;

// // public:
// //   Rect(float Ax, float Ay, float Bx, float By, float Cx, float Cy, float Dx, float Dy);
// //   ~Rect() {}

// //   friend istream &operator>>(istream &in, Rect &k);
// // };

// // Rect::Rect(float Ax = 0, float Ay = 0, float Bx = 0, float By = 0, float Cx = 0, float Cy = 0, float Dx = 0, float Dy = 0)
// //     : a(Ax, Ay), b(Bx, By), c(Cx, Cy), d(Dx, Dy)
// // {
// // }

// // istream &operator>>(istream &in, Rect &k)
// // {
// //   cout << "Point A" << endl;
// //   in >> k.a;
// //   cout << "Point B" << endl;
// //   in >> k.b;
// //   cout << "Point C" << endl;
// //   in >> k.c;
// //   cout << "Point D" << endl;
// //   in >> k.d;
// //   return in;
// // }

// int main(int argc, char const *argv[])
// {
//   float sum = 0;
//   vector<Point> K(2);
//   cout << "Please Input Rect 1" << endl;
//   for (auto &elem : K)
//   {
//     cin >> elem;
//   }
//   sort(K.begin(), K.end(), comp);
//   vector<Point> P(2);
//   cout << "Please Input Rect 2" << endl;
//   for (auto &elem : P)
//   {
//     cin >> elem;
//   }
//   sort(P.begin(), P.end(), comp);
//   sum = computeArea(K[0], K[1], P[0], P[1]);
//   if (sum == -1)
//   {
//     cout << "Not Stack" << endl;
//   }

//   else
//   {
//     cout << "Area: " << sum << endl;
//   }

//   return 0;
// }

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Housing;
class Office;
class Building
{
private:
  int floor;
  int house;
  int area;

public:
  Building(int f = 0, int h = 0, int a = 0) : floor(f), house(h), area(a) {}
  // friend istream &operator>>(istream &in, Building &a);
  // friend ostream &operator<<(ostream &out, Building &a);
  friend Housing;
  friend Office;
  virtual void output() const = 0;
};

// istream &operator>>(istream &in, Building &a){
//   in >> a.floor >> a.house >> a.area;
//   return in;
// }

// ostream &operator<<(ostream &out, Building &a){
//   out << "Floor: "<<a.floor<<"\t"<<"House: "<< a.house<<"\t" <<"Area: "<< a.area ;
//   return out;
// }

class Housing : public Building
{
private:
  int bedroom;
  int washroom;

public:
  Housing(int f = 0, int h = 0, int a = 0, int b = 0, int w = 0)
      : Building(f, h, a)
  {
    bedroom = b;
    washroom = w;
  }
  ~Housing() {}
  void setup(int f, int h, int a, int b, int w);
  void output() const;
};

void Housing::setup(int f = 0, int h = 0, int a = 0, int b = 0, int w = 0)
{
  floor = f;
  house = h;
  area = a;
  bedroom = b;
  washroom = w;
}

void Housing::output() const
{
  cout << "Floor: " << floor << "\tHouse: " << house << "\tArea: " << area
       << "\tBedroom: " << bedroom << "\tWashroom: " << washroom << endl;
}

class Office : public Building
{
private:
  int defire;
  int tele;

public:
  Office(int f = 0, int h = 0, int a = 0, int d = 0, int t = 0)
      : Building(f, h, a)
  {
    defire = d;
    tele = t;
  }
  ~Office() {}
  void setup(int f, int h, int a, int d, int t);
  void output() const;
};

void Office::output() const
{
  cout << "Floor: " << floor << "\tHouse: " << house << "\tArea: " << area
       << "\tDefire: " << defire << "\tTelephone: " << tele << endl;
}

void Office::setup(int f = 0, int h = 0, int a = 0, int d = 0, int t = 0)
{
  floor = f;
  house = h;
  area = a;
  defire = d;
  tele = t;
}

int main(int argc, char const *argv[])
{
  Office office;
  Housing house;
  house.setup(20, 100, 100, 2, 2);
  office.setup(12, 100, 80, 10, 10);
  house.output();
  office.output();
  return 0;
}
