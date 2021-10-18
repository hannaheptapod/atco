#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> t(n);
    vector<int> x(n);
    vector<int> y(n);
    bool flag = 1;
    for (int i = 0; i < n; i++) cin >> t[i] >> x[i] >> y[i];
    if (x[0] + y[0] > t[0] || (x[0] + y[0] + t[0]) % 2 == 1) flag = false;
    for (int i = 0; i < n - 1; i++) {
        int distance = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i]);
        int time = t[i + 1] - t[i];
        if (distance > time || (distance + time) % 2 == 1) flag = false;
    }
    if (flag == 1) cout << "Yes";
    else cout << "No";
    return 0;
}