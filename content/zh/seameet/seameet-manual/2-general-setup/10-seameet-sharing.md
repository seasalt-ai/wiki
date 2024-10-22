---
title: "自動分享會議記錄"
description: "了解如何在 SeaMeet 中設定自動分享會議記錄的功能。此指南涵蓋如何分享會議記錄給與會者、相同網域的參與者，及使用黑名單排除特定收件人，提升會議管理效率。"
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-06-03T08:48:57+00:00
draft: false
images: []
menu:
   seameet:
      parent: "seameet-manual"
aliases:
   - /zh/seameet/10-seameet-sharing/
url: /zh/seameet/sharing/   
weight: 23
toc: true
---

## 開始使用

您可以在「**工作區設定**」的「**常用設定**」調整自動分享會議記錄的發送對象。

<br/>
<center>
<a href="/images/seameet-zh/10-seameet-sharing/seameet-auto-sharing-setting-ui.png" target="_blank">
<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in" src="/images/seameet-zh/10-seameet-sharing/seameet-auto-sharing-setting-ui.png" alt="設定SeaMeet自動分享會議記錄"/>
</a>

*常用設定*
</center>
<br/>

您可以在「**常用設定**」中設定自動分享功能，目前SeaMeet提供以下選項：

1. **只分享給自己**

    當您作為邀請者邀請機器人記錄的會議結束後，系統會自動發一封信到您的信箱。

2. **分享給所有行事曆與會者**

    當您邀請機器人轉錄的會議結束後，系統會自動發一封信到所有Google行事曆上受邀參加這個會議的與會者。

3. **分享給與我同信箱網域的與會者**

   當會議結束時，系統會自動將會議記錄發送給所有擁有與您相同域名的參與者。舉例來說，如果在會議中有來自 `@seasalt.ai` 和 `@client-company.com` 的參與者，系統只會將會議記錄發送給 `@seasalt.ai` 的參與者，而不會發送給 `@client-company.com` 的參與者。該功能僅對與您相同網域且為私人信箱的與會者有效，而不會對使用公用信箱（如Gmail、Hotmail和Outlook）的與會者生效。

4. **不自動分享給任何人（包括自己）**

   會議結束後將不會發送任何會議記錄。

如果您開啟自動分享功能，會議結束後系統會依照您的自動分享設定，自動將會議記錄以信件形式寄發給指定對象的信箱。

<center>
<img src="/images/seameet-zh/開啟SeaMeet自動分享功能.png" alt="開啟SeaMeet自動分享功能"/>
</center>

## 額外分享清單

<br/>

<center>

<a href="/images/seameet-zh/10-seameet-sharing/additional-list.png" target="_blank">

<img width="80%" style="border-radius: 0.4rem; cursor: zoom-in" src="/images/seameet-zh/10-seameet-sharing/additional-list.png" alt="設置 SeaMeet 自動分享會議記錄"/>

</a>

*額外分享清單*

</center>

<br/>

額外分享清單允許您將會議記錄發送給未參加會議的收件人。您可以將會議記錄副本（CC）和密件副本（BCC）寄給額外的收件人。

額外分享清單的一個非常有用的功能是黑名單。當您選擇將會議記錄發送給所有行事曆與會者時，可以通過黑名單將某些參與者排除在接收會議記錄之外。

請記得先啟用額外分享清單功能，才能使用它。
