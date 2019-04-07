#include <iostream>
#include <algorithm>
#include <cmath>
#include <set>
#include <string>
#include <map>

using namespace std;

int main(){
    int t;
    int n, l;
    cin >> t;
    for (int Case = 1; Case <= n; Case++){
        cin >> n >> l;
        int ar[l];
        for (int i = 0; i < l; i++){
            cin >> ar[i];
        }

        int primes[l + 1];
        for (int i = 3; i < (int)(sqrt(ar[0]) + 1); i++){
            if (ar[0] % i == 0){
                primes[0] = i;
                break;
            }
        }

        set<int> s;
        for (int i = 0; i < l; i++){
            primes[i + 1] = ar[i] / primes[i];
            s.insert(primes[i]);
        }

        sort(s.begin(), s.end());

        string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        map<int, char> ump;
        set<int>::iterator it = s.begin();

        for (int i = 0; i < 26; i++){
            int value = *it;
            ump.insert(make_pair(value, letters[i]));
            advance(it, 1);
        }

        string ans = "";
        for (int i = 0; i < l + 1; i++){
            ans += ump[primes[i]];
        }

        cout << "Case #" << Case << " : " << ans << endl;
    }

    return 0;
}