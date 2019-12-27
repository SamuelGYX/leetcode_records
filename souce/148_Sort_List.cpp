/*
148. Sort List Medium

Overview:
    
    Sort a linked list in O(nlogn) time using constant space complexity.

Solution:
    
    Merge sort without recursion.
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
    ListNode* sortList(ListNode* head) {
        if (!head || !(head->next))
            return head;
        
        ListNode* cur = head;
        int length = 0;
        while (cur) {
            length++;
            cur = cur->next;
        }
        
        ListNode preHead(0);
        preHead.next = head;
        ListNode* tail, * first, * second;
        for (int step = 1; step < length; step <<= 1) {
            tail = &preHead;
            cur = preHead.next;
            while (cur) {
                first = split(cur, step);
                second = split(cur, step);
                tail = merge(tail, first, second);
            }
        }
        return preHead.next;
    }

private:
    ListNode* split(ListNode*& cur, int step) {
        ListNode* res = cur;
        for (int i = 1; i < step && cur; i++)
            cur = cur->next;
        if (cur) {
            ListNode* tmp = cur;
            cur = cur->next;
            tmp->next = NULL;
        }
        return res;
    }
    
    ListNode* merge(ListNode* tail, ListNode* first, ListNode* second) {
        while (first && second) {
            if (first->val < second->val) {
                tail->next = first;
                first = first->next;
            } else {
                tail->next = second;
                second = second->next;
            }
            tail = tail->next;
        }
        if (first) {
            tail->next = first;
        } else {
            tail->next = second;
        }
        while (tail->next)
            tail = tail->next;
        return tail;
    }
};