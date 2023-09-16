class Solution {
public:
    string removeStars(string s) {
        int i=0,j=0,n=s.length();
        while(i<n){
            if(s[i]=='*'){
                j--;
            }else{
                s[j++] = s[i];
            }
            i++;
        }
        return s.substr(0,j);
    }
};