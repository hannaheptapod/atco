#include <iostream>
#include <vector>
using namespace std;
int div(int a);
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int min = div(a[0]);
    for (int i = 1; i < n; i++) {
        if (div(a[i]) < min) min = div(a[i]);
    }
    cout << min;
    return 0;
}
int div (int a) {
    int counter = 0;
    while (a % 2 == 0) {
        a /= 2;
        counter++;
    }
    return counter;
}