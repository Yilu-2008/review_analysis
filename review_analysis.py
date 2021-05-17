# practice - review analysis

data = []
count = 0
with open ('review.txt','r') as f:
	for line in f:  #loop循环一行一行读（行在text里面有换行符）
		data.append(line.strip())
		count += 1
		if count % 2 == 0:   #找到2的倍数
			print(len(data))
print(data)
print('已读取完毕',len(data))


# 计算所有评论的平均长度

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('评论平均长度为', sum_len/len(data))	
