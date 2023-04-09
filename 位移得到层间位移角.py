import pandas as pd
import matplotlib.pyplot as plt

# 20条波的结构位移
data = {}
for i in range(1, 21):
    # 该结构有12层
    data[i] = pd.read_table('C:/Users/周小天/10.实验数据处理/调幅位移/data20\/{}.txt'.format(i), header=None, sep=' ', index_col=0, names=['行数', '第12层',
    # 层数反转                                                                                                                     '第11层', '第10层', '第9层', '第8层', '第7层', '第6层', '第5层', '第4层', '第3层', '第2层', '第1层', ])
    data[i]=data[i].iloc[:, ::-1]
# 计算层间位移角
data_drift={}
for i in range(1,21):
    data_drift[i]=data[i].diff(axis=1).iloc[:,1:].rename(columns={'第2层':'drift_2','第3层':'drift_3','第4层':'drift_4','第5层':'drift_5','第6层':'drift_6',
                                                 '第7层':'drift_7','第8层':'drift_8','第9层':'drift_9','第10层':'drift_10','第11层':'drift_11',
                                                 '第12层':'drift_12',}) 
# 各层位移最大值及位置
max_values_disp={}
max_locs_disp={}
for i in range(1,21):
    max_values_disp[i]=data[i].abs().max()
    max_locs_disp[i]=data[i].abs().idxmax()
                                                                                                                                                                                                                                                        
# 各层层间位移角最大值及位置
max_values_drift={}
max_locs_drift={}
for i in range(1,21):
    max_values_drift[i]=data_drift[i].abs().max()
    max_locs_drift[i]=data_drift[i].abs().idxmax()                                                                                                                              
                                                                                                                             
