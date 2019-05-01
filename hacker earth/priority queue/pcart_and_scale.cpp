#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ui;

int main(int argc, char const *argv[])
{
    ui n, m, x;
    cin >> n >> m >> x;

    ui d;

    priority_queue<ui, vector<ui>, greater<ui>> pq;

    for (ui i = 0; i < n; i++)
    {
        cin >> d;
        pq.push(d);
    }

    ui sum = 0;
    ui k;

    for (ui i = 0; i < m; i++)
    {
        sum += pq.top();
        sum = sum % 1000000007;
        k = pq.top();
        pq.pop();
        pq.push((k ^ x) + 1);

    }

    cout << sum << endl;

    return 0;
}
