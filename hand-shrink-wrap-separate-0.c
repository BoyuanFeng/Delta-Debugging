f(int x){register int r asm("20")=x;asm(""::""(r));}