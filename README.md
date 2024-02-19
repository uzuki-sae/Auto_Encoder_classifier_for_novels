# Auto_Encoder_classifier_for_novels
｜背景：本プロジェクトは修士論文で扱う研究です。小説の語彙を単語ベクトルに変換することで、抽象的な雰囲気の変動が解析可能され、人気作品を抽出することが可能にされる。 
｜目標：作品のテキストだけで、人気作品を選び出すことで、販売直前の参考にできる。 ｜進捗：完成（部分成功：誤作動の場合あり） 
｜実装:pytorch, BERT ｜機材：google colab 
｜データセット：「小説家になろう」自作コーパス 
｜インプット：作品テキスト 
｜アウトプット：インプット 
｜方法：Auto Encoderを高評価作品で訓練すると、高評価作品を入力すれば出力との損失が低く、低評価作品を入力すれば出力と入力の差ができ、損失が高くなる。この特徴を利用して、テキストから評価をどのグループに属するか予測する。 
｜ファイル：1. comformer_AE:Auto encoderを定義し、訓練する用　2. metadata_by_ncode.py 作品のメタデータをAPIを通して収集するプログラムです。 3. get_text.py 作品の内文をクローリングするプログラムです。 (Reference:https://github.com/kokokocococo555/crawling-scraping/tree/master/narouscraping)
