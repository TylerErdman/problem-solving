#include <iostream>
using namespace std;

int main() {
	int n, a;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a % 25 == 0){
           a = a / 25; 
        }
        else {a = (a / 25) + 1;}
        cout << a << "\n";
    }
	return 0;
}
