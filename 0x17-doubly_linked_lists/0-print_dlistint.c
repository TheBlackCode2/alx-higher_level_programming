#include <stdio.h>
#include "lists.h"

/**
* print_dlistint - Write a function that prints all the elements of a dlistint_t list
* @h: pointer to the head
* Return: the number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
  size_t n = 0;

  while(h != NULL)
  {
    printf("%d", h->n);
    h = h->next;
    n++;
  }

  return (n);
}
