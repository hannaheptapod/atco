#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> s(n);
    vector<int> t(n);
    for (int i = 0; i < n; i++) cin >> s[i] >> t[i];
    int a, b, c;
    string d;
    for (a = 0; a < n; a++) {
        for (b = a + 1; b < n; ++b) {
            if (t[a] > t[b]) {
                c = t[a];
                d = s[a];
                t[a] = t[b];
                s[a] = s[b];
                t[b] = c;
                s[b] = d;
            }
        }
    }
    cout << s[n - 2];
    return 0;
}