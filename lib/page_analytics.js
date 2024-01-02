// Optional script used for anonymous performance analytics hosted by Google Analytics. If you do not wish to include it, you can remove its reference from the bottom of the index page.
let id = 'G-LGHB6S47PK'

// Simple function to check if ad blockers are likely enabled
function isAdBlockerActive() {
    const adBlockerCheck = () => {
        const testDiv = document.createElement('div');
        testDiv.innerHTML = '&nbsp;';
        testDiv.className = 'adsbox adsbygoogle ad ad-300x250 ad-banner ad-header ad-sidebar';
        testDiv.style.position = 'absolute';
        testDiv.style.top = '-100px';
        testDiv.style.left = '-100px';
        document.body.appendChild(testDiv);
        const isAdBlocked = testDiv.offsetHeight === 0 || testDiv.offsetWidth === 0;
        document.body.removeChild(testDiv);
        return isAdBlocked;
    };
    return adBlockerCheck();
}

// Conditionally load Google Analytics if it is estimated that it will not be blocked by the browser
if (!isAdBlockerActive() && typeof navigator.sendBeacon !== 'undefined') {
    makeScriptTag(document.currentScript, 'https://www.googletagmanager.com/gtag/js?id=' + id, true, (msg) => {});
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());
    gtag('config', id);
}