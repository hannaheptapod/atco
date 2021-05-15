#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> input(3);
    for(int i = 0; i < 3; i++) cin >> input[i];
    int a = input[0] - input[1];
    int b = input[0] - input[2];
    if ((a > 0 && b > 0) || (a < 0 && b < 0)) {
        if (a == b * 2 || b == a * 2) cout << "Yes";
        else cout << "No";
    } else if (a == 0 || b == 0) {
        if (a == b) cout << "Yes";
        else cout << "No"; 
    } else if (a == -b) cout << "Yes";
        else cout << "No";
    return 0;
}