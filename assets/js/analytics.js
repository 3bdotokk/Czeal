/* Czeal — Analytics loader (GA4 + Microsoft Clarity)
   Single inclusion point. Loaded async, non-blocking. */
(function () {
  'use strict';

  // Prevent duplicate injection
  if (window.__czAnalyticsLoaded) return;
  window.__czAnalyticsLoaded = true;

  // ---------- Google Analytics 4 ----------
  var GA_ID = 'G-3CS7Y247CS';

  var gaScript = document.createElement('script');
  gaScript.async = true;
  gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(gaScript);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', GA_ID, { anonymize_ip: true });

  // ---------- Microsoft Clarity ----------
  (function (c, l, a, r, i, t, y) {
    c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
    t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
    y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
  })(window, document, 'clarity', 'script', 'wsafgclnx7');

})();
