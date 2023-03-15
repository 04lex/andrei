#include <iostream>

using namespace std;

int main() {
    int n, suma = 0, produs = 1;

    cout << "Introduceți n: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        produs = produs*i; //parcurge 1*2*3*4;
        suma = suma + produs; //parcurge 1+1*2+1*2*3+1*2*3*4+...
    }
    cout<<produs;
    cout << "Rezultatul este: " << suma << endl;

    return 0;
}