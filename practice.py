width = int(input('長さcmを入力>>'))
height = int(input('高さcmを入力>>'))

squere_area = width*height
triangle_area = width*height/2

ans = int(input('三角形(0)の場合と四角形(1)の場合どちらの面積を調べますか？'))
if ans==1:
    print(f'長さ{width}cmで高さ{height}cmの四角形の面積は{squere_area}平方cmです')
else:
    print(f'長さ{width}cmで高さ{height}cmの三角形の面積は{squere_area}平方cmです')
