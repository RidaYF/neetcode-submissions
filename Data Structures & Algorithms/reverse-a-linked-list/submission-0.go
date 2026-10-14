/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {

    var prev *ListNode = nil
    current := head

    for current != nil {
        nextTmp := current.Next
        current.Next = prev
        prev = current
        current = nextTmp
    }

    return prev

}
