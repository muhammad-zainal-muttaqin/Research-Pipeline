(() => {
  'use strict';

  const data = window.DATA;
  const meta = window.META;
  const byId = new Map(data.map(entry => [entry.id, entry]));
  const corpus = data.filter(entry => !entry.special);
  const documents = data.filter(entry => entry.special);
  const collections = new Map(meta.collections.map(collection => [collection.key, collection]));
  const years = Object.keys(meta.yearCounts).sort((a, b) => b - a);
  const themes = Object.keys(meta.themeCounts).sort((a, b) => a.localeCompare(b, 'id'));
  const discovery = window.createDiscovery(data);
  const pageSize = 16;
  const number = new Intl.NumberFormat('id-ID');
  const alphabetical = new Intl.Collator('id', { numeric: true, sensitivity: 'base' });
  const wideReader = matchMedia('(min-width: 960px)');
  const newer = (a, b) => (b.year || 0) - (a.year || 0) || alphabetical.compare(a.title, b.title);
  const sorting = {
    terbaru: ['Terbaru', newer],
    terlama: ['Terlama', (a, b) => (a.year || Infinity) - (b.year || Infinity) || alphabetical.compare(a.title, b.title)],
    judul: ['Judul A–Z', (a, b) => alphabetical.compare(a.title, b.title)],
    tema: ['Tema A–Z', (a, b) => alphabetical.compare(a.theme, b.theme) || newer(a, b)],
    nomor: ['Nomor entri', (a, b) => a.num - b.num],
    singkat: ['Durasi baca', (a, b) => a.words - b.words || newer(a, b)]
  };
  const papers = [
    { file: 'main7.pdf', name: 'Naskah tinjauan', detail: 'Cross-view identity in image-based fruit counting: A systematic review and a design space for class-wise inventories', lang: 'en' },
    { file: 'main7-supplementary.pdf', name: 'Bahan tambahan', detail: 'Strategi pencarian, kriteria pemilihan, cara pengodean, dan daftar periksa PRISMA 2020.' },
    { file: 'main6.pdf', name: 'Naskah pembanding', detail: 'Peta bukti dan kerangka identitas lintas pandang sebelum pendalaman sintesis.' },
    { file: 'main6-supplementary.pdf', name: 'Bahan tambahan naskah pembanding', detail: 'Metode dan lampiran peta bukti.' }
  ];
  const readingPaths = [
    ['Asosiasi lintas pandang', 'Geometri dan pelacakan untuk menautkan buah yang sama antarpandang.', ['stein2016image', 'liu2018robust', 'wang2019mango', 'genemola2020fruitb', 'zhou2024advancing', 'qi2025assessment']],
    ['Hitungan buah per pohon', 'Penghitungan buah di kebun, koreksi buah tersembunyi, dan kumpulan data tandan sawit.', ['hani2020comparative', 'anderson2021estimation', 'koirala2021attempting', 'indriani2026sawitmvc']],
    ['Perkembangan YOLO', 'Sepuluh kajian tentang pengembangan detektor objek YOLO.', ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']],
    ['Fondasi deteksi objek', 'Deteksi dua tahap, deteksi satu tahap, dan deteksi dengan transformer.', ['012', '014', '015', '016', '019', '022', '024', '025', '155']],
    ['Fusi warna dan kedalaman', 'Penggunaan data warna dan kedalaman untuk segmentasi dan deteksi.', ['035', '036', '042', '055', '058', '112', '113', '118']],
    ['Robotika dan geometri 3D', 'Estimasi pose, penggenggaman, pemetaan, dan deteksi 3D.', ['074', '082', '088', '107', '108', '117']]
  ];

  const icons = {
    book: '<path d="M12 6v14M12 6C9 4 6 4 3 5v14c3-1 6-1 9 1 3-2 6-2 9-1V5c-3-1-6-1-9 1Z"/><path d="M6 9c1-.2 2 0 3 .5M6 13c1-.2 2 0 3 .5m6-4c1-.5 2-.7 3-.5m-3 4.5c1-.5 2-.7 3-.5"/>',
    list: '<path d="M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01"/>',
    search: '<circle cx="10.8" cy="10.8" r="6.3"/><path d="m16 16 4 4"/>',
    close: '<path d="m6 6 12 12M18 6 6 18"/>',
    down: '<path d="m6 9 6 6 6-6"/>',
    jump: '<path d="M12 5v14m-5-5 5 5 5-5"/>',
    right: '<path d="M4.5 12h14m-5-5 5 5-5 5"/>',
    left: '<path d="M19.5 12h-14m5-5-5 5 5 5"/>',
    external: '<path d="M13 5h6v6m0-6-9 9M18 13v6H5V6h6"/>',
    filter: '<path d="M4 7h2.5m5 0H20M4 17h8.5m5 0H20"/><circle cx="9" cy="7" r="2.5"/><circle cx="15" cy="17" r="2.5"/>',
    file: '<path d="M6 3h8l4 4v14H6zM14 3v5h4M9 13h6m-6 4h6"/>',
    link: '<path d="m10 14 4-4m-5 6-1 1a3 3 0 0 1-4-4l4-4a3 3 0 0 1 4 0m0 6a3 3 0 0 0 4 0l4-4a3 3 0 0 0-4-4l-1 1"/>',
    copy: '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/>',
    moon: '<path d="M20 14A8.5 8.5 0 0 1 10 4a8.5 8.5 0 1 0 10 10Z"/>',
    sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2m0 15v2m-9.5-9.5h2m15 0h2M5.3 5.3l1.4 1.4m10.6 10.6 1.4 1.4m0-13.4-1.4 1.4M6.7 17.3l-1.4 1.4"/>',
    expand: '<path d="M8 4H4v4m12-4h4v4M4 16v4h4m12-4v4h-4"/>'
  };

  const chars = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
  const esc = value => String(value ?? '').replace(/[&<>"']/g, char => chars[char]);
  const icon = name => '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + icons[name] + '</svg>';
  const readTime = entry => Math.max(1, Math.round(entry.words / 200)) + ' menit baca';
  const paperUrl = file => 'manuscript/output/papers/' + file;
  const topic = entry => ({
    'Hitung Multi-Pengamatan': 'Hitung multi-pengamatan',
    'Hitung Satu Pandang': 'Hitung satu pandang',
    'Kelapa Sawit': 'Kelapa sawit',
    'Hitung per Kelas': 'Hitung per kelas',
    'Depth & Sensor 3D': 'Kedalaman dan sensor 3D',
    'Tinjauan Terdahulu': 'Tinjauan terdahulu',
    'Metode Luar Pertanian': 'Metode luar pertanian'
  }[entry.theme] || entry.theme);
  const collectionName = entry => collections.get(entry.koleksi)?.name || 'Dokumen riset';
  const labelOptions = (values, selected, any) => '<option value="">' + any + '</option>' +
    values.map(([value, label]) => '<option value="' + esc(value) + '"' +
      (value === selected ? ' selected' : '') + '>' + esc(label) + '</option>').join('');
  const linkOut = (url, label, css = 'button') => '<a class="' + css + '" href="' + esc(url) +
    '" target="_blank" rel="noopener noreferrer">' + esc(label) + icon('external') + '</a>';

  const app = document.getElementById('app');
  app.innerHTML = `
    <a class="skip-link" href="#konten" id="skip-link">Lewati ke isi</a>
    <header class="topbar">
      <div class="topbar-inner">
        <a class="brand" href="#/"><span class="brand-icon">${icon('book')}</span><span class="brand-name">Ruang Baca Riset</span></a>
        <nav class="topnav" aria-label="Navigasi utama">
          <a href="#/" id="nav-catalogue">Katalog</a>
          <a href="#/dokumen" id="nav-documents" aria-label="Dokumen riset">Dokumen<span class="nav-long"> riset</span></a>
        </nav>
        <div class="toolbar">
          <button class="icon-button" id="search-jump" type="button" aria-label="Cari kajian" aria-keyshortcuts="/">${icon('search')}</button>
          <button class="icon-button" id="theme-switch" type="button"></button>
        </div>
      </div>
      <div class="reading-progress" aria-hidden="true"><span></span></div>
    </header>
    <main id="konten" tabindex="-1"></main>
    <div class="toast" id="notice" role="status"></div>
    <dialog class="pdf-dialog" id="pdf-preview" aria-labelledby="preview-title">
      <div class="preview-top">
        <h2 id="preview-title"></h2>
        <div class="preview-actions">
          <a class="button" id="preview-link" target="_blank" rel="noopener noreferrer">Buka PDF${icon('external')}</a>
          <button class="icon-button" id="preview-expand" type="button" aria-label="Penuhi layar" aria-pressed="false">${icon('expand')}</button>
          <form method="dialog"><button class="icon-button" type="submit" aria-label="Tutup pratinjau" autofocus>${icon('close')}</button></form>
        </div>
      </div>
      <div class="preview-frame"></div>
    </dialog>
  `;

  const find = selector => app.querySelector(selector);
  const main = find('main');
  const preview = find('#pdf-preview');
  const themeSwitch = find('#theme-switch');
  const progress = find('.reading-progress span');
  const catalogueScroll = new Map();
  const markdown = new Map();
  let route;
  let ticket = 0;
  let searchTimer;
  let toastTimer;
  let focusSearch = false;
  let outlineHeadings = [];
  let scrollFrame;

  function loadPreference(key) {
    try { return localStorage.getItem(key); } catch { return null; }
  }

  function savePreference(key, value) {
    try { localStorage.setItem(key, value); } catch {}
  }

  function setTheme(theme, save = false) {
    document.documentElement.dataset.theme = theme;
    const dark = theme === 'dark';
    themeSwitch.innerHTML = icon(dark ? 'sun' : 'moon');
    themeSwitch.setAttribute('aria-label', dark ? 'Gunakan tema terang' : 'Gunakan tema gelap');
    themeSwitch.title = dark ? 'Tema terang' : 'Tema gelap';
    if (save) savePreference('rp-theme', theme);
  }

  function decode(text) {
    try { return decodeURIComponent(text); } catch { return text; }
  }

  function readRoute() {
    const [path, heading = ''] = location.hash.replace(/^#\/?/, '').split('#', 2);
    const [rawId = '', ...query] = path.split('?');
    const params = new URLSearchParams(query.join('?'));
    const collection = params.get('koleksi');
    const sort = params.get('urut');
    const page = Number(params.get('hal'));
    return {
      id: decode(rawId),
      heading: decode(heading),
      q: params.get('q')?.trim() || '',
      collection: collections.has(collection) ? collection : '',
      themes: [...new Set((params.get('tema') || '').split('|'))].filter(value => themes.includes(value)),
      year: years.includes(params.get('thn')) ? params.get('thn') : '',
      sort: Object.hasOwn(sorting, sort) ? sort : '',
      page: Number.isSafeInteger(page) && page > 0 ? page : 1
    };
  }

  function href(id = '', filters = {}, heading = '') {
    const params = new URLSearchParams();
    if (filters.q) params.set('q', filters.q);
    if (filters.collection) params.set('koleksi', filters.collection);
    if (filters.themes?.length) params.set('tema', filters.themes.join('|'));
    if (filters.year) params.set('thn', filters.year);
    if (filters.sort) params.set('urut', filters.sort);
    if (filters.page > 1) params.set('hal', filters.page);
    return '#/' + encodeURIComponent(id) + (params.size ? '?' + params : '') +
      (heading ? '#' + encodeURIComponent(heading) : '');
  }

  function filter(options, replace = false) {
    const q = find('#search-input').value.trim();
    const next = href('', { ...route, q, page: 1, ...options });
    if (next === location.hash) return;
    if (replace) {
      history.replaceState(null, '', next);
      route = readRoute();
      renderResults();
    } else {
      location.hash = next;
    }
  }

  function markedText(text, query) {
    const words = [...new Set(query.match(/[\p{L}\p{N}]{2,}/gu) || [])].sort((a, b) => b.length - a.length);
    if (!words.length) return esc(text);
    const parts = text.split(new RegExp('(' + words.join('|') + ')', 'giu'));
    return parts.map((part, index) => index % 2 ? '<mark>' + esc(part) + '</mark>' : esc(part)).join('');
  }

  function orderedEntries(filters) {
    const candidates = filters.q ? discovery.search(filters.q) : corpus;
    const matching = candidates.filter(entry =>
      (!filters.collection || entry.koleksi === filters.collection) &&
      (!filters.themes.length || filters.themes.includes(entry.theme)) &&
      (!filters.year || String(entry.year) === filters.year));
    const compare = sorting[filters.sort]?.[1] || (filters.q ? null : newer);
    return compare ? matching.sort(compare) : matching;
  }

  function filterChips() {
    const chips = [];
    if (route.collection) {
      chips.push([collections.get(route.collection).name, { collection: '' }]);
    }
    route.themes.forEach(value => {
      chips.push([topic({ theme: value }), { themes: route.themes.filter(item => item !== value) }]);
    });
    if (route.year) chips.push([route.year, { year: '' }]);
    return chips.map(([name, change]) =>
      '<a class="active-filter" href="' + esc(href('', { ...route, page: 1, ...change })) +
      '" aria-label="' + esc('Hapus filter ' + name) + '">' + esc(name) + icon('close') + '</a>'
    ).join('');
  }

  function resultCard(entry, position) {
    const title = markedText(entry.title, route.q);
    const authors = entry.authors || [];
    const byline = authors.slice(0, 2).join(' · ') + (authors.length > 2 ? ' dan ' + number.format(authors.length - 2) + ' lainnya' : '');
    return '<article class="result-card"><span class="result-index" aria-hidden="true">' +
      number.format(position).padStart(2, '0') + '</span><div class="result-content">' +
      '<h3><a href="' + esc(href(entry.id, route)) + '">' + title + '</a></h3>' +
      '<div class="result-meta"><span class="topic-label' + (entry.koleksi === 'deteksi' ? ' detection' : '') + '">' + esc(topic(entry)) + '</span>' +
      (entry.year ? '<span>' + entry.year + '</span>' : '') + '</div>' +
      (byline ? '<p class="result-byline">' + markedText(byline, route.q) + '</p>' : '') +
      (entry.summary || entry.desc ? '<p class="result-summary">' + markedText(entry.summary || entry.desc, route.q) + '</p>' : '') +
      '</div><span class="result-arrow" aria-hidden="true">' + icon('right') + '</span></article>';
  }

  function renderResults() {
    const list = orderedEntries(route);
    const pageCount = Math.max(1, Math.ceil(list.length / pageSize));
    const page = Math.min(route.page, pageCount);
    const start = (page - 1) * pageSize;
    const end = Math.min(list.length, start + pageSize);
    const activeFilter = !!(route.collection || route.themes.length || route.year);
    const termField = find('#search-input');
    if (termField.value.trim() !== route.q) termField.value = route.q;
    find('#clear-search').hidden = !termField.value;
    find('.search-key').hidden = !!termField.value;
    find('#filter-reset').hidden = !activeFilter;
    find('#filter-count').textContent = activeFilter ? ' (' + (route.themes.length + Boolean(route.collection) + Boolean(route.year)) + ')' : '';
    app.querySelectorAll('[data-collection]').forEach(input => { input.checked = input.value === route.collection; });
    const availableThemes = collections.get(route.collection)?.themes || themes;
    const topicNames = [...new Set([...availableThemes, ...route.themes])]
      .sort((a, b) => alphabetical.compare(topic({ theme: a }), topic({ theme: b })))
      .map(value => [value, topic({ theme: value })]);
    if (route.themes.length > 1) topicNames.unshift([route.themes.join('|'), route.themes.length + ' tema dipilih']);
    find('#topic-filter').innerHTML = labelOptions(topicNames, route.themes.join('|'), 'Semua tema');
    find('#year-filter').value = route.year;
    find('#sort-order option[value=""]').disabled = !route.q;
    find('#sort-order').value = route.sort || (route.q ? '' : 'terbaru');
    find('#applied-filters').innerHTML = filterChips();
    find('#results-count').textContent = number.format(list.length) + (route.q ? ' hasil' : ' kajian');
    find('#results-range').textContent = start || end < list.length ?
      'Menampilkan ' + number.format(start + 1) + '–' + number.format(end) : '';
    find('#result-list').innerHTML = list.length ? list.slice(start, end).map((entry, i) => resultCard(entry, start + i + 1)).join('') :
      '<div class="empty-results"><h3>Hasil tidak ditemukan</h3><p>Coba kata kunci lain atau ubah filter.</p>' +
      '<a class="button" href="#/">Lihat semua kajian</a></div>';
    find('#pagination').hidden = pageCount <= 1;
    const pageLink = (pageNumber, content, label, css = '', current = false) =>
      '<a href="' + esc(href('', { ...route, page: pageNumber })) + '" aria-label="' + esc(label) + '"' +
      (current ? ' aria-current="page"' : '') + ' class="' + css + '">' + content + '</a>';
    const pageNumbers = [...new Set([1, page - 1, page, page + 1, pageCount])]
      .filter(value => value >= 1 && value <= pageCount).sort((a, b) => a - b);
    find('#pagination').innerHTML = pageCount <= 1 ? '' :
      (page > 1 ? pageLink(page - 1, icon('left'), 'Halaman sebelumnya', 'page-step') : '') +
      pageNumbers.map((value, index) =>
        (index && value - pageNumbers[index - 1] > 1 ? '<span aria-hidden="true">…</span>' : '') +
        pageLink(value, number.format(value), 'Halaman ' + number.format(value), '', value === page)
      ).join('') + (page < pageCount ? pageLink(page + 1, icon('right'), 'Halaman berikutnya', 'page-step') : '');
  }

  function viewCatalogue() {
    const last = byId.get(loadPreference('rp-last'));
    const resume = last && !last.special ? '<a class="resume-link" href="' + esc(href(last.id)) +
      '" title="' + esc(last.title) + '" aria-label="' + esc('Lanjutkan membaca: ' + last.title) + '">' +
      icon('book') + 'Lanjutkan<span class="resume-long"> membaca</span></a>' : '';
    main.innerHTML = `
      <section class="catalogue-head" aria-labelledby="catalogue-title">
        <div class="catalogue-intro page-width">
          <div class="catalogue-name">
            <h1 id="catalogue-title">Katalog kajian</h1>
            <p>Penghitungan buah, deteksi objek, dan sensor kedalaman.</p>
          </div>
          <div class="catalogue-search">
            <form id="search-form" class="search-form" role="search">
              ${icon('search')}
              <label class="sr-only" for="search-input">Cari judul, penulis, topik, atau DOI</label>
              <input type="search" id="search-input" placeholder="Judul, penulis, topik, atau DOI" autocomplete="off" enterkeyhint="search">
              <kbd class="search-key" aria-hidden="true">/</kbd>
              <button class="icon-button" id="clear-search" type="button" aria-label="Hapus kata kunci" hidden>${icon('close')}</button>
            </form>
            <div class="search-extras">
              <nav class="suggestions" aria-label="Contoh pencarian">
                <span>Coba:</span>
                ${['Kelapa sawit', 'YOLO', 'Pelacakan video'].map(query => '<a href="' + href('', { q: query }) + '">' + query + '</a>').join('')}
              </nav>
              ${resume}
            </div>
          </div>
        </div>
      </section>
      <div class="catalogue-grid page-width" id="katalog">
        <div class="results-bar">
          <div><h2 id="results-title" tabindex="-1"><span id="results-count" aria-live="polite"></span></h2><p id="results-range"></p></div>
          <div class="result-controls">
            <button id="filter-toggle" class="button" type="button" aria-expanded="false" aria-controls="filter-panel">
              ${icon('filter')}<span>Filter<span id="filter-count"></span></span>
            </button>
            <label class="sort-control" for="sort-order"><span>Urutkan</span><select id="sort-order">
              <option value="">Relevansi</option>
              ${Object.entries(sorting).map(([value, [label]]) => '<option value="' + value + '">' + label + '</option>').join('')}
            </select></label>
          </div>
        </div>
        <aside class="filters" id="filter-panel" aria-labelledby="filter-title">
          <div class="filter-heading">
            <h2 id="filter-title">Saring kajian</h2>
            <button id="filter-reset" class="quiet-link" type="button" aria-label="Hapus filter" hidden>Hapus</button>
          </div>
          <div id="filter-fields">
            <fieldset class="collection-options">
              <legend>Koleksi</legend>
              ${[['', 'Semua koleksi', meta.total], ...meta.collections.map(item => [item.key, item.name, item.total])].map(([key, name, total]) =>
                '<label class="collection-option"><input type="radio" name="collection" data-collection value="' + esc(key) + '">' +
                '<span>' + esc(name) + '</span><span class="collection-count">' + number.format(total) + '</span></label>'
              ).join('')}
            </fieldset>
            <label class="filter-select" for="topic-filter">Tema<select id="topic-filter"></select></label>
            <label class="filter-select" for="year-filter">Tahun<select id="year-filter">${labelOptions(years.map(year => [year, year]), route.year, 'Semua tahun')}</select></label>
          </div>
        </aside>
        <section class="results" aria-labelledby="results-title">
          <div id="applied-filters" class="active-filters" aria-label="Filter aktif"></div>
          <div id="result-list" class="result-list"></div>
          <nav class="pagination" id="pagination" aria-label="Halaman hasil pencarian"></nav>
        </section>
      </div>
    `;

    const search = find('#search-input');
    function updateQuery() {
      clearTimeout(searchTimer);
      find('#clear-search').hidden = !search.value;
      find('.search-key').hidden = !!search.value;
      filter({ q: search.value.trim() }, true);
    }
    search.addEventListener('input', () => {
      find('#clear-search').hidden = !search.value;
      find('.search-key').hidden = !!search.value;
      clearTimeout(searchTimer);
      searchTimer = setTimeout(updateQuery, 110);
    });
    find('#search-form').addEventListener('submit', event => {
      event.preventDefault();
      updateQuery();
      find('#katalog').scrollIntoView();
      find('#results-title').focus({ preventScroll: true });
    });
    find('#clear-search').addEventListener('click', () => {
      search.value = '';
      updateQuery();
      search.focus();
    });
    find('#filter-fields').addEventListener('change', event => {
      const input = event.target;
      if (input.matches('[data-collection]')) {
        const collection = input.value;
        filter({ collection, themes: route.themes.filter(theme => !collection || collections.get(collection).themes.includes(theme)) });
      } else if (input.id === 'topic-filter') {
        filter({ themes: input.value ? input.value.split('|') : [] });
      } else if (input.id === 'year-filter') {
        filter({ year: input.value });
      }
    });
    find('#filter-toggle').addEventListener('click', event => {
      const button = event.currentTarget;
      const expanded = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!expanded));
      find('.filters').classList.toggle('is-open', !expanded);
    });
    find('#filter-reset').addEventListener('click', () => {
      filter({ collection: '', themes: [], year: '' });
      const toggle = find('#filter-toggle');
      (toggle.getClientRects().length ? toggle : find('#topic-filter')).focus();
    });
    find('#sort-order').addEventListener('change', event => filter({ sort: event.target.value }));
    renderResults();
  }

  function relatedCards(related) {
    if (!related.length) return '';
    return '<section class="reader-related" id="kajian-terkait" aria-labelledby="related-title">' +
      '<h2 id="related-title">Kajian terkait</h2><div class="related-list">' +
      related.map(({ entry, reason }) => '<article class="related-card"><div>' +
        '<h3><a href="' + esc(href(entry.id, route)) + '">' + esc(entry.title) + '</a></h3>' +
        '<p>' + esc(reason) + '</p><span>' + esc(topic(entry)) + ' · ' + entry.year + '</span></div>' +
        '<span class="result-arrow">' + icon('right') + '</span></article>'
      ).join('') + '</div></section>';
  }

  function neighbours(entry) {
    if (entry.special) return '';
    const list = orderedEntries(route);
    const index = list.indexOf(entry);
    if (index < 0) return '';
    const adjacent = (next, label, direction) => next ? '<a href="' + esc(href(next.id, route)) + '">' +
      '<span>' + icon(direction) + esc(label) + '</span>' + esc(next.title) + '</a>' : '';
    const previous = adjacent(list[index - 1], 'Sebelumnya', 'left');
    const next = adjacent(list[index + 1], 'Berikutnya', 'right');
    return previous || next ? '<nav class="adjacent" aria-label="Kajian dalam hasil katalog">' + previous + next + '</nav>' : '';
  }

  function authorLinks(authors) {
    if (!authors?.length) return '';
    const link = name => '<a href="' + esc(href('', { q: name })) + '" title="' + esc('Cari kajian oleh ' + name) + '">' + esc(name) + '</a>';
    return '<div class="reader-authors">' + link(authors[0]) +
      (authors.length > 1 ? '<details class="more-authors"><summary>' +
        number.format(authors.length - 1) + ' penulis lain' + icon('down') +
        '</summary><ul class="author-panel">' + authors.slice(1).map(name => '<li>' + link(name) + '</li>').join('') + '</ul></details>' : '') +
      '</div>';
  }

  function viewReader(entry) {
    const related = entry.special ? [] : discovery.related(entry, 6);
    const sourceUrl = entry.sourceUrl || (entry.doi ? 'https://doi.org/' + encodeURI(entry.doi) : '');
    const returnTo = entry.special && !route.q ? href('dokumen') : href('', route);
    const returnLabel = entry.special && !route.q ? 'Kembali ke dokumen riset' : route.q ? 'Kembali ke hasil pencarian' : 'Kembali ke katalog';
    const collection = entry.special
      ? '<a href="#/dokumen">Dokumen riset</a>'
      : '<a href="' + esc(href('', { collection: entry.koleksi })) + '">' + esc(collectionName(entry)) + '</a>';
    const theme = entry.special ? '' : '<a class="topic-label" href="' +
      esc(href('', { collection: entry.koleksi, themes: [entry.theme] })) + '">' + esc(topic(entry)) + '</a>';
    const copyLink = new URL(href(entry.id), location.href).href;
    main.innerHTML = `
      <div class="reader page-width">
        <div class="reader-grid">
          <header class="reader-header">
            <a class="back-link" href="${esc(returnTo)}">${icon('left')}${returnLabel}</a>
            <h1>${esc(entry.title)}</h1>
            <div class="reader-byline">
              ${authorLinks(entry.authors)}
              ${theme ? '<div class="reader-meta"><span>' + esc(entry.year) + '</span>' + theme + '</div>' : ''}
            </div>
          </header>
          <aside class="reader-side" aria-label="Navigasi bacaan">
            <details class="outline" ${wideReader.matches ? 'open' : ''}>
              <summary>${icon('list')}Daftar isi${icon('down')}</summary>
              <nav id="outline-links" class="reader-panel" aria-label="Bagian kajian">
                <p class="outline-status">Memuat daftar isi…</p>
              </nav>
            </details>
            ${related.length ? '<a class="related-jump" href="' + esc(href(entry.id, route, 'kajian-terkait')) + '">Kajian terkait <span>' + number.format(related.length) + '</span>' + icon('jump') + '</a>' : ''}
            <details class="reader-source">
              <summary>${icon('file')}Sumber${icon('down')}</summary>
              <div class="reader-panel source-panel">
                <div class="source-meta">${collection}${entry.venue ? '<p>' + esc(entry.venue) + '</p>' : ''}<p>${readTime(entry)}</p></div>
                <div class="reader-actions">
                  ${entry.pdf ? linkOut(entry.pdf, 'Buka PDF', 'button primary') : ''}
                  ${sourceUrl ? linkOut(sourceUrl, 'Sumber asli', entry.pdf ? 'button' : 'button primary') : ''}
                  ${entry.source ? linkOut(entry.source, 'Buka berkas sumber') : ''}
                  <button class="button" type="button" data-copy="${esc(copyLink)}" data-copy-label="Tautan">${icon('link')}Salin tautan</button>
                  ${entry.bib ? '<button class="button" type="button" data-copy="' + esc(entry.bib) + '" data-copy-label="Kunci BibTeX" title="' + esc(entry.bib) + '">' + icon('copy') + 'Salin kunci BibTeX</button>' : ''}
                </div>
              </div>
            </details>
          </aside>
          <div class="reader-content">
            <article id="article" class="article" aria-label="Isi bacaan" aria-busy="true"></article>
            ${relatedCards(related)}
            ${neighbours(entry)}
          </div>
        </div>
      </div>
    `;
    if (!entry.special) savePreference('rp-last', entry.id);
    showArticle(entry, ticket);
  }

  function headingId(text) {
    return text.toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu, '')
      .trim().replace(/\s+/g, '-').replace(/-+/g, '-') || 'bagian';
  }

  function enhanceArticle(article, entry) {
    let move = false;
    for (const node of Array.from(article.children)) {
      if (node.tagName === 'H2') move = ['Metadata Ringkas', 'Tautan Akses'].includes(node.textContent.trim());
      if (move) article.append(node);
    }

    for (const table of article.querySelectorAll('table')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'table-wrap';
      wrapper.tabIndex = 0;
      wrapper.setAttribute('role', 'region');
      wrapper.setAttribute('aria-label', 'Tabel yang dapat digulir');
      table.before(wrapper);
      wrapper.append(table);
    }
    for (const anchor of article.querySelectorAll('a[href]')) {
      const target = anchor.getAttribute('href');
      if (target.startsWith('#/')) continue;
      if (target.startsWith('#')) {
        anchor.href = href(entry.id, route, decode(target.slice(1)));
        continue;
      }
      const relative = !/^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(target);
      if (relative) {
        const file = decode(target.split(/[?#]/, 1)[0]);
        const legacy = file.match(/(?:^|\/)(\d{3})\s-\s.*\.md$/i);
        const key = file.split('/').pop().replace(/\.md$/i, '');
        if (/(?:^|\/)withheld\//i.test(file)) {
          anchor.replaceWith(document.createTextNode(anchor.textContent));
          continue;
        }
        const knownId = legacy?.[1] || (/\.md$/i.test(file) ? key : '');
        if (knownId && byId.has(knownId)) {
          anchor.href = href(knownId, route, decode(target.split('#')[1] || ''));
          continue;
        }
      }
      try {
        const base = entry.lazy ? new URL(entry.lazy, location.href) : location.href;
        const resolved = new URL(target, base);
        if (!['https:', 'http:', 'file:', 'mailto:'].includes(resolved.protocol)) throw new Error('Protokol tautan');
        anchor.href = resolved.href;
        anchor.target = '_blank';
        anchor.rel = 'noopener noreferrer';
      } catch {
        anchor.replaceWith(document.createTextNode(anchor.textContent));
      }
    }

    const used = new Set();
    const headings = [];
    for (const heading of article.querySelectorAll('h2, h3, h4, h5, h6')) {
      const text = heading.textContent.trim();
      const base = headingId(text);
      let id = base;
      for (let duplicate = 2; used.has(id); duplicate++) id = base + '-' + duplicate;
      used.add(id);
      heading.id = id;
      const link = document.createElement('a');
      link.className = 'heading-link';
      link.href = href(entry.id, route, id);
      link.innerHTML = icon('link');
      link.setAttribute('aria-label', 'Tautan ke ' + text);
      heading.append(link);
      if (heading.tagName === 'H2') headings.push({ id, text, heading });
    }
    return headings;
  }

  function sourceText(article, entry) {
    if (!entry.src && !entry.srcLazy) return;
    const detail = document.createElement('details');
    detail.className = 'source-text';
    detail.id = 'teks-sumber';
    detail.innerHTML = '<summary>Teks lengkap dari PDF' + icon('down') + '</summary><div></div>';
    const body = detail.lastElementChild;
    detail.addEventListener('toggle', async () => {
      if (!detail.open || detail.dataset.state === 'loading' || detail.dataset.state === 'ready') return;
      detail.dataset.state = 'loading';
      body.textContent = 'Memuat teks sumber…';
      try {
        let text = entry.src;
        if (!text) {
          if (location.protocol === 'file:') throw new Error('Berkas lokal');
          const response = await fetch(entry.srcLazy);
          if (!response.ok) throw new Error(String(response.status));
          text = await response.text();
        }
        const pre = document.createElement('pre');
        pre.tabIndex = 0;
        pre.textContent = text;
        body.replaceChildren(pre);
        detail.dataset.state = 'ready';
      } catch {
        body.innerHTML = '<p>Teks sumber belum dapat dimuat. ' + linkOut(entry.srcLazy, 'Buka berkas teks', 'text-link') + '</p>';
        detail.dataset.state = 'failed';
      }
      if (detail.isConnected) updateReading();
    });
    article.append(detail);
  }

  async function showArticle(entry, version) {
    const article = find('#article');
    article.setAttribute('aria-busy', 'true');
    const overview = entry.ov ? '## Gambaran Umum\n\n' + entry.ov : '';
    function render(text) {
      article.innerHTML = window.marked.parse(text);
      outlineHeadings = enhanceArticle(article, entry);
    }
    let md = entry.md;
    let fallback = false;
    if (entry.lazy) {
      if (overview) render(overview);
      else article.innerHTML = '<p class="loading" role="status">Memuat ringkasan…</p>';
      try {
        if (location.protocol === 'file:') throw new Error('Berkas lokal');
        if (!markdown.has(entry.id)) {
          const pending = fetch(entry.lazy).then(response => {
            if (!response.ok) throw new Error(String(response.status));
            return response.text();
          }).catch(error => {
            markdown.delete(entry.id);
            throw error;
          });
          markdown.set(entry.id, pending);
        }
        md = (await markdown.get(entry.id)).replace(/^\s*#\s+[^\r\n]*\r?\n/, '');
      } catch {
        md = overview;
        fallback = true;
      }
    }
    if (version !== ticket) return;
    render(md || '');
    article.removeAttribute('aria-busy');
    if (fallback) {
      const notice = document.createElement('div');
      notice.className = 'article-notice';
      notice.innerHTML = '<p>Ringkasan lengkap belum dapat dimuat.</p>' + linkOut(entry.lazy, 'Buka berkas ringkasan') +
        (location.protocol !== 'file:' ? '<button type="button" class="button">Coba lagi</button>' : '');
      notice.querySelector('button')?.addEventListener('click', () => showArticle(entry, version));
      article.append(notice);
    }
    sourceText(article, entry);
    const nav = find('#outline-links');
    const outline = find('.outline');
    nav.innerHTML = outlineHeadings.map(({ id, text }) =>
      '<a href="' + esc(href(entry.id, route, id)) + '" data-heading="' + esc(id) + '">' + esc(text) + '</a>'
    ).join('');
    outline.hidden = !outlineHeadings.length;
    if (entry.src || entry.srcLazy) {
      nav.insertAdjacentHTML('beforeend', '<a href="' + esc(href(entry.id, route, 'teks-sumber')) + '">Teks sumber</a>');
      outline.hidden = false;
    }
    scrollToSection(route.heading);
    updateReading();
  }

  function viewDocuments() {
    main.innerHTML = `
      <div class="documents page-width">
        <header class="document-header">
          <h1>Dokumen riset</h1>
          <nav aria-label="Bagian dokumen riset">
            <a href="#/dokumen#naskah">Naskah dan bahan tambahan</a>
            <a href="#/dokumen#dokumen-pendukung">Dokumen pendukung</a>
            <a href="#/dokumen#jalur-baca">Jalur baca</a>
          </nav>
        </header>
        <section class="document-section" id="naskah" aria-labelledby="paper-title">
          <h2 id="paper-title">Naskah dan bahan tambahan</h2>
          <div class="paper-grid">${papers.map((paper, index) => `
            <article class="paper-card">
              <span class="paper-icon">${icon('file')}</span><div><h3>${esc(paper.name)}</h3>
              <p${paper.lang ? ' lang="' + paper.lang + '"' : ''}>${esc(paper.detail)}</p></div>
              <div class="paper-actions">
                ${linkOut(paperUrl(paper.file), 'Buka PDF', 'button primary')}
                <button class="button" type="button" data-preview="${index}" aria-label="${esc('Pratinjau ' + paper.name.toLowerCase())}">Pratinjau</button>
              </div>
            </article>`).join('')}</div>
        </section>
        <section class="document-section" id="dokumen-pendukung" aria-labelledby="other-documents-title">
          <h2 id="other-documents-title">Dokumen pendukung</h2>
          <div class="document-list">${documents.map(entry => '<a href="' + esc(href(entry.id)) + '">' +
            '<span class="paper-icon">' + icon('file') + '</span><span><span class="document-name">' + esc(entry.title) + '</span>' +
            '<span class="document-detail">' + esc(entry.desc) + '</span></span>' + icon('right') + '</a>').join('')}</div>
        </section>
        <section class="document-section paths" id="jalur-baca" aria-labelledby="path-title">
          <h2 id="path-title">Jalur baca</h2>
          ${readingPaths.map(([title, description, ids]) => {
            const entries = ids.map(id => byId.get(id)).filter(Boolean);
            return '<details class="reading-path"><summary><span><span class="path-title">' + esc(title) + '</span>' +
              '<span class="path-detail">' + esc(description) + '</span></span><span class="path-count">' +
              number.format(entries.length) + ' kajian</span>' + icon('down') + '</summary><ol>' +
              entries.map(entry => '<li><a href="' + esc(href(entry.id)) + '">' + esc(entry.title) + '</a></li>').join('') +
              '</ol></details>';
          }).join('')}
        </section>
      </div>
    `;
  }

  function readerDisclosures() {
    return [...main.querySelectorAll('.reader-side details[open], .more-authors[open]')]
      .filter(detail => !wideReader.matches || !detail.matches('.outline'));
  }

  function closeReaderDisclosures(except) {
    for (const detail of readerDisclosures()) {
      if (detail !== except) detail.open = false;
    }
  }

  function scrollToSection(id, focus = false) {
    if (!id) return;
    const target = document.getElementById(id);
    if (!target || !main.contains(target)) return;
    closeReaderDisclosures();
    if (target.tagName === 'DETAILS') target.open = true;
    target.scrollIntoView();
    if (focus) {
      const heading = target.matches('h2, h3, h4, h5, h6, summary') ? target : target.querySelector('h2, summary');
      if (heading) {
        if (heading.tagName !== 'SUMMARY') heading.tabIndex = -1;
        heading.focus({ preventScroll: true });
      }
    }
  }

  function updateReading() {
    if (!byId.has(route?.id)) return;
    const scrollable = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = 'scaleX(' + (scrollable > 0 ? Math.min(1, Math.max(0, scrollY / scrollable)) : 0) + ')';
    let active = outlineHeadings[0]?.id;
    const line = find('.topbar').offsetHeight + (wideReader.matches ? 0 : find('.reader-side').offsetHeight) + 27;
    for (const heading of outlineHeadings) {
      if (heading.heading.getBoundingClientRect().top > line) break;
      active = heading.id;
    }
    find('#outline-links')?.querySelectorAll('[data-heading]').forEach(anchor => {
      if (anchor.dataset.heading === active) anchor.setAttribute('aria-current', 'location');
      else anchor.removeAttribute('aria-current');
    });
  }

  function applyRoute(initial = false) {
    clearTimeout(searchTimer);
    const previous = route;
    const next = readRoute();
    const entry = byId.get(next.id);
    const sameScreen = previous?.id === next.id && (!entry || href(entry.id, previous) === href(entry.id, next));
    if (previous && !previous.id) catalogueScroll.set(href('', previous), scrollY);
    route = next;
    if (sameScreen) {
      if (!next.id) {
        renderResults();
        if (previous.page !== next.page) {
          find('#katalog').scrollIntoView();
          find('#results-title').focus({ preventScroll: true });
        }
      }
      scrollToSection(next.heading, true);
      return;
    }

    ticket++;
    if (preview.open) preview.close();
    outlineHeadings = [];
    progress.style.transform = 'scaleX(0)';
    app.dataset.view = !route.id ? 'catalogue' : entry ? 'reader' : 'documents';
    find('#search-jump').hidden = !route.id;
    for (const [selector, active] of [['#nav-catalogue', !route.id || (entry && !entry.special)], ['#nav-documents', route.id === 'dokumen' || entry?.special]]) {
      const nav = find(selector);
      if (active) nav.setAttribute('aria-current', 'page');
      else nav.removeAttribute('aria-current');
    }
    if (!route.id) viewCatalogue();
    else if (entry) viewReader(entry);
    else if (route.id === 'dokumen') viewDocuments();
    else main.innerHTML = '<div class="page-width not-found"><h1>Halaman tidak ditemukan</h1>' +
      '<p>Periksa alamat atau cari kajian di katalog.</p><a class="button primary" href="#/">Kembali ke katalog</a></div>';

    const title = entry?.title || (route.id === 'dokumen' ? 'Dokumen riset' : route.id ? 'Halaman tidak ditemukan' : 'Katalog kajian');
    document.title = title + ' · Ruang Baca Riset';
    if (!route.id && focusSearch) {
      focusSearch = false;
      window.scrollTo(0, 0);
      find('#search-input').focus();
      find('#search-input').select();
    } else {
      window.scrollTo(0, !route.id ? catalogueScroll.get(href('', route)) || 0 : 0);
      if (!initial) {
        const returnLink = !route.id && previous?.id && find('#result-list a[href="' + CSS.escape(href(previous.id, route)) + '"]');
        (returnLink || main).focus({ preventScroll: true });
      }
      scrollToSection(route.heading);
    }
    updateReading();
  }

  async function copyText(value) {
    try {
      await navigator.clipboard.writeText(value);
      return true;
    } catch {
      const textarea = document.createElement('textarea');
      const previous = document.activeElement;
      textarea.value = value;
      textarea.className = 'sr-only';
      document.body.append(textarea);
      textarea.select();
      const copied = document.execCommand('copy');
      textarea.remove();
      previous?.focus();
      return copied;
    }
  }

  function openSearch() {
    if (preview.open) return;
    if (!route.id) {
      find('#search-input').focus();
      find('#search-input').select();
    } else {
      focusSearch = true;
      location.hash = href('', route);
    }
  }

  main.addEventListener('click', async event => {
    const anchor = event.target.closest('a[href]');
    if (anchor?.getAttribute('href') === location.hash && route.heading &&
        !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey) {
      event.preventDefault();
      scrollToSection(route.heading, true);
    }
    const copy = event.target.closest('[data-copy]');
    if (copy) {
      const copied = await copyText(copy.dataset.copy);
      const notice = find('#notice');
      clearTimeout(toastTimer);
      notice.textContent = copy.dataset.copyLabel + (copied ? ' tersalin.' : ' belum dapat disalin.');
      notice.classList.add('visible');
      toastTimer = setTimeout(() => notice.classList.remove('visible'), 2500);
    }
    const button = event.target.closest('[data-preview]');
    if (button) {
      const paper = papers[Number(button.dataset.preview)];
      const url = paperUrl(paper.file);
      find('#preview-title').textContent = paper.name;
      find('#preview-link').href = url;
      const frame = document.createElement('iframe');
      frame.src = url;
      frame.title = paper.name;
      find('.preview-frame').replaceChildren(frame);
      preview.showModal();
    }
  });

  main.addEventListener('toggle', event => {
    const detail = event.target;
    if (detail.open && detail.matches('.outline, .reader-source, .more-authors')) closeReaderDisclosures(detail);
  }, true);

  document.addEventListener('click', event => {
    if (byId.has(route?.id)) closeReaderDisclosures(event.target.closest('.outline, .reader-source, .more-authors'));
  });

  preview.addEventListener('close', () => {
    find('.preview-frame').replaceChildren();
    preview.classList.remove('expanded');
    find('#preview-expand').setAttribute('aria-pressed', 'false');
    find('#preview-expand').setAttribute('aria-label', 'Penuhi layar');
  });
  find('#preview-expand').addEventListener('click', event => {
    const expanded = preview.classList.toggle('expanded');
    event.currentTarget.setAttribute('aria-pressed', String(expanded));
    event.currentTarget.setAttribute('aria-label', expanded ? 'Kecilkan pratinjau' : 'Penuhi layar');
  });
  find('#skip-link').addEventListener('click', event => {
    event.preventDefault();
    main.focus();
  });
  find('#search-jump').addEventListener('click', openSearch);
  themeSwitch.addEventListener('click', () => {
    setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark', true);
  });
  wideReader.addEventListener('change', event => {
    const outline = find('.outline');
    if (outline) outline.open = event.matches;
  });
  document.addEventListener('keydown', event => {
    const typing = event.target.matches('input, textarea, select, [contenteditable]');
    if (!preview.open && (event.key === '/' && !typing || (event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k')) {
      event.preventDefault();
      openSearch();
    }
    if (event.key === 'Escape') {
      if (event.target.id === 'search-input' && event.target.value) find('#clear-search').click();
      const menu = readerDisclosures()[0];
      if (menu) {
        closeReaderDisclosures();
        menu.querySelector('summary').focus();
      }
    }
  });
  window.addEventListener('scroll', () => {
    if (!byId.has(route?.id) || scrollFrame) return;
    scrollFrame = requestAnimationFrame(() => {
      scrollFrame = 0;
      updateReading();
    });
  }, { passive: true });
  window.addEventListener('hashchange', () => applyRoute());
  history.scrollRestoration = 'manual';
  const preferred = loadPreference('rp-theme');
  setTheme(preferred === 'light' || preferred === 'dark' ? preferred :
    matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  applyRoute(true);
})();
