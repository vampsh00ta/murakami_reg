
#include <stdlib.h>
#include <stdio.h>


typedef struct _node {
    int key;
    struct _node **childs;
    int count;
} node;

void printChilds (node *n, int deep) {
    for (int i = 0; i <deep - 1 ; ++i) {
        printf("| ");
    }
    if (deep!=0){
        printf("|");
    }

    if (deep!=0) {
        printf("-%d",n->key);
    } else {
        printf("%d",n->key);
    }
    printf("\n");

    for (int i = 0; i <n->count ; ++i) {
        printChilds(n->childs[i],deep+1);
    }





}

void printNode (node *n) {
    printChilds(n, 0);
}

node * makeNode(int x) {
    node *n = malloc(sizeof(node));
    n->key = x;
    n->count = 0;
    n->childs = NULL;
    return n;
}

node * findNode (node *n, int key) {
    if (n->key == key)
        return n;
    if (n->count > 0) {
        for (int i = 0; i < n->count; ++i) {
            node * f = findNode(n->childs[i], key);
            if (f != NULL) {
                return f;
            }
        }
        return NULL;
    }
    else {
        return NULL;
    }
}

void addNode(node * n, int parentKey, int x) {
    if (findNode(n, x)) {
        printf("Вершина %d уже создана\n",x);;
    }
    else {
        node *f = findNode(n, parentKey);
        if (f != NULL) {
            if (f->count > 0) {
                f->childs = (node **)realloc(f->childs, sizeof(node *) * (f->count + 1));
                f->childs[f->count] = makeNode(x);
                f->count++;
            }
            else if (f->count == 0) {
                f->childs = (node **)malloc(sizeof(node *));
                f->childs[0] = makeNode(x);
                f->count = 1;
            }
        }
        else {
            printf("Родителя %d не существует\n",parentKey);
        }
    }
}

void freeNode(node *n){
    for (int i = 0; i < n->count; ++i) {
        if (n->childs[i] != NULL) {
            freeNode(n->childs[i]);
        }
    }
    free(n->childs);
    n->childs = NULL;
    free(n);
    n = NULL;
}

node *findParent (node *n,int x) {
    if (n->count>0) {
        for (int i = 0; i < n->count; ++i) {
            if (n->childs[i]->key == x)
                return n;
            else {
                node * par = findParent(n->childs[i], x);
                if (par != NULL)
                    return par;
            }
        }
        return NULL;
    }
    else
        return NULL;
}

void deleteNode(node *n,int x){
    node *deletingNode = findNode(n,x);
    node *parent = findParent(n,x);

    if(deletingNode){
        int index = 0;
        for (int i = 0; i < parent->count ; ++i) {
            if (parent->childs[i]->key == x){
                index = i;
                break;
            }

        }

        freeNode(deletingNode);
        for (int i = index; i < parent->count-1; ++i) {
            parent->childs[i] = parent->childs[i+1];
        }
        parent->count--;
    }else{
        printf("элемента %d не существует",x);
    }


}

void findDeep(node * n,int *max,int deep){
    for (int i = 0; i < n->count; ++i) {
        if (n->childs[i] != NULL) {
            findDeep(n->childs[i],max,deep+1);
        }
    }
    if (*max<deep)
        *max = deep;

}

int maxDeep(node *n){
    int max = 0;
    findDeep(n,&max,0);
    return max;
}

int main() {
    int choice = 0;
    node *a = NULL;
    while(choice!=-1){
        printf("1-Создать дерево \n2-Добавить вершину\n3-Удалить вершину\n4-Максимальная глубина дерева\nДля выхода вв-те любой символ\n");

        scanf("%d",&choice);
        int parent ,child;
        switch (choice) {
            case 1:
                if(a == NULL){
                    printf("Вв-те первый элемент дерева: ");
                    scanf("%d",&child);
                    a = makeNode(child);
                }
                else{
                    printf("Дерево уже создано \n");
                }
                break;

            case 2:
                printf("Вв-те элемент родитель и его ребенок: ");
                scanf("%d%d",&parent,&child);
                printf("\n");
                addNode(a,parent,child);
                printNode(a);
                break;

            case 3:
                printf("Вв-те  вершину  для удаления: ");
                scanf("%d",&child);
                printf("\n");
                if(findNode(a,child)!=NULL){
                    deleteNode(a,child);
                    printNode(a);
                } else{
                    printf("Вершины %d не существует \n",child);
                }

                break;
            case 4:
                printf("Максимальная глубина: %d\n", maxDeep(a));
                break;
            default:
                freeNode(a);
                choice = -1;
                break;
        }
    }

    return 0;
}