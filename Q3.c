#include <stdio.h>
#include <stdlib.h>

#define MENU_SORT 1
#define MENU_FIND 2
#define MENU_ADD 3
#define MENU_REMOVE 4
#define MENU_SAVE 5
#define MENU_LOAD 6
#define MENU_QUIT 7

#define SORT_BY_ID 1
#define SORT_BY_NAME 2
#define SORT_BY_ADDRESS 3
#define SORT_BY_GRADE 4

#define FIND_BY_ID 1
#define FIND_BY_NAME 2
#define FIND_BY_ADDRESS 3
#define FIND_BY_GRADE 4

#define REMOVE_BY_ID 1
#define REMOVE_BY_NAME 2
#define REMOVE_BY_ADDRESS 3
#define REMOVE_BY_GRADE 4

typedef struct {
    int id;
    char* address;
    char* name;
    double grade;
} STUDENT;

void sortStudent(STUDENT* students, int studentSize);
void findStudent(STUDENT* students, int studentSize);
void addStudent(STUDENT** students, int* studentSize, int* studentCapacity);
void removeStudent(STUDENT** students, int* studentSize);
void saveList(STUDENT* students, int studentSize);
void loadList(STUDENT** students, int* studentSize, int* capacity);
void mergeSort(STUDENT* students, int left, int right, STUDENT** sorted, int sortBy);
void merge(STUDENT* students, int left, int mid, int right, STUDENT** sorted, int sortBy);

char* input() {
    char* str = NULL;
    int size = 0;
    int capacity = 16;
    str = (char*)malloc(capacity * sizeof(char));
    if (str == NULL) {
        printf("메모리 할당 오류!\n");
        return NULL;
    }
    char one;
    scanf(" ");
    while (1) {
        scanf("%c", &one);
        if (one == '\n') break;
        str[size++] = one;
        if (size == capacity) {
            capacity *= 2;
            char* temp = NULL;
            temp = (char*)realloc(str, capacity * sizeof(char));
            if (temp == NULL) {
                printf("메모리 할당 오류!\n");
                free(str);
                return NULL;
            }
            str = temp;
        }
    }
    str[size] = '\0';
    return str;
}

int fstrcmp(const char* s1, const char* s2) {
    while (*s1 && (*s1 == *s2)) {
        s1++;
        s2++;
    }
    return *(const unsigned char*)s1 - *(const unsigned char*)s2;
}

int sLen(const char* s) {
    int length = 0;
    while (*s != '\0') {
        length++;
        s++;
    }
    return length;
}

int main() {
    int studentCapacity = 16, studentSize = 0;
    STUDENT* students = NULL;

    students = (STUDENT*)malloc(sizeof(STUDENT) * studentCapacity);
    if (students == NULL) {
        printf("메모리 할당 오류!\n");
        return -1;
    }
    while (1) {
        int menuSelection = 0;
        printf("=====메뉴=====\n");
        printf("1. 학생 정렬\n");
        printf("2. 학생 찾기\n");
        printf("3. 학생 추가\n");
        printf("4. 학생 삭제\n");
        printf("5. 출석부 저장\n");
        printf("6. 출석부 불러오기\n");
        printf("7. 프로그램 종료\n");
        printf("메뉴 번호를 입력하세요 : ");
        scanf("%d", &menuSelection);
        switch (menuSelection) {
        case MENU_SORT:
            sortStudent(students, studentSize);
            break;
        case MENU_FIND:
            findStudent(students, studentSize);
            break;
        case MENU_ADD:
            addStudent(&students, &studentSize, &studentCapacity);
            break;
        case MENU_REMOVE:
            removeStudent(&students, &studentSize);
            break;
        case MENU_SAVE:
            saveList(students, studentSize);
            break;
        case MENU_LOAD:
            loadList(&students, &studentSize, &studentCapacity);
            break;
        case MENU_QUIT:
            /*for (int i = 0; i < studentCapacity; i++) {
                free(students[i].name);
                free(students[i].address);
            }*/
            free(students);
            return 0;
        default:
            printf("*올바른 번호를 선택해주십시오*\n");
            continue;
        }
    }
    for (int i = 0; i < studentCapacity; i++) {
        free(students[i].name);
        free(students[i].address);
    }
    free(students);
    return 0;
}

void sortStudent(STUDENT* students, int studentSize) {
    int sortBy = 0;
    do {
        printf("=====정렬 기준=====\n");
        printf("1. 번호 기준 정렬\n");
        printf("2. 이름 기준 정렬 \n");
        printf("3. 주소 기준 정렬\n");
        printf("4. 성적 기준 정렬\n");
        printf("번호를 입력하세요 : ");
        scanf("%d", &sortBy);
        if (sortBy < SORT_BY_ID || sortBy > SORT_BY_GRADE) printf("*올바른 번호를 선택해주십시오*\n");
    } while (sortBy < SORT_BY_ID || sortBy > SORT_BY_GRADE);
    printf("=====학생 조회=====\n");
    if (studentSize > 1) {
        STUDENT* sorted = NULL;
        sorted = (STUDENT*)malloc(sizeof(STUDENT) * studentSize);
        if (sorted == NULL) {
            printf("메모리 할당 오류!\n");
            return;
        }
        mergeSort(students, 0, studentSize - 1, &sorted, sortBy);
        printf("ID\tNAME\tADDRESS\tGRADE\n");
        for (int i = 0; i < studentSize; i++) {
            STUDENT nowStudent = sorted[i];
            printf("%d\t%s\t%s\t%f\n", nowStudent.id, nowStudent.name, nowStudent.address, nowStudent.grade);
        }
        free(sorted);
    }
    else if (studentSize == 1) {
        printf("ID\tNAME\tADDRESS\tGRADE\n");
        STUDENT nowStudent = students[0];
        printf("%d\t%s\t%s\t%f\n", nowStudent.id, nowStudent.name, nowStudent.address, nowStudent.grade);
    }
    else {
        printf("*아직 등록된 학생이 없습니다.*\n");
    }
}

void mergeSort(STUDENT* students, int left, int right, STUDENT** sorted, int sortBy) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(students, left, mid, sorted, sortBy);
        mergeSort(students, mid + 1, right, sorted, sortBy);
        merge(students, left, mid, right, sorted, sortBy);
    }
}

void merge(STUDENT* students, int left, int mid, int right, STUDENT** sorted, int sortBy) {
    int i, j, k, l;
    i = left;
    j = mid + 1;
    k = left;
    while (i <= mid && j <= right) {
        switch (sortBy) {
        case SORT_BY_ID:
            if (students[i].id <= students[j].id) (*sorted)[k++] = students[i++];
            else (*sorted)[k++] = students[j++];
            break;
        case SORT_BY_NAME:
            if (fstrcmp(students[i].name, students[j].name) > 0) (*sorted)[k++] = students[i++];
            else (*sorted)[k++] = students[j++];
            break;
        case SORT_BY_ADDRESS:
            if (fstrcmp(students[i].address, students[j].address) > 0) (*sorted)[k++] = students[i++];
            else (*sorted)[k++] = students[j++];
            break;
        case SORT_BY_GRADE:
            if (students[i].grade <= students[j].grade) (*sorted)[k++] = students[i++];
            else (*sorted)[k++] = students[j++];
        }
    }

    if (i > mid) {
        for (l = j; l <= right; l++) (*sorted)[k++] = students[l];
    }
    else {
        for (l = i; l <= mid; l++) (*sorted)[k++] = students[l];
    }
    for (l = left; l <= right; l++) students[l] = (*sorted)[l];
}

void findStudent(STUDENT* students, int studentSize) {
    int findType = 0;
    char* findText[4] = { "번호 검색", "이름 검색", "주소 검색", "성적 검색" };
    do {
        printf("=====학생 검색=====\n");
        printf("1. 번호 검색\n");
        printf("2. 이름 검색 \n");
        printf("3. 주소 검색\n");
        printf("4. 성적 검색\n");
        printf("번호를 입력하세요 : ");
        scanf("%d", &findType);
        if (findType < FIND_BY_ID || findType > FIND_BY_GRADE) printf("*올바른 번호를 선택해주십시오*\n");
    } while (findType < FIND_BY_ID || findType > FIND_BY_GRADE);
    printf("검색할 내용을 입력하세요 : ");
    char* searchContents;
    int searchId;
    double searchGrade;
    int fetchedSize = 0;
    STUDENT* fetched = NULL;
    fetched = (STUDENT*)malloc(sizeof(STUDENT) * studentSize);
    if (fetched == NULL) {
        printf("메모리 할당 오류!\n");
        return;
    }
    if (findType == 2 || findType == 3) searchContents = input();
    else if (findType) scanf("%d", &searchId);
    else {
        do {
            scanf("%lf", &searchGrade);
            if (searchGrade < 0) printf("양수를 입력해주세요.\n");
        } while (searchGrade < 0);
    }
    for (int i = 0; i < studentSize; i++) {
        switch (findType) {
        case FIND_BY_ID:
            if (searchId == students[i].id) fetched[fetchedSize++] = students[i];
            break;
        case FIND_BY_NAME:
            if (fstrcmp(students[i].name, searchContents) == 0) fetched[fetchedSize++] = students[i];
            break;
        case FIND_BY_ADDRESS:
            if (fstrcmp(students[i].address, searchContents) == 0) fetched[fetchedSize++] = students[i];
            break;
        case FIND_BY_GRADE:
            if (searchGrade == students[i].grade) fetched[fetchedSize++] = students[i];
        }
    }
    if (findType == 2 || findType == 3) printf("=====%s : %s 검색 결과=====\n", findText[findType - 1], searchContents);
    else if (findType == 0) printf("=====%s : %d 검색 결과=====\n", findText[findType - 1], searchId);
    else printf("=====%s : %lf 검색 결과=====\n", findText[findType - 1], searchGrade);
    if (fetchedSize > 0) {
        printf("\tID\tNAME\tADDRESS\tGRADE\n");
        for (int i = 0; i < fetchedSize; i++) {
            STUDENT nowStudent = fetched[i];
            printf("%d\t%d\t%s\t%s\t%f\n", i + 1, nowStudent.id, nowStudent.name, nowStudent.address, nowStudent.grade);
        }
    }
    else {
        printf("해당하는 조건의 결과가 없습니다.\n");
    }
    free(fetched);
    free(searchContents);
}

void addStudent(STUDENT** students, int* studentSize, int* studentCapacity) {
    int id;
    char* name;
    char* address;
    double grade;
    printf("=====학생 추가=====\n");
    printf("번호 : ");
    scanf("%d", &id);
    printf("이름 : ");
    name = input();
    printf("주소 : ");
    address = input();
    do {
        printf("성적 : ");
        scanf("%lf", &grade);
        if (grade < 0) printf("양수를 입력해주세요.\n");
    } while (grade < 0);
    STUDENT newStudent;
    newStudent.id = id;
    newStudent.name = name;
    newStudent.address = address;
    newStudent.grade = grade;
    (*students)[(*studentSize)++] = newStudent;
    if ((*studentSize) == (*studentCapacity)) {
        (*studentCapacity) *= 2;
        STUDENT* temp = NULL;
        temp = (STUDENT*)realloc((*students), (*studentCapacity) * sizeof(STUDENT));
        if (temp == NULL) {
            printf("메모리 할당 오류!\n");
            for (int i = 0; i < (*studentCapacity); i++) {
                free((*students)[i].name);
                free((*students)[i].address);
            }
            free((*students));
            return;
        }
        (*students) = temp;
    }
}

void removeStudent(STUDENT** students, int* studentSize) {
    int id;
    char* name;
    char* address;
    double grade;
    int removeType = 0;
    do {
        printf("=====학생 삭제=====\n");
        printf("1. 번호로 삭제\n");
        printf("2. 이름으로 삭제 \n");
        printf("3. 주소로 삭제\n");
        printf("4. 성적으로 삭제\n");
        printf("번호를 입력하세요 : ");
        scanf("%d", &removeType);
        if (removeType < REMOVE_BY_ID || removeType > REMOVE_BY_GRADE) printf("*올바른 번호를 선택해주십시오*\n");
    } while (removeType < REMOVE_BY_ID || removeType > REMOVE_BY_GRADE);
    printf("정보를 입력하세요 : ");
    char* removeContents;
    int removeId;
    double removeGrade;
    int candidateSize = 0;
    int* candidate = NULL;
    candidate = (int*)malloc(sizeof(int) * (*studentSize));
    if (candidate == NULL) {
        printf("메모리 할당 오류!\n");
        return;
    }
    if (removeType == REMOVE_BY_NAME || removeType == REMOVE_BY_ADDRESS) removeContents = input();
    else if (removeType == REMOVE_BY_ID) scanf("%d", &removeId);
    else {
        do {
            scanf("%lf", &removeGrade);
            if (removeGrade < 0) printf("양수를 입력해주세요.\n");
        } while (removeGrade < 0);
    }
    for (int i = 0; i < (*studentSize); i++) {
        switch (removeType) {
        case REMOVE_BY_ID:
            if (removeId == (*students)[i].id) candidate[candidateSize++] = i;
            break;
        case REMOVE_BY_NAME:
            if (fstrcmp((*students)[i].name, removeContents) == 0) candidate[candidateSize++] = i;
            break;
        case REMOVE_BY_ADDRESS:
            if (fstrcmp((*students)[i].address, removeContents) == 0) candidate[candidateSize++] = i;
            break;
        case REMOVE_BY_GRADE:
            if (removeGrade == (*students)[i].grade) candidate[candidateSize++] = i;
        }
    }
    switch (candidateSize) {
    case 0:
        printf("해당되는 학생이 없습니다!\n");
        break;
    case 1:
        printf("성공적으로 삭제했습니다!\n");
        printf("삭제된 학생의 정보 :\n");
        printf(" - 번호 : %d\n", (*students)[candidate[0]].id);
        printf(" - 이름 : %s\n", (*students)[candidate[0]].name);
        printf(" - 주소 : %s\n", (*students)[candidate[0]].address);
        printf(" - 성적 : %lf\n", (*students)[candidate[0]].grade);
        free((*students)[candidate[0]].name);
        free((*students)[candidate[0]].address);
        (*students)[candidate[0]] = (*students)[--(*studentSize)];
        break;
    default:
        printf("여러 명의 학생이 검색되었습니다.\n");
        int removeSelect = 0;
        do {
            printf("삭제할 학생의 번호를 입력해주세요.\n");
            printf("\tID\tNAME\tADDRESS\tGRADE\n");
            for (int i = 0; i < candidateSize; i++) {
                STUDENT nowStudent = (*students)[candidate[i]];
                printf("%d\t%d\t%s\t%s\t%f\n", i + 1, nowStudent.id, nowStudent.name, nowStudent.address, nowStudent.grade);
            }
            scanf("%d", &removeSelect);
            if (1 > removeSelect || removeSelect > candidateSize) printf("*올바른 번호를 선택해주십시오*\n");
        } while (1 > removeSelect || removeSelect > candidateSize);
        printf("성공적으로 삭제했습니다!\n");
        printf("삭제된 학생의 정보 :\n");
        printf(" - 번호 : %d\n", (*students)[candidate[removeSelect - 1]].id);
        printf(" - 이름 : %s\n", (*students)[candidate[removeSelect - 1]].name);
        printf(" - 주소 : %s\n", (*students)[candidate[removeSelect - 1]].address);
        printf(" - 성적 : %lf\n", (*students)[candidate[removeSelect - 1]].grade);
        free((*students)[removeSelect - 1].name);
        free((*students)[removeSelect - 1].address);
        (*students)[removeSelect - 1] = (*students)[--(*studentSize)];
    }
    free(candidate);
    //free(removeContents);
}

void saveList(STUDENT* students, int studentSize) {
    printf("저장할 파일 이름 : ");
    char* fileName = input();
    if (fileName == NULL) {
        printf("파일 이름 입력 오류!\n");
        return;
    }
    FILE* file = fopen(fileName, "w");
    if (file == NULL) {
        printf("파일을 열 수 없습니다.\n");
        free(fileName);
        return;
    }
    fprintf(file, "%d\n", studentSize);
    for (int i = 0; i < studentSize; i++) {
        int nameLength = sLen(students[i].name);
        int addressLength = sLen(students[i].address);
        fprintf(file, "%d %d\n", nameLength, addressLength);
        for (int j = 0; j < nameLength; j++) {
            fputc(students[i].name[j], file);
        }
        fputc('\n', file);
        for (int j = 0; j < addressLength; j++) {
            fputc(students[i].address[j], file);
        }
        fputc('\n', file);
        fprintf(file, "%d %lf\n", students[i].id, students[i].grade);
    }
    fclose(file);
    printf("출석부를 파일에 성공적으로 저장했습니다.\n");
    free(fileName);
}

void loadList(STUDENT** students, int* studentSize, int* capacity) {
    printf("불러올 파일 이름 : ");
    char* fileName = input();
    FILE* file = fopen(fileName, "r");
    if (file == NULL) {
        printf("파일을 열 수 없습니다.\n");
        free(fileName);
        return;
    }
    if (fscanf(file, "%d", studentSize) != 1 || *studentSize <= 0) {
        printf("잘못된 파일 형식입니다.\n");
        fclose(file);
        free(fileName);
        return;
    }
    if (*studentSize >= *capacity) {
        *capacity = (*studentSize) * 2;
        *students = (STUDENT*)realloc(*students, sizeof(STUDENT) * (*capacity));
        if (*students == NULL) {
            printf("메모리 할당 오류!\n");
            fclose(file);
            free(fileName);
            return;
        }
    }
    fgetc(file);
    for (int i = 0; i < *studentSize; i++) {
        int nameLength, addressLength;
        fscanf(file, "%d %d", &nameLength, &addressLength);
        fgetc(file);
        char* name = (char*)malloc(sizeof(char) * (nameLength + 1));
        if (name == NULL) {
            printf("메모리 할당 오류!\n");
            fclose(file);
            free(fileName);
            return;
        }
        for (int j = 0; j < nameLength; j++) name[j] = fgetc(file);
        name[nameLength] = '\0';
        fgetc(file);
        char* address = (char*)malloc(sizeof(char) * (addressLength + 1));
        if (address == NULL) {
            printf("메모리 할당 오류!\n");
            free(name);
            fclose(file);
            free(fileName);
            return;
        }
        for (int j = 0; j < addressLength; j++) {
            address[j] = fgetc(file);
        }
        address[addressLength] = '\0';
        fgetc(file);
        int id;
        double grade;
        fscanf(file, "%d %lf", &id, &grade);
        (*students)[i].id = id;
        (*students)[i].name = name;
        (*students)[i].address = address;
        (*students)[i].grade = grade;
        fgetc(file);
    }
    fclose(file);
    printf("파일에서 출석부를 성공적으로 불러왔습니다.\n");
    free(fileName);
}