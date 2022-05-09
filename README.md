# SHINRA-ML評価スクリプト

実行結果のパスと正答データのパスを指定することでSHINRA-MLの評価ができます。  
学習データは自動的にテストデータのpageid範囲のみが選択されます。

## ダミーファイルでの実行

~~~bash: ダミー実行用スクリプト.sh
python3 main.py \
  data/dummy_submission_results/en.json \
  data/dummy_answer/en.json
~~~
