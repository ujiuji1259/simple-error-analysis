# simple-error-analysis
json形式の出力結果をhtml形式に変換するリポジトリです。主に機械学習の誤り分析を想定しています。

## 基本設計
1行1json形式のファイルを受け取って、`index.html`及び各データの詳細を出力します。

## 使い方
### tableデータ
入力フォーマット
```
{
    "ID": 0,
    "title": "データ0",
    "meta": {
        "pred": "True",
        "true": "False"},
    "data": [
        {"data": "hello", "score": 0.5},
        {"data": "way", "score": 0.1}]}
```