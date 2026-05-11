# Analytics Setup

Czeal is privacy-friendly by default — no trackers are loaded out of the box.
Every page has a clean `<!-- ANALYTICS — insertion point -->` comment in its
`<head>` so you can wire up Google Analytics 4 and/or Microsoft Clarity in
seconds when you're ready.

## Option A — Google Analytics 4

1. Create a GA4 property in your Google Analytics account and copy the
   **Measurement ID** (looks like `G-XXXXXXXXXX`).
2. Open each HTML file and find the marker:

   ```html
   <!-- ANALYTICS — insertion point (disabled until IDs are ready).
        See ANALYTICS.md in the repo root for setup instructions. -->
   ```

3. Replace the marker with this snippet (update the ID):

   ```html
   <!-- Google Analytics 4 -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX', { anonymize_ip: true });
   </script>
   ```

## Option B — Microsoft Clarity

1. Create a project at https://clarity.microsoft.com/ and copy the
   **Project ID** (looks like `abcd1234ef`).
2. Replace the `<!-- ANALYTICS ... -->` marker with:

   ```html
   <!-- Microsoft Clarity -->
   <script>
     (function(c,l,a,r,i,t,y){
       c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
       t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
       y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
     })(window, document, "clarity", "script", "XXXXXXXXXX");
   </script>
   ```

## Both at once

Paste both snippets, one after the other, at the marker.

## Which pages?

The marker is present in every HTML file except the Google Search
verification file. Safe to enable on all of them.

## Privacy notes

- Add a plain-language paragraph to `privacy.html` describing what's collected.
- GA4 snippet above uses `anonymize_ip: true`.
- Consider a cookie banner if you serve users in regions that require it.
