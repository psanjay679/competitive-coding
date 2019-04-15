#include <iostream>
#define rep(n) for(int i = 0; i < n; i++)
typedef long long int ll;

using namespace std;

int main()
{
    ll n, k, d, l = 0;

    cin >> n >> k;

    rep(n)
    {
        cin >> d;
        if (d > k)
        {
            l += 2;
        }
        else
        {
            l += 1;
        }
    }

    cout << l << endl;
    return 0;
}