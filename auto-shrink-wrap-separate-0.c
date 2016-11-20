void f(int x)
{
	register int r20 asm("20") = x;
	asm("#before" : : "r"(r20));
}