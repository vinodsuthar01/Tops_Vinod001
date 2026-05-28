#include <stdio.h>

int main() {
    FILE *fp;
    char goal[100];

    fp = fopen("goals.txt", "a");

    if(fp == NULL) {
        printf("File could not be opened.\n");
        return 1;
    }

    printf("Enter your daily goal: ");
    scanf(" %[^\n]", goal);

    fprintf(fp, "%s\n", goal);

    fclose(fp);

    printf("\nSaved Goals:\n");

    fp = fopen("goals.txt", "r");

    while(fgets(goal, sizeof(goal), fp)) {
        printf("%s", goal);
    }

    fclose(fp);

    return 0;
}