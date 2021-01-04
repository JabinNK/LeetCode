class Solution {
public:
    bool hasCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if (!head){return false;}
        ListNode* p=head;
        ListNode* q=head;
        while(q->next && q->next->next){
            p=p->next;
            q=q->next->next;
            if (p==q){return true;}
        }
        return false;
    }
}