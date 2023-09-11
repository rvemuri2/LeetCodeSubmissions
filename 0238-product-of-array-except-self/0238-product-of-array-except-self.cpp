class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        int n=nums.size(),mul;
        vector<int> left(n);
        vector<int> right(n);
        left[0]=1,right[n-1]=1;
        for(int i=1;i<n;i++){
            left[i]=left[i-1]*nums[i-1]; //nums[i-1] is multiplied for left val
        }
        for(int i=n-2;i>=0;i--){
            right[i]=right[i+1]*nums[i+1];
            //nums[i+1] val is multiplied for right
        }
        for(int i=0;i<n;i++){
            ans.push_back(left[i]*right[i]);
        }  
        return ans;
    }
};