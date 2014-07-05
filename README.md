# bot をつくる準備
## Python の Twitter ライブラリ、 Tweepy をインストール
[Tweepy](https://dev.twitter.com/docs/twitter-libraries)

<pre><code> pip install tweepy </code></pre>
<pre><code> easy_install tweepy</code></pre>

* [自戒] 複数バーションの Python が入っている場合は、別のバージョンのところにインストールされる場合があるから気をつけよう

## bot 用の Twitter アカウントを取得

## dev.twitter.com で新規アプリを登録

* ログインアカウントが owner になるので bot のアカウントでログインしよう
* Consumer Key, Consumer Secret は [Test Oauth] でチェック
* [Permission] Read & Write に変更
* [API Key] Access Token を作り、Access token, Access token secret を手元に置いておく

# bot をつくる

hello.py 参照

* public timeline を取得

<pre><code>public_tweets = api.home_timeline()
	for tweet in public_tweets:
    print tweet.text</code></pre>

* Tweet する (status update)

<pre><code>status = u'はろーはろー'
api.update_status(status)</code></pre>

# cron の設定

[http://blog.mizoshiri.com/archives/215](http://blog.mizoshiri.com/archives/215) 参照。

/etc/crontab に説明があるのでそれにしたがって

<pre><code>40 * * * * yukop cd /path/to/py/ && python hoge.py</code></pre>

というかんじで指定する。


