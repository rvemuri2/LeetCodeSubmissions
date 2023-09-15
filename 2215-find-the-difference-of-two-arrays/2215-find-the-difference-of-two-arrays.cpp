class Solution {
public:
    vector<int> set_diff(vector<int>& n1, vector<int>& n2){
        unordered_set<int> S1_minus_S2;
        unordered_set<int> S2;
        for(int x: n2)
            if (S2.find(x)==S2.end()) S2.insert(x);
        for(int y: n1)
            if (S2.find(y)==S2.end()) S1_minus_S2.insert(y);
        return vector<int> (S1_minus_S2.begin(), S1_minus_S2.end());
    }
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        return {set_diff(nums1, nums2), set_diff(nums2, nums1)};
    }
};