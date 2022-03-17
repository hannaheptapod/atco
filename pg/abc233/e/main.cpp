#include <bits/stdc++.h>
using namespace std;

vector<int> string_to_bigint(string S);
string bigint_to_string(vector<int> digit);
vector<int> carry_and_fix(vector<int> digit);
vector<int> addition(vector<int> digit_a, vector<int> digit_b);

int main() {
    string X;
    cin >> X;

    int leng = X.length();

    string ans = "0";
    for (long unsigned int i = 0; i < leng; i++) {
        vector<int> d_a, d_b;
        d_a = string_to_bigint(ans);
        d_b = string_to_bigint(X);

        ans = bigint_to_string(addition(d_a, d_b));
        X = X.substr(0, leng - 1 - i);
    }

    cout << ans << endl;

    return 0;
}

vector<int> string_to_bigint(string S) {
    int N = S.size();  // N = (文字列 S の長さ)
    vector<int> digit(N);
    for (int i = 0; i < N; ++i) {
        digit[i] = S[N - i - 1] - '0';  // 10^i の位の数
    }
    return digit;
}
string bigint_to_string(vector<int> digit) {
    int N = digit.size();  // N = (配列 digit の長さ)
    string str = "";
    for (int i = N - 1; i >= 0; --i) { str += digit[i] + '0'; }
    return str;
}
vector<int> carry_and_fix(vector<int> digit) {
    int N = digit.size();
    for (int i = 0; i < N - 1; ++i) {
        // 繰り上がり処理 (K は繰り上がりの回数)
        if (digit[i] >= 10) {
            int K = digit[i] / 10;
            digit[i] -= K * 10;
            digit[i + 1] += K;
        }
        // 繰り下がり処理 (K は繰り下がりの回数)
        if (digit[i] < 0) {
            int K = (-digit[i] - 1) / 10 + 1;
            digit[i] += K * 10;
            digit[i + 1] -= K;
        }
    }
    // 一番上の桁が 10 以上なら、桁数を増やすことを繰り返す
    while (digit.back() >= 10) {
        int K = digit.back() / 10;
        digit.back() -= K * 10;
        digit.push_back(K);
    }
    // 1 桁の「0」以外なら、一番上の桁の 0 (リーディング・ゼロ) を消す
    while (digit.size() >= 2 && digit.back() == 0) { digit.pop_back(); }
    return digit;
}
vector<int> addition(vector<int> digit_a, vector<int> digit_b) {
    int N = max(digit_a.size(), digit_b.size());  // a と b の大きい方
    vector<int> digit_ans(N);  // 長さ N の配列 digit_ans を作る
    for (int i = 0; i < N; ++i) {
        digit_ans[i] = (i < digit_a.size() ? digit_a[i] : 0) +
                       (i < digit_b.size() ? digit_b[i] : 0);
        // digit_ans[i] を digit_a[i] + digit_b[i] にする (範囲外の場合は 0)
    }
    return carry_and_fix(digit_ans);  // 2-4 節「繰り上がり計算」の関数です
}
