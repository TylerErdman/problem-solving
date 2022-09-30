#include <iostream>
using namespace std;

int main() {
	int n, a, b;
    cin >> n;
    for (int i = 0;i < n; i++) {
        cin >> a >> b;
        a = a / 10;
        cout << a * b << "\n";
    }
	return 0;
}
