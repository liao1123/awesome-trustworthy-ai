/* Trustworthy AI Paper Reader — card UI over window.READER_DATA.
 * State (stars, theme) persists in localStorage under the historical
 * "trustworthy-ai-paper-reader:" prefix so earlier reading state survives. */
(function () {
  "use strict";

  var STORAGE_PREFIX = "trustworthy-ai-paper-reader:";
  var PAGE = 40;

  var state = {
    view: "domains",
    pageId: "all",
    search: "",
    starredOnly: false,
    theme: "light",
    starred: {},
    rendered: 0,
    queue: [],
  };

  var data = window.READER_DATA || { papers: {}, views: { daily: [], domains: [], conferences: [] } };
  var papers = data.papers || {};

  var el = {
    viewTabs: document.getElementById("viewTabs"),
    navTree: document.getElementById("navTree"),
    cards: document.getElementById("cards"),
    scopeHeader: document.getElementById("scopeHeader"),
    searchBox: document.getElementById("searchBox"),
    starredToggle: document.getElementById("starredToggle"),
    themeToggle: document.getElementById("themeToggle"),
    emptyState: document.getElementById("emptyState"),
    sentinel: document.getElementById("sentinel"),
    backTop: document.getElementById("backTop"),
    statsNote: document.getElementById("statsNote"),
  };

  /* ---------- storage ---------- */

  function loadStore(name, fallback) {
    try {
      var raw = window.localStorage.getItem(STORAGE_PREFIX + name);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }
  function saveStore(name, value) {
    try { window.localStorage.setItem(STORAGE_PREFIX + name, JSON.stringify(value)); } catch (e) {}
  }

  /* ---------- helpers ---------- */

  function escapeHtml(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  function safeUrl(url) {
    return /^https?:\/\//.test(url) ? url : null;
  }
  function paperLink(paper) {
    var links = paper.links || [];
    for (var i = 0; i < links.length; i++) {
      if (links[i].type && links[i].type.toLowerCase() === "arxiv") return links[i].url;
    }
    return links.length ? links[0].url : "";
  }
  function haystack(paper) {
    if (!paper._hay) {
      paper._hay = [
        paper.title, (paper.authors || []).join(" "), (paper.keywords || []).join(" "),
        paper.venue || "", paper.motivation || "", paper.method || "", paper.conclusion || "",
      ].join(" ").toLowerCase();
    }
    return paper._hay;
  }
  function matches(paper) {
    if (state.starredOnly && !state.starred[paper.id]) return false;
    if (!state.search) return true;
    var tokens = state.search.toLowerCase().split(/\s+/);
    var hay = haystack(paper);
    for (var i = 0; i < tokens.length; i++) {
      if (tokens[i] && hay.indexOf(tokens[i]) === -1) return false;
    }
    return true;
  }

  /* ---------- scope resolution ---------- */

  function viewData(view) { return (data.views && data.views[view]) || []; }

  function pagesFor(view) {
    if (view === "daily") return viewData("daily");
    if (view === "conferences") return viewData("conferences");
    var leaves = [];
    viewData("domains").forEach(function (group) {
      (group.children || []).forEach(function (leaf) {
        leaf._group = group.title;
        leaves.push(leaf);
      });
    });
    return leaves;
  }

  function scopeSections() {
    var pages = pagesFor(state.view);
    if (state.pageId !== "all") {
      pages = pages.filter(function (p) { return p.id === state.pageId; });
    }
    var sections = [];
    pages.forEach(function (page) {
      (page.sections || []).forEach(function (section) {
        sections.push({ page: page, title: section.title, papers: section.papers });
      });
    });
    return sections;
  }

  /* ---------- nav ---------- */

  function renderNav() {
    var html = [];
    html.push('<button class="nav-item nav-root' + (state.pageId === "all" ? " active" : "") +
      '" data-page="all">全部' + (state.view === "daily" ? "日报" : state.view === "domains" ? "领域论文" : "会议论文") +
      ' <span class="nav-count">' + pagesFor(state.view).length + "</span></button>");
    if (state.view === "domains") {
      viewData("domains").forEach(function (group) {
        var gid = "navgrp-" + group.id;
        var activeInside = (group.children || []).some(function (leaf) { return leaf.id === state.pageId; });
        html.push('<div class="nav-group' + (activeInside ? " open" : "") + '">');
        html.push('<button class="nav-group-header" data-toggle="' + gid + '"' +
          (activeInside ? ' aria-expanded="true"' : "") + '><span class="chev">▸</span>' +
          escapeHtml(group.title) + '<span class="nav-count">' + (group.children || []).length + "</span></button>");
        html.push('<div class="nav-group-items" id="' + gid + '"' + (activeInside ? "" : " hidden") + ">");
        (group.children || []).forEach(function (leaf) {
          var count = (leaf.sections || []).reduce(function (n, s) { return n + s.papers.length; }, 0);
          html.push('<button class="nav-item' + (state.pageId === leaf.id ? " active" : "") +
            '" data-page="' + escapeHtml(leaf.id) + '">' + escapeHtml(leaf.title) +
            ' <span class="nav-count">' + count + "</span></button>");
        });
        html.push("</div></div>");
      });
    } else {
      // daily grouped by month, conferences grouped by year — both collapsible
      var groups = {};
      var order = [];
      pagesFor(state.view).forEach(function (page) {
        var g = state.view === "daily" ? String(page.date || page.id).slice(0, 7) : String(page.year || "");
        if (!groups[g]) { groups[g] = []; order.push(g); }
        groups[g].push(page);
      });
      order.sort().reverse().forEach(function (g) {
        var gid = "navgrp-" + state.view + "-" + g;
        var activeInside = groups[g].some(function (p) { return p.id === state.pageId; });
        html.push('<div class="nav-group' + (activeInside ? " open" : "") + '">');
        html.push('<button class="nav-group-header" data-toggle="' + escapeHtml(gid) + '"' +
          (activeInside ? ' aria-expanded="true"' : "") + '><span class="chev">▸</span>' +
          escapeHtml(g || "未知") + '<span class="nav-count">' + groups[g].length + "</span></button>");
        html.push('<div class="nav-group-items" id="' + escapeHtml(gid) + '"' + (activeInside ? "" : " hidden") + ">");
        groups[g].forEach(function (page) {
          var count = (page.sections || []).reduce(function (n, s) { return n + s.papers.length; }, 0);
          html.push('<button class="nav-item' + (state.pageId === page.id ? " active" : "") +
            '" data-page="' + escapeHtml(page.id) + '">' + escapeHtml(page.title) +
            ' <span class="nav-count">' + count + "</span></button>");
        });
        html.push("</div></div>");
      });
    }
    el.navTree.innerHTML = html.join("");
    Array.prototype.forEach.call(el.navTree.querySelectorAll("[data-page]"), function (btn) {
      btn.addEventListener("click", function () {
        state.pageId = btn.getAttribute("data-page");
        renderNav();
        render();
        window.scrollTo({ top: 0 });
      });
    });
    Array.prototype.forEach.call(el.navTree.querySelectorAll("[data-toggle]"), function (btn) {
      btn.addEventListener("click", function () {
        var items = document.getElementById(btn.getAttribute("data-toggle"));
        if (!items) return;
        var open = items.hasAttribute("hidden");
        if (open) {
          items.removeAttribute("hidden");
          btn.setAttribute("aria-expanded", "true");
          btn.closest(".nav-group").classList.add("open");
        } else {
          items.setAttribute("hidden", "");
          btn.setAttribute("aria-expanded", "false");
          btn.closest(".nav-group").classList.remove("open");
        }
      });
    });
  }

  /* ---------- cards ---------- */

  function badgeHtml(paper) {
    var html = [];
    var seen = {};
    (paper.links || []).forEach(function (link) {
      var url = safeUrl(link.url);
      if (!url || seen[link.type]) return;
      seen[link.type] = true;
      html.push('<a class="badge" href="' + escapeHtml(url) + '" target="_blank" rel="noopener">' +
        escapeHtml(link.type) + "</a>");
    });
    if (paper.date) html.push('<span class="badge badge-plain">📅 ' + escapeHtml(paper.date) + "</span>");
    if (paper.venue) html.push('<span class="badge badge-venue">🏷 ' + escapeHtml(paper.venue) + "</span>");
    return html.length ? '<div class="badges">' + html.join("") + "</div>" : "";
  }

  function cardHtml(paper) {
    var href = paperLink(paper);
    var titleHtml = href
      ? '<a class="card-title" href="' + escapeHtml(href) + '" target="_blank" rel="noopener">' + escapeHtml(paper.title) + "</a>"
      : '<span class="card-title">' + escapeHtml(paper.title) + "</span>";
    var kwHtml = (paper.keywords || []).map(function (kw) {
      return '<button class="keyword" data-kw="' + escapeHtml(kw) + '">' + escapeHtml(kw) + "</button>";
    }).join("");
    var authors = (paper.authors || []).join("、");
    var starred = !!state.starred[paper.id];
    var summary = "";
    if (paper.motivation) summary += '<div class="sum-row"><span class="sum-icon">🎯</span><b>研究动机</b><span>' + escapeHtml(paper.motivation) + "</span></div>";
    if (paper.method) summary += '<div class="sum-row"><span class="sum-icon">🔬</span><b>研究方法</b><span>' + escapeHtml(paper.method) + "</span></div>";
    if (paper.conclusion) summary += '<div class="sum-row"><span class="sum-icon">📌</span><b>结论</b><span>' + escapeHtml(paper.conclusion) + "</span></div>";
    var abstract = paper.abstract
      ? '<details class="abstract"><summary>▸ 展开完整英文摘要（Abstract）</summary><p>' + escapeHtml(paper.abstract) + "</p></details>"
      : "";
    return (
      '<article class="card' + (starred ? " starred" : "") + '" data-id="' + escapeHtml(paper.id) + '">' +
      '<div class="card-head">' + titleHtml +
      '<button class="star" title="收藏" aria-label="收藏">' + (starred ? "★" : "☆") + "</button></div>" +
      badgeHtml(paper) +
      (kwHtml ? '<div class="keywords">' + kwHtml + "</div>" : "") +
      (authors ? '<div class="authors">👤 ' + escapeHtml(authors) + "</div>" : "") +
      (summary ? '<div class="summary">' + summary + "</div>" : "") +
      abstract +
      "</article>"
    );
  }

  /* ---------- render ---------- */

  function render() {
    var sections = scopeSections();
    var scopeTitle = state.pageId === "all"
      ? (state.view === "daily" ? "全部日报" : state.view === "domains" ? "全部领域" : "全部会议")
      : (pagesFor(state.view).filter(function (p) { return p.id === state.pageId; })[0] || {}).title || state.pageId;

    state.queue = [];
    var total = 0;
    sections.forEach(function (section) {
      var kept = [];
      (section.papers || []).forEach(function (pid) {
        var paper = papers[pid];
        if (paper && matches(paper)) { kept.push(paper); total++; }
      });
      if (kept.length) state.queue.push({ title: section.title, page: section.page, papers: kept });
    });

    el.scopeHeader.innerHTML =
      '<h1>' + escapeHtml(scopeTitle || "") + "</h1>" +
      '<p class="scope-meta">' + total + " 篇" +
      (state.search ? " · 搜索 “" + escapeHtml(state.search) + "”" : "") +
      (state.starredOnly ? " · 只看收藏" : "") + "</p>";

    el.cards.innerHTML = "";
    state.rendered = 0;
    renderMore();
    el.emptyState.hidden = total > 0;
    if (el.statsNote) {
      el.statsNote.textContent = data.generated
        ? "收录 " + Object.keys(papers).length + " 篇 · 数据生成于 " + data.generated
        : "收录 " + Object.keys(papers).length + " 篇";
    }
  }

  function renderMore() {
    var html = [];
    var added = 0;
    outer:
    for (var s = 0; s < state.queue.length; s++) {
      var section = state.queue[s];
      if (section.done) continue;
      if (!section.opened) {
        html.push('<h2 class="section-title">' + escapeHtml(section.title) +
          '<span class="section-count">' + section.papers.length + "</span></h2>");
        section.opened = true;
      }
      while (section.cursor === undefined) section.cursor = 0;
      while (section.cursor < section.papers.length) {
        html.push(cardHtml(section.papers[section.cursor]));
        section.cursor++;
        added++;
        if (added >= PAGE) break outer;
      }
      section.done = true;
    }
    if (html.length) {
      var tmp = document.createElement("div");
      tmp.innerHTML = html.join("");
      while (tmp.firstChild) el.cards.appendChild(tmp.firstChild);
      state.rendered += added;
      bindCardEvents(el.cards);
    }
  }

  function bindCardEvents(root) {
    Array.prototype.forEach.call(root.querySelectorAll(".card:not([data-bound])"), function (card) {
      card.setAttribute("data-bound", "1");
      var star = card.querySelector(".star");
      if (star) star.addEventListener("click", function () {
        var id = card.getAttribute("data-id");
        if (state.starred[id]) delete state.starred[id]; else state.starred[id] = 1;
        saveStore("interested", state.starred);
        card.classList.toggle("starred", !!state.starred[id]);
        star.textContent = state.starred[id] ? "★" : "☆";
        if (state.starredOnly && !state.starred[id]) render();
      });
    });
    Array.prototype.forEach.call(root.querySelectorAll(".keyword:not([data-bound])"), function (pill) {
      pill.setAttribute("data-bound", "1");
      pill.addEventListener("click", function () {
        el.searchBox.value = pill.getAttribute("data-kw");
        state.search = el.searchBox.value;
        render();
      });
    });
  }

  /* ---------- events ---------- */

  el.viewTabs.addEventListener("click", function (event) {
    var btn = event.target.closest("[data-view]");
    if (!btn) return;
    state.view = btn.getAttribute("data-view");
    state.pageId = "all";
    Array.prototype.forEach.call(el.viewTabs.querySelectorAll("button"), function (b) {
      b.classList.toggle("active", b === btn);
    });
    renderNav();
    render();
  });

  var searchTimer = null;
  el.searchBox.addEventListener("input", function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
      state.search = el.searchBox.value.trim();
      render();
    }, 160);
  });

  el.starredToggle.addEventListener("click", function () {
    state.starredOnly = !state.starredOnly;
    el.starredToggle.classList.toggle("on", state.starredOnly);
    el.starredToggle.textContent = state.starredOnly ? "★ 只看收藏" : "☆ 只看收藏";
    render();
  });

  function setTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute("data-theme", theme);
    saveStore("theme", theme);
  }
  el.themeToggle.addEventListener("click", function () {
    setTheme(state.theme === "dark" ? "light" : "dark");
  });

  if (typeof IntersectionObserver === "function") {
    new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) renderMore();
    }, { rootMargin: "600px" }).observe(el.sentinel);
  } else {
    window.addEventListener("scroll", function () {
      if (window.innerHeight + window.scrollY > document.body.offsetHeight - 800) renderMore();
    });
  }

  window.addEventListener("scroll", function () {
    el.backTop.hidden = window.scrollY < 600;
  });
  el.backTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });

  /* ---------- boot ---------- */

  state.starred = loadStore("interested", {});
  state.theme = loadStore("theme", null) || (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  setTheme(state.theme);
  renderNav();
  render();
})();
