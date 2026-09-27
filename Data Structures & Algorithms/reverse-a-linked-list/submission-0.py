from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. Sauvegarder la suite de la liste
            curr.next = prev       # 2. Inverser la direction du pointeur
            prev = curr            # 3. Déplacer 'prev' d'un pas vers l'avant
            curr = next_node       # 4. Déplacer 'curr' d'un pas vers l'avant      
        return prev  # 'prev' devient la nouvelle tête de la liste inversée
