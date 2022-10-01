#include <iostream>
using namespace std;
 
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
typedef long long ll;
 
void solve(){
    int n, a, e = 0;

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> a;
        if (a% 2 == 0) {
            e++;
        }
    }

    if (e == n) {
        cout << 0 << endl;
    }
    else {cout << e << endl;}
}
int main()
{
    fast_cin();
    ll t;
    cin >> t;
    for(int it=1;it<=t;it++) {
    solve();
    }
    return 0;
}