/* Czeal — Event tracking layer. <500B gz, no deps.
   Usage: czTrack('event_name', { key: value })
   Events are forwarded to GA4 via gtag(). */
(function () {
  'use strict';

  /**
   * Send a custom event to GA4.
   * @param {string} event - Semantic event name (snake_case).
   * @param {Object} [params] - Optional key/value payload.
   */
  function czTrack(event, params) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', event, params || {});
    }
  }

  // Expose globally
  window.czTrack = czTrack;

  // ---------- Automatic page-level tracking ----------

  // Track tool_opened when a tool page loads
  var toolPages = {
    'pomodoro': 'pomodoro_timer',
    'gpa-calculator': 'gpa_calculator'
  };

  var path = window.location.pathname;
  Object.keys(toolPages).forEach(function (slug) {
    if (path.indexOf(slug) !== -1) {
      czTrack('tool_opened', { tool_name: toolPages[slug] });
    }
  });

  // Track article_opened when an article page loads
  var articleSlugs = [
    'best-free-ai-tools-for-students',
    'best-ai-note-taking-apps',
    'ai-tools-for-homework',
    'best-ai-writing-tools-for-students',
    'best-chatgpt-prompts-for-students',
    'best-ai-productivity-apps-for-students',
    'free-ai-tools-for-online-learning',
    'best-ai-research-tools-for-students',
    'best-ai-study-apps',
    'how-students-use-ai-responsibly'
  ];

  articleSlugs.forEach(function (slug) {
    if (path.indexOf(slug) !== -1) {
      czTrack('article_opened', { article_slug: slug });
    }
  });

})();
