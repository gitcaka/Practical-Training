heght = float(input('请输入身高(m)：'))
if 1.5 <= heght <= 1.6:
    print('搬运器材')
elif 1.6 < heght <= 1.7:
    print('场地布置')
elif 1.7 < heght <= 1.8:
    print('迎宾')
else:
    print('当观众')