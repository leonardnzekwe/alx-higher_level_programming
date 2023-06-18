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
	int i, j, num_nodes, *nodes_data;

	if (*head == NULL) /* empty list case section */
		return (1);
	ptr2 = *head; /* section for dynamic memory alloc for an array of integers */
	num_nodes = 0;
	while (ptr2 != NULL)
	{
		num_nodes = num_nodes + 1;
		ptr2 = ptr2->next;
	}
	nodes_data = malloc(sizeof(int) * num_nodes);
	if (nodes_data == NULL)
		return (1);
	ptr = *head; /* section that stores the data of each node in an array */
	i = 0;
	while (ptr != NULL)
	{
		nodes_data[i] = ptr->n;
		i = i + 1;
		ptr = ptr->next;
	}
	j = 0; /* section that checks if array values reads same to & fro */
	i = i - 1;
	while (i >= 0)
	{
		if (nodes_data[j] == nodes_data[i])
		{
			i = i - 1;
			j = j + 1;
		}
		else
		{
			free(nodes_data);
			return (0);
		}
	}
	free(nodes_data);
	return (1);
}
