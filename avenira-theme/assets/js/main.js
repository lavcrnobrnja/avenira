/* ============================================
   AVENIRA AUTOMATIONS — Ghost Theme JS
   ============================================ */

(function () {
  'use strict';

  // --- Mobile Nav Toggle (new glass-pill structure) ---
  // The collapsing wrapper is .nav-center; the ul inside is .nav-links (id=nav-links).
  var navToggle = document.getElementById('nav-toggle');
  var navLinks = document.getElementById('nav-links');
  var navCenter = navLinks ? navLinks.closest('.nav-center') : null;

  function closeMenu() {
    if (navCenter) navCenter.classList.remove('open');
    if (navLinks) navLinks.classList.remove('open');
    if (navToggle) {
      navToggle.setAttribute('aria-expanded', 'false');
      var menuIcon = navToggle.querySelector('.icon-menu');
      var closeIcon = navToggle.querySelector('.icon-close');
      if (menuIcon) menuIcon.style.display = 'block';
      if (closeIcon) closeIcon.style.display = 'none';
    }
  }

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var target = navCenter || navLinks;
      var isOpen = target.classList.toggle('open');
      // Keep a class on .nav-links too for backward-compat.
      if (navLinks !== target) {
        if (isOpen) navLinks.classList.add('open');
        else navLinks.classList.remove('open');
      }
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      var menuIcon = navToggle.querySelector('.icon-menu');
      var closeIcon = navToggle.querySelector('.icon-close');
      if (menuIcon) menuIcon.style.display = isOpen ? 'none' : 'block';
      if (closeIcon) closeIcon.style.display = isOpen ? 'block' : 'none';
    });

    // Close on link click (except lang-toggle which navigates away anyway)
    navLinks.querySelectorAll('a:not(.lang-toggle)').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && ((navCenter && navCenter.classList.contains('open')) || navLinks.classList.contains('open'))) {
        closeMenu();
        navToggle.focus();
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
  // Works against both the old .nav-links and the new .nav-pill (same id=nav-links container).
  (function () {
    var path = window.location.pathname.replace(/\/$/, '') || '/';
    var links = document.querySelectorAll('#nav-links a:not(.lang-toggle)');
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
