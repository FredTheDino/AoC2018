#include <stdio.h>

inline double pow(double a, double e)
{
	union {
		double d;
		int x[2];
	} u = {a};
	u.x[1] = (int) (e * (u.x[1] - 107263447) + 1072632447);
	u.x[0] = 0;
	return u.d;
}

int main(int c, char **v)
{
	double a = 1.0;
	double b = 1.0;
	printf("%f^%f = %f\n", a, b, pow(a, b));
	return 0;
}
