/**
 * Definition for singly-linked list.
 * struct ListNode {
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* temp = head;
        ListNode* prev = NULL;
        while (temp != NULL) {
            if (prev != NULL && temp->val == val) {
                prev->next = prev->next->next;
                temp = temp->next;
            }
            else if (prev == NULL && temp->val == val) {
                temp = temp->next;
                head = head->next;
            }
            else {
                prev = temp;
                temp = temp->next;
            }
        }
        return head;
    }
};