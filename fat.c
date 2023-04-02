#include <stdio.h>

int	fatorial(int nb)
{
	int	i;
	int	result;

	i = 1;
	result = 1;
	if (nb < 0)
	{
		return (0);
	}
	else if (nb <= 1)
	{
		return (1);
	}
	while (i <= nb)
	{
		result = i * result;
		i++;
	}
	return (result);
}

int	main (void)
{
	printf("%d\n", fatorial(10));
}
