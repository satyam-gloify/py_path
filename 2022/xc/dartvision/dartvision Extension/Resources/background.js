browser.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Received request: ", request);

    if (request.greeting === "hello")
        return Promise.resolve({ farewell: "goodbye" });
});

browser.runtime.onInstalled.addListener(() => {
  console.log("Dark Mode Handler installed");
});
