#include <iostream>
using namespace std;

int main() {
	int t ; cin >> t ; 
	while (t--) 
	{
int n ; cin >> n ; 
if (n<4) 
{
    cout << "-1" << endl ;  
}
else if (n==4) 
{
    cout << "2 4 1 3" << endl ;
}
else 
{
int x = 1 , y = 2 ; 
while (x <= n) 
{
    cout << x << " " ; 
    x+=2 ; 
}
while (y <= n)
{
    cout << y << " " ; 
    y+=2 ; 
}
cout << endl ; 
}
}
}