#include <iostream>

using namespace std;

int bin_search(int ar[], int low, int high, int k){
	
	int mid = low + (high - low)/2;
	if (mid < 0){
		return -1;
	}
	else if (mid == 0){
		if (ar[mid] == k){
			return mid;
		}
		else{
			return -1;
		}
	}
	else{
		if (ar[mid] == k){
			return mid;
		}
		else if (ar[mid] > k){
			return bin_search(ar, low, mid, k);
		}
		else{
			return bin_search(ar, mid + 1, high, k);
		}
	}
}


int main()
{
	int ar[5] = {1, 2, 3, 4, 5};
	int k = 10;

	int index = bin_search(ar, 0, 5, k);

	cout << "index: " << index << endl;
	return 0;
}
