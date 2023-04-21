import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#导入数据
data = pd.read_excel('滞回曲线.xlsx',sheet_name='C1')

#可视化数据
plt.figure(figsize=(15,15))
plt.plot(data['位移'],data['力'])
plt.plot(data['位移'],[0]*len(data))
plt.show()

df = data
# 线性插值，生成新的DataFrame对象
interpolated_df = df.interpolate(method='linear')

# 找出y值为0的所有行
zero_crossings = np.where(np.diff(np.sign(interpolated_df['力'])))[0]

# 创建一个空列表来存储交叉点的信息
crossings_list = []

# 遍历所有交叉点
for idx in zero_crossings:
    # 找出当前交叉点的x坐标
    x_coord = interpolated_df.iloc[idx]['位移']
    # 找到交叉点所在的原始数据行号
    row_number = interpolated_df.index[idx]
    # 将交叉点的信息添加到列表中
    crossings_list.append((x_coord, row_number))

# 将列表转换为DataFrame格式
crossings_df = pd.DataFrame(crossings_list, columns=['x', 'Row Number'])

# 输出结果
crossings_df.to_csv('result.csv')
