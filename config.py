#!/usr/bin/env python3

config.load_autoconfig()

c.url.searchengines['goog'] = 'https://www.google.com/search?q={}'
c.url.searchengines['youtube'] = 'https://www.youtube.com/results?search_query={}'
c.url.searchengines['py'] = 'https://docs.python.org/3/search.html?q={}'
c.url.searchengines['cp'] = 'http://www.cplusplus.com/search.do?q={}'
c.url.searchengines['mpl'] = 'https://matplotlib.org/stable/search.html?q={}'
c.url.searchengines['sns'] = 'https://seaborn.pydata.org/search.html?q={}'
c.url.searchengines['sch'] = 'https://scholar.google.com/scholar?q={}'
c.url.searchengines['scholar'] = 'https://scholar.google.com/scholar?q={}'
c.url.searchengines['rs'] = 'https://www.rosettacommons.org/docs/wiki/search?q={}'
#c.url.searchengines['rs'] = 'https://www.rosettacommons.org/docs/latest/search?q={}'
c.url.searchengines['rdoc'] = 'https://guybrush.ucsf.edu/doxygen/main/search.html?query={}'
c.url.searchengines['pyr'] = 'https://graylab.jhu.edu/PyRosetta.documentation/search.html?q={}'
c.window.title_format = '{current_title} - {current_url} - qutebrowser'

c.aliases['zotero'] = 'spawn --userscript qute-zotero'
c.aliases['Zotero'] = 'hint links userscript zotero'

config.bind('o', 'set-cmd-text -s :open')
config.bind('O', 'set-cmd-text -s :open {url:pretty}')
config.bind('t', 'set-cmd-text -s :open -t')
config.bind('T', 'set-cmd-text -s :open -t -i {url:pretty}')
config.bind('zz', 'zotero')
config.bind('zf', 'Zotero')
config.bind('wa', 'open https://web.archive.org/web/{url}')
config.bind(';wa', 'hint links fill :open -t https://web.archive.org/web/{hint-url}')
config.bind(r'\sh', 'config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload')
config.bind(r'\Sh', 'config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload')
config.bind(r'\sH', 'config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload')
config.bind(r'\SH', 'config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload')
config.bind(r'\su', 'config-cycle -p -t -u {url} content.javascript.enabled ;; reload')
config.bind(r'\Su', 'config-cycle -p -u {url} content.javascript.enabled ;; reload')
config.bind('<Ctrl+j>', 'tab-next')
config.bind('<Ctrl+k>', 'tab-prev')
config.bind('<Ctrl+Shift+s>', 'set-cmd-text -s :spawn --userscript zotero')
config.bind('<Ctrl+Shift+p>', 'config-cycle content.proxy system socks://localhost:9050/')
config.bind('<Ctrl+l>', 'config-cycle tabs.show multiple never')
config.bind('<Ctrl+i>', 'mode-enter passthrough')
config.bind('<Ctrl+i>', 'mode-leave', mode='passthrough')
config.bind('<Ctrl+v>', 'insert-text {primary}', mode='insert')
config.bind('<Ctrl+v>', 'insert-text {primary}', mode='passthrough')
config.unbind('<Ctrl+v>')
