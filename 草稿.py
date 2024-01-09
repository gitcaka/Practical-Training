m = input()
if '_' in m:
    print('snake_case')
elif m[0].isupper():
    print('PascalCase')
else:
    print('camelCase')