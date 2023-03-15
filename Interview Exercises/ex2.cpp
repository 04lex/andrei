#include <iostream>
using namespace std;

int cautare(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i; 
        }
    }
    return -1; //returneaza -1 daca nu s a  gasit nmk

}

int main() {
    int arr[] = {3, 5, 2, 8, 4, 9, 1};
    int n = sizeof(arr);
    int x = 5;
    int index = cautare(arr, n, x);
    if (index == -1) {
        cout << "Valoarea " << x << " nu a fost gasita in vector.";
    } else {
        cout << "Valoarea " << x << " a fost gasita la indexul " << index << " in vector.";
    }
    return 0;
}