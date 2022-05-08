#include <bits/stdc++.h>

using namespace std;
using Graph = vector<vector<int>>;

void dfs(int v, vector<bool> &flag, Graph &g);

int main() {
    int n, res = 0;
    cin >> n;
    vector<int> a(n);
    vector<bool> flag(2 * pow(10, 5) + 1, false);
    Graph g(2 * pow(10, 5) + 1);
    for (auto &nx : a) {
        cin >> nx;
        if (!flag[nx]) {
            flag[nx] = true;
            res++;
        }
    }

    int p = 0, q = n - 1;
    while (p < q) {
        g[a[p]].push_back(a[q]);
        g[a[q]].push_back(a[p]);
        p++;
        q--;
    }

    for (int i = 1; i <= 2 * pow(10, 5); i++) {
        if (flag[i]) {
            res--;
            dfs(i, flag, g);
        }
    }

    cout << res << endl;

    return 0;
}

void dfs(int v, vector<bool> &flag, Graph &g) {
    if (!flag[v]) return;
    flag[v] = false;
    for (auto &nx : g[v]) dfs(nx, flag, g);
}
