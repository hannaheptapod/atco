#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> d(n);
    for (int i = 0; i < n; i++) cin >> d[i];
    sort(d.begin(), d.end());
    int num = 1;
    for (int i = 0; i < n; i++) {
        if (d[i + 1] - d[i] > 0) num++;
    }
    cout << num;
    return 0;
}