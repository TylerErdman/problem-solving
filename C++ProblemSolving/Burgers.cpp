#include <iostream>
using namespace std;

int main() {
	int n;
    cin >> n;
    int a;
    int b;
    for (int i = 0; i < n; i++){
        cin >> a >> b;
        if (a > b) {
            cout << b;
        }
        else {cout << a;}
        cout << "\n";
    }
	return 0;
}

