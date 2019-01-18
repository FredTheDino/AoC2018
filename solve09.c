#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define PLAYER_CNT 463
#define MARBLE_CNT (71787*100)

struct node {
	uint64_t num;
	struct node *cw;
	struct node *ccw;
};

int main(int argc, char **argv)
{
	// NOTE: Unlimited stack size needed.
	// GOTTA GO FAST
	struct node __mem[(MARBLE_CNT + 1000) * sizeof(struct node)];
	struct node *mem = (struct node *) __mem;
	struct node *current = mem++;
	uint64_t scores[PLAYER_CNT] = {0};
	current->num = 0;
	current->cw = current;
	current->ccw = current;

	for (uint64_t i = 1; i <= MARBLE_CNT; i++) {
		int player = (i - 1) % PLAYER_CNT;
		if (i % 23 == 0) {
			scores[player] += i;
			// 7 marbles counter-clockwise
			struct node *traverse = current;
			for (int k = 0; k < 7; k++) {
				traverse = traverse->ccw;
			}
			traverse->ccw->cw = traverse->cw;
			traverse->cw->ccw = traverse->ccw;
			current = traverse->cw;
			scores[player] += traverse->num;
			// Skipp that slow free.
		} else {
			struct node *next = current->cw;
			struct node *nextnext = next->cw;
			struct node *insert = mem++;
			insert->num = i;
			insert->cw = nextnext;
			nextnext->ccw = insert;
			insert->ccw = next;
			next->cw = insert;
			current = insert;
		}
	}

	uint64_t max = 0;
	for (int i = 0; i < PLAYER_CNT; i++) {
		max = scores[i] > max ? scores[i] : max;
	}
	printf("%lld\n", max);
}

