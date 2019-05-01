#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long int ui;

int main()
{
    ui n;
    cin >> n;

    ui d;

    priority_queue <ui, vector<ui>, greater<ui> > pqmin;
    priority_queue<ui> pqmax;

    for (ui i = 0; i < n; i++)
    {
        cin >> d;
        pqmin.push(d);
        pqmax.push(d);
    }

    // sort(ar, ar + n);

    ui k;
    cin >> k;

    ui kth;
    char c;
    ui temp_ar[n];

    for (ui i = 0; i < k; i++)
    {
        cin >> kth >> c;
        if (c == 'S')
        {
            for (ui j = 0; j < kth; j++){
                temp_ar[j] = pqmin.top();
                pqmin.pop();
            }

            cout << temp_ar[kth - 1] << endl;

            for (ui j = 0; j < kth; j++){
                pqmin.push(temp_ar[j]);
            }
        }
        else
        {
            for (ui j = 0; j < kth; j++){
                temp_ar[j] = pqmax.top();
                pqmax.pop();
            }

            cout << temp_ar[kth - 1] << endl;
            
            for (ui j = 0; j < kth; j++)
            {
                pqmax.push(temp_ar[j]);
            }
        }
        
    }

    return 0;

}