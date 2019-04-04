#include <iostream>
#define rep(n) for(auto i = 0; i < n; i++)

using namespace std;

int bin_search(int ar[], int low, int high, int k){
	
	int mid = low + (high - low)/2;
	if (low < high){
		if (ar[mid] == k){
			return mid;
		}
		else if (ar[mid] < k){
			return bin_search(ar, mid + 1, high, k);
		}
		else{
			return bin_search(ar, low, mid, k);
		}
	}
}


int main()
{
	int n;
	cin >> n;

	int ar[n] 
	
	rep(n){
		cin >> ar[i];
	}

	int k;
	cin >> k;

	int index = bin_search(ar, 0, 5, k);

	cout << "index: " << index << endl;
	return 0;
}
