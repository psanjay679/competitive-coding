#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

#define sz 65536

int main(){
    int n;
    cin >> n;

    bitset<sz> bits;

    vector< vector<int> > v;
    int d;
    for (int i = 0; i < n; i++){
        cin >> d;
        bits[d] = 1;
    }

    cout << bits << endl;

    for (int b = 0; b < (1 << n); b++){
        vector<int> subset;
        for (int i = 0; i < n; i++){
            if (bits[b] & (1 << i)) subset.push_back(i);
        }

        v.push_back(subset);
    }

    cout << "{\n";
    for (int i = 0; i < v.size(); i++){
        cout << "{ ";
        for (int j = 0; j < v[i].size(); j++){
            cout << v[i][j] << " ";
        }
        cout << "}\n";
    }

    cout << "}\n";


    return 0;
}
