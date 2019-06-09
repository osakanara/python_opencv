import cv2
import time


"""
関数：画像の合成
"""
def composite_phto(add_img, back_img):
    # 処理開始時間
    start_time = time.time()

    # 画像の読込
    img1 = cv2.imread(add_img)
    img2 = cv2.imread(back_img)

    # 画像を合成する場所を設定
    height, width = img1.shape[:2]
    # 画像の合成
    img2[0:height, 0:width] = img1

    # 経過時間
    elapsed_time = time.time() - start_time
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    # 画像の保存
    cv2.imwrite('new.jpg', img2)

"""
関数：画像の縮小　縮小方法色々
最近傍補間法：nearest
バイリニア補間：linear
バイキュービック補間：cubic
サンプリング：area
Lanczos法補間：lanczos
"""
def resize_photo(resize_img, width, height, interpolation):
    # 処理開始時間
    start_time = time.time()

    # 画像の読込
    resize_img =cv2.imread(resize_img)

    # 縮小方法による場合分け
    if interpolation == 'nearest':
        resized_img = cv2.resize(resize_img, (width, height), interpolation=cv2.INTER_NEAREST)
    elif interpolation == 'linear':
        resized_img = cv2.resize(resize_img, (width, height), interpolation=cv2.INTER_LINEAR)
    elif interpolation == 'cubic':
        resized_img = cv2.resize(resize_img, (width, height), interpolation=cv2.INTER_CUBIC)
    elif interpolation == 'area':
        resized_img = cv2.resize(resize_img, (width, height), interpolation=cv2.INTER_AREA)
    else:
        resized_img = cv2.resize(resize_img, (width, height), interpolation=cv2.INTER_LANCZOS4)
    # 経過時間
    resize_time = time.time() - start_time
    print(interpolation + "_resize_time:{0}".format(resize_time) + "[sec]")

    # 画像の保存
    cv2.imwrite('resized.jpg', resized_img)


"""
関数：画像の（縦）連結
連結する画像：concat_img
連結回数：count
"""
def concat_photo(in_img, count):

    # 処理開始時間
    start_time = time.time()
    # 画像の読込
    img = cv2.imread(in_img)
    # 連結回数分の配列を作成
    concat_list = []
    for _ in range(count):
        concat_list.append(img)

    # 画像の連結
    concat_img = cv2.vconcat(concat_list)

    # 経過時間
    concat_time = time.time() - start_time
    print("concat_time:{0}".format(concat_time) + "[sec]")

    # 画像の保存
    cv2.imwrite('concat.jpg', concat_img)




# メイン処理
if __name__== '__main__':
    # 画像の定義
    add_img = 'add.jpg'
    back_img = 'back.jpg'
    resize_img = 'resize.jpg'
    lena_img = 'lena.jpg'

    # 画像の合成　呼出
    composite_phto(add_img=add_img, back_img=back_img)

    # 画像のリサイズ
    resize_photo(resize_img=resize_img, width=200, height=200, interpolation='linear')

    # 画像の連結　１０回
    concat_photo(in_img=lena_img, count=10)
