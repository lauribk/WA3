#include <iostream>
#include <vector>
#include <string>

using namespace std;

void bruteForce(vector<int> & nums1,vector<int> & nums2) {
    int m = nums1.size();
    int n = nums2.size();
    vector<int> CombineArrays;
    for (int i = 0; i <= n + m;i++)
        int j = 0;
        int k = 0;
        if (nums1[j] < nums2[k]) {

        }
}

int main () {

    vector<int> num1 = {1,4,8,10};
    vector<int> num2 = {4,4,9,12};

    cout << bruteForce(num1, num2) << endl;

    return 0;
}