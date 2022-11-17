# hb_cli
Hit&Blow on terminal!

## 使い方
ターミナルで以下のコマンドを実行してインストール  
```
pip install https://github.com/toripppppy/homebrew-hb_cli/releases/download/0.0.2/hbcli-1.0.tar.gz
```

または[こちら](https://github.com/toripppppy/hb_cli/releases/tag/0.0.2)から直接`hbcli-1.0.tar.gz`をダウンロードして、
適当な場所に配置、移動して、
```
pip install hbcli-1.0.tar.gz
```

でインストールできます。


## 遊び方
```
hb
```
でスタート。
Ctrl+C または call giveup でそのゲームをギブアップできます。
```
[Hit&Blow] call 123
```
"[Hit&Blow] call"の表示につづけて３ケタの数字をコールすると、
```
H : 1
B : 0
```
のようにHitとBlowの数が帰ってきます。  
正解したらリザルトが表示されます。

---
## Hit&Blow の遊び方
簡単な数字当てゲームです。
ランダムに３ケタの数字が用意されます。数字を「コール」することで選択肢を絞ることができ、その数字を当てたらクリアです。  
コールすると、  
Hit： コールした数字・位置ともに一致した数  
Blow: コールした数字のみ一致（位置は違う）した数  
の２つの数がそれぞれ表示されるので、それらをヒントに数字を絞り込み、より少ないコールでの正解を目指しましょう。 
