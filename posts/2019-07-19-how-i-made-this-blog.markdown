---
title: How I Got This Blog Rolling (aka Hakyll For Dummies)
layout: post
comments: true
tags: hakyll, haskell
---

![One day I'll start a company where all programmers have to code in Brainfuck...](https://i.warosu.org/data/g/img/0647/55/1518802013131.jpg)

## Why Hakyll?
  
一直以來都蠻想學一下[Haskell](https://www.haskell.org/)，但又太懶沒真的認真學過
或是拿來做什麼正事... 最近事情沒那麼多，想說重新來摸一下，但光是看[Real World
Haskell](http://cnhaskell.com/)或是[Learn You a Haskell for Great
Good](http://learnyouahaskell.com/)來學好像又有點沒啥實感的樣子，就想說不如挑簡
單一點的事情來做。然後我一直都想學下怎樣自己架個部落格，所以...

一開始是打算拿另一個也是用Haskell實作的網路框架
[Yesod](https://www.yesodweb.com/)來刻一個，但是摸了一陣覺得Yesod對於Haskell語言
熟悉度的門檻還是稍微高一些，於是就拿Hakyll來用了。Hakyll基本上跟Jekyll的原理差不
多，只要寫寫markdown文檔，下幾個指令，丟給伺服器就差不多了。很久以前有嘗試用過
Jekyll，但是那時候比較嫩一點，又不是很想認真搞懂元件跟功能之間的關係，就沒有繼續
碰了。目前個人使用Hakyll的感覺是所有的邏輯都可以整合在一個地方，印象中Jekyll還有
一些需要自己去調整的東西，比起來Hakyll的整體使用經驗對我來說順蠻多的。當然有那種
根本不用開命令列就可以架Jekyll的作法，但我的重點就是要自己做啊... 所以不考慮。至
於在實際操作上，Haskell的code其實一旦習慣了就還蠻好懂的，整個程式的邏輯很清楚，
要加什麼特別神奇的功能我想應該也是有辦法做到的。社群裡面大師也很多，基本上有什麼
不會的Google一下都可以找到解答。

## How?

其實Hakyll作者自己寫的[教學文檔](https://jaspervdj.be/hakyll/tutorials.html)就已經很清楚了，我單純紀錄一下我是怎麼做的... 我的程式碼放在這裡：[https://github.com/usefulalgorithm/personal-website](https://github.com/usefulalgorithm/personal-website)

這個網站是直接host在Github Page上面，因為我懶得找別的免費的website hosting
service了... Github Page的使用方法應該蠻簡單的，直接去他們的[官方網站](https://pages.github.com/)，照著步驟做就可以了。如果不想的話，[Surge](https://surge.sh/)貌似免費用戶就有自訂網址，但我沒用過。

接下來講一下基本的操作：

### Basics

其實直接從Hakyll官方拉下來就可以直接透過`stack`來把所有東西建起來了。應該可以透過[bootstrap](https://getbootstrap.com/)之類的東西來調HTML跟CSS相關的所有東西，但我看文檔有點多就懶得讀了...

另外要佈署到Github的話，因為Github Page不會自行替我們輸出Hakyll builds，所以必須要做一些額外的步驟。網上似乎有大大有做些全自動化的CI的介紹，但因為我佈署的時候沒看到那篇文，所以基本上是照著自己覺得怎樣好用就怎麼做了。Hakyll編好的HTML檔會放在`_site/`資料夾裡面，而這些HTML檔就是實際上拿來佈署的網頁。我做的就是直接在`_site/`裡面新開一個Git repository：

```bash
$ git clone https://github.com/username/username.github.io _site
```

然後因為在做`stack exec site build`的時候生出來的檔會自己長在`_site`裡面，所以它裏頭的Git repository也跟著被修改。如果我們透過瀏覽器看過一遍，覺得沒有問題的話，就可以直接去針對`_site/`裡面的檔案去做`git add; git commit -m <Your commit message>; git push`，然後再去你的Github Page頁面網址看 看你丟上去的東西。

### Favicon

有沒有看到我的網頁的小圖示是個妙蛙種子？梗是來自這裡：[Interview with Bulbasaur](http://www.rhizomes.net/issue5/poke/bulbasaur.html)。這個應該是最簡單的，只要自己生一個`.ico`檔出來，丟在一個你覺得適合的地方就可以了。我自己的話是放在`image/`裡面，但其實放哪真的都沒差... 好了之後，在`template/default.html`的`head`裡面塞進這行:

```html
(... snipped... )
<link rel="icon" href="/images/favicon.ico"/>
(... snipped... )
```

然後`stack exec site watch`，再去`127.0.0.1`看，應該就可以在瀏覽器的tab列看到你的小圖示了。

### Disqus

雖說好像有人講說根本就不需要有讓人留言的功能，不過我覺得有的話還是炫一點... 我只看過別人用[Disqus](https://disqus.com/)，又懶得去survey有沒有其他的東西可以用，所以就決定用Disqus了。 Disqus的設定相對簡單一點，照著官網的說明操作即可。比較有點煩的是Disqus一定要註冊才能用，就... 不在意的話可以用，我個人的話如果以後有空閒的話是會想換個留言外掛來用就是了。照著官方說明做完之後，`templates/default.html`裡面應該會有一個`<comments>`部分，可以自己在`css/default.css`裡面調整一下，然後以後發文的時候markdown的metadata裡面記得要加`comments: true`。

### Tags

這個我搞得比較久，結果後來發現是低級錯誤... 基本上照著這篇做就可以了：[Add tags to your Hakyll blog](https://javran.github.io/posts/2014-03-01-add-tags-to-your-hakyll-blog.html)，但是做完之後 **千萬記得要`stack build`** ，重新編過一次`site.hs`，才會觀察到`_site/tags/`裡面有東西出現。

### RSS / Atom Feed

這個也一樣照著官網做就好了。那因為我覺得RSS訂閱那個按鈕很好看，不想要有個文字連結來做這件事情，所以花比較多時間的反而是在搞RSS訂閱的按鈕。搞好之後想說乾脆連社群媒體的那些連結也都做成一樣的形式，就不用再另外多一個Contact的頁面了。我是用[Font Awesome](https://fontawesome.com/)來找那些圖片，應該一樣照著官網上面寫的作法做就可以了，但是它也得要註冊... 另外Font Awesome貌似是可以下載下來直接放在`css/`裡面，或是也可以直接用網路上的資源庫來用。網路上的Kit貌似載入速度似乎不是太好，圖片要稍微等一等才會正確地出現，我覺得用起來實在是有點不... 所以就直接在`templates/default.html`的`<head>`裡面加了一段自己去load的腳本，然後用不那麼新的FA庫，載入速度就快了一些。我用原本的Kit時在沒有快取時的速度大概是改用腳本時的五倍吧...就一簡單的部落格要載個十幾秒，實在是沒必要。

```html
<script type="text/javascript"> (function() { var css =
  document.createElement('link'); css.href =
    'https://use.fontawesome.com/releases/v5.1.0/css/all.css'; css.rel =
    'stylesheet'; css.type = 'text/css';
  document.getElementsByTagName('head')[0].appendChild(css); })();
</script>
```

## That's all!

大概是這樣了，其實很多都是照著別人的東西上的說明做的，沒啥特別了不起的地方...
