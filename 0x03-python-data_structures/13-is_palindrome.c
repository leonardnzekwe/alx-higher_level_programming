#include "lists.h"

/**
 * is_palindrome - function that checks
 * if a singly linked list is a palindrome
 * An empty list is considered a palindrome
 * @head: node head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr2;
	int i, j, num_nodes;

	if (*head == NULL)
		return (0);

	ptr2 = *head;
	num_nodes = 0;
	while (ptr2 != NULL)
	{
		num_nodes = num_nodes + 1;
		ptr2 = ptr2->next;
	}
	int nodes_data[num_nodes];

	ptr = *head;
	i = 0;
	while (ptr != NULL)
	{
		nodes_data[i] = ptr->n;
		i = i + 1;
		ptr = ptr->next;
	}

	j = 0;
	i = i - 1;
	while (i >= 0)
	{
		if (nodes_data[j] == nodes_data[i])
		{
			i = i - 1;
			j = j + 1;
		}
		else
			return (0);
	}
	return (1);
}
