#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for the presence of loop in a linked list
 * @list: the list that is to be checked
 * Return: 1, if loop is present ortherwise, 0 is returned
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node = NULL, **head = NULL;
	int i = 0;
	listint_t **addr_all_nodes = malloc(sizeof(listint_t *) * 31);

	if (addr_all_nodes)
	{
		for (i = 0; i < 31; i++)
			addr_all_nodes[i] = NULL;
	}
	head = malloc(sizeof(listint_t *));
	head = &list;
	for (i = 0; list; i++)
	{
		current_node = list;
		if (check_storage(current_node, addr_all_nodes) == 1)
		{
			free_storage(addr_all_nodes);
			list = *head;
			printf("%i : value of *head", ((*head)->next)->n);
			return (1);
		}
		store_address(current_node, i, addr_all_nodes);
		list = list->next;
	}
	printf("%i : value of *head", ((*head)->next)->n);
	free_storage(addr_all_nodes);
	list = *head;

	return (0);
}

/**
 * check_storage - checks for an existence of a given memory location
 * @current_node: the memory location to be looked up
 * @all_nodes_addr: the storage for all memory locations
 * Return: 1, if memory location exists, else 0 is returned
 */
int check_storage(listint_t *current_node, listint_t **all_nodes_addr)
{
	int i;

	i = 0;
	while (all_nodes_addr[i])
	{
		if (current_node == all_nodes_addr[i])
			return (1);
		i++;
	}
	return (0);
}

/**
 * free_storage - frees up the used space for storing memory locations
 * @all_nodes_addr: the list of memory addresses for traversed nodes
 */
void free_storage(listint_t **all_nodes_addr)
{
	int i = 0;

	for (i = 0; i < 31; i++)
	{
		if (all_nodes_addr[i])
			free(all_nodes_addr[i]);
	}
	if (all_nodes_addr)
		free(all_nodes_addr);
}

/**
 * store_address - stores memory address of each traversed node
 * @current_node: the current node, being processed
 * @store_at_pos: index location to save a memory location
 * @all_nodes_addr: the list of all traversed nodes' location 
 */
void store_address(
		listint_t *current_node,
		int store_at_pos,
		listint_t **all_nodes_addr)
{
	all_nodes_addr[store_at_pos] = current_node;
}
