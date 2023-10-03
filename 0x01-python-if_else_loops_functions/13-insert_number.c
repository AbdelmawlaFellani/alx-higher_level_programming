#include "lists.h"
/**
 * insert_node - Inserts a node into a sorted linked list.
 * @head: Pointer to a pointer to the head of the list.
 * @number: Value to insert into the new node.
 *
 * Return: Address of the new node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr;
	listint_t *new;

	curr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (curr->next != NULL && curr->next->n < number)
		{
			curr = curr->next;
		}
		new->next = curr->next;
		curr->next = new;
		return (new);
	}
}
