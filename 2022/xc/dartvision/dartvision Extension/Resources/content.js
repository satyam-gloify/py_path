// Determine runtime (Chrome or Firefox)
const runtime = typeof browser !== 'undefined' ? browser : chrome;
const storage = typeof browser !== 'undefined' ? browser.storage.local : chrome.storage.local;

console.log("Content script loaded");

// Define the dark mode CSS
const darkModeCSS = `
    html, body, div, span, applet, object, iframe,
    h1, h2, h3, h4, h5, h6, p, blockquote, pre,
    a, abbr, acronym, address, big, cite, code,
    del, dfn, em, img, ins, kbd, q, s, samp,
    small, strike, strong, sub, sup, tt, var,
    b, u, i, center, dl, dt, dd, ol, ul, li,
    fieldset, form, label, legend, table, caption,
    tbody, tfoot, thead, tr, th, td, article, aside,
    canvas, details, embed, figure, figcaption, footer,
    header, hgroup, menu, nav, output, ruby, section,
    summary, time, mark, audio, video {
        background-color: #222222 !important;
        color: #e0e0e0 !important;
        border-color: #333 !important;
    }

    a {
        color: #bb86fc !important;
    }

    img, video {
        filter: brightness(0.8) !important;
    }

    ::placeholder {
        color: #757575 !important;
    }
`;

// Function to apply dark mode
const applyDarkMode = () => {
    if (!document.getElementById('dark-mode-style')) {
        const style = document.createElement('style');
        style.id = 'dark-mode-style';
        style.textContent = darkModeCSS;
        document.head.appendChild(style);
        console.log("Dark mode applied");
    }
};

// Function to remove dark mode
const removeDarkMode = () => {
    const style = document.getElementById('dark-mode-style');
    if (style) {
        style.remove();
        console.log("Dark mode removed");
    }
};

// Apply dark mode based on the saved state for the current site
const hostname = window.location.hostname;
storage.get([hostname], (result) => {
    if (result[hostname]) {
        console.log("Dark mode enabled for this site");
        applyDarkMode();
    } else {
        console.log("Dark mode not enabled for this site");
        removeDarkMode();
    }
});

// Listen for messages from the popup or background script
runtime.runtime.onMessage.addListener((message) => {
    console.log("Received message:", message);
    if (message.darkMode) {
        applyDarkMode();
        storage.set({ [hostname]: true }, () => {
            console.log(`Dark mode preference saved: enabled for ${hostname}`);
        });
    } else {
        removeDarkMode();
        storage.set({ [hostname]: false }, () => {
            console.log(`Dark mode preference saved: disabled for ${hostname}`);
        });
    }
});

// Observe dynamically added elements and ensure dark mode applies to them
const observer = new MutationObserver(() => {
    applyDarkMode();
});

observer.observe(document.body, {
    childList: true,
    subtree: true,
});
