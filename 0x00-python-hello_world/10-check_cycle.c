#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *mv_once;
	listint_t *mv_twice;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	mv_once = list;
	mv_twice = list->next;
	while (mv_twice != NULL && mv_twice->next != NULL)
	{
		if (mv_once == mv_twice)
		{
			return (1);
		}
		mv_once = mv_once->next;
		mv_twice = mv_twice->next->next;
	}
	return (0);
}
