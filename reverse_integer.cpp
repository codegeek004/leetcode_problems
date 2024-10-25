//problem 7
class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while(x!=0){
            //if 123 is input it runs like 123%10 -> 12%10 -> 1
            int digit = x % 10;
            //multiplying to get the ones, tens, hundred with 10 to reverse the order each time and adding the digit to get the reversed value
            ans = (ans*10) + digit;
            x = x / 10;

        }
        return ans;
        
    }
};
