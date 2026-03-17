###02_types_funcs.py


###一、数据生成


import numpy as np

scores = np.random.randint(0,100,size = (5,4))#五名学生四门课的成绩
print(scores)

student = ["S01" ,"S02", "S03", "S04", "S05"]
lesson = ["C1", "C2" ,"C3", "C4"]

print("student\t"+ "\t\t".join(lesson))#输出学生课程成绩单
for i in range(0,5):
    print(student[i],end = "\t\t")
    print("\t\t".join(map(str,scores[i])))


###二、基础数据的输出


print(scores[0,])
print(scores[:,1])


###三、基本统计


for i in range(5):
    print(f"studentS{i+1}'s scores: {np.sum(scores[i,])}")#每位学生的总分
    print(f"The highest lesson score:{np.max(scores[i])}")#每个学生最高的课程分数
for j in range(4):
    print(f"lessonC{j+1}'s average scores: {np.mean(scores[:,j])}")#每门课的平均分

sumscores = np.sum(scores,axis = 1)
highest_index = np.argmax(sumscores)
highest_score = np.max(sumscores)

print(f"The highest index:{highest_index}")
print(f"The highest score:{highest_score}")


###四、条件筛选（向量化）


high_student = np.where(scores[:,0] > 85)[0]
print("The student whose lessons' scores > 85:",high_student)

for i in high_student:
    print(f" great students' id:S{i+1}")#第 1 门课成绩 > 85 的学生索引和 id 列表

lower = np.where((scores < 60).any(axis = 1))[0]
print("The student whose lessons' scores < 60:",lower)

for i in lower:
    print(f"lower' id:S{i+1}")#存在任一科目成绩 < 60 的学生索引的 id 列表

good_student = np.where((scores >= 60).all(axis = 1))[0]
print("The student whose  lessons' scores < 60:",good_student)

for i in good_student:
    print(f"good students' id:S{i+1}")#全部科目都 >= 60 的学生索引的 id 列表


###五、数组变换与广播


scores += 5
scores = np.clip(scores,0,100)

print(scores[1,])

total = np.sum(scores, axis = 1)
index = np.argsort(-total)
sorted_scores = scores[index]

print(sorted_scores)


###六、标准化与协方差


mean = np.mean(scores,axis = 0)
std = np. std(scores,axis = 0)
scores_std = (scores - mean) / std#标准化

print(scores_std)

cov_matrix = np.cov(scores_std, rowvar=False)

print(cov_matrix)