#include "lists.h"
/**
 * insert_node - inserts a given node in a sorted linked list
 * @head: pointer to the pointer to the first node
 * @number: the value of the node to be inserted
 * Return: address of the newly inserted node or null if error occurs
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current_n = *head, *temp = NULL, *pre_n = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (current_n->next != NULL)
	{
		if (new->n > current_n->n)
		{
			pre_n = current_n;
			current_n = current_n->next;
		}
		else
		{
			if (pre_n == NULL)
			{
				new->next = current_n;
				*head = new;
				return (new);
			}
			temp = pre_n->next;
			pre_n->next = new;
			new->next = temp;
			return (new);
		}
	}
	if (current_n->next == NULL)
	{
			current_n = *head;
			while (current_n->next != NULL)
				current_n = current_n->next;
			current_n->next = new;
	}
	return (new);
}
