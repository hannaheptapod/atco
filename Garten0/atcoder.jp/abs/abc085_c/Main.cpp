#include <iostream>
using namespace std;

int main() {
    int n, y;
    cin >> n >> y;
    y /= 1000;
    
    int a = -1, b = -1, c = -1;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            int k = n - i - j;
            int total = 10 * i + 5 * j + k;
            if (total == y && k >= 0) {
                a = i;
                b = j;
                c = k;
                break;
            }
        }
    }
    cout << a << " " << b << " " << c << endl;
    return 0;
}