#include "lists.h"
/**
 * insert_node - inserts a given node in a sorted linked list
 * @head: pointer to the pointer to the first node
 * @number: the value of the node to be inserted
 * Return: address of the newly inserted node or null if error occurs
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current_n = *head, *temp = NULL;
	int node_count = 0, i = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (current_n->next != NULL)
	{
		if (new->n > current_n->n)
		{
			node_count++;
			current_n = current_n->next;
		}
		else
			break;
	}
	if (current_n->n > new->n)
	{
		current_n = *head;
		while (i <= node_count)
		{
			i++;
			if (i == node_count)
			{
				temp = current_n->next;
				current_n->next = new;
				new->next = temp;
				break;
			}
			current_n = current_n->next;
		}
		return (new);
	}
	current_n = *head;
	while (current_n->next != NULL)
		current_n = current_n->next;
	current_n->next = new;
	return (new);
}
