#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/*
 * is_palindrome - Check if a linked list is palindrome
 * @head: First node of a list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if head == NULL
	{
		return (0);
	}

