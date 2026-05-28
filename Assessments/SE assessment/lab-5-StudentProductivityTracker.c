#include <stdio.h>

int main() {
    FILE *fp;
    int choice, day;
    float hours, total = 0, data[7];
    int i;

    do {
        printf("\n===== Student Productivity Tracker =====\n");
        printf("1. Log Study Hours\n");
        printf("2. Generate Weekly Report\n");
        printf("3. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch(choice) {

            case 1:
                fp = fopen("studyhours.txt", "a");

                printf("Enter day number (1-7): ");
                scanf("%d", &day);

                printf("Enter study hours: ");
                scanf("%f", &hours);

                fprintf(fp, "Day %d : %.2f hours\n", day, hours);

                fclose(fp);

                printf("Study hours saved successfully!\n");
                break;

            case 2:
                fp = fopen("studyhours.txt", "r");

                if(fp == NULL) {
                    printf("No data found.\n");
                    break;
                }

                printf("\n===== Weekly Report =====\n");

                char line[100];

                while(fgets(line, sizeof(line), fp)) {
                    printf("%s", line);
                }

                fclose(fp);
                break;

            case 3:
                printf("Exiting program...\n");
                break;

            default:
                printf("Invalid choice!\n");
        }

    } while(choice != 3);

    return 0;
}