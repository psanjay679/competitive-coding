#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ui;

struct greaters{ 
  bool operator()(const long& a,const long& b) const{ 
    return a>b; 
  } 
};

int main(int argc, char const *argv[])
{
    ui n;
    cin >> n;

    ui a, b;

    // priority_queue<ui, vector<ui>, greater<ui>> minHeap;
    // priority_queue<ui> maxHeap;
    vector <ui> minHeap;
    vector <ui> maxHeap;
    make_heap(maxHeap.begin(), maxHeap.end());
    make_heap(minHeap.begin(), minHeap.end(), greaters());

    for (ui i = 0; i < n; i++)
    {
        cin >> a >> b;
        switch (a)
        {
            case 1:
                minHeap.push_back(b);
                maxHeap.push_back(b);
                break;
            case 3:
                cout << maxHeap.front() << endl;
                break;
            case 4:
                cout << minHeap.front() << endl;
                break;

            case 2:
                // This has to be taken care
                break;
        }
    }
    return 0;
}