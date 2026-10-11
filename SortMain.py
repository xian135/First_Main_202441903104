# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202441903104
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)
# 程序运行测试入口：所有成员最终在此处调用自己的算法

# 快速排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def szyquickSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()

    def quick_sort_recursion(sub_arr):
        # 递归终止条件：数组长度小于等于1，直接返回
        if len(sub_arr) <= 1:
            return sub_arr
        # 选取基准元素
        pivot = sub_arr[len(sub_arr) // 2]
        # 小于基准的元素
        left = [x for x in sub_arr if x < pivot]
        # 等于基准的元素
        middle = [x for x in sub_arr if x == pivot]
        # 大于基准的元素
        right = [x for x in sub_arr if x > pivot]
        # 递归左右子数组，合并结果
        return quick_sort_recursion(left) + middle + quick_sort_recursion(right)

    #调用递归排序函数，拿到排序结果
    sortedArr = quick_sort_recursion(sortedArr)
    #将排序后的数组返回给调用者
    return sortedArr

if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组: ", testArr)
    # 调用自己的快速排序算法
    result = szyquickSort(testArr)
    # 输出结果
    print("宋舟翼-快速排序算法排序结果: ", result)
