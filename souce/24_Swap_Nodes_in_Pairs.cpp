/*
24. Swap Nodes in Pairs
Medium

Overview:

    Swap every two nodes on a list.

Solutions:

    1. Common sequential solution.

        Keep 3 pointers of pre, cur, and nex nodes.

    2. Recursion

Compare:
                Runtime Memory
    Sequential  4 ms    8.7 MB
    Recursion   0 ms    8.6 MB
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        ListNode* nexNode = head->next;
        ListNode* curNode = head;
        ListNode* preNode = NULL;
        
        curNode->next = nexNode->next;
        nexNode->next = curNode;
        head = nexNode;
        
        while (true) {
            if (curNode->next == NULL || curNode->next->next == NULL)
                break;
            
            preNode = curNode;
            curNode = curNode->next;
            nexNode = curNode->next;
            
            preNode->next = nexNode;
            curNode->next = nexNode->next;
            nexNode->next = curNode;
        }
        
        return head;
    }
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        ListNode* nexNode = head->next;
        
        head->next = swapPairs(nexNode->next);
        nexNode->next = head;
        
        return nexNode;
    }
};