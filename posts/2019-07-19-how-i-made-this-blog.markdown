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

其實Hakyll作者自己寫的[教學文檔](https://jaspervdj.be/hakyll/tutorials.html)就已
經很清楚了，我單純紀錄一下我是怎麼做的... 我的程式碼放在這裡：
[https://github.com/usefulalgorithm/personal-website](https://github.com/usefulalgorithm/personal-website)

這個網站是直接host在Github Page上面，因為我懶得找別的免費的website hosting
service了... Github Page的使用方法應該蠻簡單的，直接去他們的[官方網站
](https://pages.github.com/)，照著步驟做就可以了。如果不想的話，
[Surge](https://surge.sh/)貌似免費用戶就有自訂網址，但我沒用過。

其他的deployment我其實也就照著官方說明做，稍微有微調了一下HTML排版、字型跟 CSS的
一些屬性。

比較可以講的是我有加了Disqus跟標籤功能，標籤功能要用需要去改`site.hs`，改完之後
還要記得重新用`stack build`重新編過一次。我就是忘記需要重新編過，卡超久...
