#!/usr/bin/env python
import random
import re
import sys


# 被りを確認 => bool
def isDuplicated(s : str):
    return len(set(s)) != len(s)


# コールのフォーマットを確認 => bool
def isCorrectFormat(s : str):
    return re.fullmatch(r'\d{3}', s) and not isDuplicated(s)


# ギブアップ機能
def giveup():
    print(f'\n-- GIVEUP --\nAnswer : {A}\nCall   : {callCount}\n------------\n')
    sys.exit() # 終了


# コールを取得
def getCall():
    call = input('[Hit&Blow] call ')
    global callCount
    callCount += 1

    if call == 'giveup': # ギブアップ
        giveup()

    if not isCorrectFormat(call):
        print('please call again.')
        call = getCall() # もう一回コールさせる

    return call


# 判定
def judge(call : str):
    '''コールされた数字を判定

    完全一致 => Hit
    数字一致 => Blow
    '''
    def hit(c : list): # hitをカウント
        count = 0
        for i, v in enumerate(c):
            if isDuplicated([v, A[i]]): count += 1
        return count

    def blow(c : list): # blowをカウント
        count = 0
        for v in c:
            if v in A: count += 1
        return count - hit(c) # hitしている場合を除外

    # call を数値のリストに変換
    call = [int(s) for s in call]

    # 結果を表示
    H = hit(call)
    B = blow(call)

    print(f'H: {H} \nB: {B}\n')

    if H == 3:
        # ゲームクリア
        print(f'-- GAME CLEAR --\nAnswer : {A}\nCall   : {callCount}\n----------------\n')
    else:
        # 次のコールへ
        judge(getCall())

# 実行時に呼び出す
def main():
    # ゲームスタート
    print('-- GAME START --\ncall giveup | Ctrl+cで終了\n')

    global callCount, A
    # 答え（0~9から重複なし３ケタ）を用意
    A = random.sample(range(10), k=3)
    # コール回数カウント用
    callCount = 0

    try:
        judge(getCall()) # コール

    except KeyboardInterrupt: #Ctrl+c
        print('')
        giveup() # ギブアップとみなす