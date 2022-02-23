/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.ArrayList;

class Solution {
    public ListNode reverseList(ListNode head) {       
        ListNode front, mid, back;
        
        if (head == null) return null;
        
        back = null;
        mid = head;
        front = head.next;
        
        while (front!=null) {
            mid.next = back;
            
            back = mid;
            mid = front;
            front = front.next;
        }
        mid.next = back;
    
        return mid;
    }
   
}
