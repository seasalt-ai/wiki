const bindWidgets = (() => {
    const select = selector => document.querySelector(selector);
    const selectAll = selector => document.querySelectorAll(selector);

    const channelTypes = {
        line: "line",
        facebook: "facebook",
        whatsapp: "whatsapp",
        webchat: "webchat"
    };

    const widgetContainer = select("#sui-right-widgets");

    const init = () => {
        // bindWidgets
        bindWidgetContent(channelTypes.webchat);
        bindWidgetContent(channelTypes.line, "https://lin.ee/fFNydh0a");
        bindWidgetContent(
            channelTypes.facebook,
            "https://mobile.facebook.com/profile.php?id=106953261045343"
        );
        bindWidgetContent(
            channelTypes.whatsapp,
            "https://api.whatsapp.com/send/?phone=%2B14252987474&text&type=phone_number&app_absent=0"
        );

        // for mobile use --- start
        const widgetBtn = select("#sui-widget-btn");

        const handleWidgetBtnClick = () => {
            const widgetIcons = selectAll(".widget-btn");

            if (widgetBtn.className == "close") {
                widgetIcons?.forEach((div) => {
                    div?.classList?.remove('show');
                })
                widgetBtn.classList.remove("close");
                select("#sui-webchat").style.display = "none";
            } else {
                widgetIcons?.forEach((div) => {
                    div?.classList?.add('show');
                })
                widgetBtn.classList.add("close");
            }
        };

        widgetBtn.addEventListener("click", handleWidgetBtnClick);
        // for mobile use --- end
    };

    const bindWidgetContent = (channel, url = "") => {
        if (channel === channelTypes.webchat) {
            const webChatButton = document.createElement("button");
            webChatButton.id = "sui-webchat-btn";
            webChatButton.className = "widget-btn";
            
            const iframeContainer = document.createElement("iframe");
            iframeContainer.id = "sui-webchat";

            const handleClick = () => {
                const widgetIcons = selectAll(".widget-btn");
                
                if (
                    iframeContainer.src !==
                    "https://chat.seasalt.ai/chat/9e4cef8823b94d019b954db6f4328a93"
                ) {
                    iframeContainer.src =
                        "https://chat.seasalt.ai/chat/9e4cef8823b94d019b954db6f4328a93";
                }
                if (iframeContainer.style.display !== "block") {
                    iframeContainer.style.display = "block";
                    widgetIcons?.forEach((div) => {
                        div?.classList?.add('show-iframe');
                    })
                } else {
                    iframeContainer.style.display = "none";
                    widgetIcons?.forEach((div) => {
                        div?.classList?.remove('show-iframe');
                    })
                }
            };
            webChatButton.addEventListener("click", handleClick);

            widgetContainer.prepend(iframeContainer);
            widgetContainer.prepend(webChatButton);
        } else {
            const widgetButton = document.createElement("a");
            widgetButton.id = `sui-${channel}-btn`;
            widgetButton.className = "widget-btn";
            widgetButton.href = url;
            widgetButton.rel = "noopener noreferrer";
            widgetButton.target = "_blank";

            widgetContainer.prepend(widgetButton);
        }
    };

    return { init, channelTypes };
})();
