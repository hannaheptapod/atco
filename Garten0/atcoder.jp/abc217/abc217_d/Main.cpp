#include <bits/stdc++.h>
using namespace std;

int main() {
    int l, q;
    cin >> l >> q;
    vector<int> cut = {0, l};
    int n = 1;

    for (int i = 0; i < q; i++) {
        int c, x;
        cin >> c >> x;
        if (c == 1) {
            int ok = 0;
            int ng = n;

            while (ok + 1 < ng) {
                int md = (ok + ng) / 2;
                if (cut[md] < x) {
                    ok = md;
                    }
                else {
                    ng = md;
                }
            }
            cut.insert(cut.begin() + ng, x);
            n++;
        }
        else {
            int ok = 0;
            int ng = n;

            while (ok + 1 < ng) {
                int md = (ok + ng) / 2;
                if (cut[md] < x) {
                    ok = md;
                    }
                else {
                    ng = md;
                }
            }
            int ans = cut[ng] - cut[ok];
            cout << ans << endl;
        }
    }
    return 0;
}