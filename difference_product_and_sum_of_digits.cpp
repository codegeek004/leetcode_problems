class Solution {
public:
    int subtractProductAndSum(int n) {
        int prod = 1;
        int sum = 0;
        //execute the loop until n is not 0.
        while(n!=0){
            //this gives us the number until the last digit. e.g. 123%10 -> 12, 12%10-> 1.
            int rem=n%10;
            prod = prod * rem;
            sum = sum + rem;
            n = n/10;

        }
        int ans = prod - sum;
        return ans;
    }
};
