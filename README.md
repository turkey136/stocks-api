# stocks-api

## Environment
* Docker 20.10.9
* docker-compose 1.25.5
* Python 3.9.7
* Django 3.2.8
* psycopg2 2.9.1
* postgres 12.2

## Development
* 環境変数の設定
  * `$ touch .env`
  * .env ファイルに以下を追加
  * ```
    STOCK_SECRET_KEY=#{your random string}
    STOCK_DB_HOST=db
    STOCK_DB_USER=postgres
    STOCK_DB_PASSWORD=postgres
    STOCK_DB_NAME=postgres
    STOCK_DB_PORT=5432
    DEBUG=True
    ```
* Docker でビルド
  * `$ docker-compose build`
* seed データの投入
  * `$ docker-compose rum --rm api python3 manage.py runscript seed`
* サーバの起動
  * `$ docker-compose up api`
* スクリプトの実行
  * 前日の株価取得
    * `$ docker-compose rum --rm api python3 manage.py runscript daily_stock_crawl`

# API ドキュメント
* サーバ起動
  * ドキュメント閲覧
    * `$ docker-compose up swagger-ui`
  * エディタ
    * `$ docker-compose up swagger-editor`
* 閲覧
  * http://localhost:8003
* エディタ
  * http://localhost:8002
