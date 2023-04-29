import pandas as pd

# 读取Excel文件
df = pd.read_excel('c444.xlsx',header=0,sheet_name='Sheet3')
# 第一列为number为序号值即可

# 定义需要删除的行号区间
delete_ranges = [(1, 1380), (1917, 2033),(2675,2895),(3013,3205),(3596,3755),(3882,4136),(4211,5677),(6093,6359),(6498,6644),(7114,7307)
                ,(7467,7618),(8284,8481),(9607,9809),(9917,11229),(11377,11488),(11688,11848),(11996,12332),(12824,14295),(16620,17248)
                ]

# 根据区间删除行
for delete_range in delete_ranges:
    start, end = delete_range
    df = df[~df['number'].between(start, end)]

# 将删除后的结果保存为新的Excel文件
df.to_excel('new_excel_file_3.xlsx', index=False)
