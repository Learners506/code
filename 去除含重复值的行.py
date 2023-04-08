import pandas as pd
import matplotlib.pyplot as plt
# 读取数据
data = pd.read_excel('jiaguC1.xlsx')

# 去除col_name列中的重复行
data = data.drop_duplicates(subset='disp', keep='first')
# 可视化
plt.figure(figsize=(15,15))
plt.plot(data['disp'],data['force'])
plt.show()
