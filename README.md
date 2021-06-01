# simple-error-analysis
json形式の出力結果をhtml形式に変換するリポジトリです。主に機械学習の誤り分析を想定しています。

## 基本設計
1行1json形式のファイルを受け取って、`index.html`及び各データの詳細を出力します。

## 使い方
### tableデータ
Entity linkingのような、１入力に対して複数の答えを見たい場合に有用です。  
- 入力フォーマット
```
{
    "ID": 0,
    "title": "データ0",
    "meta": {
        "is_true": "True",
        "mention": "input_mention"},
    "data": [
        {"entity": "candidate_1", "score": 0.5},
        {"entity": "candidate_2", "score": 0.1}
    ]
}
```
基本的に`meta`や`data`のkeyは任意です。全てのデータで揃えるようにしてください。  
`ID`と`title`は省略できます。

- コマンド  
`table-converter /path/to/input_json.jsonl /path/to/output_dir`
