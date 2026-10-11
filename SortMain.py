# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202441903104
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)

# 插入排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def tzlInsertionSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()
    n = len(sortedArr)
    # 外层循环：从第二个元素开始，依次将元素插入到左侧已排序序列中
    for i in range(1, n):
        key = sortedArr[i]
        j = i - 1
        # 内层循环：将比key大的元素依次后移，为key腾出插入位置
        while j >= 0 and sortedArr[j] > key:
            sortedArr[j + 1] = sortedArr[j]
            j -= 1
        # 将key插入到正确位置
        sortedArr[j + 1] = key
    return sortedArr

# 选择排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：排序完成后的升序数组
def pzsSelectSort(arr):
    # 复制原数组，保护原始数据不被修改
    sortedArr = arr.copy()
    # 获取数组长度
    n = len(sortedArr)
    # 外层循环，确定每一轮最小值存放位置
    for i in range(n):
        # 假设当前i下标为最小值下标
        minIndex = i
        # 内层循环，在未排序区间寻找最小值下标
        for j in range(i + 1, n):
            # 如果找到更小的值，更新最小值下标
            if sortedArr[j] < sortedArr[minIndex]:
                minIndex = j
        # 交换最小值到未排序区间的最前面
        sortedArr[i], sortedArr[minIndex] = sortedArr[minIndex], sortedArr[i]
    # 返回排序完成数组
    return sortedArr

# 快速排序
# 功能：查找数组中第k小的元素，不需要完整排序
# 参数：arr - 原始数字数组；k - 目标位次，从0开始计数
# 返回值：数组第k小的元素
def quickSelect(arr, k):
    # 分区函数，选取最右侧元素作为基准，划分左右区间
    def partition(left, right):
        # 设置基准元素为区间最右侧的值
        pivot = arr[right]
        # i记录小于等于基准值区域的边界下标
        i = left
        # 遍历区间内除基准以外所有元素
        for j in range(left, right):
            # 当前元素小于等于基准，划入左区间
            if arr[j] <= pivot:
                # 交换元素到左区间边界位置
                arr[i], arr[j] = arr[j], arr[i]
                # 左区间边界右移
                i += 1
        # 将基准元素放到分界位置
        arr[i], arr[right] = arr[right], arr[i]
        # 返回基准元素所在下标
        return i
    # 递归函数，在left~right区间查找第k小元素
    def select(left, right):
        # 获取分区后基准元素的位置
        pos = partition(left, right)
        # 基准下标正好等于k，找到目标直接返回
        if pos == k:
            return arr[pos]
        # 目标在右半区间，向右递归
        elif pos < k:
            return select(pos + 1, right)
        # 目标在左半区间，向左递归
        else:
            return select(left, pos - 1)
    # 在整个数组范围启动递归查找
    return select(0, len(arr)-1)

# 程序运行测试入口：所有成员最终在此处调用自己的算法
if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 宋舟翼：调用快速排序
    result2 = szyQuickSort(testArr.copy())
    print("宋舟翼-快速排序结果：", result2)
    # 谭张路：调用插入排序
    result3 = tzlInsertionSort(testArr.copy())
    print("谭张路-插入排序结果：", result3)
    # 彭攒淞：调用自己的选择排序算法
    result = pzsSelectSort(testArr.copy())
    print("彭攒淞-选择排序结果：", result)
