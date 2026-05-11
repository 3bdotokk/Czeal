/* Czeal — article reading progress + share buttons. <1KB gz, no deps. */
(function () {
  'use strict';

  // ---------- Reading progress bar ----------
  var bar = document.querySelector('.read-progress-bar');
  if (bar) {
    var ticking = false;
    function update() {
      var doc = document.documentElement;
      var scrollable = doc.scrollHeight - doc.clientHeight;
      var pct = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
      bar.style.width = (pct * 100) + '%';
      ticking = false;
    }
    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  }

  // ---------- Share buttons ----------
  function toast(msg) {
    var t = document.getElementById('share-toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('is-visible');
    clearTimeout(toast._tid);
    toast._tid = setTimeout(function () { t.classList.remove('is-visible'); }, 1800);
  }

  function shareUrl(kind) {
    var url = encodeURIComponent(window.location.href);
    var title = encodeURIComponent(document.title);
    switch (kind) {
      case 'twitter':  return 'https://twitter.com/intent/tweet?url=' + url + '&text=' + title;
      case 'facebook': return 'https://www.facebook.com/sharer/sharer.php?u=' + url;
      case 'linkedin': return 'https://www.linkedin.com/sharing/share-offsite/?url=' + url;
      default: return null;
    }
  }

  document.querySelectorAll('[data-share]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      var kind = btn.getAttribute('data-share');
      if (kind === 'copy') {
        e.preventDefault();
        var href = window.location.href;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(href).then(
            function () { toast('Link copied'); },
            function () { toast('Copy failed'); }
          );
        } else {
          // Fallback for older browsers
          try {
            var ta = document.createElement('textarea');
            ta.value = href;
            ta.setAttribute('readonly', '');
            ta.style.position = 'fixed';
            ta.style.top = '-9999px';
            document.body.appendChild(ta);
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            toast('Link copied');
          } catch (err) {
            toast('Copy failed');
          }
        }
        return;
      }
      var target = shareUrl(kind);
      if (!target) return;
      e.preventDefault();
      window.open(target, '_blank', 'noopener,noreferrer,width=620,height=520');
    });
  });
})();
