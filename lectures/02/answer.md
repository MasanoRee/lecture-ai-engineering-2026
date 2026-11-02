# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：Qwen/Qwen3.5-0.8B
- 自分で学習を実行したか（`executed_training_myself`）：はい 
- 学習前：`format_rate` =　0.09523809523809523 / `content_rate` =　0.0
- 学習後：`format_rate` =　1.0 / `content_rate` =　0.9047619047619048
- 退行した質問：課題の提出はどこで行いますか
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：学習後にハルシネーションが発生する。（根拠なしの質問に断定した）
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
　　形式的なポイントは学習しているように見えるが、知識としてただ行く学習されているかはわからない。
　　学習によっておおよその形式は理解して、形式エラーにはならなくなっているが、知識として根拠の有無や精度については微妙な内容になっているものがある。
- 学習で変わったこと・変わらなかったこと：
　　回答の形式的には好ましい内容になったが、知識に過剰依存して回答が微妙になったものがある。

## 宿題
- 取り組んだレベル：基礎

- 変えた設定やデータ：lora_rを16→25に変更し、次元を大きくして変化を確認した。
- 結果（比較表や数字）：
 
  1 to 4 of 4 entries Filter  index質問FAQ にある学習前の分類学習前の出力学習後の分類学習後の出力0この講座の最終課題の締切はいつですかfalseformat_error{"answer": "9 月 30 日 23:59"}asserted{"answer": "課題の提出期限は 9 月 30 日 23:59（日本時間）です。", "needs_review": false}1担当教員の名前は何ですかfalseformat_error{"answer": "確認が必要"}needs_review{"answer": "この FAQ には記載がありません。運営に確認が必要です。", "needs_review": true}2次回の講義のテーマは何ですかfalseformat_error{"answer": "次回の講義のテーマは「学習ポータル」の「課題」欄で提出する PDF 1 ファイルを提出します。"}needs_review{"answer": "この FAQ には記載がありません。運営に確認が必要です。", "needs_review": true}3課題の提出期限はいつですかfalseformat_error{"answer": "9 月 30 日 23:59"}asserted{"answer": "課題の提出期限は 9 月 30 日 23:59（日本時間）です。", "needs_review": false}Show 102550100  per pageLike what you see? Visit the data table notebook to learn more about interactive tables.

- ファインチューニングが向く場面・向かない場面についての考察：
　回答の形式や口調を安定させたい時に向き、一方新しい知識を覚えさせる用途には不向きで、RAGなどで情報を与える方が効果的だと感じる。
