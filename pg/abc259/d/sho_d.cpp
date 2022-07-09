// Link to the Problem
// https://atcoder.jp/contests/abc259/tasks/abc259_d

/*
    [ID: ruruvuvu]
    created at: 
    cleared at: 
*/

#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(),(x).end()
#define MOD 1000000007
#define INF 1000000000

typedef long long LL;
typedef long double LD;

int main()
{
    int n;
    cin >> n;
    pair<int, int> s, t;
    cin >> s.first >> s.second >> t.first >> t.second;
    vector<pair<int, int>> c(n);
    vector<int> r(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i].first >> c[i].second >> r[i];
    }

    set<int> queue, reach;
    for (int i = 0; i < n; i++) {
        int t_x = c[i].first - s.first;
        int t_y = c[i].second - s.second;
        if (t_x*t_x + t_y*t_y == r[i]*r[i])
            queue.insert(i);

        t_x = c[i].first - t.first;
        t_y = c[i].second - t.second;
        if (t_x*t_x + t_y*t_y == r[i]*r[i])
            reach.insert(i);
    }

    vector<vector<bool>> inter(n, vector<bool>(n, false));
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            int t_x = c[i].first - c[j].first;
            int t_y = c[i].second - c[j].second;
            int t_r = r[i] + r[j];
            int tt = r[i] - r[j];
            if (t_x*t_x + t_y*t_y <= t_r*t_r && t_x*t_x + t_y*t_y >= tt*tt) {
                inter[i][j] = true;
                inter[j][i] = true;
            }
        }
    }

    bool ok = false;
    set<int> expand, marked;
    while (!queue.empty()) {
        for (int q : queue) {
            marked.insert(q);
            for (int i = 0; i < n; i++) {
                if (inter[q][i] || inter[i][q]) {
                    expand.insert(i);
                }
            }
        }

        for (int e : expand) {
            auto find_e = reach.find(e);
            if (find_e != reach.end()) {
                ok = true;
            }

            find_e = marked.find(e);
            if (find_e != marked.end()) {
                expand.erase(e);
            }
        }

        if (ok) break;

        queue = expand;
    }

    if (ok) cout << "Yes" << endl;
    else cout << "No" << endl;

    return 0;
}
