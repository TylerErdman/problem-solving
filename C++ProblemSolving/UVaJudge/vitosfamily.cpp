#include <iostream>
using namespace std;
 
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
typedef long long ll;
 
void solve(){

}
int main()
{
    fast_cin();
    ll t;
    int houses;
    cin >> t;
    for(int it=1;it<=t;it++) {
        int answer;
        cin >> houses;
        int sum;
        int num;
        for (int i = 0;i < houses; i++) {
            cin >> num;
            sum = sum + num;
        }
        answer = sum / houses;
        cout << answer << endl;
    }
    return 0;
}