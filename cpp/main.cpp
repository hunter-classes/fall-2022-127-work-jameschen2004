#include <iostream>
#include <cmath>

// Completed 'Show a working if and loop' and 'Show a working function'

int absolute_value(int num) {
    if (num >= 0) {
        return num;
    } else {
        return num - (2 * num);
    }

}
int main(){
    std::cout << "Hello World! \n";
    std::cout << "The absolute value of -3 is " << absolute_value(-3) << "\n";

    for (int num = 0; num < 5; num ++) {
        std::cout << num << " squared is " << pow(num,2) << "\n";
    }
    
    return 0;
}

