---
title: "網頁機器人"
description: "發掘如何利用SeaChat將AI助理整合到您的網站和LINE通訊平台。這份指南將詳細介紹安裝網頁助理的完整過程，包括如何將提供的程式碼嵌入您的網頁HTML中。"
date: 2023-11-22T08:48:57+00:00
lastmod: 2023-11-22T08:48:57+00:00
draft: false
images: []
menu:
  seachat:
    parent: "seachat-manual"
aliases:
  - /zh/seachat/seachat-manual/04-channels/08-install-to-webpage/
url: /zh/seachat/manual/channels/webpage/
weight: 306
toc: true
---

## :movie_camera: 在网页上集成 SeaChat 小部件

  <iframe width="100%" height="400" src="https://www.youtube.com/embed/5YCiO8GEAu0?list=PL8K7_LTqly44LeOocjDOpXH0svonxa0T0" title="YouTube 视频播放器" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 30px;"></iframe>

## 自定义您的公司网页小部件

网页小部件是一个强大的工具，可让您将 SeaChat 集成到您的网站中。此功能使您能够提供实时客户支持并与网站访客互动。小部件可以根据您的品牌标识和网站设计进行定制。您还可以创建表单以收集访客信息和反馈。

## SeaChat 小部件配置

SeaChat 小部件提供多种自定义选项，帮助您创建无缝的客户体验。您可以调整小部件的外观和行为以满足您的需求。

### 基本设置和聊天设置

在这里，您可以定义小部件的名称、描述，并在 **基本设置** 中选择小部件的 UI 语言。向下滚动查看 **聊天设置**，在这里您可以定义助理在聊天中的行为。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/basic-settings.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/basic-settings.png" alt="SeaChat 的基本设置">
</a>

_样式的基本设置_

</center>
<br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/chat-settings.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/chat-settings.png" alt="SeaChat 的聊天设置">
</a>

_助理回答的聊天设置_

</center>
<br/>

每次更改后，您可以通过点击 **预览** 按钮在预览窗口中查看更改。一旦对更改满意，请点击 **保存** 按钮。

> :warning: 注意
>
> 请注意，只有点击 **保存** 按钮后更改才会保存。我们建议您点击 **预览** 按钮查看更改，只有在保存更改后才能点击 **测试 AI 助理**。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/preview-widget-chat.png" target="_blank">
<img height="100%" width="70%" style="border-radius: 5px" src="/images/seachat/zh/channels/webpage-widget/preview-widget-chat.png" alt="SeaChat 的基本设置">
</a>

_预览窗口_

</center>
<br/>

### 卡片设置

除了完全可定制的小部件外，您还可以创建卡片向客户显示信息。卡片可用于在用户首次访问您的网站时提供信息。您还可以将链接附加到卡片上，将用户引导到特定页面。要添加更多卡片，请点击 **加号** 按钮。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/card-setting.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/card-setting.png" alt="SeaChat 的聊天设置">
</a>

_设计您的卡片_

</center>
<br/>

### 自定义表单：聊天前用户信息收集表单

有时您可能希望收集客户信息。您可以创建自定义表单以收集信息，例如姓名、电子邮件和电话号码。这些信息可用于为客户提供个性化支持。根据您的使用场景，我们可以定义新表单并重复使用旧表单。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/custom-forms.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/custom-forms.png" alt="SeaChat 的自定义表单设置">
</a>

_选择或创建客户表单_

</center>
<br/>

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" alt="SeaChat 的自定义表单设置">
</a>

_聊天开始前选择_

</center>
<br/>

要编辑表单，请点击 **编辑** 按钮后点击 **&#8942;**。您还可以通过点击 **删除** 按钮删除表单。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/access-edit-forms.png" target="_blank">
<img height="100%" width="60%" src="/images/seachat/zh/channels/webpage-widget/access-edit-forms.png" alt="SeaChat 的自定义表单设置">
</a>

_选择或创建客户表单_

</center>
<br/>

### 自定义表单：客户满意度调查表单

现在，您可以通过客户满意度调查表单轻松收集客户反馈——就像设置用户信息收集表单一样！当访客尝试关闭 WebChat 小部件时，表单会自动弹出，允许访客留下星级评分并可选择写评论。

设置步骤：

1. 点击添加新表单按钮并选择客户满意度调查卡片。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/custom-forms2.png" alt="SeaChat 的自定义表单设置">
</a>

_选择客户满意度调查_

</center>
<br/>

2. 配置表格

- 打开启用开关。
- 根据您的需求自定义字段，包括：表单名称、调查标题、调查描述，并选择启用或禁用评论框（用于书面反馈）。如果启用，您还可以自定义评论框中的占位符文本。完成后点击保存。

3. 按以下 [安装步骤](/zh/seachat/manual/channels/webpage/#安装) 将更新的小部件代码安装到您的网站。

4. 查看调查结果

   现在，当访客与您的 AI 助理聊天并点击右下角图标关闭小部件时，客户满意度调查表单会弹出。如果访客提交反馈，您可以进入 SeaChat 的会话页面，通过点击会话头像查看星级评分和评论。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/csat-demo.gif" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/csat-demo.gif" alt="SeaChat 的自定义表单设置">
</a>

_展示访客如何留下反馈_

</center>
<br/>

<br/>

<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/csat-form-result.png" target="_blank">
<img height="100%" width="60%" src="/images/seachat/zh/channels/webpage-widget/csat-form-result.png" alt="SeaChat 的自定义表单设置">
</a>

_查看客户满意度调查结果_

</center>

<br/>

## 安装

现在您已经自定义了小部件，可以将其安装到您的网站。只需从 **安装小部件** 中复制提供的代码片段，并将其粘贴到您网站的 HTML 代码中。也就是当前 `<body>{...}</body>` 标签的末尾。

小部件将显示在您的网站上，使您能够为客户提供实时支持。

<br/>
<center>
<a style="border-radius: 0.4rem; cursor: zoom-in;" href="/images/seachat/zh/channels/webpage-widget/installation-code.png" target="_blank">
<img height="100%" width="100%" src="/images/seachat/zh/channels/webpage-widget/installation-code.png" alt="SeaChat 界面指导用户安装网页小部件">
</a>

_遵循安装步骤_

</center>
<br/>

## 支持

需要帮助？请联系我们：[seachat@seasalt.ai](mailto:seachat@seasalt.ai)。
