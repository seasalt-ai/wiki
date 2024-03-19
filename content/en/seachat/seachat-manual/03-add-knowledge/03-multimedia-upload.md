---
title: "Audio/Video Knowledge Base"
description: "SeaChat from Seasalt.ai transcribes Audio/Video files in knowledge base"
lead: ""
date: 2024-03-04 10:43:51.069 +0100
lastmod: 2024-03-04 10:43:51.069 +0100
weight: 32
draft: false
images: []
aliases:
  - /en/seachat/seachat-intro/03-add-knowledge/add-knowledge-intro
---

## Overview
Audio and video files can be used as knowledge base for your SeaChat agent too! Usually one can first transcribe these files to text, then upload to a chatbot platform. SeaChat takes care of the transcription step for you by directly accepting audio/video files!

You can use this functionality directly, or you can transcribe your files elsewhere, then upload the text. The choice is yours!

Note that the current implementation assumes the following:
1. language is either English or Chinese
2. there is only one speaker in the file
3. total length is less than 15 minutes

> :exclamation_question_mark: *Great, but why?* :exclamation_question_mark:
>
> The audio/video file uploads seem to be very limited than other transcription services. Why do you still list it out as a standalone feature?
>
> Because SeaChat implemented a feature that supports audio input from WhatsApp and Facebook Messenger, so that your chat agent understands speech input. Then we used the same pipeline to accept audio/video uploads!
>
> Each WhatsApp and Messenger audio message usually contains one speaker and is less than 1 minute. The multimedia upload feature is a natural extension of this.


SeaChat provides four methods to upload files to your agent. We will focus on the **Transcribe Audio/Video** method in this tutorial and by the end of the tutorial your SeaChat agent will have a customized knowledge base at your service.


## Create a SeaChat Agent
If you don't have a SeaChat account yet, you can sign up for free at [SeaChat website](https://chat.seasalt.ai/)! You can find all the information you need to create a knowledge-based chatbot in [Create an Agent](/en/seachat/seachat-intro/02-how-to-create/).


## Open Knowledge Base
Find your agent's knowledge base by navigating to the **Knowledge Base** dashboard under **Agent Configuration** in the sidebar menu. By choosing **Transcribe Audio/Video**, you can upload a video or audio file to your agent.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step2.png" alt="Image of the Knowledge Base dashboard through the Agent Configuration in the sidebar menu to show how to upload a CSV or JSON file to an agent by selecting Upload from Template File.">

## Upload File
By clicking on the upload button, you can submit to your agent choosing from various file formats[^1]. The file will be processed and the knowledge base will be updated accordingly once submitted.
[^1]: SeaChat supports .wav, .flac, .aac, .opus, .mp3, .mp4, .ogg, .m4a files.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step3.png" alt="Screenshot illustrating the navigation through the dashboard of knowledge base for SeaChat's AI agents. It illustrates the user interface">
<br/>
<br/>
<br/>

> :rotating_light: **Note** :rotating_light:
>
> Before uploading the file, check if the files meet the two following requirements:
> - The media content must be in English or Chinese.
> - The file's duration should not exceed 15 minutes.

## Check the language
Make sure to choose the correct media language for the audio or video file. For now SeaChat supports English and Traditional Chinese. Once you have included all the files to be uploaded, you can upload them by clicking on the **Submit** button.

Note that the English/Chinese support only means that your uploaded audio/video files are transcribed into
corresponding language. SeaChat, powered by an LLM in the backend, is multilingual. This means that a user
can talk with SeaChat in a totally different language. 

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step4.png" alt="Interface of SeaChat showing the bulk upload feature with a drag and drop zone and a section below for monitoring the status of each file being uploaded and a preview section for the spreadsheet data, reminding users to verify file format and content before submission.">
<br/>
<br/>


## Submit to Existing Knowledge Base
Voilà! You have successfully customized your chatbot agent with new knowledge. To view the files uploaded, you can navigate to the **Existing** section in the top-right corner of the page, where you can find the uploaded data waiting for you in the **Files** section.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step5.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Submit' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


## Review your Knowledge Base
Click on the file you just uploaded to review the content. That's it! Your SeaChat agent now has transcribed the content of the uploaded media into text. You can now use the knowledge base to test your agent. SeaChat provides additional settings to customize your knowledge base, we will continue to explore these features in the **Advance** section of the tutorial.

<br/>
<img width="80%" style="border-radius: 0.4rem" src="/images/product-updates/seachat/en/tutorial-add-knowledge/multimedia/20240319-multimedia-tutorial-step6.png" alt="Visual guide highlighting the process to finalize file uploads for agent customization by clicking the 'Next' button, with a follow-up view of the 'Existing' section in the screen top-right showcasing the uploaded files in the 'Files' section.">


## Under the Hood

There are a few things to note to use this function properly:

1. For video files, SeaChat does not do anything with the video content. All it does is to extract the audio tracks from the video, and transcribe the audio to text, which can be used in the KB.
2. For each transcribed audio and video, you can check the transcription quality in Existing Knowledge Base.
3. If you have multi-media files in another language, feel free to transcribe them to text, and then upload to Seachat -- it achieves the same goal. 
4. For the audio/video file, SeaChat assumes there's only one speaker in the file. That is, SeaChat does not perform diarization or speaker identification. If you have an audio file that contains a conversation (such as a two-person podcast), you should first transcribe it and start each line with the speaker name if applicable.


## Support
Need assistance? Contact us at [seachat@seaslt.ai](mailto:seachat@seaslt.ai).

 