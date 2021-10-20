#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    int inc = (a-b)/3 + b;
    double fc = ((double)a-b)/3 + b;
    if ((a-b)%3 == 0) cout << inc;
    else cout << fc;
    return 0;
}