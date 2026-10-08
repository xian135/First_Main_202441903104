# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202441903104
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)
# 程序运行测试入口：所有成员最终在此处调用自己的算法

# 归并排序
# 功能：采用分治思想，对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def hjxMergeSort(arr):
    # 复制原数组，避免修改外部原始数据
    sortedArr = arr.copy()
    # 递归终止条件：数组长度小于等于1，数组本身已有序，直接返回
    if len(sortedArr) <= 1:
        return sortedArr
    # 计算数组中间下标，用来分割数组
    mid = len(sortedArr) // 2
    # 递归处理左半部分数组
    left = hjxMergeSort(sortedArr[:mid])
    # 递归处理右半部分数组
    right = hjxMergeSort(sortedArr[mid:])

    # 新建空列表，用来存放合并后的有序结果
    result = []
    # i：左数组遍历下标，初始化为0
    i = 0
    # j：右数组遍历下标，初始化为0
    j = 0
    # 同时遍历左右两个有序数组，只要两个数组都还有元素就继续循环
    while i < len(left) and j < len(right):
        # 对比左右数组当前下标元素，取较小值放入结果
        if left[i] < right[j]:
            result.append(left[i])
            # 左数组下标向后移动一位
            i += 1
        else:
            result.append(right[j])
            # 右数组下标向后移动一位
            j += 1
    # 将左数组剩余未遍历的元素全部追加进结果
    result.extend(left[i:])
    # 将右数组剩余未遍历的元素全部追加进结果
    result.extend(right[j:])
    # 返回合并完成的有序数组
    return result


if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
    res1 = hjxMergeSort(testArr.copy())
    print("胡佳鑫-归并排序结果：", res1)

