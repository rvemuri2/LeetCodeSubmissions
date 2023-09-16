class Solution {
    public String removeStars(String s) {
         
        StringBuilder ans= new StringBuilder();
        
        Stack<Character>P = new Stack<>();
        
        //since operation is always possible
        //it means there is going to a character always to left of 
        // * so when we have * we pop the character 
        //else push it .
        for(int i=0;i<s.length();++i){
            char x = s.charAt(i);
            if(x == '*')P.pop();
            else P.push(x);
        }
        
        //after all the operations we form the string with left out elements
        while(!P.empty()){
            ans.append(P.peek());
            P.pop();
        }
        
        //since string formed will be in reverse order 
        //stack we get the last element so we need to reverse our string at the end
         ans.reverse();

        return ans.toString();
    }
}
