typedef int V __attribute__ ((vector_size (8 * sizeof (int))));
V a, b, c, d, e, f;
foo (int x, int y)
{
	do
	    {
			if (x)
				d = a ^ c;
			else
				d = a ^ b;
	    }
	while (y);
}