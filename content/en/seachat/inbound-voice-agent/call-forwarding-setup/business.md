---
title: "Businesses - US, VoIP, Taiwan, Singapore"
description: "SeaChat Feature Tutorial | Call Forwarding Setup (Businesses - US, VoIP, Taiwan, Singapore)"
lead: ""
date: 2024-10-03 10:43:51.069 +0100
lastmod: 2024-10-04 10:43:51.069 +0100
draft: false
images: []
weight: 404
---

## Check if the preparation step is done

To proceed with the configuration of the call forwarding, we need to make sure that we have deployed a phone number that will be answered by SeaChat AI agents. If you haven't done this, Please check out our [tutorial](https://wiki.seasalt.ai/seachat/inbound-voice-agent/call-forwarding/) on how to do so. 

## Forward your Business calls to SeaChat

Forwarding business calls can be more complex than forwarding personal calls. For specific instructions and proper setup, it's recommended to consult the official documentation or contact customer support for assistance. Please carefully proceed with the instructions below to avoid potential issues.

## US Carriers

### AT&T
- **Unconditional Call Forwarding:**  
  Lift the phone receiver and dial ```*72 ``` (or  ```72# ```), then enter the number you want to forward calls to. For long-distance calls, include 1 + the 10-digit number.  
  For local calls, use just the area code and 7-digit number, or simply the 7-digit number for calls that don't require an area code.  
  Call forwarding is activated when you hear the confirmation tone.
- **No Answer Call Forwarding:**  
  Dial  ```*92 ```, then enter the 10-digit forwarding number and press #. Wait for the confirmation tone.
- **Busy Call Forwarding:**  
  Dial  ```*90 ```, then enter the 10-digit forwarding number and press #. The confirmation tone indicates the activation of call forwarding.
- **Selective Call Forwarding:**  
  Dial  ```*63 ``` and follow prompts to forward specific pre-selected numbers.
- **Turning Off Call Forwarding:**  
  For unconditional forwarding, dial  ```*73# ```.  
  For no-answer forwarding, dial  ```*93# ```.  
  For busy forwarding, dial  ```*91# ```.

### Frontier
- **Unconditional Call Forwarding:**  
  Dial  ```*72 ``` and enter the 10-digit forwarding number. Wait for the phone to be answered and for the confirmation tone.  
  Exceptions: In certain areas (e.g., Indiana, Illinois, Pennsylvania), dial ```72#```. For Connecticut Frontier Voice customers, dial ```72``` followed by the number.
- **No Answer Call Forwarding:**  
  Dial  ```*92 ``` and set the number of rings before forwarding. Then, enter the 10-digit forwarding number.  
  Exceptions: In Seneca Gorham, dial ```52```; in Rochester, dial ```44```. You can also change the ring duration by dialing ```40``` and setting the number of seconds before forwarding.
- **Busy Call Forwarding:**  
  Dial  ```*90 ```, enter the 10-digit number, and press #.  
  Exceptions: In Seneca Gorham, dial ```50```; in Rochester, dial ```48```.
- **Selective Call Forwarding:**  
  Dial  ```*63 ``` and follow the voice instructions to manage your forwarding list.
- **Turning Off Call Forwarding:**  
  Unconditional: Dial  ```*73 ``` and press **Talk**.  
  No Answer: Dial  ```*93 ``` and press **Talk**.  
  Busy: Dial  ```*91 ``` and press **Talk**.

### US Mobile
- **Unconditional Call Forwarding:**  
  On your phone's dial pad, enter ```*72```. Then, input the 10-digit number (including the area code) where you want to forward your calls (e.g., ```*72-908-123-4567```). Tap the Call button and wait for the confirmation tone or message. End your call to activate call forwarding.
- **No Answer Call Forwarding:**  
  On your phone's dial pad, enter ```*71```. Enter the 10-digit forwarding number, including the area code (e.g., ```*71-908-123-4567```). Tap the Call button and wait for the confirmation tone or message. Call forwarding will be activated after confirmation.
- **Busy Call Forwarding:**  
  Similar to No Answer Call Forwarding, on your phone's dial pad, enter ```*71```, followed by the 10-digit number where you want calls forwarded. Tap Call and wait for the confirmation tone. End the call once forwarding is confirmed.
- **Turning Off Call Forwarding:**  
  To cancel any type of call forwarding, dial ```*73``` on your phone. Tap Call, and once you hear the confirmation tone, end the call to deactivate call forwarding.

### T-Mobile
- **Unconditional Call Forwarding:**  
  Dial ```*21``` followed by the 10-digit forwarding number and press the call button. Wait for the activation tone to confirm the setup.
- **No Answer Call Forwarding:**  
  Dial ```*61``` followed by the 10-digit forwarding number and press the call button. The forwarding will activate upon hearing the confirmation tone.
- **Busy Call Forwarding:**  
  Dial ```*67``` followed by the 10-digit forwarding number and press the call button. The call forwarding is activated once you hear the activation tone.
- **Not Reachable Call Forwarding:**  
  Dial ```*62``` followed by the 10-digit forwarding number and press the call button. The call forwarding will be activated once you hear the activation tone.
- **Turning Off Call Forwarding:**  
  Unconditional Call Forwarding: Dial ```##21#```, press the call button, and wait for the confirmation tone to turn off.  
  No Answer Call Forwarding: Dial ```##61#``` and press the call button.  
  Busy Call Forwarding: Dial ```##67#``` and press the call button.  
  Not Reachable Call Forwarding: Dial ```##62#``` and press the call button.  
  All Conditional Call Forwarding: Dial ```##004#``` to disable all conditional call forwarding.

### Comcast (Business)
- **Unconditional Call Forwarding:**  
  Before picking up the receiver or pressing **Talk**, dial ```*72```. Then, dial the 10-digit number you wish to forward calls to. Press **Talk** to activate call forwarding, which will be confirmed by a tone and message.
- **No Answer Call Forwarding:**  
  Before picking up the receiver or pressing **Talk**, dial ```*71```. Then, enter the 10-digit forwarding number and press **Talk.** Call forwarding will activate after the confirmation tone.
- **Busy Call Forwarding:**  
  Dial ```*90``` before picking up the receiver or pressing **Talk**, then enter the 10-digit forwarding number. Press **Talk,** and wait for the confirmation tone.
- **Selective Call Forwarding:**  
  Lift the receiver and dial ```*63```. Follow the voice prompts to select which numbers to forward, and activate after the confirmation code.
- **Turning Off Call Forwarding:**  
  Unconditional Call Forwarding: Dial ```*73```, wait for the confirmation tone, then hang up.  
  No Answer Call Forwarding: Dial ```*93```, wait for the tone, and hang up.  
  Busy Call Forwarding: Dial ```*91```, wait for the confirmation tone, and hang up.  
  Selective Call Forwarding: Dial ```*83```, enter rule details, and save to deactivate.

### Xfinity Mobile (Comcast consumers)
- **Unconditional Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*72```. Enter the 10-digit forwarding number provided by your answering service. Call forwarding will activate once you hear the confirmation tone.
- **No Answer Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*92```. Enter the 10-digit forwarding number. The call forwarding will activate after you hear the confirmation code.
- **Busy Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*90```. Enter the 10-digit number. Call forwarding is activated once the confirmation tone is heard.
- **Selective Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and press ```*63```. Enter the 10-digit number you want to forward. The service will activate once you hear the confirmation tone.
- **Turning Off Call Forwarding:**  
  Unconditional Call Forwarding: Dial ```*73``` to turn off the service. Wait for the confirmation tone.  
  No Answer Call Forwarding: Dial ```*93``` to deactivate. Wait for the confirmation tone.  
  Busy Call Forwarding: Dial ```*91``` to disable. Wait for the confirmation tone.  
  Selective Call Forwarding: Dial ```*83``` and press ```3``` to turn off selective forwarding. Wait for the confirmation tone.

### Verizon
- **Unconditional Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and dial ```*72``` followed by the 10-digit forwarding number (e.g., ```*72-999-555-4567```). Wait for a series of beeps, then the call will automatically end, confirming that call forwarding is active.
- **No Answer Call Forwarding:**  
  Lift the receiver, listen for the dial tone, and dial ```*71``` followed by the 10-digit forwarding number (e.g., ```*71-999-555-4567```). The call will be forwarded if not answered after 3 to 6 rings. Once you hear the beeps, the call will automatically end, confirming activation.
- **Busy Call Forwarding:**  
  Dial ```*71``` and enter the 10-digit number where you want calls to be forwarded if the line is busy. After hearing the beeps, the call will end, activating the feature.
- **Turning Off Call Forwarding:**  
  To turn off call forwarding, dial ```*73```. Wait for the confirmation tone, and the service will be deactivated.

### RingCentral
- **Call Forward for Unreachable Phones:**  
  When your phone is offline, incoming calls are forwarded to another user’s extension or an external number. This can be configured under different call handling rules:
    - User/Business hours
    - After hours
    - Custom answering rules  
      Once the phone service is restored, calls will automatically resume ringing on the original phone.

- **Requirements:**
    - The extension must have at least one desk phone with a DigitalLine assigned.
    - Desktop & Mobile Apps must be disabled in the ring list.
    - PSTN numbers should also be turned off in the ring list.
- **Conditions**:
    - All desk phones tied to the extension must be unreachable for this feature to activate.
    - If forwarding calls to other phones, all forwarding devices must be unreachable for this feature to trigger.
    - Turning on PSTN numbers or Desktop & Mobile Apps in the ring list will prevent this feature from working.
- **Enabling Call Forwarding for Unreachable Phones:**  
  Sign in to your RingCentral online account.
    - ***Non-admin users***:  
      Click Settings in the top menu. Open the Call Handling section and select your call rule (Work-hours, After-hours, or Custom).
    - ***Admin users***:  
      Click Users in the top menu. Select a user from the Users with Extensions list. Open the Call Handling section and select the desired call rule.  
      In the Work Hours tab, click Edit under Call Forward for Unreachable Phone. Toggle on the Call Redirection feature.  
      Choose where you want the calls to be forwarded:
        - Extension
        - Other number
- **Click Save to activate the forwarding rule.**

### Vonage
- **Unconditional Call Forwarding:**
    - Lift the receiver, dial ```*72```, and enter the 10-digit number you wish to forward calls to. Press 1 to confirm, and wait for the confirmation tone.
    - Online Setup: You can also set up call forwarding via your Online Account or the Vonage Enterprise Portal by navigating to the **Summary tab** > **My Numbers** > **Calling Features** > **Call Forwarding** and following the prompts to enter the forwarding number and desired ring duration before forwarding.
- **No Answer Call Forwarding:**
    - Sign in to your Online Account or Vonage Enterprise Portal. Navigate to Calling Features, select Call Forwarding, and set the number of seconds before forwarding. Enter the forwarding number and save the settings.
- **Busy Call Forwarding:**
    - For residential users, sign in to your Online Account, go to Calling Features, and enter the forwarding number. Save the settings.
    - For enterprise users, go to **Voice Settings** > **General** in the Vonage Enterprise Portal to enable busy call forwarding.
- **Selective Call Forwarding:**
    - In the Online Account or Enterprise Portal, navigate to Calling Features, set the conditions for selective forwarding, and enter the forwarding number. Save the settings.

### Google Voice
#### Android:
- **Unconditional Call Forwarding:**  
  Open the Google Voice app on your mobile device. **Tap Menu** > **Settings**, and under Custom Call Forwarding, select Manage rules. Choose the contact whose calls you want to forward, and enter the number where you want calls forwarded. The rule will be applied once saved.
- **No Answer Call Forwarding:**  
  In the Google Voice app, **go to Menu** > **Settings** > **Manage** rules. Set a rule for a specific contact or group, and select the option to forward calls when unanswered. Specify the forwarding number.
- **Busy Call Forwarding:**  
  Access Manage rules in the Google Voice settings. Choose the contact you wish to forward, and create a rule to forward calls when your line is busy. Enter the forwarding number and save the rule.
- **Selective Call Forwarding:**  
  In the Google Voice settings, under Custom Call Forwarding, tap Manage rules. Select a specific contact or contact group to forward their calls to a different number. The rule will activate after saving.
- **Turning Off Call Forwarding:**  
  To turn off custom call forwarding for a specific contact, go to Manage rules in the Google Voice settings. Find the contact or rule you want to disable, and delete or edit the rule accordingly.

#### iPhone/iOS:
- **Unconditional Call Forwarding:**  
  Open the Google Voice app on your mobile device. Tap Menu > Settings, then navigate to Custom Call Forwarding and select Manage rules. Choose a contact or contact group and enter the number you want to forward calls to. The rule will activate once saved.
- **No Answer Call Forwarding:**  
  In the Google Voice app, go to Menu > Settings > Manage rules. Create a rule to forward calls when unanswered and enter the forwarding number. The call forwarding will activate after saving the rule.
- **Busy Call Forwarding:**  
  Access the Google Voice settings under Manage rules. Set a rule for calls to be forwarded when the line is busy. Enter the forwarding number and save the changes.
- **Selective Call Forwarding:**  
  In Google Voice, go to Manage rules under Custom Call Forwarding. Set a rule to forward calls from specific contacts or groups and specify the forwarding number. The service will activate after saving.
- **Turning Off Call Forwarding:**  
  To turn off custom call forwarding for a specific contact or group, go to Manage rules in Google Voice, find the rule you want to disable, and delete or edit the rule.

## Taiwan Carriers
### Chunghwa Telecom
- **Immediate Call Forwarding:**  
  To activate, dial ```*77``` followed by the forwarding number, then hang up.  
  To deactivate, dial ```#77```.
- **Busy Line Call Forwarding:**  
  To activate, dial ```*76``` followed by the forwarding number, then hang up.  
  To deactivate, dial #76.
- **No Answer Call Forwarding:**  
  To activate, dial ```*75``` followed by the forwarding number, then hang up.  
  To deactivate, dial #75.

### Taiwan Mobile
- **Unconditional Call Forwarding:**  
  Forward to a Landline: Dial ```*21``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*21``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*21``` followed by the mobile number, then ```*24#```, and press Send.
- **No Answer Call Forwarding:**  
  Forward to a Landline: Dial ```*61``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*61``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*61``` followed by the mobile number, then ```*24#```, and press Send.
- **Unavailable Call Forwarding:**  
  Forward to a Landline: Dial ```*62``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*62``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*62*``` followed by the mobile number, then ```*24#```, and press Send.
- **Busy Line Call Forwarding:**  
  Forward to a Landline: Dial ```*67*``` followed by the area code and phone number, then ```*11#```, and press Send.  
  Forward to a Mobile Phone: Dial ```*67``` followed by the mobile number, then ```*11#```, and press Send.  
  Video Calls Forward to Mobile: Dial ```*67``` followed by the mobile number, then ```*24#```, and press Send.
- **Cancel Call Forwarding:**  
  To cancel individual forwarding settings, dial ## followed by the specific service code (21/61/62/67) and #, then press Send.  
  To cancel all call forwarding, dial ##002# and press Send.

## Singapore Carriers
### Singtel
- **Unconditional Call Transfer:**  
  Lift the handset, wait for the dial tone, and dial ```#210YYYYYYYY#```, where ```YYYYYYYY``` is the number you want calls to be forwarded to. Wait for the repeated tone and hang up. Your call transfer is now activated.
- **Cancel Unconditional Call Transfer:**  
  Lift the handset, wait for the dial tone, and dial ```#211#```. Wait for the repeated tone and hang up.
- **Call Transfer When No Reply:**  
  Lift the handset, wait for the dial tone, and dial ```#220YYYYYYYY#``` where ```YYYYYYYY``` is the number to forward calls when there’s no reply. Wait for the repeated tone and hang up.
- **Cancel Call Transfer When No Reply:**  
  Lift the handset, wait for the dial tone, and dial ```#221#```. Wait for the repeated tone and hang up.
- **Call Transfer When Busy:**  
  Lift the handset, wait for the dial tone, and dial ```#230YYYYYYYY#``` where ```YYYYYYYY``` is the number to forward calls when your line is busy. Wait for the repeated tone and hang up.
- **Cancel Call Transfer When Busy:**  
  Lift the handset, wait for the dial tone, and dial ```#231#```. Wait for the repeated tone and hang up.


