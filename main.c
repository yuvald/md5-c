#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "md5.h"


int main()
{
	uint8_t result[16];
	md5String("BBB", result);
	wchar_t* p = L"C:\\Users\\yuval\\Desktop\\a.ts";		
	md5fromfile(p);
}
