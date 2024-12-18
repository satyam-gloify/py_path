console.log("Hello World!", typeof browser !== 'undefined' ? browser : chrome);

document.addEventListener('DOMContentLoaded', async () => {
    const toggle = document.getElementById('darkModeSwitch');
    console.log("DOM content loaded");

    // Use `chrome` for Chrome/Safari and `browser` for Firefox/other WebExtension browsers
    const runtime = typeof chrome !== 'undefined' ? chrome : browser;
    const storage = typeof chrome !== 'undefined' ? chrome.storage.local : browser.storage.local;

    try {
        // Get the current active tab's URL
        const [tab] = await runtime.tabs.query({ active: true, currentWindow: true });
        const url = new URL(tab.url).hostname;

        // Load the saved dark mode preference for this site
        storage.get([url], (result) => {
            console.log("Storage result for this site:", result);
            toggle.checked = result[url] || false;
        });

        // Listen for toggle changes and save the preference
        toggle.addEventListener('change', () => {
            const isEnabled = toggle.checked;
            console.log(`Dark mode ${isEnabled ? 'enabled' : 'disabled'} for ${url}`);

            storage.set({ [url]: isEnabled }, () => {
                console.log(`Saved dark mode setting for ${url}`);
            });

            // Notify the content script to apply/remove dark mode
            runtime.tabs.sendMessage(tab.id, { darkMode: isEnabled });
        });
    } catch (error) {
        console.error("Error in popup.js:", error);
    }
});
