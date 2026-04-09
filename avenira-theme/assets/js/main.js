/* ============================================
   AVENIRA AUTOMATIONS — Ghost Theme JS
   ============================================ */

(function () {
  'use strict';

  // --- Mobile Nav Toggle ---
  const navToggle = document.getElementById('nav-toggle');
  const navLinks = document.getElementById('nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);
      // Swap icon
      if (navToggle.querySelector('.icon-menu')) {
        navToggle.querySelector('.icon-menu').style.display = isOpen ? 'none' : 'block';
      }
      if (navToggle.querySelector('.icon-close')) {
        navToggle.querySelector('.icon-close').style.display = isOpen ? 'block' : 'none';
      }
    });

    // Close on link click
    navLinks.querySelectorAll('a:not(.lang-toggle)').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        if (navToggle.querySelector('.icon-menu')) navToggle.querySelector('.icon-menu').style.display = 'block';
        if (navToggle.querySelector('.icon-close')) navToggle.querySelector('.icon-close').style.display = 'none';
      });
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.focus();
        if (navToggle.querySelector('.icon-menu')) navToggle.querySelector('.icon-menu').style.display = 'block';
        if (navToggle.querySelector('.icon-close')) navToggle.querySelector('.icon-close').style.display = 'none';
      }
    });
  }

  // --- Cookie Consent (Loi 25) ---
  var cookieBanner = document.getElementById('cookie-banner');
  var cookieAccept = document.getElementById('cookie-accept');
  var cookieDecline = document.getElementById('cookie-decline');

  if (cookieBanner) {
    var consent = localStorage.getItem('avenira_cookie_consent');
    if (!consent) {
      cookieBanner.classList.add('show');
    }

    if (cookieAccept) {
      cookieAccept.addEventListener('click', function () {
        localStorage.setItem('avenira_cookie_consent', 'accepted');
        cookieBanner.classList.remove('show');
      });
    }

    if (cookieDecline) {
      cookieDecline.addEventListener('click', function () {
        localStorage.setItem('avenira_cookie_consent', 'declined');
        cookieBanner.classList.remove('show');
      });
    }
  }

  // --- Active nav indicator ---
  (function () {
    var path = window.location.pathname.replace(/\/$/, '') || '/';
    var links = document.querySelectorAll('.nav-links a:not(.lang-toggle)');
    links.forEach(function (link) {
      var href = link.getAttribute('href');
      if (!href) return;
      try {
        var linkPath = new URL(href, window.location.origin).pathname.replace(/\/$/, '') || '/';
        if (path === linkPath) {
          link.setAttribute('aria-current', 'page');
        }
      } catch (e) { /* ignore */ }
    });
  })();

  // --- Scroll header shadow ---
  var header = document.querySelector('.site-header');
  if (header) {
    var scrolled = false;
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10 && !scrolled) {
        header.style.boxShadow = '0 4px 24px rgba(0,0,0,0.3)';
        scrolled = true;
      } else if (window.scrollY <= 10 && scrolled) {
        header.style.boxShadow = 'none';
        scrolled = false;
      }
    }, { passive: true });
  }

})();
