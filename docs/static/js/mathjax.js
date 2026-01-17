// Config MathJax
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  startup: {
    ready: () => {
      MathJax.startup.defaultReady();
      // Обработка MathJax при инициализации
      MathJax.startup.output.clearCache();
      MathJax.typesetClear();
      MathJax.texReset();
      MathJax.typesetPromise();
    }
  }
};

// Обработка при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
  if (window.MathJax && window.MathJax.typesetPromise) {
    // Небольшая задержка для гарантии рендеринга
    setTimeout(() => {
      MathJax.typesetPromise();
    }, 100);
  }
});

// Для SPA навигации (если используется)
document.addEventListener('navigation', () => {
  if (window.MathJax && window.MathJax.typesetPromise) {
    setTimeout(() => {
      MathJax.startup.output.clearCache();
      MathJax.typesetClear();
      MathJax.texReset();
      MathJax.typesetPromise();
    }, 100);
  }
});