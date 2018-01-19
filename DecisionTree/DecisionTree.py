#!/usr/bin/python
# -*- coding: utf-8 -*- 

from  math import log
import operator


# 计算信息熵,输入数据集，返回信息熵
def calculateEntropy(dataSet):
    totalNum = len(dataSet)
    labelCounts = {}
    for line in dataSet:
        currentLabel = line[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    entropy = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / totalNum
        entropy -= prob * log(prob, 2)

    return entropy


# 按某一属性的值划分数据集
# 输入为数据集，属性的索引，属性的取值
def splitData(dataSet, index, value):
    splitDataSet = []
    for line in dataSet:
        if line[index] == value:
            data = line[:index]
            data.extend(line[index + 1:])
            splitDataSet.append(data)
    return splitDataSet


# 选择最好的属性来划分数据
# 输入数据集，输出最大信息增益的属性索引
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calculateEntropy(dataSet)
    maxInformationGain = 0.0
    bestFeatureIndex = -1

    for index in range(numFeatures):
        featureList = []
        for line in dataSet:
            if line[index] not in featureList:
                featureList.append(line[index])
        newEntropy = 0.0
        for feature in featureList:
            splitDataSet = splitData(dataSet, index, feature)
            prob = float(len(splitDataSet)) / len(dataSet)
            newEntropy += calculateEntropy(splitDataSet) * prob

        informationGain = baseEntropy - newEntropy
        if informationGain > maxInformationGain:
            maxInformationGain = informationGain
            bestFeatureIndex = index
    return bestFeatureIndex


# 投票表决函数
# 输入为分类列表，输出为多数表决的结果
def voteResult(classList):
    classCounts = {}
    for value in classList:
        if value not in classCounts:
            classCounts[value] = 0
        classCounts[value] += 1

    sortClassCounts = sorted(classCounts.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortClassCounts[0][0]


# 用递归的办法生成决策树，结果用一个字典来表示
# 输入为数据集和每个属性的取值，输出为决策树（用字典表示）
def createDecisionTree(dataSet, labels):
    classList = [line[-1] for line in dataSet]
    if len(set(classList)) == 1:  # 如果分类集合只有一个元素则终止递归
        return classList[0]

    if len(dataSet[0]) == 1:  # 如果所有的属性都使用过了，则终止递归
        return voteResult(classList)

    bestFeatureIndex = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = labels[bestFeatureIndex]
    decisionTree = {bestFeatureLabel: {}}
    del (labels[bestFeatureIndex])

    featureList = [line[bestFeatureIndex] for line in dataSet]
    uniqueFeatureList = set(featureList)

    for value in uniqueFeatureList:
        splitDataSet = splitData(dataSet, bestFeatureIndex, value)
        decisionTree[bestFeatureLabel][value] = createDecisionTree(splitDataSet, labels)
    return decisionTree


# ---------------------------测试--------------------------
# 测试数据
def testData():
    dataSet = [[1, 1, 1, "yes"],
               [1, 1, 0, "yes"],
               [1, 0, 1, "no"],
               [1, 0, 0, "yes"],
               [0, 0, 1, "no"],
               [0, 0, 0, "no"],
               [0, 1, 1, "no"],
               [0, 1, 0, "no"]]
    labels = ["985","211","本科"]
    return dataSet, labels


# 测试calculateEntropy函数
def test_calculateEntropy():
    dataSet, labels = testData()
    entropy = calculateEntropy(dataSet)
    print(entropy)


# 测试splitData函数
def test_splitData():
    dataSet, labels = testData()
    splitDataSet = splitData(dataSet, 0, 0)
    print(splitDataSet)


# 测试chooseBestFeatureToSplit函数
def test_chooseBestFeatureToSplit():
    dataSet, labels = testData()
    bestFeatureIndex = chooseBestFeatureToSplit(dataSet)
    print(bestFeatureIndex)


# 测试createDecisionTree函数
def test_createDecisionTree():
    dataSet, labels = testData()
    decisionTree = createDecisionTree(dataSet, labels)
    print(decisionTree)


test_createDecisionTree()
# test_splitData()
# test_chooseBestFeatureToSplit()