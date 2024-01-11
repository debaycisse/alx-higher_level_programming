#include "lists.h"

/**
 * print_dlistint - prints out the doubly-linked list
 * @h: pointer to the fist node in the linked list
 * Return: the number of elements in a list whose head node is given
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count;
	const dlistint_t *current = h;

	count = 0;
	while (current != NULL)
	{
		count++;
		printf("%i\n", current->n);
		current = current->next;
	}
	return (count);
}
