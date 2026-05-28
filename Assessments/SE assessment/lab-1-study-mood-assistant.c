#include <stdio.h>

int main() {
    int hours;

    printf("Enter hours studied today: ");
    scanf("%d", &hours);

    if(hours >= 8) {
        printf("Excellent dedication! Keep it up.\n");
    }
    else if(hours >= 5) {
        printf("Good job! You are making progress.\n");
    }
    else if(hours >= 2) {
        printf("You can do better. Stay focused.\n");
    }
    else {
        printf("Start studying seriously today!\n");
    }

    return 0;
}