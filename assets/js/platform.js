/* Czeal — platform UI glue. Mobile nav. <500B gz. */
(function () {
  'use strict';

  function init() {
    var toggles = document.querySelectorAll('[data-mobile-nav-toggle]');
    toggles.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var id = btn.getAttribute('aria-controls');
        if (!id) return;
        var menu = document.getElementById(id);
        if (!menu) return;
        var isOpen = menu.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    });

    // Close the menu when a link inside it is clicked (e.g. hash link stays on page)
    document.querySelectorAll('.mobile-menu a').forEach(function (a) {
      a.addEventListener('click', function () {
        var menu = a.closest('.mobile-menu');
        if (!menu) return;
        menu.classList.remove('is-open');
        var ctl = document.querySelector('[aria-controls="' + menu.id + '"]');
        if (ctl) ctl.setAttribute('aria-expanded', 'false');
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
