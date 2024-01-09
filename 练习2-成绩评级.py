score = int(input('请输入成绩：'))
if score < 60:
    print('不合格')
elif 60 <= score < 70:
    print('中等')
elif 70 <= score < 80:
    print('良好')
else:
    print('优秀')