#include <iostream>
using namespace std;

int main() {
    int a, b, c, x;
    cin >> a >> b >> c >> x;
    x = x / 50;
    int res = 0;
    for (int aNum = 0; aNum <= a; ++aNum) {
        for (int bNum = 0; bNum <= b; ++bNum) {
            for (int cNum = 0; cNum <= c; ++cNum) {
                int total = 10 * aNum + 2 * bNum + cNum;
                if (total == x) res++;
            }
        }
    }
    cout << res << endl;
}