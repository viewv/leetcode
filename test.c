#include <stdio.h>

int singleNumber(int *nums, int numsSize)
{
    int i, j;
    int flag = 0;
    for (i = 0; i < numsSize; i++)
    {
        flag = 0;
        for (j = 0; j < numsSize; j++)
        {
            if (i != j && nums[i] == nums[j])
                flag = 1;
        }
        if (flag == 0)
        {
            return nums[i];
        }
    }
    return nums[0];
}

int main(int argc, char const *argv[])
{
    int nums[3] = {1, 2, 1};
    printf("%d\n", singleNumber(nums, 3));
    return 0;
}
