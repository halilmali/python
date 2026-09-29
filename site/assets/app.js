
(function () {
  "use strict";
  var body = document.body;

  /* ---------- safe storage (localStorage can be blocked on file:// or embedded) ---------- */
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- theme ---------- */
  var themeBtn = document.getElementById("themeBtn");
  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    store.set("p4-theme", t);
    if (themeBtn) themeBtn.textContent = t === "dark" ? "Light" : "Dark";
  }
  var saved = store.get("p4-theme");
  if (saved) applyTheme(saved);
  else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches)
    applyTheme("dark");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });

  /* ---------- mobile nav ---------- */
  var burger = document.getElementById("hamburger");
  if (burger) burger.addEventListener("click", function () {
    body.classList.toggle("nav-open");
  });

  /* ---------- checkpoints & progress ---------- */
  var ALL = window.P4_CHECKPOINTS || {};
  var ids = Object.keys(ALL);
  function checkedCount() {
    var n = 0;
    for (var i = 0; i < ids.length; i++)
      if (store.get("p4-ck-" + ids[i]) === "1") n++;
    return n;
  }
  function paintOverall() {
    var total = ids.length;
    var done = checkedCount();
    var pct = total ? Math.round(100 * done / total) : 0;
    document.querySelectorAll(".js-overall-fill").forEach(function (el) {
      el.style.width = pct + "%";
    });
    document.querySelectorAll(".js-overall-lbl").forEach(function (el) {
      el.textContent = done + " / " + total + " checkpoints (" + pct + "%)";
    });
  }
  var boxes = Array.prototype.slice.call(document.querySelectorAll("input[data-ckpt]"));
  boxes.forEach(function (box) {
    var id = box.getAttribute("data-ckpt");
    box.checked = store.get("p4-ck-" + id) === "1";
    box.addEventListener("change", function () {
      store.set("p4-ck-" + id, box.checked ? "1" : "0");
      paintOverall(); paintPage();
    });
  });
  function paintPage() {
    if (!boxes.length) {
      var w = document.querySelector(".progresswrap");
      if (w) w.style.display = "none";
      return;
    }
    var done = boxes.filter(function (b) { return b.checked; }).length;
    var pct = Math.round(100 * done / boxes.length);
    var fill = document.querySelector(".progresswrap .fill");
    var lbl = document.querySelector(".progresswrap .lbl");
    if (fill) fill.style.width = pct + "%";
    if (lbl) lbl.textContent = "Module checkpoints: " + done + " / " + boxes.length +
      " (" + pct + "%)";
  }
  paintOverall(); paintPage();

  /* ---------- copy buttons ---------- */
  function copyText(text, btn) {
    function done(ok) {
      var old = btn.textContent;
      btn.textContent = ok ? "Copied!" : "Select & copy";
      setTimeout(function () { btn.textContent = old; }, 1400);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { done(true); },
        function () { fallback(); });
    } else fallback();
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta); done(ok);
    }
  }
  document.querySelectorAll(".codeblock .copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var pre = btn.closest(".codeblock").querySelector("pre");
      copyText(pre.innerText, btn);
    });
  });

  /* ---------- search ---------- */
  var idx = window.P4_SEARCH || [];
  var input = document.getElementById("searchInput");
  var box = document.getElementById("searchResults");
  var items = [], sel = -1;
  function snippet(text, q) {
    var lower = text.toLowerCase(), qi = lower.indexOf(q);
    if (qi < 0) return text.slice(0, 90);
    var start = Math.max(0, qi - 34);
    return (start > 0 ? "\u2026" : "") + text.slice(start, qi + 60) + "\u2026";
  }
  function runSearch(q) {
    q = q.trim().toLowerCase();
    if (q.length < 2) { box.classList.remove("open"); box.innerHTML = ""; return; }
    var scored = [];
    for (var i = 0; i < idx.length; i++) {
      var it = idx[i];
      var t = it.t.toLowerCase(), x = it.x.toLowerCase();
      var score = -1;
      if (t.indexOf(q) === 0) score = 100;
      else if (t.indexOf(q) >= 0) score = 60;
      else {
        var count = 0, pos = 0;
        while ((pos = x.indexOf(q, pos)) >= 0 && count < 6) { count++; pos += q.length; }
        if (count) score = 10 + count;
      }
      if (score >= 0) scored.push({ s: score, t: it.t, u: it.u, x: it.x });
    }
    scored.sort(function (a, b) { return b.s - a.s; });
    var top = scored.slice(0, 12);
    if (!top.length) {
      box.innerHTML = '<div class="none">No results for "' +
        q.replace(/</g, "&lt;") + '"</div>';
    } else {
      box.innerHTML = top.map(function (r) {
        return '<a href="' + r.u + '"><div class="rt">' + r.t +
          '</div><div class="rs">' + snippet(r.x, q) + "</div></a>";
      }).join("");
    }
    box.classList.add("open"); sel = -1;
  }
  if (input && box) {
    input.addEventListener("input", function () { runSearch(input.value); });
    input.addEventListener("focus", function () { if (input.value.trim().length >= 2)
      box.classList.add("open"); });
    document.addEventListener("click", function (e) {
      if (!box.contains(e.target) && e.target !== input) box.classList.remove("open");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && document.activeElement !== input) {
        e.preventDefault(); input.focus();
      } else if (e.key === "Escape") { box.classList.remove("open"); input.blur(); }
      else if (box.classList.contains("open") && (e.key === "ArrowDown" || e.key === "ArrowUp")) {
        e.preventDefault();
        var links = box.querySelectorAll("a");
        if (!links.length) return;
        sel = e.key === "ArrowDown" ? Math.min(sel + 1, links.length - 1)
                                    : Math.max(sel - 1, 0);
        links.forEach(function (l) { l.classList.remove("sel"); });
        links[sel].classList.add("sel"); links[sel].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && sel >= 0) {
        var links2 = box.querySelectorAll("a");
        if (links2[sel]) links2[sel].click();
      }
    });
    // navigate on click then clear
    box.addEventListener("click", function () { box.classList.remove("open"); });
  }
})();
