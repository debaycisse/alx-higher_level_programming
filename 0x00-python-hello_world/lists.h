#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);
int check_storage(listint_t *current_node, listint_t **all_nodes_addr);
void free_storage(listint_t **all_nodes_addr);
void store_address(listint_t *current_node, int store_at_pos, listint_t **all_nodes_addr);

#endif /* LISTS_H */
