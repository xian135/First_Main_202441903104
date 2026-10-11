# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202441903104
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)


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


# 程序运行测试入口：所有成员最终在此处调用自己的算法
if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)

    # 彭攒淞：调用自己的选择排序算法
    result = pzsSelectSort(testArr.copy())
    print("彭攒淞-选择排序结果：", result)
