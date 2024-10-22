---
title: "結束會議記錄"
description: "了解如何手動或自動結束 SeaMeet 會議記錄，機器人將在適當情況下自動退出，完全掌握 SeaMeet Copilot 在會議紀錄上的控制。"
date: 2023-11-22T08:48:57+00:00
lastmod: 2024-06-03T08:48:57+00:00
draft: false
images: []
menu:
  seameet:
    parent: "seameet-manual"
aliases:
   - /zh/seameet/11-seameet-end-a-meeting/
url: /zh/seameet/end-a-meeting/   
weight: 34
toc: true
---


當會議結束時，您可以選擇：

1. 在SeaMeet會議頁面按下中止會議紀錄的按鈕

<center>
<img src="/images/seameet-zh/SeaMeet會議頁面按下中止會議紀錄.png" alt="SeaMeet會議頁面按下中止會議紀錄"/>
</center>

2. 或者在擴充程式手動按下中止會議的按鈕

<center>
<img src="/images/seameet-zh/在SeaMeet擴充程式手動按下中止會議的按鈕.png" alt="在SeaMeet擴充程式手動按下中止會議的按鈕"/>
</center>

若您忘記手動中止會議紀錄，則機器人會在以下狀況直接離開Google Meet會議室：

1. 當所有與會者都離開會議室的30秒後
2. 若有用戶仍然留在會議室中，機器人會等待15分鐘確認是否為會議暫停，若15分鐘內無人說話，機器人便會自動離開
