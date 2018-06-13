#include<iostream>

using namespace std;

class Clock{
    public:
        void setTime(int newH, int newM);
    private:
        int h,m;
};

void Clock::setTime(int newH,int newM){
    h=newH;
    m=newM;
}

int main(){
    Clock clock;
    clock.setTime(5,30);
    return 0;
}