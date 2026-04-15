class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        control = {None:None}
        aux = head
        while aux:
            temp = Node(aux.val)
            control[aux] = temp
            aux = aux.next
        
        curr = head
        while curr:
            cp = control[curr]
            cp.random = control[curr.random]
            cp.next = control[curr.next]
            curr = curr.next

        return control[head]