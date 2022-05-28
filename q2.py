def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 5
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
  # left : 探索する配列左端のindex, right : 探索する配列左端のindex
  left = 0
  right = len(sorted_array) -1 

  # 探索する範囲がなくなるまで，探索を繰り返す
  # 探索する配列の大きさが偶数の場合，前半の配列末尾を中間の値とする
  while left < right + 1:
    mid = int((left + right) / 2)

    # 値が見つかった時，探索結果のindexを返す
    if sorted_array[mid] == target_number:
      return mid

    # 探索対象より「配列の中間の値」が大きい時，探索する配列の右端を更新する
    elif target_number < sorted_array[mid]:
      right = mid - 1

    # 探索対象より「配列の中間の値」が小さい時，探索する配列の左端を更新する
    elif sorted_array[mid] < target_number:
      left = mid + 1

  # 探索対象が存在しない場合、-1を出力
  return -1

if __name__ == '__main__':
    main()
