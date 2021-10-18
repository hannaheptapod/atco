#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    //for (int i = 0; i < n; i++) cout << a[i]; cout << endl;
    if (n % 2 == 0) {
        int max = 0;
        for (int i = 0; i < n / 2; i++) max += (a[2 * i + 1] - a[2 * i]);
        cout << max;
    } else {
        int max = a[0];
        for (int i = 0; i < n / 2; i++) max += (a[2 * i + 2] - a[2 * i + 1]);
        cout << max;
    }
    return 0;
}