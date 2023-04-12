# 目的

![image-20230412160537607](vlookup查找.assets/image-20230412160537607.png)

两列数据，取出a列数据中某个数据对应b列的数据。

将想要查找的数据填在c列

![image-20230412160703821](vlookup查找.assets/image-20230412160703821.png)

在d列中填入：

```
=IFERROR(INDEX(B:B,MATCH($C2,A:A,0)),"")
```

![image-20230412160732904](vlookup查找.assets/image-20230412160732904.png)

即可查找出。

