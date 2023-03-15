#include <iostream>

using namespace std;


class MyClass {
public:
    // Constructor
    MyClass(int value) {
        myValue = value;
    }

    // Member function
    void printValue() {
        cout << "The value is " << myValue << std::endl;
    }

private:
    int myValue;
};

int main() {
    // Create a MyClass object using the constructor
    MyClass obj(42);

    // Call the printValue() member function
    obj.printValue();

    return 0;
}