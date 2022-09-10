#include <iostream>
using namespace std;

int main()
{   int x = 10;
    int *pr;
    pr = &x;
    int y = *pr;
    cout<<"add of x is "<<pr<<endl;
    cout<<"add of y is "<<&y<<endl;
    cout<<"add of pr is "<<&pr<<endl;
    





    return 0;
}