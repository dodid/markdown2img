import markdown as md
import requests
import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title='Markdown文章编辑和图片生成器,小红书,微信公众号,抖音,快手,微博', layout='wide')

html_begin = '''
<!DOCTYPE html>
<html lang="en" class="__variable_20951f __variable_bbf4d0 light" style="color-scheme: light;">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>HTML Document with Math Formulas</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dom-to-image/2.6.0/dom-to-image.min.js" integrity="sha512-01CJ9/g7e8cUmY0DFTMcUw/ikS799FHiOA0eyHsUWfOetgbx/t6oV4otQ5zXKQyIrQGTHSmRVPIgrgLcZi/WMA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
window.MathJax = {
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process',
    renderActions: {
      find: [10, function (doc) {
        for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
          const display = !!node.type.match(/; *mode=display/);
          const math = new doc.options.MathItem(node.textContent, doc.inputJax[0], display);
          const text = document.createTextNode('');
          const sibling = node.previousElementSibling;
          node.parentNode.replaceChild(text, node);
          math.start = {node: text, delim: '', n: 0};
          math.end = {node: text, delim: '', n: 0};
          doc.math.push(math);
          if (sibling && sibling.matches('.MathJax_Preview')) {
            sibling.parentNode.removeChild(sibling);
          }
        }
      }, '']
    }
  }
};
</script>
<link rel="preload" as="font" href="/app/static/2aaf0723e720e8b9-s.p.woff2" crossorigin="" type="font/woff2">
<link rel="preload" as="font" href="/app/static/8e992d4bd80b0720-s.p.woff2" crossorigin="" type="font/woff2">
<style>
.radix-themes[data-is-root-theme=true] {
  position: relative;
  z-index: 0
}

.rt-reset-a {
  text-decoration: none;
  color: inherit;
  outline: none
}

.rt-reset-button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-color: transparent;
  border: none;
  font-size: inherit;
  font-family: inherit;
  line-height: inherit;
  letter-spacing: inherit;
  outline: none;
  color: inherit;
  padding: 0;
  margin: 0;
  text-align: initial;
  -webkit-tap-highlight-color: transparent
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 300;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Semilight"), local("Segoe UI")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 300;
  font-style: italic;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Semilight Italic"), local("Segoe UI Italic")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 400;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 400;
  font-style: italic;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Italic")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 500;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Semibold"), local("Segoe UI")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 500;
  font-style: italic;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Semibold Italic"), local("Segoe UI Italic")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 700;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Bold")
}

@font-face {
  font-family: "Segoe UI (Custom)";
  font-weight: 700;
  font-style: italic;
  size-adjust: 103%;
  descent-override: 35%;
  ascent-override: 105%;
  src: local("Segoe UI Bold Italic")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 300;
  descent-override: 35%;
  src: local("Open Sans Light"), local("Open Sans Regular")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 300;
  font-style: italic;
  descent-override: 35%;
  src: local("Open Sans Light Italic"), local("Open Sans Italic")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 400;
  descent-override: 35%;
  src: local("Open Sans Regular")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 400;
  font-style: italic;
  descent-override: 35%;
  src: local("Open Sans Italic")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 500;
  descent-override: 35%;
  src: local("Open Sans Medium"), local("Open Sans Regular")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 500;
  font-style: italic;
  descent-override: 35%;
  src: local("Open Sans Medium Italic"), local("Open Sans Italic")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 700;
  descent-override: 35%;
  src: local("Open Sans Bold")
}

@font-face {
  font-family: "Open Sans (Custom)";
  font-weight: 700;
  font-style: italic;
  descent-override: 35%;
  src: local("Open Sans Bold Italic")
}

@font-face {
  font-family: "Consolas (Custom)";
  font-weight: 400;
  size-adjust: 110%;
  ascent-override: 85%;
  descent-override: 22%;
  src: local("Consolas")
}

@font-face {
  font-family: "Consolas (Custom)";
  font-weight: 400;
  font-style: italic;
  size-adjust: 110%;
  ascent-override: 85%;
  descent-override: 22%;
  src: local("Consolas Italic")
}

@font-face {
  font-family: "Consolas (Custom)";
  font-weight: 700;
  size-adjust: 110%;
  ascent-override: 85%;
  descent-override: 22%;
  src: local("Consolas Bold")
}

@font-face {
  font-family: "Consolas (Custom)";
  font-weight: 700;
  font-style: italic;
  size-adjust: 110%;
  ascent-override: 85%;
  descent-override: 22%;
  src: local("Consolas Bold Italic")
}

.radix-themes {
  --font-size-1: calc(12px * var(--scaling));
  --font-size-2: calc(14px * var(--scaling));
  --font-size-3: calc(16px * var(--scaling));
  --font-size-4: calc(18px * var(--scaling));
  --font-size-5: calc(20px * var(--scaling));
  --font-size-6: calc(24px * var(--scaling));
  --font-size-7: calc(28px * var(--scaling));
  --font-size-8: calc(35px * var(--scaling));
  --font-size-9: calc(60px * var(--scaling));
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  --line-height-1: calc(16px * var(--scaling));
  --line-height-2: calc(20px * var(--scaling));
  --line-height-3: calc(24px * var(--scaling));
  --line-height-4: calc(26px * var(--scaling));
  --line-height-5: calc(28px * var(--scaling));
  --line-height-6: calc(30px * var(--scaling));
  --line-height-7: calc(36px * var(--scaling));
  --line-height-8: calc(40px * var(--scaling));
  --line-height-9: calc(60px * var(--scaling));
  --letter-spacing-1: 0.0025em;
  --letter-spacing-2: 0em;
  --letter-spacing-3: 0em;
  --letter-spacing-4: -0.0025em;
  --letter-spacing-5: -0.005em;
  --letter-spacing-6: -0.00625em;
  --letter-spacing-7: -0.0075em;
  --letter-spacing-8: -0.01em;
  --letter-spacing-9: -0.025em;
  --default-font-family: -apple-system, BlinkMacSystemFont, "Segoe UI (Custom)", Roboto, "Helvetica Neue", "Open Sans (Custom)", system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  --default-font-size: var(--font-size-3);
  --default-font-style: normal;
  --default-font-weight: var(--font-weight-regular);
  --default-line-height: 1.5;
  --default-letter-spacing: 0em;
  --default-leading-trim-start: 0.42em;
  --default-leading-trim-end: 0.36em;
  --heading-font-family: var(--default-font-family);
  --heading-font-size-adjust: 1;
  --heading-font-style: normal;
  --heading-leading-trim-start: var(--default-leading-trim-start);
  --heading-leading-trim-end: var(--default-leading-trim-end);
  --heading-letter-spacing: 0em;
  --heading-line-height-1: calc(16px * var(--scaling));
  --heading-line-height-2: calc(18px * var(--scaling));
  --heading-line-height-3: calc(22px * var(--scaling));
  --heading-line-height-4: calc(24px * var(--scaling));
  --heading-line-height-5: calc(26px * var(--scaling));
  --heading-line-height-6: calc(30px * var(--scaling));
  --heading-line-height-7: calc(36px * var(--scaling));
  --heading-line-height-8: calc(40px * var(--scaling));
  --heading-line-height-9: calc(60px * var(--scaling));
  --code-font-family: "Menlo", "Consolas (Custom)", "Bitstream Vera Sans Mono", monospace, "Apple Color Emoji", "Segoe UI Emoji";
  --code-font-size-adjust: 0.95;
  --code-font-style: normal;
  --code-font-weight: inherit;
  --code-letter-spacing: -0.007em;
  --strong-font-family: var(--default-font-family);
  --strong-font-size-adjust: 1;
  --strong-font-style: inherit;
  --strong-font-weight: var(--font-weight-bold);
  --strong-letter-spacing: 0em;
  --em-font-family: "Times New Roman", "Times", serif;
  --em-font-size-adjust: 1.18;
  --em-font-style: italic;
  --em-font-weight: inherit;
  --em-letter-spacing: -0.025em;
  --quote-font-family: "Times New Roman", "Times", serif;
  --quote-font-size-adjust: 1.18;
  --quote-font-style: italic;
  --quote-font-weight: inherit;
  --quote-letter-spacing: -0.025em;
  overflow-wrap: break-word;
  font-family: var(--default-font-family);
  font-size: var(--default-font-size);
  font-weight: var(--default-font-weight);
  font-style: var(--default-font-style);
  line-height: var(--default-line-height);
  letter-spacing: var(--default-letter-spacing);
  -webkit-text-size-adjust: none;
  -moz-text-size-adjust: none;
  text-size-adjust: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale
}

.light,
.light-theme,
:root {
  --tomato-1: #fffcfc;
  --tomato-2: #fff8f7;
  --tomato-3: #fff0ee;
  --tomato-4: #ffe6e2;
  --tomato-5: #fdd8d3;
  --tomato-6: #fac7be;
  --tomato-7: #f3b0a2;
  --tomato-8: #ea9280;
  --tomato-9: #e54d2e;
  --tomato-10: #d84224;
  --tomato-11: #c33113;
  --tomato-12: #5c271f
}

.dark,
.dark-theme {
  --tomato-1: #1d1412;
  --tomato-2: #291612;
  --tomato-3: #3b1a14;
  --tomato-4: #471d16;
  --tomato-5: #532017;
  --tomato-6: #652318;
  --tomato-7: #862919;
  --tomato-8: #ca3416;
  --tomato-9: #e54d2e;
  --tomato-10: #f46e53;
  --tomato-11: #ff8870;
  --tomato-12: #fbd3cb
}

.light,
.light-theme,
:root {
  --tomato-a1: rgba(255, 5, 5, .012);
  --tomato-a2: rgba(255, 38, 5, .032);
  --tomato-a3: rgba(255, 31, 1, .067);
  --tomato-a4: rgba(255, 34, 1, .114);
  --tomato-a5: rgba(244, 29, 1, .173);
  --tomato-a6: rgba(236, 35, 0, .255);
  --tomato-a7: rgba(222, 37, 0, .365);
  --tomato-a8: rgba(213, 36, 1, .499);
  --tomato-a9: rgba(223, 37, 0, .82);
  --tomato-a10: rgba(210, 35, 0, .859);
  --tomato-a11: rgba(190, 32, 0, .926);
  --tomato-a12: rgba(70, 9, 0, .879)
}

.dark,
.dark-theme {
  --tomato-a1: rgba(251, 0, 0, .022);
  --tomato-a2: rgba(254, 0, 0, .074);
  --tomato-a3: rgba(254, 38, 0, .152);
  --tomato-a4: rgba(254, 50, 14, .204);
  --tomato-a5: rgba(254, 55, 20, .256);
  --tomato-a6: rgba(255, 59, 24, .334);
  --tomato-a7: rgba(255, 60, 26, .477);
  --tomato-a8: rgba(255, 60, 22, .771);
  --tomato-a9: rgba(255, 83, 49, .888);
  --tomato-a10: rgba(255, 114, 86, .953);
  --tomato-a11: #ff8870;
  --tomato-a12: rgba(255, 214, 206, .983)
}

.light,
.light-theme,
:root {
  --red-1: #fffcfc;
  --red-2: #fff7f7;
  --red-3: #ffefef;
  --red-4: #ffe5e5;
  --red-5: #fdd8d8;
  --red-6: #f9c6c6;
  --red-7: #f3aeaf;
  --red-8: #eb9091;
  --red-9: #e5484d;
  --red-10: #d93d42;
  --red-11: #c62a2f;
  --red-12: #641723
}

.dark,
.dark-theme {
  --red-1: #1f1315;
  --red-2: #291618;
  --red-3: #3b191d;
  --red-4: #481a20;
  --red-5: #551c22;
  --red-6: #691d25;
  --red-7: #8c1d28;
  --red-8: #d21e24;
  --red-9: #e5484d;
  --red-10: #f26669;
  --red-11: #ff8589;
  --red-12: #ffd1d9
}

.light,
.light-theme,
:root {
  --red-a1: rgba(255, 5, 5, .012);
  --red-a2: rgba(255, 5, 5, .032);
  --red-a3: rgba(255, 1, 1, .063);
  --red-a4: rgba(255, 0, 0, .102);
  --red-a5: rgba(242, 0, 0, .153);
  --red-a6: rgba(228, 1, 1, .224);
  --red-a7: rgba(217, 0, 4, .318);
  --red-a8: rgba(209, 0, 4, .436);
  --red-a9: rgba(219, 0, 7, .718);
  --red-a10: rgba(205, 0, 7, .761);
  --red-a11: rgba(187, 0, 6, .836);
  --red-a12: rgba(85, 0, 13, .91)
}

.dark,
.dark-theme {
  --red-a1: rgba(250, 0, 0, .031);
  --red-a2: rgba(254, 0, 25, .074);
  --red-a3: rgba(254, 31, 57, .152);
  --red-a4: rgba(255, 33, 63, .208);
  --red-a5: rgba(254, 39, 61, .265);
  --red-a6: rgba(255, 38, 60, .351);
  --red-a7: rgba(255, 34, 56, .503);
  --red-a8: rgba(255, 31, 39, .806);
  --red-a9: rgba(255, 78, 84, .888);
  --red-a10: rgba(255, 107, 109, .944);
  --red-a11: #ff8589;
  --red-a12: #ffd1d9
}

.light,
.light-theme,
:root {
  --crimson-1: #fffcfd;
  --crimson-2: #fff7fb;
  --crimson-3: #feeff6;
  --crimson-4: #fce5f0;
  --crimson-5: #f9d8e7;
  --crimson-6: #f4c6db;
  --crimson-7: #edadc8;
  --crimson-8: #e58fb1;
  --crimson-9: #e93d82;
  --crimson-10: #dc3175;
  --crimson-11: #cb1d63;
  --crimson-12: #621639
}

.dark,
.dark-theme {
  --crimson-1: #1d1418;
  --crimson-2: #29151d;
  --crimson-3: #391826;
  --crimson-4: #441a2b;
  --crimson-5: #511c31;
  --crimson-6: #641e3a;
  --crimson-7: #881f49;
  --crimson-8: #cf1761;
  --crimson-9: #e93d82;
  --crimson-10: #f46396;
  --crimson-11: #ff85ab;
  --crimson-12: #fdd3e8
}

.light,
.light-theme,
:root {
  --crimson-a1: rgba(255, 5, 88, .012);
  --crimson-a2: rgba(255, 5, 130, .032);
  --crimson-a3: rgba(239, 1, 112, .063);
  --crimson-a4: rgba(226, 0, 109, .102);
  --crimson-a5: rgba(216, 0, 97, .153);
  --crimson-a6: rgba(206, 1, 93, .224);
  --crimson-a7: rgba(199, 0, 83, .322);
  --crimson-a8: rgba(196, 0, 79, .44);
  --crimson-a9: rgba(226, 0, 90, .761);
  --crimson-a10: rgba(212, 0, 85, .808);
  --crimson-a11: rgba(196, 0, 79, .887);
  --crimson-a12: rgba(83, 0, 39, .914)
}

.dark,
.dark-theme {
  --crimson-a1: rgba(251, 0, 25, .022);
  --crimson-a2: rgba(254, 0, 93, .074);
  --crimson-a3: rgba(255, 24, 120, .143);
  --crimson-a4: rgba(254, 34, 122, .191);
  --crimson-a5: rgba(255, 40, 126, .247);
  --crimson-a6: rgba(254, 42, 127, .33);
  --crimson-a7: rgba(255, 38, 125, .485);
  --crimson-a8: rgba(255, 23, 116, .793);
  --crimson-a9: rgba(255, 65, 141, .905);
  --crimson-a10: rgba(255, 103, 156, .953);
  --crimson-a11: #ff85ac;
  --crimson-a12: rgba(255, 212, 234, .992)
}

.light,
.light-theme,
:root {
  --pink-1: #fffcfe;
  --pink-2: #fff7fc;
  --pink-3: #feeef8;
  --pink-4: #fce5f3;
  --pink-5: #f9d8ec;
  --pink-6: #f3c6e2;
  --pink-7: #ecadd4;
  --pink-8: #e38ec3;
  --pink-9: #d6409f;
  --pink-10: #cd3093;
  --pink-11: #c41c87;
  --pink-12: #651249
}

.dark,
.dark-theme {
  --pink-1: #1f121b;
  --pink-2: #291523;
  --pink-3: #37192e;
  --pink-4: #411c35;
  --pink-5: #4b1f3d;
  --pink-6: #5d224a;
  --pink-7: #7c2860;
  --pink-8: #bc2f88;
  --pink-9: #d6409f;
  --pink-10: #e45eaf;
  --pink-11: #f986c9;
  --pink-12: #fdd1ea
}

.light,
.light-theme,
:root {
  --pink-a1: rgba(255, 5, 172, .012);
  --pink-a2: rgba(255, 5, 159, .032);
  --pink-a3: rgba(240, 1, 148, .067);
  --pink-a4: rgba(226, 0, 139, .102);
  --pink-a5: rgba(216, 0, 129, .153);
  --pink-a6: rgba(201, 1, 124, .224);
  --pink-a7: rgba(196, 0, 121, .322);
  --pink-a8: rgba(192, 0, 118, .444);
  --pink-a9: rgba(200, 0, 127, .75);
  --pink-a10: rgba(193, 0, 122, .812);
  --pink-a11: rgba(189, 0, 120, .891);
  --pink-a12: rgba(90, 0, 60, .93)
}

.dark,
.dark-theme {
  --pink-a1: rgba(250, 0, 121, .031);
  --pink-a2: rgba(254, 0, 174, .074);
  --pink-a3: rgba(254, 31, 187, .135);
  --pink-a4: rgba(254, 47, 189, .178);
  --pink-a5: rgba(255, 56, 192, .221);
  --pink-a6: rgba(255, 57, 192, .299);
  --pink-a7: rgba(255, 61, 190, .433);
  --pink-a8: rgba(255, 57, 182, .71);
  --pink-a9: rgba(255, 73, 188, .823);
  --pink-a10: rgba(255, 103, 194, .884);
  --pink-a11: rgba(255, 137, 206, .975);
  --pink-a12: rgba(255, 210, 236, .992)
}

.light,
.light-theme,
:root {
  --plum-1: #fefcff;
  --plum-2: #fff8ff;
  --plum-3: #fceffc;
  --plum-4: #f9e5f9;
  --plum-5: #f3d9f4;
  --plum-6: #ebc8ed;
  --plum-7: #dfafe3;
  --plum-8: #cf91d8;
  --plum-9: #ab4aba;
  --plum-10: #a43cb4;
  --plum-11: #9c2bad;
  --plum-12: #53195d
}

.dark,
.dark-theme {
  --plum-1: #1d131d;
  --plum-2: #261526;
  --plum-3: #341b34;
  --plum-4: #3d1f3e;
  --plum-5: #462348;
  --plum-6: #542957;
  --plum-7: #6e3473;
  --plum-8: #9e49ab;
  --plum-9: #ab4aba;
  --plum-10: #be66cd;
  --plum-11: #dc8eeb;
  --plum-12: #f4d4f4
}

.light,
.light-theme,
:root {
  --plum-a1: rgba(172, 5, 255, .012);
  --plum-a2: rgba(255, 5, 255, .028);
  --plum-a3: rgba(208, 1, 208, .063);
  --plum-a4: rgba(196, 0, 196, .102);
  --plum-a5: rgba(175, 2, 181, .15);
  --plum-a6: rgba(163, 0, 172, .216);
  --plum-a7: rgba(152, 0, 166, .314);
  --plum-a8: rgba(143, 0, 165, .432);
  --plum-a9: rgba(137, 0, 158, .71);
  --plum-a10: rgba(136, 0, 157, .765);
  --plum-a11: rgba(136, 0, 156, .832);
  --plum-a12: rgba(64, 0, 75, .902)
}

.dark,
.dark-theme {
  --plum-a1: rgba(251, 0, 251, .022);
  --plum-a2: rgba(253, 0, 253, .061);
  --plum-a3: rgba(254, 48, 254, .122);
  --plum-a4: rgba(248, 66, 254, .165);
  --plum-a5: rgba(246, 77, 255, .208);
  --plum-a6: rgba(244, 86, 255, .273);
  --plum-a7: rgba(242, 95, 255, .394);
  --plum-a8: rgba(234, 101, 255, .637);
  --plum-a9: rgba(233, 95, 255, .702);
  --plum-a10: rgba(235, 124, 255, .784);
  --plum-a11: rgba(238, 153, 255, .914);
  --plum-a12: rgba(255, 221, 255, .953)
}

.light,
.light-theme,
:root {
  --purple-1: #fefcfe;
  --purple-2: #fdfaff;
  --purple-3: #f9f1fe;
  --purple-4: #f3e7fc;
  --purple-5: #eddbf9;
  --purple-6: #e3ccf4;
  --purple-7: #d3b4ed;
  --purple-8: #be93e4;
  --purple-9: #8e4ec6;
  --purple-10: #8445bc;
  --purple-11: #793aaf;
  --purple-12: #402060
}

.dark,
.dark-theme {
  --purple-1: #1b141d;
  --purple-2: #231528;
  --purple-3: #311c3a;
  --purple-4: #3a2046;
  --purple-5: #422451;
  --purple-6: #4d2a61;
  --purple-7: #61357e;
  --purple-8: #8349b6;
  --purple-9: #8e4ec6;
  --purple-10: #9e63d5;
  --purple-11: #c794f9;
  --purple-12: #ecd9fa
}

.light,
.light-theme,
:root {
  --purple-a1: rgba(171, 5, 171, .012);
  --purple-a2: rgba(155, 5, 255, .02);
  --purple-a3: rgba(146, 0, 237, .055);
  --purple-a4: rgba(128, 2, 224, .095);
  --purple-a5: rgba(128, 1, 213, .142);
  --purple-a6: rgba(117, 0, 200, .2);
  --purple-a7: rgba(107, 1, 194, .295);
  --purple-a8: rgba(102, 0, 191, .424);
  --purple-a9: rgba(92, 0, 173, .695);
  --purple-a10: rgba(87, 0, 163, .73);
  --purple-a11: rgba(81, 0, 151, .773);
  --purple-a12: rgba(37, 0, 73, .875)
}

.dark,
.dark-theme {
  --purple-a1: rgba(159, 0, 251, .022);
  --purple-a2: rgba(181, 0, 252, .07);
  --purple-a3: rgba(193, 51, 254, .148);
  --purple-a4: rgba(194, 64, 254, .2);
  --purple-a5: rgba(194, 73, 255, .247);
  --purple-a6: rgba(191, 81, 254, .317);
  --purple-a7: rgba(189, 89, 255, .442);
  --purple-a8: rgba(181, 96, 255, .684);
  --purple-a9: rgba(180, 96, 255, .754);
  --purple-a10: rgba(187, 115, 255, .819);
  --purple-a11: rgba(203, 151, 255, .975);
  --purple-a12: rgba(241, 221, 255, .979)
}

.light,
.light-theme,
:root {
  --violet-1: #fdfcfe;
  --violet-2: #fbfaff;
  --violet-3: #f5f2ff;
  --violet-4: #ede9fe;
  --violet-5: #e4defc;
  --violet-6: #d7cff9;
  --violet-7: #c4b8f3;
  --violet-8: #aa99ec;
  --violet-9: #6e56cf;
  --violet-10: #644fc1;
  --violet-11: #5746af;
  --violet-12: #2f265f
}

.dark,
.dark-theme {
  --violet-1: #17151f;
  --violet-2: #1c172b;
  --violet-3: #271f3f;
  --violet-4: #2d254c;
  --violet-5: #342a58;
  --violet-6: #3d316a;
  --violet-7: #4c3e89;
  --violet-8: #6654c0;
  --violet-9: #6e56cf;
  --violet-10: #836add;
  --violet-11: #b399ff;
  --violet-12: #e2ddfe
}

.light,
.light-theme,
:root {
  --violet-a1: rgba(88, 5, 171, .012);
  --violet-a2: rgba(55, 5, 255, .02);
  --violet-a3: rgba(60, 0, 255, .051);
  --violet-a4: rgba(46, 2, 244, .087);
  --violet-a5: rgba(47, 1, 232, .13);
  --violet-a6: rgba(42, 1, 223, .189);
  --violet-a7: rgba(43, 1, 212, .279);
  --violet-a8: rgba(42, 0, 208, .4);
  --violet-a9: rgba(37, 0, 182, .663);
  --violet-a10: rgba(31, 0, 165, .691);
  --violet-a11: rgba(24, 0, 145, .726);
  --violet-a12: rgba(10, 0, 67, .851)
}

.dark,
.dark-theme {
  --violet-a1: rgba(0, 0, 250, .031);
  --violet-a2: rgba(72, 12, 253, .083);
  --violet-a3: rgba(113, 65, 255, .169);
  --violet-a4: rgba(116, 81, 254, .226);
  --violet-a5: rgba(124, 88, 254, .278);
  --violet-a6: rgba(129, 94, 255, .355);
  --violet-a7: rgba(129, 101, 255, .49);
  --violet-a8: rgba(131, 106, 255, .728);
  --violet-a9: rgba(133, 102, 255, .793);
  --violet-a10: rgba(149, 120, 255, .853);
  --violet-a11: #b399ff;
  --violet-a12: rgba(227, 222, 255, .996)
}

.light,
.light-theme,
:root {
  --indigo-1: #fdfdfe;
  --indigo-2: #f8faff;
  --indigo-3: #f0f4ff;
  --indigo-4: #e6edfe;
  --indigo-5: #d9e2fc;
  --indigo-6: #c6d4f9;
  --indigo-7: #aec0f5;
  --indigo-8: #8da4ef;
  --indigo-9: #3e63dd;
  --indigo-10: #3a5ccc;
  --indigo-11: #3451b2;
  --indigo-12: #1f2d5c
}

.dark,
.dark-theme {
  --indigo-1: #131620;
  --indigo-2: #15192d;
  --indigo-3: #1a2242;
  --indigo-4: #1e284f;
  --indigo-5: #202d5c;
  --indigo-6: #24366e;
  --indigo-7: #2c438f;
  --indigo-8: #3b5dce;
  --indigo-9: #3e63dd;
  --indigo-10: #5c73e7;
  --indigo-11: #99a1ff;
  --indigo-12: #dddffe
}

.light,
.light-theme,
:root {
  --indigo-a1: rgba(5, 5, 130, .008);
  --indigo-a2: rgba(5, 76, 255, .028);
  --indigo-a3: rgba(1, 68, 255, .059);
  --indigo-a4: rgba(2, 71, 245, .099);
  --indigo-a5: rgba(2, 60, 235, .15);
  --indigo-a6: rgba(1, 61, 228, .224);
  --indigo-a7: rgba(0, 56, 224, .318);
  --indigo-a8: rgba(1, 52, 219, .448);
  --indigo-a9: rgba(0, 49, 210, .757);
  --indigo-a10: rgba(0, 44, 189, .773);
  --indigo-a11: rgba(0, 37, 158, .797);
  --indigo-a12: rgba(0, 16, 70, .879)
}

.dark,
.dark-theme {
  --indigo-a1: rgba(0, 0, 252, .035);
  --indigo-a2: rgba(0, 34, 255, .091);
  --indigo-a3: rgba(35, 79, 255, .182);
  --indigo-a4: rgba(49, 90, 254, .239);
  --indigo-a5: rgba(51, 95, 254, .295);
  --indigo-a6: rgba(56, 106, 255, .373);
  --indigo-a7: rgba(63, 107, 255, .516);
  --indigo-a8: rgba(68, 112, 255, .788);
  --indigo-a9: rgba(68, 112, 255, .853);
  --indigo-a10: rgba(100, 126, 255, .897);
  --indigo-a11: #99a1ff;
  --indigo-a12: rgba(222, 224, 255, .996)
}

.light,
.light-theme,
:root {
  --blue-1: #fbfdff;
  --blue-2: #f5faff;
  --blue-3: #edf6ff;
  --blue-4: #e1f0ff;
  --blue-5: #cee7fe;
  --blue-6: #b7d9f8;
  --blue-7: #96c7f2;
  --blue-8: #5eb0ef;
  --blue-9: #0091ff;
  --blue-10: #0880ea;
  --blue-11: #0b68cb;
  --blue-12: #113264
}

.dark,
.dark-theme {
  --blue-1: #0f1720;
  --blue-2: #0f1b2d;
  --blue-3: #11253f;
  --blue-4: #122b4c;
  --blue-5: #12325a;
  --blue-6: #123d6f;
  --blue-7: #0f5096;
  --blue-8: #1276e2;
  --blue-9: #0091ff;
  --blue-10: #3cabff;
  --blue-11: #6bc1ff;
  --blue-12: #c2e6ff
}

.light,
.light-theme,
:root {
  --blue-a1: rgba(5, 130, 255, .016);
  --blue-a2: rgba(5, 130, 255, .04);
  --blue-a3: rgba(2, 128, 255, .071);
  --blue-a4: rgba(1, 128, 255, .118);
  --blue-a5: rgba(1, 130, 250, .193);
  --blue-a6: rgba(1, 119, 230, .283);
  --blue-a7: rgba(0, 119, 223, .412);
  --blue-a8: rgba(0, 130, 230, .632);
  --blue-a9: #0091ff;
  --blue-a10: rgba(0, 125, 233, .969);
  --blue-a11: rgba(0, 97, 201, .957);
  --blue-a12: rgba(0, 36, 89, .934)
}

.dark,
.dark-theme {
  --blue-a1: rgba(0, 0, 252, .035);
  --blue-a2: rgba(0, 55, 255, .091);
  --blue-a3: rgba(0, 102, 255, .169);
  --blue-a4: rgba(0, 110, 254, .226);
  --blue-a5: rgba(3, 116, 255, .286);
  --blue-a6: rgba(8, 123, 255, .377);
  --blue-a7: rgba(7, 127, 255, .546);
  --blue-a8: rgba(17, 132, 255, .875);
  --blue-a9: #0091ff;
  --blue-a10: #3cabff;
  --blue-a11: #6bc1ff;
  --blue-a12: #c2e4ff
}

.light,
.light-theme,
:root {
  --cyan-1: #fafdfe;
  --cyan-2: #f2fcfd;
  --cyan-3: #e7f9fb;
  --cyan-4: #d8f3f6;
  --cyan-5: #c4eaef;
  --cyan-6: #aadee6;
  --cyan-7: #84cdda;
  --cyan-8: #3db9cf;
  --cyan-9: #05a2c2;
  --cyan-10: #0894b3;
  --cyan-11: #0c7792;
  --cyan-12: #0d3c48
}

.dark,
.dark-theme {
  --cyan-1: #07191d;
  --cyan-2: #0b1d22;
  --cyan-3: #0f272e;
  --cyan-4: #112f37;
  --cyan-5: #143741;
  --cyan-6: #17444f;
  --cyan-7: #1d5b6a;
  --cyan-8: #28879f;
  --cyan-9: #05a2c2;
  --cyan-10: #13b7d8;
  --cyan-11: #20d0f3;
  --cyan-12: #b6ecf7
}

.light,
.light-theme,
:root {
  --cyan-a1: rgba(5, 155, 205, .02);
  --cyan-a2: rgba(0, 198, 216, .051);
  --cyan-a3: rgba(2, 192, 213, .095);
  --cyan-a4: rgba(0, 177, 196, .153);
  --cyan-a5: rgba(1, 164, 186, .232);
  --cyan-a6: rgba(1, 156, 180, .334);
  --cyan-a7: rgba(0, 151, 178, .483);
  --cyan-a8: rgba(0, 163, 192, .761);
  --cyan-a9: rgba(0, 161, 193, .981);
  --cyan-a10: rgba(0, 144, 176, .969);
  --cyan-a11: rgba(0, 113, 141, .953);
  --cyan-a12: rgba(0, 50, 62, .95)
}

.dark,
.dark-theme {
  --cyan-a1: rgba(0, 71, 251, .022);
  --cyan-a2: rgba(0, 138, 251, .044);
  --cyan-a3: rgba(0, 181, 253, .096);
  --cyan-a4: rgba(0, 194, 253, .135);
  --cyan-a5: rgba(2, 200, 254, .178);
  --cyan-a6: rgba(20, 207, 254, .239);
  --cyan-a7: rgba(38, 212, 255, .355);
  --cyan-a8: rgba(51, 214, 255, .585);
  --cyan-a9: rgba(0, 212, 255, .736);
  --cyan-a10: rgba(18, 215, 255, .832);
  --cyan-a11: rgba(32, 218, 255, .949);
  --cyan-a12: rgba(187, 244, 255, .966)
}

.light,
.light-theme,
:root {
  --teal-1: #fafefd;
  --teal-2: #f1fcfa;
  --teal-3: #e7f9f5;
  --teal-4: #d9f3ee;
  --teal-5: #c7ebe5;
  --teal-6: #afdfd7;
  --teal-7: #8dcec3;
  --teal-8: #53b9ab;
  --teal-9: #12a594;
  --teal-10: #0e9888;
  --teal-11: #067a6f;
  --teal-12: #0d3d38
}

.dark,
.dark-theme {
  --teal-1: #091a16;
  --teal-2: #091f1a;
  --teal-3: #0d2923;
  --teal-4: #0f312b;
  --teal-5: #123a32;
  --teal-6: #16463d;
  --teal-7: #1b5e54;
  --teal-8: #238b7f;
  --teal-9: #12a594;
  --teal-10: #0abba4;
  --teal-11: #0bd8b6;
  --teal-12: #adf0dd
}

.light,
.light-theme,
:root {
  --teal-a1: rgba(5, 205, 155, .02);
  --teal-a2: rgba(1, 200, 164, .055);
  --teal-a3: rgba(2, 192, 151, .095);
  --teal-a4: rgba(2, 175, 140, .15);
  --teal-a5: rgba(0, 164, 137, .22);
  --teal-a6: rgba(0, 153, 128, .314);
  --teal-a7: rgba(1, 146, 122, .448);
  --teal-a8: rgba(0, 151, 131, .675);
  --teal-a9: rgba(0, 158, 140, .93);
  --teal-a10: rgba(0, 146, 129, .946);
  --teal-a11: rgba(0, 119, 107, .977);
  --teal-a12: rgba(0, 51, 46, .95)
}

.dark,
.dark-theme {
  --teal-a1: rgba(0, 246, 0, .009);
  --teal-a2: rgba(0, 250, 87, .031);
  --teal-a3: rgba(0, 254, 174, .074);
  --teal-a4: rgba(0, 253, 199, .109);
  --teal-a5: rgba(0, 254, 199, .148);
  --teal-a6: rgba(14, 254, 210, .2);
  --teal-a7: rgba(34, 254, 221, .304);
  --teal-a8: rgba(46, 255, 231, .498);
  --teal-a9: rgba(14, 255, 227, .611);
  --teal-a10: rgba(4, 255, 221, .706);
  --teal-a11: rgba(8, 255, 214, .832);
  --teal-a12: rgba(183, 255, 235, .936)
}

.light,
.light-theme,
:root {
  --green-1: #fbfefc;
  --green-2: #f2fcf5;
  --green-3: #e9f9ee;
  --green-4: #ddf3e4;
  --green-5: #ccebd7;
  --green-6: #b4dfc4;
  --green-7: #92ceac;
  --green-8: #5bb98c;
  --green-9: #30a46c;
  --green-10: #299764;
  --green-11: #18794e;
  --green-12: #193b2d
}

.dark,
.dark-theme {
  --green-1: #0d1912;
  --green-2: #0f1d17;
  --green-3: #12281f;
  --green-4: #143125;
  --green-5: #173a2a;
  --green-6: #194633;
  --green-7: #1f5e41;
  --green-8: #2c8c5e;
  --green-9: #30a46c;
  --green-10: #35b979;
  --green-11: #3dd68c;
  --green-12: #b1f1cb
}

.light,
.light-theme,
:root {
  --green-a1: rgba(5, 192, 67, .016);
  --green-a2: rgba(0, 196, 59, .051);
  --green-a3: rgba(2, 186, 60, .087);
  --green-a4: rgba(1, 166, 53, .134);
  --green-a5: rgba(0, 155, 54, .2);
  --green-a6: rgba(1, 147, 54, .295);
  --green-a7: rgba(0, 140, 61, .428);
  --green-a8: rgba(0, 147, 76, .644);
  --green-a9: rgba(0, 143, 74, .812);
  --green-a10: rgba(0, 131, 70, .84);
  --green-a11: rgba(0, 107, 59, .906);
  --green-a12: rgba(0, 38, 22, .902)
}

.dark,
.dark-theme {
  --green-a1: rgba(0, 224, 0, .005);
  --green-a2: rgba(0, 251, 0, .022);
  --green-a3: rgba(0, 252, 122, .07);
  --green-a4: rgba(0, 253, 144, .109);
  --green-a5: rgba(17, 254, 147, .148);
  --green-a6: rgba(29, 254, 160, .2);
  --green-a7: rgba(47, 254, 158, .304);
  --green-a8: rgba(64, 255, 162, .503);
  --green-a9: rgba(64, 255, 162, .607);
  --green-a10: rgba(66, 255, 164, .697);
  --green-a11: rgba(69, 255, 165, .823);
  --green-a12: rgba(187, 255, 214, .94)
}

.light,
.light-theme,
:root {
  --grass-1: #fbfefb;
  --grass-2: #f3fcf3;
  --grass-3: #ebf9eb;
  --grass-4: #dff3df;
  --grass-5: #ceebcf;
  --grass-6: #b7dfba;
  --grass-7: #97cf9c;
  --grass-8: #65ba75;
  --grass-9: #46a758;
  --grass-10: #3d9a50;
  --grass-11: #297c3b;
  --grass-12: #203c25
}

.dark,
.dark-theme {
  --grass-1: #0d1912;
  --grass-2: #131d16;
  --grass-3: #18281d;
  --grass-4: #1b3021;
  --grass-5: #1e3926;
  --grass-6: #24452d;
  --grass-7: #2d5d39;
  --grass-8: #428a4f;
  --grass-9: #46a758;
  --grass-10: #5cbc6e;
  --grass-11: #71d083;
  --grass-12: #c2f0c2
}

.light,
.light-theme,
:root {
  --grass-a1: rgba(5, 192, 5, .016);
  --grass-a2: rgba(5, 192, 5, .048);
  --grass-a3: rgba(2, 179, 2, .079);
  --grass-a4: rgba(1, 160, 1, .126);
  --grass-a5: rgba(1, 151, 6, .193);
  --grass-a6: rgba(1, 142, 12, .283);
  --grass-a7: rgba(0, 138, 12, .408);
  --grass-a8: rgba(0, 141, 26, .604);
  --grass-a9: rgba(0, 134, 25, .726);
  --grass-a10: rgba(0, 122, 25, .761);
  --grass-a11: rgba(0, 99, 22, .84);
  --grass-a12: rgba(0, 32, 6, .875)
}

.dark,
.dark-theme {
  --grass-a1: rgba(0, 224, 0, .005);
  --grass-a2: rgba(0, 251, 0, .022);
  --grass-a3: rgba(24, 253, 96, .07);
  --grass-a4: rgba(53, 255, 110, .104);
  --grass-a5: rgba(66, 255, 123, .143);
  --grass-a6: rgba(85, 255, 131, .195);
  --grass-a7: rgba(94, 255, 134, .299);
  --grass-a8: rgba(109, 255, 136, .494);
  --grass-a9: rgba(98, 255, 127, .62);
  --grass-a10: rgba(120, 255, 145, .71);
  --grass-a11: rgba(136, 255, 158, .797);
  --grass-a12: rgba(206, 255, 206, .936)
}

.light,
.light-theme,
:root {
  --orange-1: #fefcfb;
  --orange-2: #fff8f4;
  --orange-3: #ffedd5;
  --orange-4: #ffe0bb;
  --orange-5: #ffd3a4;
  --orange-6: #ffc291;
  --orange-7: #ffaa7d;
  --orange-8: #ed8a5c;
  --orange-9: #f76808;
  --orange-10: #ed5f00;
  --orange-11: #99543a;
  --orange-12: #582d1d
}

.dark,
.dark-theme {
  --orange-1: #1f1206;
  --orange-2: #271504;
  --orange-3: #341c0a;
  --orange-4: #3f220d;
  --orange-5: #4b2910;
  --orange-6: #5d3213;
  --orange-7: #7e4318;
  --orange-8: #c36522;
  --orange-9: #f76808;
  --orange-10: #ff802b;
  --orange-11: #ffa366;
  --orange-12: #ffe0c2
}

.light,
.light-theme,
:root {
  --orange-a1: rgba(192, 67, 5, .016);
  --orange-a2: rgba(255, 97, 5, .044);
  --orange-a3: rgba(255, 145, 1, .165);
  --orange-a4: rgba(255, 140, 1, .267);
  --orange-a5: rgba(255, 132, 0, .357);
  --orange-a6: rgba(255, 115, 1, .432);
  --orange-a7: rgba(255, 89, 0, .51);
  --orange-a8: rgba(227, 72, 0, .64);
  --orange-a9: rgba(247, 99, 0, .969);
  --orange-a10: #ed5f00;
  --orange-a11: rgba(123, 33, 0, .773);
  --orange-a12: rgba(67, 18, 0, .887)
}

.dark,
.dark-theme {
  --orange-a1: rgba(250, 0, 0, .031);
  --orange-a2: rgba(255, 0, 0, .065);
  --orange-a3: rgba(253, 55, 0, .122);
  --orange-a4: rgba(255, 85, 0, .169);
  --orange-a5: rgba(255, 102, 0, .221);
  --orange-a6: rgba(255, 110, 7, .299);
  --orange-a7: rgba(255, 120, 24, .442);
  --orange-a8: rgba(255, 128, 37, .741);
  --orange-a9: rgba(255, 106, 7, .966);
  --orange-a10: #ff802b;
  --orange-a11: #ffa366;
  --orange-a12: #ffe0c2
}

.light,
.light-theme,
:root {
  --brown-1: #fefdfc;
  --brown-2: #fcf9f6;
  --brown-3: #f8f1ea;
  --brown-4: #f4e9dd;
  --brown-5: #efddcc;
  --brown-6: #e8cdb5;
  --brown-7: #ddb896;
  --brown-8: #d09e72;
  --brown-9: #ad7f58;
  --brown-10: #9e7352;
  --brown-11: #815e46;
  --brown-12: #3e332e
}

.dark,
.dark-theme {
  --brown-1: #1a1513;
  --brown-2: #1e1a17;
  --brown-3: #29221d;
  --brown-4: #312821;
  --brown-5: #3b2f26;
  --brown-6: #48392d;
  --brown-7: #614c3a;
  --brown-8: #937153;
  --brown-9: #ad7f58;
  --brown-10: #bd926c;
  --brown-11: #dbb594;
  --brown-12: #f2e1ca
}

.light,
.light-theme,
:root {
  --brown-a1: rgba(171, 88, 5, .012);
  --brown-a2: rgba(171, 88, 5, .036);
  --brown-a3: rgba(171, 86, 2, .083);
  --brown-a4: rgba(173, 90, 1, .134);
  --brown-a5: rgba(175, 85, 0, .2);
  --brown-a6: rgba(176, 82, 1, .291);
  --brown-a7: rgba(172, 83, 0, .412);
  --brown-a8: rgba(170, 79, 0, .553);
  --brown-a9: rgba(130, 61, 0, .655);
  --brown-a10: rgba(112, 49, 0, .679);
  --brown-a11: rgba(81, 33, 0, .726);
  --brown-a12: rgba(20, 6, 0, .82)
}

.dark,
.dark-theme {
  --brown-a1: rgba(246, 0, 0, .009);
  --brown-a2: rgba(255, 102, 0, .026);
  --brown-a3: rgba(254, 159, 92, .074);
  --brown-a4: hsla(26, 98%, 71%, .109);
  --brown-a5: hsla(26, 99%, 73%, .152);
  --brown-a6: rgba(255, 183, 125, .208);
  --brown-a7: hsla(28, 99%, 76%, .317);
  --brown-a8: rgba(255, 191, 135, .533);
  --brown-a9: hsla(28, 99%, 74%, .646);
  --brown-a10: rgba(255, 194, 141, .715);
  --brown-a11: rgba(255, 210, 171, .845);
  --brown-a12: rgba(255, 237, 213, .944)
}

.light,
.light-theme,
:root {
  --sky-1: #f9feff;
  --sky-2: #f1fcff;
  --sky-3: #e2f9ff;
  --sky-4: #d2f4fd;
  --sky-5: #bfebf8;
  --sky-6: #a5dced;
  --sky-7: #82cae0;
  --sky-8: #46b8d8;
  --sky-9: #7ce2fe;
  --sky-10: #72dbf8;
  --sky-11: #256e93;
  --sky-12: #1a404d
}

.dark,
.dark-theme {
  --sky-1: #0c1820;
  --sky-2: #0d1d26;
  --sky-3: #112733;
  --sky-4: #132f3d;
  --sky-5: #163648;
  --sky-6: #1a4358;
  --sky-7: #205975;
  --sky-8: #2d87b4;
  --sky-9: #7ce2fe;
  --sky-10: #8ae8ff;
  --sky-11: #52d4ff;
  --sky-12: #c2f3ff
}

.light,
.light-theme,
:root {
  --sky-a1: rgba(5, 213, 255, .024);
  --sky-a2: rgba(1, 200, 255, .055);
  --sky-a3: rgba(1, 204, 255, .114);
  --sky-a4: rgba(1, 191, 244, .177);
  --sky-a5: rgba(0, 174, 227, .251);
  --sky-a6: rgba(0, 156, 204, .353);
  --sky-a7: rgba(0, 147, 192, .491);
  --sky-a8: rgba(0, 158, 201, .726);
  --sky-a9: rgba(0, 198, 253, .514);
  --sky-a10: rgba(0, 190, 242, .553);
  --sky-a11: rgba(0, 86, 129, .855);
  --sky-a12: rgba(0, 43, 58, .902)
}

.dark,
.dark-theme {
  --sky-a1: rgba(0, 25, 252, .035);
  --sky-a2: rgba(0, 106, 253, .061);
  --sky-a3: rgba(0, 153, 255, .117);
  --sky-a4: rgba(0, 165, 254, .161);
  --sky-a5: rgba(15, 167, 255, .208);
  --sky-a6: rgba(31, 180, 254, .278);
  --sky-a7: rgba(44, 185, 255, .403);
  --sky-a8: rgba(55, 188, 255, .676);
  --sky-a9: rgba(125, 227, 255, .996);
  --sky-a10: #8ae8ff;
  --sky-a11: #52d4ff;
  --sky-a12: #c2f3ff
}

.light,
.light-theme,
:root {
  --mint-1: #f9fefd;
  --mint-2: #effefa;
  --mint-3: #ddfbf3;
  --mint-4: #ccf7ec;
  --mint-5: #bbeee2;
  --mint-6: #a6e1d3;
  --mint-7: #87d0bf;
  --mint-8: #51bda7;
  --mint-9: #86ead4;
  --mint-10: #7fe1cc;
  --mint-11: #27756a;
  --mint-12: #16433c
}

.dark,
.dark-theme {
  --mint-1: #081917;
  --mint-2: #0a1f1d;
  --mint-3: #0d2927;
  --mint-4: #0e322e;
  --mint-5: #103b36;
  --mint-6: #134842;
  --mint-7: #186057;
  --mint-8: #248f7d;
  --mint-9: #86ead4;
  --mint-10: #95f3d9;
  --mint-11: #49dfbe;
  --mint-12: #c4f5e1
}

.light,
.light-theme,
:root {
  --mint-a1: rgba(5, 213, 172, .024);
  --mint-a2: rgba(1, 239, 176, .063);
  --mint-a3: rgba(1, 225, 165, .134);
  --mint-a4: rgba(0, 215, 161, .2);
  --mint-a5: rgba(0, 191, 147, .267);
  --mint-a6: rgba(1, 169, 130, .35);
  --mint-a7: rgba(0, 155, 119, .471);
  --mint-a8: rgba(0, 158, 127, .683);
  --mint-a9: rgba(0, 211, 165, .475);
  --mint-a10: rgba(0, 195, 153, .502);
  --mint-a11: rgba(0, 92, 80, .848);
  --mint-a12: rgba(0, 49, 42, .914)
}

.dark,
.dark-theme {
  --mint-a1: rgba(0, 224, 0, .005);
  --mint-a2: rgba(0, 250, 187, .031);
  --mint-a3: rgba(0, 254, 229, .074);
  --mint-a4: rgba(0, 254, 220, .113);
  --mint-a5: rgba(0, 254, 221, .152);
  --mint-a6: rgba(0, 255, 225, .208);
  --mint-a7: rgba(24, 255, 228, .312);
  --mint-a8: rgba(47, 255, 220, .516);
  --mint-a9: rgba(145, 255, 231, .91);
  --mint-a10: rgba(156, 255, 227, .949);
  --mint-a11: rgba(81, 255, 217, .862);
  --mint-a12: rgba(204, 255, 234, .957)
}

.light,
.light-theme,
:root {
  --lime-1: #fcfdfa;
  --lime-2: #f7fcf0;
  --lime-3: #edfada;
  --lime-4: #e2f5c4;
  --lime-5: #d5edaf;
  --lime-6: #c6de99;
  --lime-7: #b2ca7f;
  --lime-8: #9ab654;
  --lime-9: #bdee63;
  --lime-10: #b0e64d;
  --lime-11: #59682c;
  --lime-12: #37401c
}

.dark,
.dark-theme {
  --lime-1: #141807;
  --lime-2: #181d0c;
  --lime-3: #1f2711;
  --lime-4: #252f14;
  --lime-5: #2c3717;
  --lime-6: #36431b;
  --lime-7: #485921;
  --lime-8: #70862d;
  --lime-9: #bdee63;
  --lime-10: #c4f042;
  --lime-11: #bbd926;
  --lime-12: #e3f7ba
}

.light,
.light-theme,
:root {
  --lime-a1: rgba(105, 155, 5, .02);
  --lime-a2: rgba(119, 204, 1, .059);
  --lime-a3: rgba(133, 221, 2, .146);
  --lime-a4: rgba(131, 212, 1, .232);
  --lime-a5: rgba(122, 198, 0, .314);
  --lime-a6: rgba(112, 172, 0, .4);
  --lime-a7: rgba(102, 149, 0, .502);
  --lime-a8: rgba(105, 146, 0, .671);
  --lime-a9: rgba(148, 227, 0, .612);
  --lime-a10: rgba(143, 219, 0, .702);
  --lime-a11: rgba(55, 73, 0, .828);
  --lime-a12: rgba(30, 41, 0, .891)
}

.dark,
.dark-theme {
  --lime-a1: rgba(18, 24, 0, .709);
  --lime-a2: rgba(25, 251, 0, .022);
  --lime-a3: rgba(132, 255, 0, .065);
  --lime-a4: rgba(152, 254, 0, .1);
  --lime-a5: rgba(171, 254, 17, .135);
  --lime-a6: rgba(183, 254, 40, .187);
  --lime-a7: rgba(195, 255, 56, .282);
  --lime-a8: rgba(208, 255, 68, .477);
  --lime-a9: rgba(202, 255, 105, .927);
  --lime-a10: rgba(208, 255, 69, .936);
  --lime-a11: rgba(219, 255, 41, .836);
  --lime-a12: hsla(80, 99%, 88%, .966)
}

.light,
.light-theme,
:root {
  --yellow-1: #fdfdf9;
  --yellow-2: #fffbe0;
  --yellow-3: #fff8c6;
  --yellow-4: #fcf3af;
  --yellow-5: #f7ea9b;
  --yellow-6: #ecdd85;
  --yellow-7: #dac56e;
  --yellow-8: #c9aa45;
  --yellow-9: #fbe32d;
  --yellow-10: #f9da10;
  --yellow-11: #775f28;
  --yellow-12: #473b1f
}

.dark,
.dark-theme {
  --yellow-1: #1c1500;
  --yellow-2: #221a04;
  --yellow-3: #2c230a;
  --yellow-4: #342a0e;
  --yellow-5: #3d3211;
  --yellow-6: #493d14;
  --yellow-7: #615119;
  --yellow-8: #8f7d24;
  --yellow-9: #fbe32d;
  --yellow-10: #fcea5c;
  --yellow-11: #fe3;
  --yellow-12: #fff5ad
}

.light,
.light-theme,
:root {
  --yellow-a1: rgba(171, 171, 5, .024);
  --yellow-a2: rgba(255, 221, 1, .122);
  --yellow-a3: rgba(255, 225, 1, .224);
  --yellow-a4: rgba(246, 217, 0, .314);
  --yellow-a5: rgba(235, 203, 1, .393);
  --yellow-a6: rgba(215, 183, 0, .479);
  --yellow-a7: rgba(190, 152, 0, .569);
  --yellow-a8: rgba(181, 139, 0, .73);
  --yellow-a9: rgba(250, 221, 0, .824);
  --yellow-a10: rgba(249, 216, 0, .938);
  --yellow-a11: rgba(94, 66, 0, .844);
  --yellow-a12: rgba(46, 32, 0, .879)
}

.dark,
.dark-theme {
  --yellow-a1: rgba(246, 0, 0, .018);
  --yellow-a2: rgba(251, 71, 0, .044);
  --yellow-a3: rgba(254, 152, 0, .087);
  --yellow-a4: rgba(253, 173, 0, .122);
  --yellow-a5: rgba(254, 186, 0, .161);
  --yellow-a6: rgba(254, 196, 5, .213);
  --yellow-a7: rgba(254, 205, 27, .317);
  --yellow-a8: rgba(255, 220, 47, .516);
  --yellow-a9: rgba(255, 230, 45, .983);
  --yellow-a10: rgba(255, 236, 93, .988);
  --yellow-a11: #fe3;
  --yellow-a12: #fff5ad
}

.light,
.light-theme,
:root {
  --amber-1: #fefdfb;
  --amber-2: #fff9ed;
  --amber-3: #fff3d0;
  --amber-4: #ffecb7;
  --amber-5: #ffe0a1;
  --amber-6: #f5d08c;
  --amber-7: #e4bb78;
  --amber-8: #d6a35c;
  --amber-9: #ffc53d;
  --amber-10: #ffba19;
  --amber-11: #915930;
  --amber-12: #4f3422
}

.dark,
.dark-theme {
  --amber-1: #1f1300;
  --amber-2: #251804;
  --amber-3: #30200b;
  --amber-4: #39270f;
  --amber-5: #432e12;
  --amber-6: #533916;
  --amber-7: #6f4d1d;
  --amber-8: #a9762a;
  --amber-9: #ffc53d;
  --amber-10: #ffcb47;
  --amber-11: #ffcc4d;
  --amber-12: #ffe7b3
}

.light,
.light-theme,
:root {
  --amber-a1: rgba(192, 130, 5, .016);
  --amber-a2: rgba(255, 171, 2, .071);
  --amber-a3: rgba(255, 192, 1, .185);
  --amber-a4: rgba(255, 187, 1, .283);
  --amber-a5: rgba(255, 170, 1, .369);
  --amber-a6: rgba(233, 151, 0, .451);
  --amber-a7: rgba(204, 126, 0, .53);
  --amber-a8: rgba(191, 112, 0, .64);
  --amber-a9: rgba(255, 179, 0, .761);
  --amber-a10: rgba(255, 179, 1, .899);
  --amber-a11: rgba(120, 50, 0, .812);
  --amber-a12: rgba(52, 21, 0, .867)
}

.dark,
.dark-theme {
  --amber-a1: rgba(250, 0, 0, .031);
  --amber-a2: rgba(252, 25, 0, .057);
  --amber-a3: rgba(255, 102, 0, .104);
  --amber-a4: rgba(255, 128, 0, .143);
  --amber-a5: rgba(254, 140, 0, .187);
  --amber-a6: rgba(255, 151, 16, .256);
  --amber-a7: rgba(255, 164, 37, .377);
  --amber-a8: rgba(255, 174, 53, .628);
  --amber-a9: #ffc53d;
  --amber-a10: #ffcb47;
  --amber-a11: #ffcd4d;
  --amber-a12: #ffe7b3
}

.light,
.light-theme,
:root {
  --gold-1: #fdfdfc;
  --gold-2: #fbf9f2;
  --gold-3: #f5f2e9;
  --gold-4: #eeeadd;
  --gold-5: #e5dfd0;
  --gold-6: #dad1bd;
  --gold-7: #cbbda4;
  --gold-8: #b8a383;
  --gold-9: #978365;
  --gold-10: #89775c;
  --gold-11: #71624b;
  --gold-12: #3b352b
}

.dark,
.dark-theme {
  --gold-1: #171613;
  --gold-2: #1b1a17;
  --gold-3: #24231e;
  --gold-4: #2c2a24;
  --gold-5: #34312a;
  --gold-6: #413c33;
  --gold-7: #564f42;
  --gold-8: #847662;
  --gold-9: #978365;
  --gold-10: #a99679;
  --gold-11: #cbb99f;
  --gold-12: #e8e2d9
}

.light,
.light-theme,
:root {
  --gold-a1: rgba(88, 88, 5, .012);
  --gold-a2: rgba(176, 138, 0, .051);
  --gold-a3: rgba(140, 106, 2, .087);
  --gold-a4: rgba(128, 99, 1, .134);
  --gold-a5: rgba(114, 82, 1, .185);
  --gold-a6: rgba(112, 77, 0, .259);
  --gold-a7: rgba(110, 69, 0, .357);
  --gold-a8: rgba(109, 66, 0, .487);
  --gold-a9: rgba(83, 50, 0, .604);
  --gold-a10: rgba(71, 42, 0, .64);
  --gold-a11: rgba(54, 32, 0, .706);
  --gold-a12: rgba(19, 12, 0, .832)
}

.dark,
.dark-theme {
  --gold-a1: rgba(19, 14, 0, .209);
  --gold-a2: rgba(255, 179, 0, .013);
  --gold-a3: rgba(255, 236, 139, .052);
  --gold-a4: hsla(45, 98%, 82%, .087);
  --gold-a5: hsla(42, 97%, 83%, .122);
  --gold-a6: hsla(39, 98%, 84%, .178);
  --gold-a7: hsla(39, 99%, 85%, .269);
  --gold-a8: hsla(35, 99%, 86%, .468);
  --gold-a9: rgba(255, 218, 164, .55);
  --gold-a10: rgba(255, 224, 179, .628);
  --gold-a11: rgba(255, 231, 198, .775);
  --gold-a12: hsla(36, 98%, 97%, .901)
}

.light,
.light-theme,
:root {
  --bronze-1: #fdfcfc;
  --bronze-2: #fdf8f6;
  --bronze-3: #f8f1ee;
  --bronze-4: #f2e8e4;
  --bronze-5: #eaddd7;
  --bronze-6: #e0cec7;
  --bronze-7: #d2bab0;
  --bronze-8: #bfa094;
  --bronze-9: #a18072;
  --bronze-10: #947467;
  --bronze-11: #7d5e54;
  --bronze-12: #43302b
}

.dark,
.dark-theme {
  --bronze-1: #191514;
  --bronze-2: #1c1918;
  --bronze-3: #272220;
  --bronze-4: #302926;
  --bronze-5: #382f2c;
  --bronze-6: #463a35;
  --bronze-7: #5d4c45;
  --bronze-8: #8d7266;
  --bronze-9: #a18072;
  --bronze-10: #b39283;
  --bronze-11: #d4b3a5;
  --bronze-12: #ede0d9
}

.light,
.light-theme,
:root {
  --bronze-a1: rgba(88, 5, 5, .012);
  --bronze-a2: rgba(199, 60, 5, .036);
  --bronze-a3: rgba(151, 46, 1, .067);
  --bronze-a4: rgba(132, 38, 0, .106);
  --bronze-a5: rgba(121, 39, 0, .157);
  --bronze-a6: rgba(114, 33, 0, .22);
  --bronze-a7: rgba(110, 33, 0, .31);
  --bronze-a8: rgba(103, 29, 0, .42);
  --bronze-a9: rgba(85, 26, 0, .553);
  --bronze-a10: rgba(76, 22, 0, .597);
  --bronze-a11: rgba(61, 15, 0, .671);
  --bronze-a12: rgba(29, 6, 0, .832)
}

.dark,
.dark-theme {
  --bronze-a1: rgba(224, 0, 0, .005);
  --bronze-a2: rgba(246, 80, 24, .018);
  --bronze-a3: rgba(255, 178, 147, .065);
  --bronze-a4: hsla(18, 99%, 81%, .104);
  --bronze-a5: hsla(15, 98%, 83%, .139);
  --bronze-a6: hsla(18, 98%, 83%, .2);
  --bronze-a7: hsla(17, 99%, 84%, .299);
  --bronze-a8: hsla(18, 99%, 85%, .507);
  --bronze-a9: hsla(18, 99%, 84%, .594);
  --bronze-a10: rgba(255, 206, 184, .671);
  --bronze-a11: rgba(255, 215, 197, .814);
  --bronze-a12: hsla(21, 98%, 96%, .923)
}

.light,
.light-theme,
:root {
  --gray-1: #fcfcfc;
  --gray-2: #f9f9f9;
  --gray-3: #f1f1f1;
  --gray-4: #ebebeb;
  --gray-5: #e4e4e4;
  --gray-6: #ddd;
  --gray-7: #d4d4d4;
  --gray-8: #bbb;
  --gray-9: #8d8d8d;
  --gray-10: grey;
  --gray-11: #646464;
  --gray-12: #202020
}

.dark,
.dark-theme {
  --gray-1: #181818;
  --gray-2: #1b1b1b;
  --gray-3: #282828;
  --gray-4: #303030;
  --gray-5: #373737;
  --gray-6: #3f3f3f;
  --gray-7: #4a4a4a;
  --gray-8: #606060;
  --gray-9: #6e6e6e;
  --gray-10: #818181;
  --gray-11: #b1b1b1;
  --gray-12: #eee
}

.light,
.light-theme,
:root {
  --gray-a1: rgba(0, 0, 0, .012);
  --gray-a2: rgba(0, 0, 0, .024);
  --gray-a3: rgba(0, 0, 0, .055);
  --gray-a4: rgba(0, 0, 0, .078);
  --gray-a5: rgba(0, 0, 0, .106);
  --gray-a6: rgba(0, 0, 0, .133);
  --gray-a7: rgba(0, 0, 0, .169);
  --gray-a8: rgba(0, 0, 0, .267);
  --gray-a9: rgba(0, 0, 0, .447);
  --gray-a10: rgba(0, 0, 0, .498);
  --gray-a11: rgba(0, 0, 0, .608);
  --gray-a12: rgba(0, 0, 0, .875)
}

.dark,
.dark-theme {
  --gray-a1: hsla(0, 0%, 100%, 0);
  --gray-a2: hsla(0, 0%, 100%, .013);
  --gray-a3: hsla(0, 0%, 100%, .069);
  --gray-a4: hsla(0, 0%, 100%, .104);
  --gray-a5: hsla(0, 0%, 100%, .134);
  --gray-a6: hsla(0, 0%, 100%, .169);
  --gray-a7: hsla(0, 0%, 100%, .216);
  --gray-a8: hsla(0, 0%, 100%, .312);
  --gray-a9: hsla(0, 0%, 100%, .372);
  --gray-a10: hsla(0, 0%, 100%, .455);
  --gray-a11: hsla(0, 0%, 100%, .662);
  --gray-a12: hsla(0, 0%, 100%, .926)
}

.light,
.light-theme,
:root {
  --mauve-1: #fdfcfd;
  --mauve-2: #faf9fb;
  --mauve-3: #f3f1f5;
  --mauve-4: #eceaef;
  --mauve-5: #e6e3e9;
  --mauve-6: #dfdce3;
  --mauve-7: #d5d3db;
  --mauve-8: #bcbac7;
  --mauve-9: #8e8c99;
  --mauve-10: #817f8b;
  --mauve-11: #65636d;
  --mauve-12: #211f26
}

.dark,
.dark-theme {
  --mauve-1: #191719;
  --mauve-2: #1e1a1e;
  --mauve-3: #2b272c;
  --mauve-4: #332f35;
  --mauve-5: #3a363c;
  --mauve-6: #423e45;
  --mauve-7: #4d4951;
  --mauve-8: #625f69;
  --mauve-9: #6f6d78;
  --mauve-10: #82808b;
  --mauve-11: #b1afb8;
  --mauve-12: #eeeef0
}

.light,
.light-theme,
:root {
  --mauve-a1: rgba(88, 5, 88, .012);
  --mauve-a2: rgba(47, 5, 88, .024);
  --mauve-a3: rgba(37, 0, 73, .055);
  --mauve-a4: rgba(26, 2, 62, .083);
  --mauve-a5: rgba(28, 0, 55, .11);
  --mauve-a6: rgba(23, 1, 52, .138);
  --mauve-a7: rgba(12, 1, 47, .173);
  --mauve-a8: rgba(8, 0, 49, .271);
  --mauve-a9: rgba(4, 0, 29, .451);
  --mauve-a10: rgba(4, 0, 24, .502);
  --mauve-a11: rgba(3, 0, 16, .612);
  --mauve-a12: rgba(2, 0, 8, .879)
}

.dark,
.dark-theme {
  --mauve-a1: rgba(224, 0, 224, .005);
  --mauve-a2: rgba(255, 101, 255, .026);
  --mauve-a3: rgba(242, 196, 254, .087);
  --mauve-a4: rgba(238, 206, 254, .126);
  --mauve-a5: rgba(242, 216, 255, .156);
  --mauve-a6: rgba(239, 219, 255, .195);
  --mauve-a7: rgba(239, 223, 255, .247);
  --mauve-a8: rgba(235, 226, 255, .351);
  --mauve-a9: rgba(233, 228, 255, .416);
  --mauve-a10: rgba(237, 233, 255, .498);
  --mauve-a11: rgba(245, 242, 255, .693);
  --mauve-a12: rgba(253, 253, 255, .936)
}

.light,
.light-theme,
:root {
  --slate-1: #fcfcfd;
  --slate-2: #f9f9fb;
  --slate-3: #f2f2f5;
  --slate-4: #ebebef;
  --slate-5: #e4e4e9;
  --slate-6: #dddde3;
  --slate-7: #d3d4db;
  --slate-8: #b9bbc6;
  --slate-9: #8b8d98;
  --slate-10: #7e808a;
  --slate-11: #60646c;
  --slate-12: #1c2024
}

.dark,
.dark-theme {
  --slate-1: #18181a;
  --slate-2: #1b1b1f;
  --slate-3: #27282d;
  --slate-4: #2e3035;
  --slate-5: #35373c;
  --slate-6: #3c3f44;
  --slate-7: #464b50;
  --slate-8: #5a6165;
  --slate-9: #696e77;
  --slate-10: #7d828a;
  --slate-11: #adb1b8;
  --slate-12: #edeef0
}

.light,
.light-theme,
:root {
  --slate-a1: rgba(5, 5, 88, .012);
  --slate-a2: rgba(5, 5, 88, .024);
  --slate-a3: rgba(0, 0, 59, .051);
  --slate-a4: rgba(2, 2, 52, .079);
  --slate-a5: rgba(0, 0, 48, .106);
  --slate-a6: rgba(1, 1, 46, .134);
  --slate-a7: rgba(1, 6, 47, .173);
  --slate-a8: rgba(0, 8, 47, .275);
  --slate-a9: rgba(0, 4, 29, .455);
  --slate-a10: rgba(0, 4, 24, .506);
  --slate-a11: rgba(0, 7, 19, .624);
  --slate-a12: rgba(0, 5, 9, .891)
}

.dark,
.dark-theme {
  --slate-a1: rgba(24, 24, 246, .009);
  --slate-a2: rgba(121, 121, 250, .031);
  --slate-a3: rgba(189, 200, 255, .091);
  --slate-a4: rgba(199, 214, 254, .126);
  --slate-a5: rgba(210, 223, 255, .156);
  --slate-a6: rgba(212, 228, 254, .191);
  --slate-a7: rgba(213, 234, 254, .243);
  --slate-a8: rgba(222, 243, 255, .334);
  --slate-a9: rgba(221, 233, 255, .412);
  --slate-a10: rgba(228, 238, 255, .494);
  --slate-a11: rgba(239, 245, 255, .693);
  --slate-a12: rgba(252, 253, 255, .936)
}

.light,
.light-theme,
:root {
  --sage-1: #fbfdfc;
  --sage-2: #f7f9f8;
  --sage-3: #f0f2f1;
  --sage-4: #e9eceb;
  --sage-5: #e3e6e4;
  --sage-6: #dcdfdd;
  --sage-7: #d2d5d3;
  --sage-8: #b8bcba;
  --sage-9: #868e8b;
  --sage-10: #7a817f;
  --sage-11: #5f6563;
  --sage-12: #1a211e
}

.dark,
.dark-theme {
  --sage-1: #161918;
  --sage-2: #181c1a;
  --sage-3: #252927;
  --sage-4: #2c312f;
  --sage-5: #343836;
  --sage-6: #3b403e;
  --sage-7: #474c4a;
  --sage-8: #5c615f;
  --sage-9: #63706b;
  --sage-10: #78837f;
  --sage-11: #aab2af;
  --sage-12: #eceeed
}

.light,
.light-theme,
:root {
  --sage-a1: rgba(5, 130, 68, .016);
  --sage-a2: rgba(5, 67, 36, .032);
  --sage-a3: rgba(1, 34, 18, .059);
  --sage-a4: rgba(2, 37, 25, .087);
  --sage-a5: rgba(0, 28, 9, .11);
  --sage-a6: rgba(1, 23, 9, .138);
  --sage-a7: rgba(1, 18, 6, .177);
  --sage-a8: rgba(1, 15, 8, .279);
  --sage-a9: rgba(0, 17, 11, .475);
  --sage-a10: rgba(0, 14, 10, .522);
  --sage-a11: rgba(0, 10, 7, .628);
  --sage-a12: rgba(0, 8, 5, .899)
}

.dark,
.dark-theme {
  --sage-a1: rgba(0, 224, 22, .005);
  --sage-a2: rgba(24, 246, 135, .018);
  --sage-a3: rgba(200, 254, 227, .074);
  --sage-a4: rgba(208, 253, 235, .109);
  --sage-a5: rgba(225, 254, 240, .139);
  --sage-a6: rgba(225, 254, 242, .174);
  --sage-a7: rgba(232, 254, 245, .226);
  --sage-a8: rgba(238, 254, 248, .317);
  --sage-a9: rgba(221, 255, 242, .381);
  --sage-a10: rgba(231, 255, 246, .464);
  --sage-a11: rgba(243, 255, 250, .667);
  --sage-a12: rgba(253, 255, 254, .927)
}

.light,
.light-theme,
:root {
  --olive-1: #fcfdfc;
  --olive-2: #f8faf8;
  --olive-3: #f1f3f1;
  --olive-4: #eaecea;
  --olive-5: #e3e5e3;
  --olive-6: #dbdedb;
  --olive-7: #d2d4d1;
  --olive-8: #b9bcb8;
  --olive-9: #898e87;
  --olive-10: #7c817b;
  --olive-11: #60655f;
  --olive-12: #1d211c
}

.dark,
.dark-theme {
  --olive-1: #171916;
  --olive-2: #191c19;
  --olive-3: #262926;
  --olive-4: #2d312d;
  --olive-5: #343834;
  --olive-6: #3c403c;
  --olive-7: #474b47;
  --olive-8: #5c615c;
  --olive-9: #667063;
  --olive-10: #7b8378;
  --olive-11: #adb3ab;
  --olive-12: #eceeec
}

.light,
.light-theme,
:root {
  --olive-a1: rgba(5, 88, 5, .012);
  --olive-a2: rgba(5, 77, 5, .028);
  --olive-a3: rgba(0, 37, 0, .055);
  --olive-a4: rgba(2, 26, 2, .083);
  --olive-a5: rgba(0, 18, 0, .11);
  --olive-a6: rgba(1, 22, 1, .142);
  --olive-a7: rgba(6, 17, 1, .181);
  --olive-a8: rgba(4, 15, 1, .279);
  --olive-a9: rgba(4, 15, 0, .471);
  --olive-a10: rgba(2, 12, 0, .518);
  --olive-a11: rgba(2, 10, 0, .628);
  --olive-a12: rgba(1, 6, 0, .891)
}

.dark,
.dark-theme {
  --olive-a1: rgba(0, 224, 0, .005);
  --olive-a2: rgba(80, 246, 80, .018);
  --olive-a3: rgba(213, 254, 213, .074);
  --olive-a4: rgba(217, 253, 217, .109);
  --olive-a5: rgba(225, 254, 225, .139);
  --olive-a6: rgba(231, 254, 231, .174);
  --olive-a7: rgba(237, 255, 237, .221);
  --olive-a8: rgba(238, 254, 238, .317);
  --olive-a9: rgba(229, 255, 221, .381);
  --olive-a10: rgba(237, 255, 231, .464);
  --olive-a11: rgba(246, 255, 243, .671);
  --olive-a12: rgba(253, 255, 253, .927)
}

.light,
.light-theme,
:root {
  --sand-1: #fdfdfc;
  --sand-2: #f9f9f8;
  --sand-3: #f2f2f0;
  --sand-4: #ebebe9;
  --sand-5: #e4e4e2;
  --sand-6: #ddddda;
  --sand-7: #d3d2ce;
  --sand-8: #bcbbb5;
  --sand-9: #8d8d86;
  --sand-10: #80807a;
  --sand-11: #63635e;
  --sand-12: #21201c
}

.dark,
.dark-theme {
  --sand-1: #181816;
  --sand-2: #1b1b1a;
  --sand-3: #282826;
  --sand-4: #30302e;
  --sand-5: #383734;
  --sand-6: #403f3c;
  --sand-7: #4c4b47;
  --sand-8: #62605b;
  --sand-9: #6f6d66;
  --sand-10: #83817a;
  --sand-11: #b2b1aa;
  --sand-12: #eeeeec
}

.light,
.light-theme,
:root {
  --sand-a1: rgba(88, 88, 5, .012);
  --sand-a2: rgba(41, 41, 5, .028);
  --sand-a3: rgba(34, 34, 1, .059);
  --sand-a4: rgba(25, 25, 2, .087);
  --sand-a5: rgba(18, 18, 1, .114);
  --sand-a6: rgba(22, 22, 2, .146);
  --sand-a7: rgba(27, 22, 1, .193);
  --sand-a8: rgba(25, 21, 1, .291);
  --sand-a9: rgba(15, 15, 0, .475);
  --sand-a10: rgba(12, 12, 0, .522);
  --sand-a11: rgba(8, 8, 0, .632);
  --sand-a12: rgba(6, 5, 0, .891)
}

.dark,
.dark-theme {
  --sand-a1: rgba(24, 24, 0, .084);
  --sand-a2: hsla(60, 99%, 85%, .013);
  --sand-a3: hsla(60, 86%, 93%, .07);
  --sand-a4: hsla(60, 98%, 96%, .104);
  --sand-a5: hsla(45, 95%, 94%, .139);
  --sand-a6: hsla(45, 91%, 95%, .174);
  --sand-a7: hsla(48, 92%, 95%, .226);
  --sand-a8: hsla(43, 96%, 96%, .321);
  --sand-a9: hsla(47, 98%, 95%, .377);
  --sand-a10: hsla(47, 96%, 96%, .464);
  --sand-a11: hsla(52, 98%, 98%, .667);
  --sand-a12: rgba(255, 255, 253, .927)
}

:root {
  --black-a1: rgba(0, 0, 0, .012);
  --black-a2: rgba(0, 0, 0, .024);
  --black-a3: rgba(0, 0, 0, .055);
  --black-a4: rgba(0, 0, 0, .078);
  --black-a5: rgba(0, 0, 0, .106);
  --black-a6: rgba(0, 0, 0, .133);
  --black-a7: rgba(0, 0, 0, .169);
  --black-a8: rgba(0, 0, 0, .267);
  --black-a9: rgba(0, 0, 0, .447);
  --black-a10: rgba(0, 0, 0, .498);
  --black-a11: rgba(0, 0, 0, .608);
  --black-a12: rgba(0, 0, 0, .875);
  --white-a1: transparent;
  --white-a2: hsla(0, 0%, 100%, .013);
  --white-a3: hsla(0, 0%, 100%, .069);
  --white-a4: hsla(0, 0%, 100%, .104);
  --white-a5: hsla(0, 0%, 100%, .134);
  --white-a6: hsla(0, 0%, 100%, .169);
  --white-a7: hsla(0, 0%, 100%, .216);
  --white-a8: hsla(0, 0%, 100%, .312);
  --white-a9: hsla(0, 0%, 100%, .372);
  --white-a10: hsla(0, 0%, 100%, .455);
  --white-a11: hsla(0, 0%, 100%, .662);
  --white-a12: hsla(0, 0%, 100%, .926)
}

.radix-themes {
  color: var(--gray-12);
  --color-overlay: var(--gray-a8);
  --color-panel-solid: #fff;
  --color-panel-translucent: hsla(0, 0%, 100%, .8);
  --color-surface: hsla(0, 0%, 100%, .9)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --color-overlay: rgba(0, 0, 0, .75);
  --color-panel-solid: var(--gray-2);
  --color-panel-translucent: var(--gray-2-translucent);
  --color-surface: rgba(0, 0, 0, .25)
}

.radix-themes {
  --color-selection-root: var(--accent-a6)
}

.radix-themes ::-moz-selection {
  background-color: var(--accent-a6)
}

.radix-themes ::selection {
  background-color: var(--accent-a6)
}

.radix-themes [data-accent-color=gray] ::-moz-selection,
.radix-themes [data-accent-color=gray]::-moz-selection {
  background-color: var(--color-selection-root)
}

.radix-themes [data-accent-color=gray] ::selection,
.radix-themes [data-accent-color=gray]::selection {
  background-color: var(--color-selection-root)
}

:root {
  --tomato-9-contrast: #fff;
  --red-9-contrast: #fff;
  --crimson-9-contrast: #fff;
  --pink-9-contrast: #fff;
  --plum-9-contrast: #fff;
  --purple-9-contrast: #fff;
  --violet-9-contrast: #fff;
  --indigo-9-contrast: #fff;
  --blue-9-contrast: #fff;
  --cyan-9-contrast: #fff;
  --teal-9-contrast: #fff;
  --green-9-contrast: #fff;
  --grass-9-contrast: #fff;
  --orange-9-contrast: #fff;
  --brown-9-contrast: #fff;
  --sky-9-contrast: #1c2024;
  --mint-9-contrast: #1a211e;
  --lime-9-contrast: #1d211c;
  --yellow-9-contrast: #21201c;
  --amber-9-contrast: #21201c;
  --gold-9-contrast: #fff;
  --bronze-9-contrast: #fff;
  --gray-9-contrast: #fff
}

.dark,
.dark-theme {
  --gray-2-translucent: rgba(29, 29, 29, .7);
  --mauve-2-translucent: rgba(32, 27, 33, .7);
  --slate-2-translucent: rgba(29, 29, 33, .7);
  --sage-2-translucent: rgba(24, 30, 27, .7);
  --olive-2-translucent: rgba(26, 30, 26, .7);
  --sand-2-translucent: rgba(29, 29, 26, .7)
}

.light,
.light-theme,
:root {
  --tomato-surface: var(--tomato-a2);
  --red-surface: var(--red-a2);
  --crimson-surface: var(--crimson-a2);
  --pink-surface: var(--pink-a2);
  --plum-surface: var(--plum-a2);
  --purple-surface: var(--purple-a2);
  --violet-surface: var(--violet-a2);
  --indigo-surface: var(--indigo-a2);
  --blue-surface: var(--blue-a2);
  --cyan-surface: var(--cyan-a2);
  --teal-surface: var(--teal-a2);
  --green-surface: var(--green-a2);
  --grass-surface: var(--grass-a2);
  --orange-surface: var(--orange-a2);
  --brown-surface: var(--brown-a2);
  --sky-surface: var(--sky-a2);
  --mint-surface: var(--mint-a2);
  --lime-surface: var(--lime-a2);
  --yellow-surface: var(--yellow-a2);
  --amber-surface: var(--amber-a2);
  --gold-surface: var(--gold-a2);
  --bronze-surface: var(--bronze-a2);
  --gray-surface: #fff
}

.dark,
.dark-theme {
  --tomato-surface: var(--tomato-a2);
  --red-surface: var(--red-a2);
  --crimson-surface: var(--crimson-a2);
  --pink-surface: var(--pink-a2);
  --plum-surface: var(--plum-a2);
  --purple-surface: var(--purple-a2);
  --violet-surface: var(--violet-a2);
  --indigo-surface: var(--indigo-a2);
  --blue-surface: var(--blue-a2);
  --cyan-surface: var(--cyan-a2);
  --teal-surface: var(--teal-a2);
  --green-surface: var(--green-a2);
  --grass-surface: var(--grass-a2);
  --orange-surface: var(--orange-a2);
  --brown-surface: var(--brown-a2);
  --sky-surface: var(--sky-a2);
  --mint-surface: var(--mint-a2);
  --lime-surface: var(--lime-a2);
  --yellow-surface: var(--yellow-a2);
  --amber-surface: var(--amber-a2);
  --gold-surface: var(--gold-a2);
  --bronze-surface: var(--bronze-a2);
  --gray-surface: var(--gray-a2)
}

[data-accent-color=tomato] {
  --color-surface-accent: var(--tomato-surface);
  --accent-1: var(--tomato-1);
  --accent-2: var(--tomato-2);
  --accent-3: var(--tomato-3);
  --accent-4: var(--tomato-4);
  --accent-5: var(--tomato-5);
  --accent-6: var(--tomato-6);
  --accent-7: var(--tomato-7);
  --accent-8: var(--tomato-8);
  --accent-9: var(--tomato-9);
  --accent-9-contrast: var(--tomato-9-contrast);
  --accent-10: var(--tomato-10);
  --accent-11: var(--tomato-11);
  --accent-12: var(--tomato-12);
  --accent-a1: var(--tomato-a1);
  --accent-a2: var(--tomato-a2);
  --accent-a3: var(--tomato-a3);
  --accent-a4: var(--tomato-a4);
  --accent-a5: var(--tomato-a5);
  --accent-a6: var(--tomato-a6);
  --accent-a7: var(--tomato-a7);
  --accent-a8: var(--tomato-a8);
  --accent-a9: var(--tomato-a9);
  --accent-a10: var(--tomato-a10);
  --accent-a11: var(--tomato-a11);
  --accent-a12: var(--tomato-a12)
}

[data-accent-color=red] {
  --color-surface-accent: var(--red-surface);
  --accent-1: var(--red-1);
  --accent-2: var(--red-2);
  --accent-3: var(--red-3);
  --accent-4: var(--red-4);
  --accent-5: var(--red-5);
  --accent-6: var(--red-6);
  --accent-7: var(--red-7);
  --accent-8: var(--red-8);
  --accent-9: var(--red-9);
  --accent-9-contrast: var(--red-9-contrast);
  --accent-10: var(--red-10);
  --accent-11: var(--red-11);
  --accent-12: var(--red-12);
  --accent-a1: var(--red-a1);
  --accent-a2: var(--red-a2);
  --accent-a3: var(--red-a3);
  --accent-a4: var(--red-a4);
  --accent-a5: var(--red-a5);
  --accent-a6: var(--red-a6);
  --accent-a7: var(--red-a7);
  --accent-a8: var(--red-a8);
  --accent-a9: var(--red-a9);
  --accent-a10: var(--red-a10);
  --accent-a11: var(--red-a11);
  --accent-a12: var(--red-a12)
}

[data-accent-color=crimson] {
  --color-surface-accent: var(--crimson-surface);
  --accent-1: var(--crimson-1);
  --accent-2: var(--crimson-2);
  --accent-3: var(--crimson-3);
  --accent-4: var(--crimson-4);
  --accent-5: var(--crimson-5);
  --accent-6: var(--crimson-6);
  --accent-7: var(--crimson-7);
  --accent-8: var(--crimson-8);
  --accent-9: var(--crimson-9);
  --accent-9-contrast: var(--crimson-9-contrast);
  --accent-10: var(--crimson-10);
  --accent-11: var(--crimson-11);
  --accent-12: var(--crimson-12);
  --accent-a1: var(--crimson-a1);
  --accent-a2: var(--crimson-a2);
  --accent-a3: var(--crimson-a3);
  --accent-a4: var(--crimson-a4);
  --accent-a5: var(--crimson-a5);
  --accent-a6: var(--crimson-a6);
  --accent-a7: var(--crimson-a7);
  --accent-a8: var(--crimson-a8);
  --accent-a9: var(--crimson-a9);
  --accent-a10: var(--crimson-a10);
  --accent-a11: var(--crimson-a11);
  --accent-a12: var(--crimson-a12)
}

[data-accent-color=pink] {
  --color-surface-accent: var(--pink-surface);
  --accent-1: var(--pink-1);
  --accent-2: var(--pink-2);
  --accent-3: var(--pink-3);
  --accent-4: var(--pink-4);
  --accent-5: var(--pink-5);
  --accent-6: var(--pink-6);
  --accent-7: var(--pink-7);
  --accent-8: var(--pink-8);
  --accent-9: var(--pink-9);
  --accent-9-contrast: var(--pink-9-contrast);
  --accent-10: var(--pink-10);
  --accent-11: var(--pink-11);
  --accent-12: var(--pink-12);
  --accent-a1: var(--pink-a1);
  --accent-a2: var(--pink-a2);
  --accent-a3: var(--pink-a3);
  --accent-a4: var(--pink-a4);
  --accent-a5: var(--pink-a5);
  --accent-a6: var(--pink-a6);
  --accent-a7: var(--pink-a7);
  --accent-a8: var(--pink-a8);
  --accent-a9: var(--pink-a9);
  --accent-a10: var(--pink-a10);
  --accent-a11: var(--pink-a11);
  --accent-a12: var(--pink-a12)
}

[data-accent-color=plum] {
  --color-surface-accent: var(--plum-surface);
  --accent-1: var(--plum-1);
  --accent-2: var(--plum-2);
  --accent-3: var(--plum-3);
  --accent-4: var(--plum-4);
  --accent-5: var(--plum-5);
  --accent-6: var(--plum-6);
  --accent-7: var(--plum-7);
  --accent-8: var(--plum-8);
  --accent-9: var(--plum-9);
  --accent-9-contrast: var(--plum-9-contrast);
  --accent-10: var(--plum-10);
  --accent-11: var(--plum-11);
  --accent-12: var(--plum-12);
  --accent-a1: var(--plum-a1);
  --accent-a2: var(--plum-a2);
  --accent-a3: var(--plum-a3);
  --accent-a4: var(--plum-a4);
  --accent-a5: var(--plum-a5);
  --accent-a6: var(--plum-a6);
  --accent-a7: var(--plum-a7);
  --accent-a8: var(--plum-a8);
  --accent-a9: var(--plum-a9);
  --accent-a10: var(--plum-a10);
  --accent-a11: var(--plum-a11);
  --accent-a12: var(--plum-a12)
}

[data-accent-color=purple] {
  --color-surface-accent: var(--purple-surface);
  --accent-1: var(--purple-1);
  --accent-2: var(--purple-2);
  --accent-3: var(--purple-3);
  --accent-4: var(--purple-4);
  --accent-5: var(--purple-5);
  --accent-6: var(--purple-6);
  --accent-7: var(--purple-7);
  --accent-8: var(--purple-8);
  --accent-9: var(--purple-9);
  --accent-9-contrast: var(--purple-9-contrast);
  --accent-10: var(--purple-10);
  --accent-11: var(--purple-11);
  --accent-12: var(--purple-12);
  --accent-a1: var(--purple-a1);
  --accent-a2: var(--purple-a2);
  --accent-a3: var(--purple-a3);
  --accent-a4: var(--purple-a4);
  --accent-a5: var(--purple-a5);
  --accent-a6: var(--purple-a6);
  --accent-a7: var(--purple-a7);
  --accent-a8: var(--purple-a8);
  --accent-a9: var(--purple-a9);
  --accent-a10: var(--purple-a10);
  --accent-a11: var(--purple-a11);
  --accent-a12: var(--purple-a12)
}

[data-accent-color=violet] {
  --color-surface-accent: var(--violet-surface);
  --accent-1: var(--violet-1);
  --accent-2: var(--violet-2);
  --accent-3: var(--violet-3);
  --accent-4: var(--violet-4);
  --accent-5: var(--violet-5);
  --accent-6: var(--violet-6);
  --accent-7: var(--violet-7);
  --accent-8: var(--violet-8);
  --accent-9: var(--violet-9);
  --accent-9-contrast: var(--violet-9-contrast);
  --accent-10: var(--violet-10);
  --accent-11: var(--violet-11);
  --accent-12: var(--violet-12);
  --accent-a1: var(--violet-a1);
  --accent-a2: var(--violet-a2);
  --accent-a3: var(--violet-a3);
  --accent-a4: var(--violet-a4);
  --accent-a5: var(--violet-a5);
  --accent-a6: var(--violet-a6);
  --accent-a7: var(--violet-a7);
  --accent-a8: var(--violet-a8);
  --accent-a9: var(--violet-a9);
  --accent-a10: var(--violet-a10);
  --accent-a11: var(--violet-a11);
  --accent-a12: var(--violet-a12)
}

[data-accent-color=indigo] {
  --color-surface-accent: var(--indigo-surface);
  --accent-1: var(--indigo-1);
  --accent-2: var(--indigo-2);
  --accent-3: var(--indigo-3);
  --accent-4: var(--indigo-4);
  --accent-5: var(--indigo-5);
  --accent-6: var(--indigo-6);
  --accent-7: var(--indigo-7);
  --accent-8: var(--indigo-8);
  --accent-9: var(--indigo-9);
  --accent-9-contrast: var(--indigo-9-contrast);
  --accent-10: var(--indigo-10);
  --accent-11: var(--indigo-11);
  --accent-12: var(--indigo-12);
  --accent-a1: var(--indigo-a1);
  --accent-a2: var(--indigo-a2);
  --accent-a3: var(--indigo-a3);
  --accent-a4: var(--indigo-a4);
  --accent-a5: var(--indigo-a5);
  --accent-a6: var(--indigo-a6);
  --accent-a7: var(--indigo-a7);
  --accent-a8: var(--indigo-a8);
  --accent-a9: var(--indigo-a9);
  --accent-a10: var(--indigo-a10);
  --accent-a11: var(--indigo-a11);
  --accent-a12: var(--indigo-a12)
}

[data-accent-color=blue] {
  --color-surface-accent: var(--blue-surface);
  --accent-1: var(--blue-1);
  --accent-2: var(--blue-2);
  --accent-3: var(--blue-3);
  --accent-4: var(--blue-4);
  --accent-5: var(--blue-5);
  --accent-6: var(--blue-6);
  --accent-7: var(--blue-7);
  --accent-8: var(--blue-8);
  --accent-9: var(--blue-9);
  --accent-9-contrast: var(--blue-9-contrast);
  --accent-10: var(--blue-10);
  --accent-11: var(--blue-11);
  --accent-12: var(--blue-12);
  --accent-a1: var(--blue-a1);
  --accent-a2: var(--blue-a2);
  --accent-a3: var(--blue-a3);
  --accent-a4: var(--blue-a4);
  --accent-a5: var(--blue-a5);
  --accent-a6: var(--blue-a6);
  --accent-a7: var(--blue-a7);
  --accent-a8: var(--blue-a8);
  --accent-a9: var(--blue-a9);
  --accent-a10: var(--blue-a10);
  --accent-a11: var(--blue-a11);
  --accent-a12: var(--blue-a12)
}

[data-accent-color=cyan] {
  --color-surface-accent: var(--cyan-surface);
  --accent-1: var(--cyan-1);
  --accent-2: var(--cyan-2);
  --accent-3: var(--cyan-3);
  --accent-4: var(--cyan-4);
  --accent-5: var(--cyan-5);
  --accent-6: var(--cyan-6);
  --accent-7: var(--cyan-7);
  --accent-8: var(--cyan-8);
  --accent-9: var(--cyan-9);
  --accent-9-contrast: var(--cyan-9-contrast);
  --accent-10: var(--cyan-10);
  --accent-11: var(--cyan-11);
  --accent-12: var(--cyan-12);
  --accent-a1: var(--cyan-a1);
  --accent-a2: var(--cyan-a2);
  --accent-a3: var(--cyan-a3);
  --accent-a4: var(--cyan-a4);
  --accent-a5: var(--cyan-a5);
  --accent-a6: var(--cyan-a6);
  --accent-a7: var(--cyan-a7);
  --accent-a8: var(--cyan-a8);
  --accent-a9: var(--cyan-a9);
  --accent-a10: var(--cyan-a10);
  --accent-a11: var(--cyan-a11);
  --accent-a12: var(--cyan-a12)
}

[data-accent-color=teal] {
  --color-surface-accent: var(--teal-surface);
  --accent-1: var(--teal-1);
  --accent-2: var(--teal-2);
  --accent-3: var(--teal-3);
  --accent-4: var(--teal-4);
  --accent-5: var(--teal-5);
  --accent-6: var(--teal-6);
  --accent-7: var(--teal-7);
  --accent-8: var(--teal-8);
  --accent-9: var(--teal-9);
  --accent-9-contrast: var(--teal-9-contrast);
  --accent-10: var(--teal-10);
  --accent-11: var(--teal-11);
  --accent-12: var(--teal-12);
  --accent-a1: var(--teal-a1);
  --accent-a2: var(--teal-a2);
  --accent-a3: var(--teal-a3);
  --accent-a4: var(--teal-a4);
  --accent-a5: var(--teal-a5);
  --accent-a6: var(--teal-a6);
  --accent-a7: var(--teal-a7);
  --accent-a8: var(--teal-a8);
  --accent-a9: var(--teal-a9);
  --accent-a10: var(--teal-a10);
  --accent-a11: var(--teal-a11);
  --accent-a12: var(--teal-a12)
}

[data-accent-color=green] {
  --color-surface-accent: var(--green-surface);
  --accent-1: var(--green-1);
  --accent-2: var(--green-2);
  --accent-3: var(--green-3);
  --accent-4: var(--green-4);
  --accent-5: var(--green-5);
  --accent-6: var(--green-6);
  --accent-7: var(--green-7);
  --accent-8: var(--green-8);
  --accent-9: var(--green-9);
  --accent-9-contrast: var(--green-9-contrast);
  --accent-10: var(--green-10);
  --accent-11: var(--green-11);
  --accent-12: var(--green-12);
  --accent-a1: var(--green-a1);
  --accent-a2: var(--green-a2);
  --accent-a3: var(--green-a3);
  --accent-a4: var(--green-a4);
  --accent-a5: var(--green-a5);
  --accent-a6: var(--green-a6);
  --accent-a7: var(--green-a7);
  --accent-a8: var(--green-a8);
  --accent-a9: var(--green-a9);
  --accent-a10: var(--green-a10);
  --accent-a11: var(--green-a11);
  --accent-a12: var(--green-a12)
}

[data-accent-color=grass] {
  --color-surface-accent: var(--grass-surface);
  --accent-1: var(--grass-1);
  --accent-2: var(--grass-2);
  --accent-3: var(--grass-3);
  --accent-4: var(--grass-4);
  --accent-5: var(--grass-5);
  --accent-6: var(--grass-6);
  --accent-7: var(--grass-7);
  --accent-8: var(--grass-8);
  --accent-9: var(--grass-9);
  --accent-9-contrast: var(--grass-9-contrast);
  --accent-10: var(--grass-10);
  --accent-11: var(--grass-11);
  --accent-12: var(--grass-12);
  --accent-a1: var(--grass-a1);
  --accent-a2: var(--grass-a2);
  --accent-a3: var(--grass-a3);
  --accent-a4: var(--grass-a4);
  --accent-a5: var(--grass-a5);
  --accent-a6: var(--grass-a6);
  --accent-a7: var(--grass-a7);
  --accent-a8: var(--grass-a8);
  --accent-a9: var(--grass-a9);
  --accent-a10: var(--grass-a10);
  --accent-a11: var(--grass-a11);
  --accent-a12: var(--grass-a12)
}

[data-accent-color=orange] {
  --color-surface-accent: var(--orange-surface);
  --accent-1: var(--orange-1);
  --accent-2: var(--orange-2);
  --accent-3: var(--orange-3);
  --accent-4: var(--orange-4);
  --accent-5: var(--orange-5);
  --accent-6: var(--orange-6);
  --accent-7: var(--orange-7);
  --accent-8: var(--orange-8);
  --accent-9: var(--orange-9);
  --accent-9-contrast: var(--orange-9-contrast);
  --accent-10: var(--orange-10);
  --accent-11: var(--orange-11);
  --accent-12: var(--orange-12);
  --accent-a1: var(--orange-a1);
  --accent-a2: var(--orange-a2);
  --accent-a3: var(--orange-a3);
  --accent-a4: var(--orange-a4);
  --accent-a5: var(--orange-a5);
  --accent-a6: var(--orange-a6);
  --accent-a7: var(--orange-a7);
  --accent-a8: var(--orange-a8);
  --accent-a9: var(--orange-a9);
  --accent-a10: var(--orange-a10);
  --accent-a11: var(--orange-a11);
  --accent-a12: var(--orange-a12)
}

[data-accent-color=brown] {
  --color-surface-accent: var(--brown-surface);
  --accent-1: var(--brown-1);
  --accent-2: var(--brown-2);
  --accent-3: var(--brown-3);
  --accent-4: var(--brown-4);
  --accent-5: var(--brown-5);
  --accent-6: var(--brown-6);
  --accent-7: var(--brown-7);
  --accent-8: var(--brown-8);
  --accent-9: var(--brown-9);
  --accent-9-contrast: var(--brown-9-contrast);
  --accent-10: var(--brown-10);
  --accent-11: var(--brown-11);
  --accent-12: var(--brown-12);
  --accent-a1: var(--brown-a1);
  --accent-a2: var(--brown-a2);
  --accent-a3: var(--brown-a3);
  --accent-a4: var(--brown-a4);
  --accent-a5: var(--brown-a5);
  --accent-a6: var(--brown-a6);
  --accent-a7: var(--brown-a7);
  --accent-a8: var(--brown-a8);
  --accent-a9: var(--brown-a9);
  --accent-a10: var(--brown-a10);
  --accent-a11: var(--brown-a11);
  --accent-a12: var(--brown-a12)
}

[data-accent-color=sky] {
  --color-surface-accent: var(--sky-surface);
  --accent-1: var(--sky-1);
  --accent-2: var(--sky-2);
  --accent-3: var(--sky-3);
  --accent-4: var(--sky-4);
  --accent-5: var(--sky-5);
  --accent-6: var(--sky-6);
  --accent-7: var(--sky-7);
  --accent-8: var(--sky-8);
  --accent-9: var(--sky-9);
  --accent-9-contrast: var(--sky-9-contrast);
  --accent-10: var(--sky-10);
  --accent-11: var(--sky-11);
  --accent-12: var(--sky-12);
  --accent-a1: var(--sky-a1);
  --accent-a2: var(--sky-a2);
  --accent-a3: var(--sky-a3);
  --accent-a4: var(--sky-a4);
  --accent-a5: var(--sky-a5);
  --accent-a6: var(--sky-a6);
  --accent-a7: var(--sky-a7);
  --accent-a8: var(--sky-a8);
  --accent-a9: var(--sky-a9);
  --accent-a10: var(--sky-a10);
  --accent-a11: var(--sky-a11);
  --accent-a12: var(--sky-a12)
}

[data-accent-color=mint] {
  --color-surface-accent: var(--mint-surface);
  --accent-1: var(--mint-1);
  --accent-2: var(--mint-2);
  --accent-3: var(--mint-3);
  --accent-4: var(--mint-4);
  --accent-5: var(--mint-5);
  --accent-6: var(--mint-6);
  --accent-7: var(--mint-7);
  --accent-8: var(--mint-8);
  --accent-9: var(--mint-9);
  --accent-9-contrast: var(--mint-9-contrast);
  --accent-10: var(--mint-10);
  --accent-11: var(--mint-11);
  --accent-12: var(--mint-12);
  --accent-a1: var(--mint-a1);
  --accent-a2: var(--mint-a2);
  --accent-a3: var(--mint-a3);
  --accent-a4: var(--mint-a4);
  --accent-a5: var(--mint-a5);
  --accent-a6: var(--mint-a6);
  --accent-a7: var(--mint-a7);
  --accent-a8: var(--mint-a8);
  --accent-a9: var(--mint-a9);
  --accent-a10: var(--mint-a10);
  --accent-a11: var(--mint-a11);
  --accent-a12: var(--mint-a12)
}

[data-accent-color=lime] {
  --color-surface-accent: var(--lime-surface);
  --accent-1: var(--lime-1);
  --accent-2: var(--lime-2);
  --accent-3: var(--lime-3);
  --accent-4: var(--lime-4);
  --accent-5: var(--lime-5);
  --accent-6: var(--lime-6);
  --accent-7: var(--lime-7);
  --accent-8: var(--lime-8);
  --accent-9: var(--lime-9);
  --accent-9-contrast: var(--lime-9-contrast);
  --accent-10: var(--lime-10);
  --accent-11: var(--lime-11);
  --accent-12: var(--lime-12);
  --accent-a1: var(--lime-a1);
  --accent-a2: var(--lime-a2);
  --accent-a3: var(--lime-a3);
  --accent-a4: var(--lime-a4);
  --accent-a5: var(--lime-a5);
  --accent-a6: var(--lime-a6);
  --accent-a7: var(--lime-a7);
  --accent-a8: var(--lime-a8);
  --accent-a9: var(--lime-a9);
  --accent-a10: var(--lime-a10);
  --accent-a11: var(--lime-a11);
  --accent-a12: var(--lime-a12)
}

[data-accent-color=yellow] {
  --color-surface-accent: var(--yellow-surface);
  --accent-1: var(--yellow-1);
  --accent-2: var(--yellow-2);
  --accent-3: var(--yellow-3);
  --accent-4: var(--yellow-4);
  --accent-5: var(--yellow-5);
  --accent-6: var(--yellow-6);
  --accent-7: var(--yellow-7);
  --accent-8: var(--yellow-8);
  --accent-9: var(--yellow-9);
  --accent-9-contrast: var(--yellow-9-contrast);
  --accent-10: var(--yellow-10);
  --accent-11: var(--yellow-11);
  --accent-12: var(--yellow-12);
  --accent-a1: var(--yellow-a1);
  --accent-a2: var(--yellow-a2);
  --accent-a3: var(--yellow-a3);
  --accent-a4: var(--yellow-a4);
  --accent-a5: var(--yellow-a5);
  --accent-a6: var(--yellow-a6);
  --accent-a7: var(--yellow-a7);
  --accent-a8: var(--yellow-a8);
  --accent-a9: var(--yellow-a9);
  --accent-a10: var(--yellow-a10);
  --accent-a11: var(--yellow-a11);
  --accent-a12: var(--yellow-a12)
}

[data-accent-color=amber] {
  --color-surface-accent: var(--amber-surface);
  --accent-1: var(--amber-1);
  --accent-2: var(--amber-2);
  --accent-3: var(--amber-3);
  --accent-4: var(--amber-4);
  --accent-5: var(--amber-5);
  --accent-6: var(--amber-6);
  --accent-7: var(--amber-7);
  --accent-8: var(--amber-8);
  --accent-9: var(--amber-9);
  --accent-9-contrast: var(--amber-9-contrast);
  --accent-10: var(--amber-10);
  --accent-11: var(--amber-11);
  --accent-12: var(--amber-12);
  --accent-a1: var(--amber-a1);
  --accent-a2: var(--amber-a2);
  --accent-a3: var(--amber-a3);
  --accent-a4: var(--amber-a4);
  --accent-a5: var(--amber-a5);
  --accent-a6: var(--amber-a6);
  --accent-a7: var(--amber-a7);
  --accent-a8: var(--amber-a8);
  --accent-a9: var(--amber-a9);
  --accent-a10: var(--amber-a10);
  --accent-a11: var(--amber-a11);
  --accent-a12: var(--amber-a12)
}

[data-accent-color=gold] {
  --color-surface-accent: var(--gold-surface);
  --accent-1: var(--gold-1);
  --accent-2: var(--gold-2);
  --accent-3: var(--gold-3);
  --accent-4: var(--gold-4);
  --accent-5: var(--gold-5);
  --accent-6: var(--gold-6);
  --accent-7: var(--gold-7);
  --accent-8: var(--gold-8);
  --accent-9: var(--gold-9);
  --accent-9-contrast: var(--gold-9-contrast);
  --accent-10: var(--gold-10);
  --accent-11: var(--gold-11);
  --accent-12: var(--gold-12);
  --accent-a1: var(--gold-a1);
  --accent-a2: var(--gold-a2);
  --accent-a3: var(--gold-a3);
  --accent-a4: var(--gold-a4);
  --accent-a5: var(--gold-a5);
  --accent-a6: var(--gold-a6);
  --accent-a7: var(--gold-a7);
  --accent-a8: var(--gold-a8);
  --accent-a9: var(--gold-a9);
  --accent-a10: var(--gold-a10);
  --accent-a11: var(--gold-a11);
  --accent-a12: var(--gold-a12)
}

[data-accent-color=bronze] {
  --color-surface-accent: var(--bronze-surface);
  --accent-1: var(--bronze-1);
  --accent-2: var(--bronze-2);
  --accent-3: var(--bronze-3);
  --accent-4: var(--bronze-4);
  --accent-5: var(--bronze-5);
  --accent-6: var(--bronze-6);
  --accent-7: var(--bronze-7);
  --accent-8: var(--bronze-8);
  --accent-9: var(--bronze-9);
  --accent-9-contrast: var(--bronze-9-contrast);
  --accent-10: var(--bronze-10);
  --accent-11: var(--bronze-11);
  --accent-12: var(--bronze-12);
  --accent-a1: var(--bronze-a1);
  --accent-a2: var(--bronze-a2);
  --accent-a3: var(--bronze-a3);
  --accent-a4: var(--bronze-a4);
  --accent-a5: var(--bronze-a5);
  --accent-a6: var(--bronze-a6);
  --accent-a7: var(--bronze-a7);
  --accent-a8: var(--bronze-a8);
  --accent-a9: var(--bronze-a9);
  --accent-a10: var(--bronze-a10);
  --accent-a11: var(--bronze-a11);
  --accent-a12: var(--bronze-a12)
}

[data-gray-color=mauve] {
  --gray-1: var(--mauve-1);
  --gray-2: var(--mauve-2);
  --gray-2-translucent: var(--mauve-2-translucent);
  --gray-3: var(--mauve-3);
  --gray-4: var(--mauve-4);
  --gray-5: var(--mauve-5);
  --gray-6: var(--mauve-6);
  --gray-7: var(--mauve-7);
  --gray-8: var(--mauve-8);
  --gray-9: var(--mauve-9);
  --gray-10: var(--mauve-10);
  --gray-11: var(--mauve-11);
  --gray-12: var(--mauve-12);
  --gray-a1: var(--mauve-a1);
  --gray-a2: var(--mauve-a2);
  --gray-a3: var(--mauve-a3);
  --gray-a4: var(--mauve-a4);
  --gray-a5: var(--mauve-a5);
  --gray-a6: var(--mauve-a6);
  --gray-a7: var(--mauve-a7);
  --gray-a8: var(--mauve-a8);
  --gray-a9: var(--mauve-a9);
  --gray-a10: var(--mauve-a10);
  --gray-a11: var(--mauve-a11);
  --gray-a12: var(--mauve-a12)
}

[data-gray-color=slate] {
  --gray-1: var(--slate-1);
  --gray-2: var(--slate-2);
  --gray-2-translucent: var(--slate-2-translucent);
  --gray-3: var(--slate-3);
  --gray-4: var(--slate-4);
  --gray-5: var(--slate-5);
  --gray-6: var(--slate-6);
  --gray-7: var(--slate-7);
  --gray-8: var(--slate-8);
  --gray-9: var(--slate-9);
  --gray-10: var(--slate-10);
  --gray-11: var(--slate-11);
  --gray-12: var(--slate-12);
  --gray-a1: var(--slate-a1);
  --gray-a2: var(--slate-a2);
  --gray-a3: var(--slate-a3);
  --gray-a4: var(--slate-a4);
  --gray-a5: var(--slate-a5);
  --gray-a6: var(--slate-a6);
  --gray-a7: var(--slate-a7);
  --gray-a8: var(--slate-a8);
  --gray-a9: var(--slate-a9);
  --gray-a10: var(--slate-a10);
  --gray-a11: var(--slate-a11);
  --gray-a12: var(--slate-a12)
}

[data-gray-color=sage] {
  --gray-1: var(--sage-1);
  --gray-2: var(--sage-2);
  --gray-2-translucent: var(--sage-2-translucent);
  --gray-3: var(--sage-3);
  --gray-4: var(--sage-4);
  --gray-5: var(--sage-5);
  --gray-6: var(--sage-6);
  --gray-7: var(--sage-7);
  --gray-8: var(--sage-8);
  --gray-9: var(--sage-9);
  --gray-10: var(--sage-10);
  --gray-11: var(--sage-11);
  --gray-12: var(--sage-12);
  --gray-a1: var(--sage-a1);
  --gray-a2: var(--sage-a2);
  --gray-a3: var(--sage-a3);
  --gray-a4: var(--sage-a4);
  --gray-a5: var(--sage-a5);
  --gray-a6: var(--sage-a6);
  --gray-a7: var(--sage-a7);
  --gray-a8: var(--sage-a8);
  --gray-a9: var(--sage-a9);
  --gray-a10: var(--sage-a10);
  --gray-a11: var(--sage-a11);
  --gray-a12: var(--sage-a12)
}

[data-gray-color=olive] {
  --gray-1: var(--olive-1);
  --gray-2: var(--olive-2);
  --gray-2-translucent: var(--olive-2-translucent);
  --gray-3: var(--olive-3);
  --gray-4: var(--olive-4);
  --gray-5: var(--olive-5);
  --gray-6: var(--olive-6);
  --gray-7: var(--olive-7);
  --gray-8: var(--olive-8);
  --gray-9: var(--olive-9);
  --gray-10: var(--olive-10);
  --gray-11: var(--olive-11);
  --gray-12: var(--olive-12);
  --gray-a1: var(--olive-a1);
  --gray-a2: var(--olive-a2);
  --gray-a3: var(--olive-a3);
  --gray-a4: var(--olive-a4);
  --gray-a5: var(--olive-a5);
  --gray-a6: var(--olive-a6);
  --gray-a7: var(--olive-a7);
  --gray-a8: var(--olive-a8);
  --gray-a9: var(--olive-a9);
  --gray-a10: var(--olive-a10);
  --gray-a11: var(--olive-a11);
  --gray-a12: var(--olive-a12)
}

[data-gray-color=sand] {
  --gray-1: var(--sand-1);
  --gray-2: var(--sand-2);
  --gray-2-translucent: var(--sand-2-translucent);
  --gray-3: var(--sand-3);
  --gray-4: var(--sand-4);
  --gray-5: var(--sand-5);
  --gray-6: var(--sand-6);
  --gray-7: var(--sand-7);
  --gray-8: var(--sand-8);
  --gray-9: var(--sand-9);
  --gray-10: var(--sand-10);
  --gray-11: var(--sand-11);
  --gray-12: var(--sand-12);
  --gray-a1: var(--sand-a1);
  --gray-a2: var(--sand-a2);
  --gray-a3: var(--sand-a3);
  --gray-a4: var(--sand-a4);
  --gray-a5: var(--sand-a5);
  --gray-a6: var(--sand-a6);
  --gray-a7: var(--sand-a7);
  --gray-a8: var(--sand-a8);
  --gray-a9: var(--sand-a9);
  --gray-a10: var(--sand-a10);
  --gray-a11: var(--sand-a11);
  --gray-a12: var(--sand-a12)
}

[data-accent-color=gray] {
  --color-surface-accent: var(--gray-surface);
  --accent-1: var(--gray-1);
  --accent-2: var(--gray-2);
  --accent-3: var(--gray-3);
  --accent-4: var(--gray-4);
  --accent-5: var(--gray-5);
  --accent-6: var(--gray-6);
  --accent-7: var(--gray-7);
  --accent-8: var(--gray-8);
  --accent-9: var(--gray-9);
  --accent-9-contrast: var(--gray-9-contrast);
  --accent-10: var(--gray-10);
  --accent-11: var(--gray-11);
  --accent-12: var(--gray-12);
  --accent-a1: var(--gray-a1);
  --accent-a2: var(--gray-a2);
  --accent-a3: var(--gray-a3);
  --accent-a4: var(--gray-a4);
  --accent-a5: var(--gray-a5);
  --accent-a6: var(--gray-a6);
  --accent-a7: var(--gray-a7);
  --accent-a8: var(--gray-a8);
  --accent-a9: var(--gray-a9);
  --accent-a10: var(--gray-a10);
  --accent-a11: var(--gray-a11);
  --accent-a12: var(--gray-a12)
}

.radix-themes {
  --color-background: #fff
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --color-background: var(--gray-1)
}

.radix-themes:where([data-has-background=true]) {
  background-color: var(--color-background)
}

.radix-themes:where([data-panel-background=solid]) {
  --color-panel: var(--color-panel-solid)
}

.radix-themes:where([data-panel-background=translucent]) {
  --color-panel: var(--color-panel-translucent)
}

.radix-themes {
  --shadow-1: inset 0 0 0 1px var(--gray-a5), inset 0 1.5px 2px 0 var(--black-a6);
  --shadow-2: 0 0 0 1px var(--gray-a3), 0 0 0 0.5px var(--gray-a3), 0px 1px 1px 0px var(--gray-a3), 0px 2px 1px -1px var(--gray-a3), 0px 1px 3px 0px var(--black-a3);
  --shadow-3: 0 0 0 1px var(--gray-a3), 0px 2px 3px -2px var(--gray-a3), 0px 3px 12px -4px var(--black-a3), 0px 4px 16px -8px var(--black-a4);
  --shadow-4: 0 0 0 1px var(--gray-a3), 0px 8px 40px var(--gray-a3), 0px 12px 32px -16px var(--black-a3);
  --shadow-5: 0 0 0 1px var(--gray-a3), 0px 12px 60px var(--gray-a6), 0px 12px 32px -16px var(--black-a6);
  --shadow-6: 0 0 0 1px var(--gray-a3), 0px 16px 64px var(--gray-a7), 0px 16px 36px -20px var(--gray-a7)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --shadow-1: inset 0 1px var(--gray-a4), inset 0 0 0.5px var(--gray-a3), inset 0 -1px 0px var(--gray-a3), inset 0 0 0 1px var(--gray-a6), inset 0 1px 3px 0 var(--black-a10), inset 0 1px 3px 0 var(--black-a12);
  --shadow-2: 0 0 0 1px var(--gray-5), 0 0 0 0.5px var(--black-a4), 0px 2px 1px -1px var(--black-a9), 0px 1px 1px 0px var(--black-a9), 0px 1px 3px 0px var(--black-a9);
  --shadow-3: 0 0 0 1px var(--gray-5), 0px 2px 3px -2px var(--black-a5), 0px 3px 8px -2px var(--black-a8), 0px 4px 12px -4px var(--black-a9);
  --shadow-4: 0 0 0 1px var(--gray-5), 0px 8px 40px var(--black-a7), 0px 12px 32px -16px var(--black-a8);
  --shadow-5: 0 0 0 1px var(--gray-5), 0px 12px 60px var(--black-a8), 0px 12px 32px -16px var(--black-a10);
  --shadow-6: 0 0 0 1px var(--gray-5), 0px 16px 64px var(--black-a11), 0px 16px 36px -20px var(--black-a12)
}

.radix-themes {
  --space-1: calc(4px * var(--scaling));
  --space-2: calc(8px * var(--scaling));
  --space-3: calc(12px * var(--scaling));
  --space-4: calc(16px * var(--scaling));
  --space-5: calc(24px * var(--scaling));
  --space-6: calc(32px * var(--scaling));
  --space-7: calc(40px * var(--scaling));
  --space-8: calc(48px * var(--scaling));
  --space-9: calc(64px * var(--scaling));
  --radius-factor: 1;
  --radius-full: 0px
}

.radix-themes [data-radius],
.radix-themes:where([data-radius]) {
  --radius-1: calc(3px * var(--scaling) * var(--radius-factor));
  --radius-2: calc(4px * var(--scaling) * var(--radius-factor));
  --radius-3: calc(6px * var(--scaling) * var(--radius-factor));
  --radius-4: calc(8px * var(--scaling) * var(--radius-factor));
  --radius-5: calc(12px * var(--scaling) * var(--radius-factor));
  --radius-6: calc(16px * var(--scaling) * var(--radius-factor))
}

.radix-themes [data-radius=none],
.radix-themes:where([data-radius=none]) {
  --radius-factor: 0;
  --radius-full: 0px
}

.radix-themes [data-radius=small],
.radix-themes:where([data-radius=small]) {
  --radius-factor: 0.5;
  --radius-full: 0px
}

.radix-themes [data-radius=medium],
.radix-themes:where([data-radius=medium]) {
  --radius-factor: 1;
  --radius-full: 0px
}

.radix-themes [data-radius=large],
.radix-themes:where([data-radius=large]) {
  --radius-factor: 1.5;
  --radius-full: 0px
}

.radix-themes [data-radius=full],
.radix-themes:where([data-radius=full]) {
  --radius-factor: 2;
  --radius-full: 9999px
}

.radix-themes {
  --scaling: 1
}

.radix-themes:where([data-scaling="90%"]) {
  --scaling: 0.9
}

.radix-themes:where([data-scaling="95%"]) {
  --scaling: 0.95
}

.radix-themes:where([data-scaling="100%"]) {
  --scaling: 1
}

.radix-themes:where([data-scaling="105%"]) {
  --scaling: 1.05
}

.radix-themes:where([data-scaling="110%"]) {
  --scaling: 1.1
}

@media (prefers-reduced-motion:no-preference) {
  @keyframes slideUpAndFadeIn {
    0% {
      opacity: 0;
      transform: translateY(4px) scale(.97)
    }

    to {
      opacity: 1;
      transform: translateY(0) scale(1)
    }
  }

  @keyframes slideUpAndFadeOut {
    0% {
      opacity: 1;
      transform: translateY(0) scale(1)
    }

    to {
      opacity: 0;
      transform: translateY(-4px) scale(.97)
    }
  }

  @keyframes slideDownAndFadeIn {
    0% {
      opacity: 0;
      transform: translateY(-4px) scale(.97)
    }

    to {
      opacity: 1;
      transform: translateY(0) scale(1)
    }
  }

  @keyframes slideDownAndFadeOut {
    0% {
      opacity: 1;
      transform: translateY(0) scale(1)
    }

    to {
      opacity: 0;
      transform: translateY(4px) scale(.97)
    }
  }

  @keyframes slideLeftAndFadeIn {
    0% {
      opacity: 0;
      transform: translateX(4px) scale(.97)
    }

    to {
      opacity: 1;
      transform: translateX(0) scale(1)
    }
  }

  @keyframes slideLeftAndFadeOut {
    0% {
      opacity: 1;
      transform: translateX(0) scale(1)
    }

    to {
      opacity: 0;
      transform: translateX(-4px) scale(.97)
    }
  }

  @keyframes slideRightAndFadeIn {
    0% {
      opacity: 0;
      transform: translateX(-4px) scale(.97)
    }

    to {
      opacity: 1;
      transform: translateX(0) scale(1)
    }
  }

  @keyframes slideRightAndFadeOut {
    0% {
      opacity: 1;
      transform: translateX(0) scale(1)
    }

    to {
      opacity: 0;
      transform: translateX(4px) scale(.97)
    }
  }

  .rt-PopperContent {
    animation-duration: .3s;
    animation-timing-function: cubic-bezier(.16, 1, .3, 1)
  }

  .rt-PopperContent[data-state=open][data-side=top] {
    animation-name: slideUpAndFadeIn
  }

  .rt-PopperContent[data-state=open][data-side=bottom] {
    animation-name: slideDownAndFadeIn
  }

  .rt-PopperContent[data-state=open][data-side=left] {
    animation-name: slideLeftAndFadeIn
  }

  .rt-PopperContent[data-state=open][data-side=right] {
    animation-name: slideRightAndFadeIn
  }

  .rt-PopperContent[data-state=closed] {
    animation-duration: .15s
  }

  .rt-PopperContent[data-state=closed][data-side=top] {
    animation-name: slideDownAndFadeOut
  }

  .rt-PopperContent[data-state=closed][data-side=bottom] {
    animation-name: slideUpAndFadeOut
  }

  .rt-PopperContent[data-state=closed][data-side=left],
  .rt-PopperContent[data-state=closed][data-side=right] {
    animation-name: slideRightAndFadeOut
  }

  @keyframes fadeIn {
    0% {
      opacity: 0
    }

    to {
      opacity: 1
    }
  }

  @keyframes fadeOut {
    0% {
      opacity: 1
    }

    to {
      opacity: 0
    }
  }
}

.rt-AvatarRoot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  vertical-align: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  width: var(--avatar-size);
  height: var(--avatar-size);
  flex-shrink: 0
}

.rt-AvatarImage {
  -o-object-fit: cover;
  object-fit: cover
}

.rt-AvatarFallback,
.rt-AvatarImage {
  width: 100%;
  height: 100%;
  border-radius: inherit
}

.rt-AvatarFallback {
  z-index: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1
}

.rt-AvatarFallback svg {
  width: var(--avatar-font-size-one-letter);
  height: var(--avatar-font-size-one-letter)
}

.rt-AvatarFallback {
  font-weight: var(--font-weight-medium);
  text-transform: uppercase
}

.rt-AvatarFallback.rt-one-letter {
  font-size: var(--avatar-font-size-one-letter)
}

.rt-AvatarFallback.rt-two-letters {
  font-size: var(--avatar-font-size-two-letters, var(--avatar-font-size-one-letter))
}

@media all {
  .rt-AvatarRoot.rt-r-size-1 {
    --avatar-size: var(--space-5);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-2);
    --avatar-font-size-two-letters: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-AvatarRoot.rt-r-size-2 {
    --avatar-size: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-3);
    --avatar-font-size-two-letters: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-AvatarRoot.rt-r-size-3 {
    --avatar-size: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-4);
    --avatar-font-size-two-letters: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-AvatarRoot.rt-r-size-4 {
    --avatar-size: var(--space-8);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-5);
    --avatar-font-size-two-letters: var(--font-size-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-AvatarRoot.rt-r-size-5 {
    --avatar-size: var(--space-9);
    border-radius: max(var(--radius-4), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-6);
    letter-spacing: var(--letter-spacing-6)
  }

  .rt-AvatarRoot.rt-r-size-6 {
    --avatar-size: 80px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.rt-r-size-6,
  .rt-AvatarRoot.rt-r-size-7 {
    border-radius: max(var(--radius-5), var(--radius-full));
    letter-spacing: var(--letter-spacing-7)
  }

  .rt-AvatarRoot.rt-r-size-7 {
    --avatar-size: 96px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.rt-r-size-8 {
    --avatar-size: 128px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-8);
    letter-spacing: var(--letter-spacing-8)
  }

  .rt-AvatarRoot.rt-r-size-9 {
    --avatar-size: 160px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-9);
    letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:520px) {
  .rt-AvatarRoot.xs\:rt-r-size-1 {
    --avatar-size: var(--space-5);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-2);
    --avatar-font-size-two-letters: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-AvatarRoot.xs\:rt-r-size-2 {
    --avatar-size: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-3);
    --avatar-font-size-two-letters: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-AvatarRoot.xs\:rt-r-size-3 {
    --avatar-size: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-4);
    --avatar-font-size-two-letters: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-AvatarRoot.xs\:rt-r-size-4 {
    --avatar-size: var(--space-8);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-5);
    --avatar-font-size-two-letters: var(--font-size-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-AvatarRoot.xs\:rt-r-size-5 {
    --avatar-size: var(--space-9);
    border-radius: max(var(--radius-4), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-6);
    letter-spacing: var(--letter-spacing-6)
  }

  .rt-AvatarRoot.xs\:rt-r-size-6 {
    --avatar-size: 80px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.xs\:rt-r-size-6,
  .rt-AvatarRoot.xs\:rt-r-size-7 {
    border-radius: max(var(--radius-5), var(--radius-full));
    letter-spacing: var(--letter-spacing-7)
  }

  .rt-AvatarRoot.xs\:rt-r-size-7 {
    --avatar-size: 96px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.xs\:rt-r-size-8 {
    --avatar-size: 128px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-8);
    letter-spacing: var(--letter-spacing-8)
  }

  .rt-AvatarRoot.xs\:rt-r-size-9 {
    --avatar-size: 160px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-9);
    letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:768px) {
  .rt-AvatarRoot.sm\:rt-r-size-1 {
    --avatar-size: var(--space-5);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-2);
    --avatar-font-size-two-letters: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-AvatarRoot.sm\:rt-r-size-2 {
    --avatar-size: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-3);
    --avatar-font-size-two-letters: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-AvatarRoot.sm\:rt-r-size-3 {
    --avatar-size: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-4);
    --avatar-font-size-two-letters: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-AvatarRoot.sm\:rt-r-size-4 {
    --avatar-size: var(--space-8);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-5);
    --avatar-font-size-two-letters: var(--font-size-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-AvatarRoot.sm\:rt-r-size-5 {
    --avatar-size: var(--space-9);
    border-radius: max(var(--radius-4), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-6);
    letter-spacing: var(--letter-spacing-6)
  }

  .rt-AvatarRoot.sm\:rt-r-size-6 {
    --avatar-size: 80px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.sm\:rt-r-size-6,
  .rt-AvatarRoot.sm\:rt-r-size-7 {
    border-radius: max(var(--radius-5), var(--radius-full));
    letter-spacing: var(--letter-spacing-7)
  }

  .rt-AvatarRoot.sm\:rt-r-size-7 {
    --avatar-size: 96px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.sm\:rt-r-size-8 {
    --avatar-size: 128px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-8);
    letter-spacing: var(--letter-spacing-8)
  }

  .rt-AvatarRoot.sm\:rt-r-size-9 {
    --avatar-size: 160px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-9);
    letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1024px) {
  .rt-AvatarRoot.md\:rt-r-size-1 {
    --avatar-size: var(--space-5);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-2);
    --avatar-font-size-two-letters: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-AvatarRoot.md\:rt-r-size-2 {
    --avatar-size: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-3);
    --avatar-font-size-two-letters: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-AvatarRoot.md\:rt-r-size-3 {
    --avatar-size: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-4);
    --avatar-font-size-two-letters: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-AvatarRoot.md\:rt-r-size-4 {
    --avatar-size: var(--space-8);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-5);
    --avatar-font-size-two-letters: var(--font-size-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-AvatarRoot.md\:rt-r-size-5 {
    --avatar-size: var(--space-9);
    border-radius: max(var(--radius-4), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-6);
    letter-spacing: var(--letter-spacing-6)
  }

  .rt-AvatarRoot.md\:rt-r-size-6 {
    --avatar-size: 80px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.md\:rt-r-size-6,
  .rt-AvatarRoot.md\:rt-r-size-7 {
    border-radius: max(var(--radius-5), var(--radius-full));
    letter-spacing: var(--letter-spacing-7)
  }

  .rt-AvatarRoot.md\:rt-r-size-7 {
    --avatar-size: 96px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.md\:rt-r-size-8 {
    --avatar-size: 128px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-8);
    letter-spacing: var(--letter-spacing-8)
  }

  .rt-AvatarRoot.md\:rt-r-size-9 {
    --avatar-size: 160px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-9);
    letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1280px) {
  .rt-AvatarRoot.lg\:rt-r-size-1 {
    --avatar-size: var(--space-5);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-2);
    --avatar-font-size-two-letters: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-AvatarRoot.lg\:rt-r-size-2 {
    --avatar-size: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-3);
    --avatar-font-size-two-letters: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-AvatarRoot.lg\:rt-r-size-3 {
    --avatar-size: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-4);
    --avatar-font-size-two-letters: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-AvatarRoot.lg\:rt-r-size-4 {
    --avatar-size: var(--space-8);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-5);
    --avatar-font-size-two-letters: var(--font-size-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-AvatarRoot.lg\:rt-r-size-5 {
    --avatar-size: var(--space-9);
    border-radius: max(var(--radius-4), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-6);
    letter-spacing: var(--letter-spacing-6)
  }

  .rt-AvatarRoot.lg\:rt-r-size-6 {
    --avatar-size: 80px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.lg\:rt-r-size-6,
  .rt-AvatarRoot.lg\:rt-r-size-7 {
    border-radius: max(var(--radius-5), var(--radius-full));
    letter-spacing: var(--letter-spacing-7)
  }

  .rt-AvatarRoot.lg\:rt-r-size-7 {
    --avatar-size: 96px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.lg\:rt-r-size-8 {
    --avatar-size: 128px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-8);
    letter-spacing: var(--letter-spacing-8)
  }

  .rt-AvatarRoot.lg\:rt-r-size-9 {
    --avatar-size: 160px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-9);
    letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1640px) {
  .rt-AvatarRoot.xl\:rt-r-size-1 {
    --avatar-size: var(--space-5);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-2);
    --avatar-font-size-two-letters: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-AvatarRoot.xl\:rt-r-size-2 {
    --avatar-size: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-3);
    --avatar-font-size-two-letters: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-AvatarRoot.xl\:rt-r-size-3 {
    --avatar-size: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-4);
    --avatar-font-size-two-letters: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-AvatarRoot.xl\:rt-r-size-4 {
    --avatar-size: var(--space-8);
    border-radius: max(var(--radius-3), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-5);
    --avatar-font-size-two-letters: var(--font-size-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-AvatarRoot.xl\:rt-r-size-5 {
    --avatar-size: var(--space-9);
    border-radius: max(var(--radius-4), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-6);
    letter-spacing: var(--letter-spacing-6)
  }

  .rt-AvatarRoot.xl\:rt-r-size-6 {
    --avatar-size: 80px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.xl\:rt-r-size-6,
  .rt-AvatarRoot.xl\:rt-r-size-7 {
    border-radius: max(var(--radius-5), var(--radius-full));
    letter-spacing: var(--letter-spacing-7)
  }

  .rt-AvatarRoot.xl\:rt-r-size-7 {
    --avatar-size: 96px;
    --avatar-font-size-one-letter: var(--font-size-7)
  }

  .rt-AvatarRoot.xl\:rt-r-size-8 {
    --avatar-size: 128px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-8);
    letter-spacing: var(--letter-spacing-8)
  }

  .rt-AvatarRoot.xl\:rt-r-size-9 {
    --avatar-size: 160px;
    border-radius: max(var(--radius-6), var(--radius-full));
    --avatar-font-size-one-letter: var(--font-size-9);
    letter-spacing: var(--letter-spacing-9)
  }
}

.rt-AvatarRoot.rt-variant-solid .rt-AvatarFallback {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-AvatarRoot.rt-variant-solid:where(.rt-high-contrast) .rt-AvatarFallback {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-AvatarRoot.rt-variant-soft .rt-AvatarFallback {
  background-color: var(--accent-a3);
  color: var(--accent-a11)
}

.rt-AvatarRoot.rt-variant-soft:where(.rt-high-contrast) .rt-AvatarFallback {
  color: var(--accent-12)
}

.rt-Badge {
  display: inline-flex;
  align-items: center;
  box-sizing: border-box;
  white-space: nowrap;
  font-weight: var(--font-weight-medium);
  flex-shrink: 0;
  line-height: 1;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  cursor: default
}

@media all {
  .rt-Badge.rt-r-size-1 {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    padding: calc(var(--space-1) / 2) var(--space-2);
    gap: var(--space-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-Badge.rt-r-size-2 {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    padding: calc(var(--space-1) * 1.5) var(--space-4);
    gap: var(--space-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }
}

@media (min-width:520px) {
  .rt-Badge.xs\:rt-r-size-1 {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    padding: calc(var(--space-1) / 2) var(--space-2);
    gap: var(--space-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-Badge.xs\:rt-r-size-2 {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    padding: calc(var(--space-1) * 1.5) var(--space-4);
    gap: var(--space-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }
}

@media (min-width:768px) {
  .rt-Badge.sm\:rt-r-size-1 {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    padding: calc(var(--space-1) / 2) var(--space-2);
    gap: var(--space-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-Badge.sm\:rt-r-size-2 {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    padding: calc(var(--space-1) * 1.5) var(--space-4);
    gap: var(--space-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }
}

@media (min-width:1024px) {
  .rt-Badge.md\:rt-r-size-1 {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    padding: calc(var(--space-1) / 2) var(--space-2);
    gap: var(--space-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-Badge.md\:rt-r-size-2 {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    padding: calc(var(--space-1) * 1.5) var(--space-4);
    gap: var(--space-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }
}

@media (min-width:1280px) {
  .rt-Badge.lg\:rt-r-size-1 {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    padding: calc(var(--space-1) / 2) var(--space-2);
    gap: var(--space-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-Badge.lg\:rt-r-size-2 {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    padding: calc(var(--space-1) * 1.5) var(--space-4);
    gap: var(--space-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }
}

@media (min-width:1640px) {
  .rt-Badge.xl\:rt-r-size-1 {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    padding: calc(var(--space-1) / 2) var(--space-2);
    gap: var(--space-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-Badge.xl\:rt-r-size-2 {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    padding: calc(var(--space-1) * 1.5) var(--space-4);
    gap: var(--space-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }
}

.rt-Badge.rt-variant-solid {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-Badge.rt-variant-solid:where(.rt-high-contrast) {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-Badge.rt-variant-surface {
  background-color: var(--color-surface-accent);
  box-shadow: inset 0 0 0 1px var(--accent-a7);
  color: var(--accent-a11)
}

.rt-Badge.rt-variant-surface:where(.rt-high-contrast) {
  color: var(--accent-12)
}

.rt-Badge.rt-variant-soft {
  background-color: var(--accent-a3);
  color: var(--accent-a11)
}

.rt-Badge.rt-variant-soft:where(.rt-high-contrast) {
  color: var(--accent-12)
}

.rt-Badge.rt-variant-outline {
  box-shadow: inset 0 0 0 1px var(--accent-a8);
  color: var(--accent-a11)
}

.rt-Badge.rt-variant-outline:where(.rt-high-contrast) {
  box-shadow: inset 0 0 0 1px var(--accent-a7), inset 0 0 0 1px var(--gray-a11);
  color: var(--accent-12)
}

.rt-Blockquote {
  border-left: max(var(--space-1), .25em) solid var(--accent-a6);
  padding-left: min(var(--space-5), max(var(--space-3), .5em))
}

.rt-BaseButton,
.rt-Box {
  box-sizing: border-box
}

.rt-BaseButton {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  vertical-align: top
}

.rt-BaseButton:where(:not(.rt-variant-ghost)) {
  height: var(--base-button-height)
}

.rt-BaseButton:where(.rt-variant-ghost) {
  box-sizing: content-box;
  height: -moz-fit-content;
  height: fit-content
}

@media all {
  .rt-BaseButton.rt-r-size-1 {
    --base-button__classic-active__offset-override: 1px;
    --base-button-height: var(--space-5);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-BaseButton.rt-r-size-2 {
    --base-button-height: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-BaseButton.rt-r-size-3 {
    --base-button-height: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-BaseButton.rt-r-size-4 {
    --base-button-height: var(--space-8);
    border-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:520px) {
  .rt-BaseButton.xs\:rt-r-size-1 {
    --base-button__classic-active__offset-override: 1px;
    --base-button-height: var(--space-5);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-BaseButton.xs\:rt-r-size-2 {
    --base-button-height: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-BaseButton.xs\:rt-r-size-3 {
    --base-button-height: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-BaseButton.xs\:rt-r-size-4 {
    --base-button-height: var(--space-8);
    border-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:768px) {
  .rt-BaseButton.sm\:rt-r-size-1 {
    --base-button__classic-active__offset-override: 1px;
    --base-button-height: var(--space-5);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-BaseButton.sm\:rt-r-size-2 {
    --base-button-height: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-BaseButton.sm\:rt-r-size-3 {
    --base-button-height: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-BaseButton.sm\:rt-r-size-4 {
    --base-button-height: var(--space-8);
    border-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:1024px) {
  .rt-BaseButton.md\:rt-r-size-1 {
    --base-button__classic-active__offset-override: 1px;
    --base-button-height: var(--space-5);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-BaseButton.md\:rt-r-size-2 {
    --base-button-height: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-BaseButton.md\:rt-r-size-3 {
    --base-button-height: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-BaseButton.md\:rt-r-size-4 {
    --base-button-height: var(--space-8);
    border-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:1280px) {
  .rt-BaseButton.lg\:rt-r-size-1 {
    --base-button__classic-active__offset-override: 1px;
    --base-button-height: var(--space-5);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-BaseButton.lg\:rt-r-size-2 {
    --base-button-height: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-BaseButton.lg\:rt-r-size-3 {
    --base-button-height: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-BaseButton.lg\:rt-r-size-4 {
    --base-button-height: var(--space-8);
    border-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:1640px) {
  .rt-BaseButton.xl\:rt-r-size-1 {
    --base-button__classic-active__offset-override: 1px;
    --base-button-height: var(--space-5);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-BaseButton.xl\:rt-r-size-2 {
    --base-button-height: var(--space-6);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-BaseButton.xl\:rt-r-size-3 {
    --base-button-height: var(--space-7);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-BaseButton.xl\:rt-r-size-4 {
    --base-button-height: var(--space-8);
    border-radius: max(var(--radius-4), var(--radius-full))
  }
}

.radix-themes {
  --button__classic__pseudo-inset: 1px;
  --button__classic__border: initial;
  --button__classic-hover-high-contrast__overlay-color: var(--black-a7);
  --button__classic__shadows: inset 0 1px 0 1px var(--white-a10), inset 0 6px 4px -4px var(--white-a8), inset 0 -1px 0.5px 1px var(--black-a8);
  --button__classic-active__shadows: inset 0 1px 0 1px var(--black-a4), inset 0 6px 4px -4px var(--black-a8), inset 0 -1px 0 1px var(--white-a3), inset 0 -6px 4px -4px var(--white-a6)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --button__classic__pseudo-inset: 0px;
  --button__classic__border: 0 0 0 1px var(--black-a8);
  --button__classic-hover-high-contrast__overlay-color: var(--black-a4);
  --button__classic__shadows: inset 0 1px 0 0 var(--white-a8), inset 0 5px 3px -3px var(--white-a8), inset 0 -1px 0.5px 0 var(--black-a10);
  --button__classic-active__shadows: inset 0 1px 0 0 var(--black-a5), inset 0 5px 3px -3px var(--black-a8), inset 0 -1px 0 0 var(--white-a3), inset 0 -5px 3px -3px var(--white-a6)
}

.rt-BaseButton.rt-variant-classic {
  background-color: var(--accent-9);
  background-image: linear-gradient(var(--black-a2), transparent 50%);
  color: var(--accent-9-contrast);
  --button__classic__box-shadow: var(--button__classic__border, inset 0 0 0 1px var(--black-a5), inset 0 0 0 1px var(--accent-10)), var(--button__classic__shadows);
  box-shadow: var(--button__classic__box-shadow);
  position: relative;
  z-index: 0
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-classic:where(:hover) {
    background-image: linear-gradient(var(--black-a4), transparent)
  }

  .rt-BaseButton.rt-variant-classic:where(:hover):where(.rt-high-contrast) {
    background-image: linear-gradient(var(--button__classic-hover-high-contrast__overlay-color), var(--button__classic-hover-high-contrast__overlay-color))
  }
}

.rt-BaseButton.rt-variant-classic:where([data-state=open]) {
  background-image: linear-gradient(var(--black-a4), transparent)
}

.rt-BaseButton.rt-variant-classic:where([data-state=open]):where(.rt-high-contrast) {
  background-image: linear-gradient(var(--button__classic-hover-high-contrast__overlay-color), var(--button__classic-hover-high-contrast__overlay-color))
}

.rt-BaseButton.rt-variant-classic:where(:active:not([data-state=open], :disabled)) {
  background-image: linear-gradient(var(--black-a6), transparent);
  padding-top: var(--base-button__classic-active__offset-override, 2px);
  --button__classic__box-shadow: var(--button__classic__border, inset 0 0 0 1px var(--black-a10), inset 0 0 0 1px var(--accent-10)), var(--button__classic-active__shadows)
}

.rt-BaseButton.rt-variant-classic:where(:active:not([data-state=open], :disabled)):after {
  opacity: 0
}

.rt-BaseButton.rt-variant-classic:after,
.rt-BaseButton.rt-variant-classic:before {
  content: "";
  position: absolute;
  inset: var(--button__classic__pseudo-inset);
  border-radius: inherit;
  pointer-events: none
}

.rt-BaseButton.rt-variant-classic:before {
  z-index: 1;
  background-image: linear-gradient(var(--accent-a4), transparent 50%);
  mix-blend-mode: darken
}

.rt-BaseButton.rt-variant-classic:after {
  z-index: 2;
  background-image: linear-gradient(transparent 50%, var(--white-a8));
  mix-blend-mode: soft-light
}

.rt-BaseButton.rt-variant-classic:where(:focus-visible) {
  box-shadow: 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8), var(--button__classic__box-shadow)
}

.rt-BaseButton.rt-variant-classic:where(.rt-high-contrast) {
  background-color: var(--accent-12);
  color: var(--gray-1);
  --button__classic__box-shadow: var(--button__classic__border, inset 0 0 0 1px var(--black-a8), inset 0 0 0 1px var(--accent-12)), var(--button__classic__shadows)
}

.rt-BaseButton.rt-variant-classic:where(.rt-high-contrast):active:not([data-state=open]) {
  --button__classic__box-shadow: var(--button__classic__border, inset 0 0 0 1px var(--black-a10), inset 0 0 0 1px var(--accent-12)), var(--button__classic-active__shadows)
}

.radix-themes {
  --button-filter__solid-active: brightness(0.92) saturate(1.1);
  --button-filter__solid-high-contrast-hover: contrast(0.88) saturate(1.1) brightness(1.1);
  --button-filter__solid-high-contrast-active: contrast(0.82) saturate(1.2) brightness(1.16)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --button-filter__solid-active: brightness(1.08);
  --button-filter__solid-high-contrast-hover: brightness(0.95) saturate(1.1);
  --button-filter__solid-high-contrast-active: brightness(0.9) saturate(1.2)
}

.rt-BaseButton.rt-variant-solid {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-solid:where(:hover) {
    background-color: var(--accent-10)
  }
}

.rt-BaseButton.rt-variant-solid:where([data-state=open]) {
  background-color: var(--accent-10)
}

.rt-BaseButton.rt-variant-solid:where(:active:not([data-state=open])) {
  background-color: var(--accent-10);
  filter: var(--button-filter__solid-active)
}

.rt-BaseButton.rt-variant-solid:where(:focus-visible) {
  box-shadow: 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-BaseButton.rt-variant-solid:where(.rt-high-contrast) {
  background-color: var(--accent-12);
  color: var(--gray-1)
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-solid:where(.rt-high-contrast):where(:hover) {
    background-color: var(--accent-12);
    filter: var(--button-filter__solid-high-contrast-hover)
  }
}

.rt-BaseButton.rt-variant-solid:where(.rt-high-contrast):where([data-state=open]) {
  background-color: var(--accent-12);
  filter: var(--button-filter__solid-high-contrast-hover)
}

.rt-BaseButton.rt-variant-solid:where(.rt-high-contrast):where(:active:not([data-state=open])) {
  background-color: var(--accent-12);
  filter: var(--button-filter__solid-high-contrast-active)
}

.rt-BaseButton.rt-variant-ghost,
.rt-BaseButton.rt-variant-soft {
  color: var(--accent-a11)
}

.rt-BaseButton.rt-variant-ghost:where(:focus-visible),
.rt-BaseButton.rt-variant-soft:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-BaseButton.rt-variant-ghost:where(.rt-high-contrast),
.rt-BaseButton.rt-variant-soft:where(.rt-high-contrast) {
  color: var(--accent-12)
}

.rt-BaseButton.rt-variant-soft {
  background-color: var(--accent-a3)
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-soft:where(:hover) {
    background-color: var(--accent-a4)
  }
}

.rt-BaseButton.rt-variant-soft:where([data-state=open]) {
  background-color: var(--accent-a4)
}

.rt-BaseButton.rt-variant-soft:where(:active:not([data-state=open])) {
  background-color: var(--accent-a5)
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-ghost:where(:hover) {
    background-color: var(--accent-a3)
  }
}

.rt-BaseButton.rt-variant-ghost:where([data-state=open]) {
  background-color: var(--accent-a3)
}

.rt-BaseButton.rt-variant-ghost:where(:active:not([data-state=open])) {
  background-color: var(--accent-a4)
}

.rt-BaseButton.rt-variant-outline {
  box-shadow: inset 0 0 0 1px var(--accent-a8);
  color: var(--accent-a11)
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-outline:where(:hover) {
    background-color: var(--accent-a2)
  }
}

.rt-BaseButton.rt-variant-outline:where([data-state=open]) {
  background-color: var(--accent-a2)
}

.rt-BaseButton.rt-variant-outline:where(:active:not([data-state=open])) {
  background-color: var(--accent-a3)
}

.rt-BaseButton.rt-variant-outline:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-a8), 0 0 0 1px var(--accent-a8)
}

.rt-BaseButton.rt-variant-outline:where(.rt-high-contrast) {
  box-shadow: inset 0 0 0 1px var(--accent-a7), inset 0 0 0 1px var(--gray-a11);
  color: var(--accent-12)
}

.rt-BaseButton.rt-variant-outline:where(.rt-high-contrast):where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-a7), inset 0 0 0 1px var(--gray-a12), 0 0 0 1px var(--accent-a7), 0 0 0 1px var(--gray-a12)
}

.rt-BaseButton.rt-variant-surface {
  background-color: var(--color-surface-accent);
  box-shadow: inset 0 0 0 1px var(--accent-a7);
  color: var(--accent-a11)
}

@media (hover:hover) {
  .rt-BaseButton.rt-variant-surface:where(:hover) {
    box-shadow: inset 0 0 0 1px var(--accent-a8)
  }
}

.rt-BaseButton.rt-variant-surface:where([data-state=open]) {
  box-shadow: inset 0 0 0 1px var(--accent-a8)
}

.rt-BaseButton.rt-variant-surface:where(:active:not([data-state=open])) {
  background-color: var(--accent-a3);
  box-shadow: inset 0 0 0 1px var(--accent-a8)
}

.rt-BaseButton.rt-variant-surface:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-BaseButton.rt-variant-surface:where(.rt-high-contrast) {
  color: var(--accent-12)
}

.rt-BaseButton:disabled {
  color: var(--gray-a8);
  cursor: not-allowed;
  box-shadow: none;
  filter: none;
  background-color: transparent;
  background-image: none
}

.rt-BaseButton:disabled:where(:not(.rt-variant-ghost)) {
  background-color: var(--gray-a3)
}

.rt-BaseButton:disabled:after,
.rt-BaseButton:disabled:before {
  display: none
}

.rt-Button:where(:not(.rt-variant-ghost)) svg {
  opacity: .9
}

.rt-Button:where(.rt-variant-ghost) {
  padding: var(--button-ghost-padding-y) var(--button-ghost-padding-x);
  --margin-top: 0px;
  --margin-right: 0px;
  --margin-bottom: 0px;
  --margin-left: 0px;
  --margin-top-override: calc(var(--margin-top, 0px) - var(--button-ghost-padding-y));
  --margin-right-override: calc(var(--margin-right, 0px) - var(--button-ghost-padding-x));
  --margin-bottom-override: calc(var(--margin-bottom, 0px) - var(--button-ghost-padding-y));
  --margin-left-override: calc(var(--margin-left, 0px) - var(--button-ghost-padding-x));
  margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
}

:where(.rt-Button:where(.rt-variant-ghost))>* {
  --margin-top-override: initial;
  --margin-right-override: initial;
  --margin-bottom-override: initial;
  --margin-left-override: initial
}

@media all {
  .rt-Button.rt-r-size-1 {
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-Button.rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-Button.rt-r-size-1:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.rt-r-size-2 {
    gap: var(--space-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-Button.rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-Button.rt-r-size-2:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.rt-r-size-3 {
    gap: var(--space-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-Button.rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-Button.rt-r-size-3:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-3);
    --button-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-Button.rt-r-size-4 {
    gap: var(--space-3);
    font-size: var(--font-size-4);
    line-height: var(--line-height-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-Button.rt-r-size-4:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-Button.rt-r-size-4:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-4);
    --button-ghost-padding-y: var(--space-2)
  }
}

@media (min-width:520px) {
  .rt-Button.xs\:rt-r-size-1 {
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-Button.xs\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-Button.xs\:rt-r-size-1:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.xs\:rt-r-size-2 {
    gap: var(--space-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-Button.xs\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-Button.xs\:rt-r-size-2:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.xs\:rt-r-size-3 {
    gap: var(--space-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-Button.xs\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-Button.xs\:rt-r-size-3:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-3);
    --button-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-Button.xs\:rt-r-size-4 {
    gap: var(--space-3);
    font-size: var(--font-size-4);
    line-height: var(--line-height-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-Button.xs\:rt-r-size-4:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-Button.xs\:rt-r-size-4:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-4);
    --button-ghost-padding-y: var(--space-2)
  }
}

@media (min-width:768px) {
  .rt-Button.sm\:rt-r-size-1 {
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-Button.sm\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-Button.sm\:rt-r-size-1:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.sm\:rt-r-size-2 {
    gap: var(--space-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-Button.sm\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-Button.sm\:rt-r-size-2:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.sm\:rt-r-size-3 {
    gap: var(--space-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-Button.sm\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-Button.sm\:rt-r-size-3:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-3);
    --button-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-Button.sm\:rt-r-size-4 {
    gap: var(--space-3);
    font-size: var(--font-size-4);
    line-height: var(--line-height-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-Button.sm\:rt-r-size-4:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-Button.sm\:rt-r-size-4:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-4);
    --button-ghost-padding-y: var(--space-2)
  }
}

@media (min-width:1024px) {
  .rt-Button.md\:rt-r-size-1 {
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-Button.md\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-Button.md\:rt-r-size-1:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.md\:rt-r-size-2 {
    gap: var(--space-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-Button.md\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-Button.md\:rt-r-size-2:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.md\:rt-r-size-3 {
    gap: var(--space-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-Button.md\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-Button.md\:rt-r-size-3:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-3);
    --button-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-Button.md\:rt-r-size-4 {
    gap: var(--space-3);
    font-size: var(--font-size-4);
    line-height: var(--line-height-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-Button.md\:rt-r-size-4:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-Button.md\:rt-r-size-4:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-4);
    --button-ghost-padding-y: var(--space-2)
  }
}

@media (min-width:1280px) {
  .rt-Button.lg\:rt-r-size-1 {
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-Button.lg\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-Button.lg\:rt-r-size-1:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.lg\:rt-r-size-2 {
    gap: var(--space-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-Button.lg\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-Button.lg\:rt-r-size-2:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.lg\:rt-r-size-3 {
    gap: var(--space-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-Button.lg\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-Button.lg\:rt-r-size-3:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-3);
    --button-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-Button.lg\:rt-r-size-4 {
    gap: var(--space-3);
    font-size: var(--font-size-4);
    line-height: var(--line-height-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-Button.lg\:rt-r-size-4:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-Button.lg\:rt-r-size-4:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-4);
    --button-ghost-padding-y: var(--space-2)
  }
}

@media (min-width:1640px) {
  .rt-Button.xl\:rt-r-size-1 {
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-Button.xl\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-Button.xl\:rt-r-size-1:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.xl\:rt-r-size-2 {
    gap: var(--space-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-Button.xl\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-Button.xl\:rt-r-size-2:where(.rt-variant-ghost) {
    gap: var(--space-1);
    --button-ghost-padding-x: var(--space-2);
    --button-ghost-padding-y: var(--space-1)
  }

  .rt-Button.xl\:rt-r-size-3 {
    gap: var(--space-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-Button.xl\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-Button.xl\:rt-r-size-3:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-3);
    --button-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-Button.xl\:rt-r-size-4 {
    gap: var(--space-3);
    font-size: var(--font-size-4);
    line-height: var(--line-height-4);
    letter-spacing: var(--letter-spacing-4)
  }

  .rt-Button.xl\:rt-r-size-4:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-Button.xl\:rt-r-size-4:where(.rt-variant-ghost) {
    gap: var(--space-2);
    --button-ghost-padding-x: var(--space-4);
    --button-ghost-padding-y: var(--space-2)
  }
}

.rt-Button:where(:not(.rt-variant-ghost)) {
  font-weight: var(--font-weight-medium)
}

.rt-CalloutRoot {
  display: flex;
  flex-wrap: nowrap;
  align-items: flex-start;
  text-align: left
}

.rt-CalloutIcon {
  display: inline-flex;
  align-items: center;
  vertical-align: bottom;
  flex-shrink: 0;
  height: var(--line-height)
}

.rt-CalloutIcon>svg {
  display: block
}

@media all {
  .rt-CalloutRoot.rt-r-size-1 {
    gap: var(--space-2);
    padding: var(--space-3);
    border-radius: var(--radius-3)
  }

  .rt-CalloutRoot.rt-r-size-2 {
    gap: var(--space-3);
    padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-CalloutRoot.rt-r-size-3 {
    gap: var(--space-4);
    padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:520px) {
  .rt-CalloutRoot.xs\:rt-r-size-1 {
    gap: var(--space-2);
    padding: var(--space-3);
    border-radius: var(--radius-3)
  }

  .rt-CalloutRoot.xs\:rt-r-size-2 {
    gap: var(--space-3);
    padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-CalloutRoot.xs\:rt-r-size-3 {
    gap: var(--space-4);
    padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:768px) {
  .rt-CalloutRoot.sm\:rt-r-size-1 {
    gap: var(--space-2);
    padding: var(--space-3);
    border-radius: var(--radius-3)
  }

  .rt-CalloutRoot.sm\:rt-r-size-2 {
    gap: var(--space-3);
    padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-CalloutRoot.sm\:rt-r-size-3 {
    gap: var(--space-4);
    padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1024px) {
  .rt-CalloutRoot.md\:rt-r-size-1 {
    gap: var(--space-2);
    padding: var(--space-3);
    border-radius: var(--radius-3)
  }

  .rt-CalloutRoot.md\:rt-r-size-2 {
    gap: var(--space-3);
    padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-CalloutRoot.md\:rt-r-size-3 {
    gap: var(--space-4);
    padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1280px) {
  .rt-CalloutRoot.lg\:rt-r-size-1 {
    gap: var(--space-2);
    padding: var(--space-3);
    border-radius: var(--radius-3)
  }

  .rt-CalloutRoot.lg\:rt-r-size-2 {
    gap: var(--space-3);
    padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-CalloutRoot.lg\:rt-r-size-3 {
    gap: var(--space-4);
    padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1640px) {
  .rt-CalloutRoot.xl\:rt-r-size-1 {
    gap: var(--space-2);
    padding: var(--space-3);
    border-radius: var(--radius-3)
  }

  .rt-CalloutRoot.xl\:rt-r-size-2 {
    gap: var(--space-3);
    padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-CalloutRoot.xl\:rt-r-size-3 {
    gap: var(--space-4);
    padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

.rt-CalloutRoot.rt-variant-soft {
  background-color: var(--accent-a3)
}

.rt-CalloutRoot.rt-variant-outline,
.rt-CalloutRoot.rt-variant-surface {
  box-shadow: inset 0 0 0 1px var(--accent-a6)
}

.rt-CalloutRoot.rt-variant-surface {
  background-color: var(--color-surface-accent)
}

.rt-Card {
  position: relative
}

.rt-Card:where(button, a) {
  display: block
}

.rt-Card:after {
  inset: 0;
  position: absolute;
  pointer-events: none;
  border-radius: inherit;
  content: ""
}

.rt-CardInner {
  position: relative;
  box-sizing: border-box;
  border-radius: inherit;
  overflow: hidden;
  height: 100%;
  --inset-padding: var(--card-padding);
  padding: var(--inset-padding)
}

.rt-Card:where(.rt-variant-ghost) {
  --margin-top: 0px;
  --margin-right: 0px;
  --margin-bottom: 0px;
  --margin-left: 0px;
  --margin-top-override: calc(var(--margin-top, 0px) - var(--card-padding));
  --margin-right-override: calc(var(--margin-right, 0px) - var(--card-padding));
  --margin-bottom-override: calc(var(--margin-bottom, 0px) - var(--card-padding));
  --margin-left-override: calc(var(--margin-left, 0px) - var(--card-padding));
  margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
}

:where(.rt-Card:where(.rt-variant-ghost))>* {
  --margin-top-override: initial;
  --margin-right-override: initial;
  --margin-bottom-override: initial;
  --margin-left-override: initial
}

@media all {
  .rt-Card.rt-r-size-1 {
    --card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-Card.rt-r-size-2 {
    --card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-Card.rt-r-size-3 {
    --card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-Card.rt-r-size-4 {
    --card-padding: var(--space-6);
    border-radius: var(--radius-5)
  }

  .rt-Card.rt-r-size-5 {
    --card-padding: var(--space-8);
    border-radius: var(--radius-6)
  }
}

@media (min-width:520px) {
  .rt-Card.xs\:rt-r-size-1 {
    --card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-Card.xs\:rt-r-size-2 {
    --card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-Card.xs\:rt-r-size-3 {
    --card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-Card.xs\:rt-r-size-4 {
    --card-padding: var(--space-6);
    border-radius: var(--radius-5)
  }

  .rt-Card.xs\:rt-r-size-5 {
    --card-padding: var(--space-8);
    border-radius: var(--radius-6)
  }
}

@media (min-width:768px) {
  .rt-Card.sm\:rt-r-size-1 {
    --card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-Card.sm\:rt-r-size-2 {
    --card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-Card.sm\:rt-r-size-3 {
    --card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-Card.sm\:rt-r-size-4 {
    --card-padding: var(--space-6);
    border-radius: var(--radius-5)
  }

  .rt-Card.sm\:rt-r-size-5 {
    --card-padding: var(--space-8);
    border-radius: var(--radius-6)
  }
}

@media (min-width:1024px) {
  .rt-Card.md\:rt-r-size-1 {
    --card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-Card.md\:rt-r-size-2 {
    --card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-Card.md\:rt-r-size-3 {
    --card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-Card.md\:rt-r-size-4 {
    --card-padding: var(--space-6);
    border-radius: var(--radius-5)
  }

  .rt-Card.md\:rt-r-size-5 {
    --card-padding: var(--space-8);
    border-radius: var(--radius-6)
  }
}

@media (min-width:1280px) {
  .rt-Card.lg\:rt-r-size-1 {
    --card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-Card.lg\:rt-r-size-2 {
    --card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-Card.lg\:rt-r-size-3 {
    --card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-Card.lg\:rt-r-size-4 {
    --card-padding: var(--space-6);
    border-radius: var(--radius-5)
  }

  .rt-Card.lg\:rt-r-size-5 {
    --card-padding: var(--space-8);
    border-radius: var(--radius-6)
  }
}

@media (min-width:1640px) {
  .rt-Card.xl\:rt-r-size-1 {
    --card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-Card.xl\:rt-r-size-2 {
    --card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-Card.xl\:rt-r-size-3 {
    --card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-Card.xl\:rt-r-size-4 {
    --card-padding: var(--space-6);
    border-radius: var(--radius-5)
  }

  .rt-Card.xl\:rt-r-size-5 {
    --card-padding: var(--space-8);
    border-radius: var(--radius-6)
  }
}

.rt-Card.rt-variant-surface {
  background-color: var(--color-panel)
}

.rt-Card.rt-variant-surface:after {
  box-shadow: inset 0 0 0 1px var(--gray-a6)
}

@media (hover:hover) {
  .rt-Card.rt-variant-surface:where(button, [href]):hover:after {
    box-shadow: inset 0 0 0 1px var(--gray-a8)
  }
}

.rt-Card.rt-variant-surface:where(button, [href]):active:after {
  box-shadow: inset 0 0 0 1px var(--gray-a8), inset 0 0 0 1px var(--gray-a6)
}

.rt-Card.rt-variant-surface:where(button, [href]):focus-visible:after {
  box-shadow: 0 0 0 2px var(--accent-a8)
}

.rt-Card.rt-variant-classic {
  background-color: var(--color-panel)
}

.rt-Card.rt-variant-classic:before {
  inset: 0;
  position: absolute;
  pointer-events: none;
  border-radius: inherit;
  box-shadow: var(--shadow-2);
  transition: box-shadow .18s;
  content: ""
}

@media (hover:hover) {
  .rt-Card.rt-variant-classic:where(button, [href]):hover:before {
    transition-duration: 40ms;
    box-shadow: var(--shadow-3), var(--shadow-2)
  }
}

.rt-Card.rt-variant-classic:where(button, [href]):active:before {
  transition-duration: 40ms;
  box-shadow: var(--shadow-2), var(--shadow-2)
}

.rt-Card.rt-variant-classic:where(button, [href]):focus-visible:after {
  box-shadow: 0 0 0 2px var(--accent-a8)
}

@media (hover:hover) {
  .rt-Card.rt-variant-ghost:where(button, [href]):hover {
    background-color: var(--gray-a3)
  }
}

.rt-Card.rt-variant-ghost:where(button, [href]):focus-visible:after {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-CheckboxRoot {
  display: inline-flex;
  align-items: center;
  vertical-align: bottom;
  flex-shrink: 0;
  height: var(--line-height-2)
}

.rt-CheckboxButton {
  display: inline-flex;
  box-sizing: border-box
}

.rt-CheckboxButton,
.rt-CheckboxIndicator {
  align-items: center;
  justify-content: center;
  height: var(--checkbox-size);
  width: var(--checkbox-size)
}

.rt-CheckboxIndicator {
  display: flex
}

.rt-CheckboxIndicator svg {
  width: 56.25%;
  height: 56.25%
}

@media all {
  .rt-CheckboxRoot.rt-r-size-1 {
    --checkbox-size: var(--space-4)
  }

  .rt-CheckboxRoot.rt-r-size-1 .rt-CheckboxButton {
    border-radius: var(--radius-1)
  }

  .rt-CheckboxRoot.rt-r-size-2 {
    --checkbox-size: var(--space-5)
  }

  .rt-CheckboxRoot.rt-r-size-2 .rt-CheckboxButton {
    border-radius: var(--radius-2)
  }
}

@media (min-width:520px) {
  .rt-CheckboxRoot.xs\:rt-r-size-1 {
    --checkbox-size: var(--space-4)
  }

  .rt-CheckboxRoot.xs\:rt-r-size-1 .rt-CheckboxButton {
    border-radius: var(--radius-1)
  }

  .rt-CheckboxRoot.xs\:rt-r-size-2 {
    --checkbox-size: var(--space-5)
  }

  .rt-CheckboxRoot.xs\:rt-r-size-2 .rt-CheckboxButton {
    border-radius: var(--radius-2)
  }
}

@media (min-width:768px) {
  .rt-CheckboxRoot.sm\:rt-r-size-1 {
    --checkbox-size: var(--space-4)
  }

  .rt-CheckboxRoot.sm\:rt-r-size-1 .rt-CheckboxButton {
    border-radius: var(--radius-1)
  }

  .rt-CheckboxRoot.sm\:rt-r-size-2 {
    --checkbox-size: var(--space-5)
  }

  .rt-CheckboxRoot.sm\:rt-r-size-2 .rt-CheckboxButton {
    border-radius: var(--radius-2)
  }
}

@media (min-width:1024px) {
  .rt-CheckboxRoot.md\:rt-r-size-1 {
    --checkbox-size: var(--space-4)
  }

  .rt-CheckboxRoot.md\:rt-r-size-1 .rt-CheckboxButton {
    border-radius: var(--radius-1)
  }

  .rt-CheckboxRoot.md\:rt-r-size-2 {
    --checkbox-size: var(--space-5)
  }

  .rt-CheckboxRoot.md\:rt-r-size-2 .rt-CheckboxButton {
    border-radius: var(--radius-2)
  }
}

@media (min-width:1280px) {
  .rt-CheckboxRoot.lg\:rt-r-size-1 {
    --checkbox-size: var(--space-4)
  }

  .rt-CheckboxRoot.lg\:rt-r-size-1 .rt-CheckboxButton {
    border-radius: var(--radius-1)
  }

  .rt-CheckboxRoot.lg\:rt-r-size-2 {
    --checkbox-size: var(--space-5)
  }

  .rt-CheckboxRoot.lg\:rt-r-size-2 .rt-CheckboxButton {
    border-radius: var(--radius-2)
  }
}

@media (min-width:1640px) {
  .rt-CheckboxRoot.xl\:rt-r-size-1 {
    --checkbox-size: var(--space-4)
  }

  .rt-CheckboxRoot.xl\:rt-r-size-1 .rt-CheckboxButton {
    border-radius: var(--radius-1)
  }

  .rt-CheckboxRoot.xl\:rt-r-size-2 {
    --checkbox-size: var(--space-5)
  }

  .rt-CheckboxRoot.xl\:rt-r-size-2 .rt-CheckboxButton {
    border-radius: var(--radius-2)
  }
}

.rt-CheckboxButton.rt-variant-surface:where([data-state=unchecked]) {
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a7)
}

.rt-CheckboxButton.rt-variant-surface:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--gray-a7), 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-CheckboxButton.rt-variant-surface:where([data-state=checked]) {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-CheckboxButton.rt-variant-surface:where([data-state=checked]):where(:focus-visible) {
  box-shadow: 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-CheckboxButton.rt-variant-surface:where([data-state=checked]):where(.rt-high-contrast) {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-CheckboxButton.rt-variant-classic:where([data-state=unchecked]) {
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a3), var(--shadow-1)
}

.rt-CheckboxButton.rt-variant-classic:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--gray-a3), var(--shadow-1), 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-CheckboxButton.rt-variant-classic:where([data-state=checked]) {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-CheckboxButton.rt-variant-classic:where([data-state=checked]):where(:focus-visible) {
  box-shadow: 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-CheckboxButton.rt-variant-classic:where([data-state=checked]):where(.rt-high-contrast) {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-CheckboxButton.rt-variant-soft {
  background-color: var(--accent-a5)
}

.rt-CheckboxButton.rt-variant-soft:where(:focus-visible) {
  box-shadow: 0 0 0 2px var(--accent-1), 0 0 0 4px var(--accent-a8)
}

.rt-CheckboxButton.rt-variant-soft:where([data-state=checked]) {
  color: var(--accent-11)
}

.rt-CheckboxButton.rt-variant-soft:where([data-state=checked]):where(.rt-high-contrast) {
  color: var(--accent-12)
}

.rt-CheckboxButton[data-disabled] {
  box-shadow: inset 0 0 0 1px var(--gray-a6);
  background-color: var(--gray-a3);
  cursor: not-allowed;
  color: var(--gray-a8)
}

.rt-Code {
  box-sizing: border-box;
  font-family: var(--code-font-family);
  font-size: calc(var(--code-font-size-adjust) * 1em);
  font-style: var(--code-font-style);
  font-weight: var(--code-font-weight);
  line-height: 1.25;
  letter-spacing: calc(var(--code-letter-spacing) + var(--letter-spacing, var(--default-letter-spacing)));
  border-radius: calc((.5px + .2em) * var(--radius-factor))
}

@media all {
  .rt-Code.rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--code-font-size-adjust));
    line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Code.rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--code-font-size-adjust));
    line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Code.rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--code-font-size-adjust));
    line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Code.rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--code-font-size-adjust));
    line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Code.rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--code-font-size-adjust));
    line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Code.rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--code-font-size-adjust));
    line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Code.rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--code-font-size-adjust));
    line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Code.rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--code-font-size-adjust));
    line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Code.rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--code-font-size-adjust));
    line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:520px) {
  .rt-Code.xs\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--code-font-size-adjust));
    line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Code.xs\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--code-font-size-adjust));
    line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Code.xs\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--code-font-size-adjust));
    line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Code.xs\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--code-font-size-adjust));
    line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Code.xs\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--code-font-size-adjust));
    line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Code.xs\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--code-font-size-adjust));
    line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Code.xs\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--code-font-size-adjust));
    line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Code.xs\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--code-font-size-adjust));
    line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Code.xs\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--code-font-size-adjust));
    line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:768px) {
  .rt-Code.sm\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--code-font-size-adjust));
    line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Code.sm\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--code-font-size-adjust));
    line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Code.sm\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--code-font-size-adjust));
    line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Code.sm\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--code-font-size-adjust));
    line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Code.sm\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--code-font-size-adjust));
    line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Code.sm\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--code-font-size-adjust));
    line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Code.sm\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--code-font-size-adjust));
    line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Code.sm\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--code-font-size-adjust));
    line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Code.sm\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--code-font-size-adjust));
    line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1024px) {
  .rt-Code.md\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--code-font-size-adjust));
    line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Code.md\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--code-font-size-adjust));
    line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Code.md\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--code-font-size-adjust));
    line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Code.md\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--code-font-size-adjust));
    line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Code.md\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--code-font-size-adjust));
    line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Code.md\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--code-font-size-adjust));
    line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Code.md\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--code-font-size-adjust));
    line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Code.md\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--code-font-size-adjust));
    line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Code.md\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--code-font-size-adjust));
    line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1280px) {
  .rt-Code.lg\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--code-font-size-adjust));
    line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Code.lg\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--code-font-size-adjust));
    line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Code.lg\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--code-font-size-adjust));
    line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Code.lg\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--code-font-size-adjust));
    line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Code.lg\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--code-font-size-adjust));
    line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Code.lg\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--code-font-size-adjust));
    line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Code.lg\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--code-font-size-adjust));
    line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Code.lg\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--code-font-size-adjust));
    line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Code.lg\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--code-font-size-adjust));
    line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1640px) {
  .rt-Code.xl\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--code-font-size-adjust));
    line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Code.xl\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--code-font-size-adjust));
    line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Code.xl\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--code-font-size-adjust));
    line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Code.xl\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--code-font-size-adjust));
    line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Code.xl\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--code-font-size-adjust));
    line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Code.xl\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--code-font-size-adjust));
    line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Code.xl\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--code-font-size-adjust));
    line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Code.xl\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--code-font-size-adjust));
    line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Code.xl\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--code-font-size-adjust));
    line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

.rt-Code:where(:not(.rt-variant-ghost)) {
  padding: .1em .25em;
  font-size: calc(95% * var(--code-font-size-adjust))
}

.rt-Code.rt-variant-ghost {
  color: var(--accent-a11)
}

.rt-Code.rt-variant-ghost:where(.rt-high-contrast) {
  color: var(--accent-12)
}

.rt-Code.rt-variant-solid {
  background-color: var(--accent-a9);
  color: var(--accent-9-contrast)
}

.rt-Code.rt-variant-solid:where(.rt-high-contrast) {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-Code.rt-variant-soft {
  background-color: var(--accent-a3);
  color: var(--accent-a11)
}

.rt-Code.rt-variant-soft:where(.rt-high-contrast) {
  background-color: var(--accent-a4);
  color: var(--accent-12)
}

.rt-Code.rt-variant-outline {
  box-shadow: inset 0 0 0 1px var(--accent-a8);
  color: var(--accent-a11)
}

.rt-Code.rt-variant-outline:where(.rt-high-contrast) {
  box-shadow: inset 0 0 0 1px var(--accent-a7), inset 0 0 0 1px var(--gray-a11);
  color: var(--accent-12)
}

.radix-themes {
  --container-1: 448px;
  --container-2: 688px;
  --container-3: 880px;
  --container-4: 1136px
}

.rt-Container {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
  flex-grow: 1
}

.rt-ContainerInner {
  width: 100%
}

@media all {
  .rt-Container.rt-r-size-1 .rt-ContainerInner {
    max-width: var(--container-1)
  }

  .rt-Container.rt-r-size-2 .rt-ContainerInner {
    max-width: var(--container-2)
  }

  .rt-Container.rt-r-size-3 .rt-ContainerInner {
    max-width: var(--container-3)
  }

  .rt-Container.rt-r-size-4 .rt-ContainerInner {
    max-width: var(--container-4)
  }
}

@media (min-width:520px) {
  .rt-Container.xs\:rt-r-size-1 .rt-ContainerInner {
    max-width: var(--container-1)
  }

  .rt-Container.xs\:rt-r-size-2 .rt-ContainerInner {
    max-width: var(--container-2)
  }

  .rt-Container.xs\:rt-r-size-3 .rt-ContainerInner {
    max-width: var(--container-3)
  }

  .rt-Container.xs\:rt-r-size-4 .rt-ContainerInner {
    max-width: var(--container-4)
  }
}

@media (min-width:768px) {
  .rt-Container.sm\:rt-r-size-1 .rt-ContainerInner {
    max-width: var(--container-1)
  }

  .rt-Container.sm\:rt-r-size-2 .rt-ContainerInner {
    max-width: var(--container-2)
  }

  .rt-Container.sm\:rt-r-size-3 .rt-ContainerInner {
    max-width: var(--container-3)
  }

  .rt-Container.sm\:rt-r-size-4 .rt-ContainerInner {
    max-width: var(--container-4)
  }
}

@media (min-width:1024px) {
  .rt-Container.md\:rt-r-size-1 .rt-ContainerInner {
    max-width: var(--container-1)
  }

  .rt-Container.md\:rt-r-size-2 .rt-ContainerInner {
    max-width: var(--container-2)
  }

  .rt-Container.md\:rt-r-size-3 .rt-ContainerInner {
    max-width: var(--container-3)
  }

  .rt-Container.md\:rt-r-size-4 .rt-ContainerInner {
    max-width: var(--container-4)
  }
}

@media (min-width:1280px) {
  .rt-Container.lg\:rt-r-size-1 .rt-ContainerInner {
    max-width: var(--container-1)
  }

  .rt-Container.lg\:rt-r-size-2 .rt-ContainerInner {
    max-width: var(--container-2)
  }

  .rt-Container.lg\:rt-r-size-3 .rt-ContainerInner {
    max-width: var(--container-3)
  }

  .rt-Container.lg\:rt-r-size-4 .rt-ContainerInner {
    max-width: var(--container-4)
  }
}

@media (min-width:1640px) {
  .rt-Container.xl\:rt-r-size-1 .rt-ContainerInner {
    max-width: var(--container-1)
  }

  .rt-Container.xl\:rt-r-size-2 .rt-ContainerInner {
    max-width: var(--container-2)
  }

  .rt-Container.xl\:rt-r-size-3 .rt-ContainerInner {
    max-width: var(--container-3)
  }

  .rt-Container.xl\:rt-r-size-4 .rt-ContainerInner {
    max-width: var(--container-4)
  }
}

.rt-BaseMenuContent {
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  overflow: hidden;
  background-color: var(--base-menu-bg);
  --base-menu-radius: min((var(--base-menu-item-height)/2 + var(--base-menu-padding)), max(var(--radius-3), var(--radius-full)));
  border-radius: var(--base-menu-radius)
}

.rt-BaseMenuContent .rt-ScrollAreaScrollbar {
  --base-menu-scrollbar-margin: max(calc(var(--base-menu-radius) / 1.5), var(--base-menu-padding));
  margin-top: var(--base-menu-scrollbar-margin);
  margin-bottom: var(--base-menu-scrollbar-margin)
}

.rt-BaseMenuViewport {
  flex: 1 1 0%;
  display: flex;
  flex-direction: column;
  overflow: auto;
  padding: var(--base-menu-padding)
}

.rt-BaseMenuContent:has(.rt-ScrollAreaScrollbar[data-orientation=vertical]) .rt-BaseMenuViewport {
  padding-right: 12px
}

.rt-BaseMenuItem {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: max(var(--radius-2), var(--radius-full));
  height: var(--base-menu-item-height);
  padding-left: var(--space-5);
  padding-right: var(--space-3);
  position: relative;
  box-sizing: border-box;
  outline: none;
  cursor: default;
  scroll-margin: var(--base-menu-padding) 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none
}

.rt-BaseMenuItem[data-disabled] {
  pointer-events: none
}

.rt-BaseMenuContent:not(:has(.rt-BaseMenuCheckboxItem, .rt-BaseMenuRadioItem)) .rt-BaseMenuItem {
  padding-left: var(--space-3)
}

.rt-BaseMenuContent:has(.rt-BaseMenuCheckboxItem, .rt-BaseMenuRadioItem) .rt-BaseMenuItem {
  padding-left: var(--space-5)
}

.rt-BaseMenuShortcut {
  display: flex;
  align-items: center;
  margin-left: var(--space-5)
}

.rt-BaseMenuShortcut svg {
  margin-right: calc(-2px * var(--scaling))
}

.rt-BaseMenuItemIndicator {
  position: absolute;
  left: 0;
  width: var(--space-5);
  display: inline-flex;
  align-items: center;
  justify-content: center
}

.rt-BaseMenuSeparator {
  height: 1px;
  margin: var(--space-2) var(--space-3)
}

.rt-BaseMenuLabel {
  display: flex;
  align-items: center;
  height: var(--base-menu-item-height);
  padding-left: var(--space-5);
  padding-right: var(--space-3);
  font-size: var(--font-size-1);
  line-height: var(--line-height-1);
  letter-spacing: var(--letter-spacing-1);
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  cursor: default
}

.rt-BaseMenuLabel:not(:first-child) {
  margin-top: var(--space-2)
}

.rt-BaseMenuContent:not(:has(.rt-BaseMenuCheckboxItem, .rt-BaseMenuRadioItem)) .rt-BaseMenuLabel {
  padding-left: var(--space-3)
}

.rt-BaseMenuContent:has(.rt-BaseMenuCheckboxItem, .rt-BaseMenuRadioItem) .rt-BaseMenuLabel {
  padding-left: var(--space-5)
}

.rt-BaseMenuArrow {
  fill: var(--base-menu-bg)
}

@media all {
  .rt-BaseMenuContent.rt-r-size-1 {
    --base-menu-padding: var(--space-1);
    --base-menu-item-height: var(--space-5)
  }

  .rt-BaseMenuContent.rt-r-size-1 .rt-BaseMenuItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-BaseMenuContent.rt-r-size-2 {
    --base-menu-padding: var(--space-2);
    --base-menu-item-height: var(--space-6)
  }

  .rt-BaseMenuContent.rt-r-size-2 .rt-BaseMenuItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }
}

@media (min-width:520px) {
  .rt-BaseMenuContent.xs\:rt-r-size-1 {
    --base-menu-padding: var(--space-1);
    --base-menu-item-height: var(--space-5)
  }

  .rt-BaseMenuContent.xs\:rt-r-size-1 .rt-BaseMenuItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-BaseMenuContent.xs\:rt-r-size-2 {
    --base-menu-padding: var(--space-2);
    --base-menu-item-height: var(--space-6)
  }

  .rt-BaseMenuContent.xs\:rt-r-size-2 .rt-BaseMenuItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }
}

@media (min-width:768px) {
  .rt-BaseMenuContent.sm\:rt-r-size-1 {
    --base-menu-padding: var(--space-1);
    --base-menu-item-height: var(--space-5)
  }

  .rt-BaseMenuContent.sm\:rt-r-size-1 .rt-BaseMenuItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-BaseMenuContent.sm\:rt-r-size-2 {
    --base-menu-padding: var(--space-2);
    --base-menu-item-height: var(--space-6)
  }

  .rt-BaseMenuContent.sm\:rt-r-size-2 .rt-BaseMenuItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }
}

@media (min-width:1024px) {
  .rt-BaseMenuContent.md\:rt-r-size-1 {
    --base-menu-padding: var(--space-1);
    --base-menu-item-height: var(--space-5)
  }

  .rt-BaseMenuContent.md\:rt-r-size-1 .rt-BaseMenuItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-BaseMenuContent.md\:rt-r-size-2 {
    --base-menu-padding: var(--space-2);
    --base-menu-item-height: var(--space-6)
  }

  .rt-BaseMenuContent.md\:rt-r-size-2 .rt-BaseMenuItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }
}

@media (min-width:1280px) {
  .rt-BaseMenuContent.lg\:rt-r-size-1 {
    --base-menu-padding: var(--space-1);
    --base-menu-item-height: var(--space-5)
  }

  .rt-BaseMenuContent.lg\:rt-r-size-1 .rt-BaseMenuItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-BaseMenuContent.lg\:rt-r-size-2 {
    --base-menu-padding: var(--space-2);
    --base-menu-item-height: var(--space-6)
  }

  .rt-BaseMenuContent.lg\:rt-r-size-2 .rt-BaseMenuItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }
}

@media (min-width:1640px) {
  .rt-BaseMenuContent.xl\:rt-r-size-1 {
    --base-menu-padding: var(--space-1);
    --base-menu-item-height: var(--space-5)
  }

  .rt-BaseMenuContent.xl\:rt-r-size-1 .rt-BaseMenuItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-BaseMenuContent.xl\:rt-r-size-2 {
    --base-menu-padding: var(--space-2);
    --base-menu-item-height: var(--space-6)
  }

  .rt-BaseMenuContent.xl\:rt-r-size-2 .rt-BaseMenuItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }
}

.rt-BaseMenuContent {
  --base-menu-bg: var(--color-panel-solid);
  box-shadow: var(--shadow-5)
}

.rt-BaseMenuItem[data-accent-color] {
  color: var(--accent-a11)
}

.rt-BaseMenuItem[data-disabled] {
  color: var(--gray-a8)
}

.rt-BaseMenuShortcut {
  color: var(--gray-a11)
}

.rt-BaseMenuItem[data-disabled] .rt-BaseMenuShortcut,
.rt-BaseMenuItem[data-highlighted] .rt-BaseMenuShortcut,
.rt-BaseMenuSubTrigger[data-state=open] .rt-BaseMenuShortcut {
  color: inherit
}

.rt-BaseMenuLabel {
  color: var(--gray-a11)
}

.rt-BaseMenuSeparator {
  background-color: var(--gray-a6)
}

.rt-BaseMenuContent.rt-variant-solid .rt-BaseMenuSubTrigger[data-state=open] {
  background-color: var(--gray-a3)
}

.rt-BaseMenuContent.rt-variant-solid .rt-BaseMenuSubTriggerIcon {
  color: var(--gray-12)
}

.rt-BaseMenuContent.rt-variant-solid .rt-BaseMenuItem[data-highlighted] {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-BaseMenuContent.rt-variant-solid .rt-BaseMenuItem[data-highlighted] .rt-BaseMenuSubTriggerIcon {
  color: var(--accent-9-contrast)
}

.rt-BaseMenuContent.rt-variant-solid:where(.rt-high-contrast) .rt-BaseMenuItem[data-highlighted] {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-BaseMenuContent.rt-variant-solid:where(.rt-high-contrast) .rt-BaseMenuItem[data-highlighted] .rt-BaseMenuSubTriggerIcon {
  color: var(--accent-1)
}

.rt-BaseMenuContent.rt-variant-solid:where(.rt-high-contrast) .rt-BaseMenuItem[data-highlighted][data-accent-color] {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-BaseMenuContent.rt-variant-soft .rt-BaseMenuSubTrigger[data-state=open] {
  background-color: var(--accent-a3)
}

.rt-BaseMenuContent.rt-variant-soft .rt-BaseMenuSubTriggerIcon {
  color: var(--gray-12)
}

.rt-BaseMenuContent.rt-variant-soft .rt-BaseMenuItem[data-highlighted] {
  background-color: var(--accent-a5)
}

.rt-BaseMenuContent.rt-variant-soft .rt-BaseMenuItem[data-highlighted][data-accent-color] {
  color: var(--accent-12)
}

.rt-ContextMenuContent {
  max-height: var(--radix-context-menu-content-available-height);
  transform-origin: var(--radix-context-menu-content-transform-origin)
}

.rt-DialogOverlay {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  inset: 0;
  padding-bottom: 5vh
}

.rt-DialogOverlay:after {
  content: "";
  position: absolute;
  inset: 0;
  background-color: var(--color-overlay);
  filter: saturate(.5)
}

.rt-DialogContent {
  width: 100%;
  max-height: 90vh;
  max-width: 580px;
  outline: none;
  overflow: auto;
  background-color: var(--color-panel-solid);
  box-shadow: var(--shadow-6);
  box-sizing: border-box;
  z-index: 1;
  --inset-padding: var(--dialog-padding);
  padding: var(--inset-padding)
}

@media all {
  .rt-DialogContent.rt-r-size-1 {
    --dialog-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.rt-r-size-2 {
    --dialog-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.rt-r-size-3 {
    --dialog-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-DialogContent.rt-r-size-4 {
    --dialog-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:520px) {
  .rt-DialogContent.xs\:rt-r-size-1 {
    --dialog-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.xs\:rt-r-size-2 {
    --dialog-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.xs\:rt-r-size-3 {
    --dialog-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-DialogContent.xs\:rt-r-size-4 {
    --dialog-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:768px) {
  .rt-DialogContent.sm\:rt-r-size-1 {
    --dialog-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.sm\:rt-r-size-2 {
    --dialog-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.sm\:rt-r-size-3 {
    --dialog-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-DialogContent.sm\:rt-r-size-4 {
    --dialog-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1024px) {
  .rt-DialogContent.md\:rt-r-size-1 {
    --dialog-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.md\:rt-r-size-2 {
    --dialog-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.md\:rt-r-size-3 {
    --dialog-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-DialogContent.md\:rt-r-size-4 {
    --dialog-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1280px) {
  .rt-DialogContent.lg\:rt-r-size-1 {
    --dialog-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.lg\:rt-r-size-2 {
    --dialog-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.lg\:rt-r-size-3 {
    --dialog-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-DialogContent.lg\:rt-r-size-4 {
    --dialog-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1640px) {
  .rt-DialogContent.xl\:rt-r-size-1 {
    --dialog-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.xl\:rt-r-size-2 {
    --dialog-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-DialogContent.xl\:rt-r-size-3 {
    --dialog-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-DialogContent.xl\:rt-r-size-4 {
    --dialog-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (prefers-reduced-motion:no-preference) {
  @keyframes DialogOverlayNoop {
    0% {
      opacity: 1
    }

    to {
      opacity: 1
    }
  }

  @keyframes DialogOverlayShow {
    0% {
      opacity: 0
    }

    to {
      opacity: 1
    }
  }

  @keyframes DialogOverlayHide {
    0% {
      opacity: 1
    }

    to {
      opacity: 0
    }
  }

  @keyframes DialogContentShow {
    0% {
      opacity: 0;
      transform: translateY(5px) scale(.97)
    }

    to {
      opacity: 1;
      transform: translateY(0) scale(1)
    }
  }

  @keyframes DialogContentHide {
    0% {
      opacity: 1;
      transform: translateY(0) scale(1)
    }

    to {
      opacity: 0;
      transform: translateY(5px) scale(.99)
    }
  }

  .rt-DialogOverlay[data-state=closed] {
    animation: DialogOverlayNoop .25s cubic-bezier(.16, 1, .3, 1)
  }

  .rt-DialogOverlay[data-state=open]:after {
    animation: DialogOverlayShow .4s cubic-bezier(.16, 1, .3, 1)
  }

  .rt-DialogOverlay[data-state=closed]:after {
    animation: DialogOverlayHide .25s cubic-bezier(.16, 1, .3, 1)
  }

  .rt-DialogContent[data-state=open] {
    animation: DialogContentShow .2s cubic-bezier(.16, 1, .3, 1)
  }

  .rt-DialogContent[data-state=closed] {
    animation: DialogContentHide .15s cubic-bezier(.16, 1, .3, 1)
  }
}

.rt-DropdownMenuContent {
  max-height: var(--radix-dropdown-menu-content-available-height);
  transform-origin: var(--radix-dropdown-menu-content-transform-origin)
}

.rt-Em {
  box-sizing: border-box;
  font-family: var(--em-font-family);
  font-size: calc(var(--em-font-size-adjust) * 1em);
  font-style: var(--em-font-style);
  font-weight: var(--em-font-weight);
  line-height: 1.25;
  letter-spacing: calc(var(--em-letter-spacing) + var(--letter-spacing, var(--default-letter-spacing)));
  color: inherit
}

.rt-Flex {
  display: flex
}

.rt-Flex,
.rt-Grid {
  box-sizing: border-box;
  justify-content: flex-start
}

.rt-Grid {
  display: grid;
  align-items: stretch;
  grid-template-columns: var(--grid-template-columns);
  grid-template-rows: var(--grid-template-rows);
  --grid-template-columns: var(--grid-template-columns-initial, 1fr);
  --grid-template-rows: var(--grid-template-rows-initial, none)
}

@media (min-width:520px) {
  .rt-Grid {
    --grid-template-columns: var(--grid-template-columns-xs, var(--grid-template-columns-initial, 1fr));
    --grid-template-rows: var(--grid-template-rows-xs, var(--grid-template-rows-initial, none))
  }
}

@media (min-width:768px) {
  .rt-Grid {
    --grid-template-columns: var(--grid-template-columns-sm, var(--grid-template-columns-xs, var(--grid-template-columns-initial, 1fr)));
    --grid-template-rows: var(--grid-template-rows-sm, var(--grid-template-rows-xs, var(--grid-template-rows-initial, none)))
  }
}

@media (min-width:1024px) {
  .rt-Grid {
    --grid-template-columns: var(--grid-template-columns-md, var(--grid-template-columns-sm, var(--grid-template-columns-xs, var(--grid-template-columns-initial, 1fr))));
    --grid-template-rows: var(--grid-template-rows-md, var(--grid-template-rows-sm, var(--grid-template-rows-xs, var(--grid-template-rows-initial, none))))
  }
}

@media (min-width:1280px) {
  .rt-Grid {
    --grid-template-columns: var(--grid-template-columns-lg, var(--grid-template-columns-md, var(--grid-template-columns-sm, var(--grid-template-columns-xs, var(--grid-template-columns-initial, 1fr)))));
    --grid-template-rows: var(--grid-template-rows-lg, var(--grid-template-rows-md, var(--grid-template-rows-sm, var(--grid-template-rows-xs, var(--grid-template-rows-initial, none)))))
  }
}

@media (min-width:1640px) {
  .rt-Grid {
    --grid-template-columns: var(--grid-template-columns-xl, var(--grid-template-columns-lg, var(--grid-template-columns-md, var(--grid-template-columns-sm, var(--grid-template-columns-xs, var(--grid-template-columns-initial, 1fr))))));
    --grid-template-rows: var(--grid-template-rows-xl, var(--grid-template-rows-lg, var(--grid-template-rows-md, var(--grid-template-rows-sm, var(--grid-template-rows-xs, var(--grid-template-rows-initial, none))))))
  }
}

.rt-Heading {
  margin: 0;
  font-family: var(--heading-font-family);
  font-style: var(--heading-font-style);
  --leading-trim-start: var(--heading-leading-trim-start);
  --leading-trim-end: var(--heading-leading-trim-end);
  line-height: var(--line-height)
}

.rt-Heading:where([data-accent-color]) {
  color: var(--accent-a11)
}

.rt-Heading:where([data-accent-color]) .rt-Text:where(.rt-high-contrast),
.rt-Heading:where([data-accent-color]):where(.rt-high-contrast) {
  color: var(--accent-a12)
}

@media all {
  .rt-Heading.rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-1);
    letter-spacing: calc(var(--letter-spacing-1) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-2);
    letter-spacing: calc(var(--letter-spacing-2) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-3);
    letter-spacing: calc(var(--letter-spacing-3) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-4);
    letter-spacing: calc(var(--letter-spacing-4) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-5);
    letter-spacing: calc(var(--letter-spacing-5) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-6);
    letter-spacing: calc(var(--letter-spacing-6) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-7);
    letter-spacing: calc(var(--letter-spacing-7) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-8);
    letter-spacing: calc(var(--letter-spacing-8) + var(--heading-letter-spacing))
  }

  .rt-Heading.rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-9);
    letter-spacing: calc(var(--letter-spacing-9) + var(--heading-letter-spacing))
  }
}

@media (min-width:520px) {
  .rt-Heading.xs\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-1);
    letter-spacing: calc(var(--letter-spacing-1) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-2);
    letter-spacing: calc(var(--letter-spacing-2) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-3);
    letter-spacing: calc(var(--letter-spacing-3) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-4);
    letter-spacing: calc(var(--letter-spacing-4) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-5);
    letter-spacing: calc(var(--letter-spacing-5) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-6);
    letter-spacing: calc(var(--letter-spacing-6) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-7);
    letter-spacing: calc(var(--letter-spacing-7) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-8);
    letter-spacing: calc(var(--letter-spacing-8) + var(--heading-letter-spacing))
  }

  .rt-Heading.xs\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-9);
    letter-spacing: calc(var(--letter-spacing-9) + var(--heading-letter-spacing))
  }
}

@media (min-width:768px) {
  .rt-Heading.sm\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-1);
    letter-spacing: calc(var(--letter-spacing-1) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-2);
    letter-spacing: calc(var(--letter-spacing-2) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-3);
    letter-spacing: calc(var(--letter-spacing-3) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-4);
    letter-spacing: calc(var(--letter-spacing-4) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-5);
    letter-spacing: calc(var(--letter-spacing-5) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-6);
    letter-spacing: calc(var(--letter-spacing-6) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-7);
    letter-spacing: calc(var(--letter-spacing-7) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-8);
    letter-spacing: calc(var(--letter-spacing-8) + var(--heading-letter-spacing))
  }

  .rt-Heading.sm\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-9);
    letter-spacing: calc(var(--letter-spacing-9) + var(--heading-letter-spacing))
  }
}

@media (min-width:1024px) {
  .rt-Heading.md\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-1);
    letter-spacing: calc(var(--letter-spacing-1) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-2);
    letter-spacing: calc(var(--letter-spacing-2) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-3);
    letter-spacing: calc(var(--letter-spacing-3) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-4);
    letter-spacing: calc(var(--letter-spacing-4) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-5);
    letter-spacing: calc(var(--letter-spacing-5) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-6);
    letter-spacing: calc(var(--letter-spacing-6) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-7);
    letter-spacing: calc(var(--letter-spacing-7) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-8);
    letter-spacing: calc(var(--letter-spacing-8) + var(--heading-letter-spacing))
  }

  .rt-Heading.md\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-9);
    letter-spacing: calc(var(--letter-spacing-9) + var(--heading-letter-spacing))
  }
}

@media (min-width:1280px) {
  .rt-Heading.lg\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-1);
    letter-spacing: calc(var(--letter-spacing-1) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-2);
    letter-spacing: calc(var(--letter-spacing-2) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-3);
    letter-spacing: calc(var(--letter-spacing-3) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-4);
    letter-spacing: calc(var(--letter-spacing-4) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-5);
    letter-spacing: calc(var(--letter-spacing-5) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-6);
    letter-spacing: calc(var(--letter-spacing-6) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-7);
    letter-spacing: calc(var(--letter-spacing-7) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-8);
    letter-spacing: calc(var(--letter-spacing-8) + var(--heading-letter-spacing))
  }

  .rt-Heading.lg\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-9);
    letter-spacing: calc(var(--letter-spacing-9) + var(--heading-letter-spacing))
  }
}

@media (min-width:1640px) {
  .rt-Heading.xl\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-1);
    letter-spacing: calc(var(--letter-spacing-1) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-2);
    letter-spacing: calc(var(--letter-spacing-2) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-3);
    letter-spacing: calc(var(--letter-spacing-3) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-4);
    letter-spacing: calc(var(--letter-spacing-4) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-5);
    letter-spacing: calc(var(--letter-spacing-5) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-6);
    letter-spacing: calc(var(--letter-spacing-6) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-7);
    letter-spacing: calc(var(--letter-spacing-7) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-8);
    letter-spacing: calc(var(--letter-spacing-8) + var(--heading-letter-spacing))
  }

  .rt-Heading.xl\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * var(--heading-font-size-adjust));
    --line-height: var(--heading-line-height-9);
    letter-spacing: calc(var(--letter-spacing-9) + var(--heading-letter-spacing))
  }
}

.rt-HoverCardContent {
  background-color: var(--color-panel-solid);
  box-shadow: var(--shadow-4);
  overflow: auto;
  --inset-padding: var(--hover-card-padding);
  padding: var(--inset-padding);
  transform-origin: var(--radix-hover-card-content-transform-origin)
}

@media all {
  .rt-HoverCardContent.rt-r-size-1 {
    --hover-card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.rt-r-size-2 {
    --hover-card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.rt-r-size-3 {
    --hover-card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:520px) {
  .rt-HoverCardContent.xs\:rt-r-size-1 {
    --hover-card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.xs\:rt-r-size-2 {
    --hover-card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.xs\:rt-r-size-3 {
    --hover-card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:768px) {
  .rt-HoverCardContent.sm\:rt-r-size-1 {
    --hover-card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.sm\:rt-r-size-2 {
    --hover-card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.sm\:rt-r-size-3 {
    --hover-card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1024px) {
  .rt-HoverCardContent.md\:rt-r-size-1 {
    --hover-card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.md\:rt-r-size-2 {
    --hover-card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.md\:rt-r-size-3 {
    --hover-card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1280px) {
  .rt-HoverCardContent.lg\:rt-r-size-1 {
    --hover-card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.lg\:rt-r-size-2 {
    --hover-card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.lg\:rt-r-size-3 {
    --hover-card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1640px) {
  .rt-HoverCardContent.xl\:rt-r-size-1 {
    --hover-card-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.xl\:rt-r-size-2 {
    --hover-card-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-HoverCardContent.xl\:rt-r-size-3 {
    --hover-card-padding: var(--space-5);
    border-radius: var(--radius-5)
  }
}

.rt-IconButton:where(:not(.rt-variant-ghost)) {
  height: var(--base-button-height);
  width: var(--base-button-height)
}

.rt-IconButton:where(.rt-variant-ghost) {
  padding: var(--icon-button-ghost-padding);
  --margin-top: 0px;
  --margin-right: 0px;
  --margin-bottom: 0px;
  --margin-left: 0px;
  --margin-top-override: calc(var(--margin-top, 0px) - var(--icon-button-ghost-padding));
  --margin-right-override: calc(var(--margin-right, 0px) - var(--icon-button-ghost-padding));
  --margin-bottom-override: calc(var(--margin-bottom, 0px) - var(--icon-button-ghost-padding));
  --margin-left-override: calc(var(--margin-left, 0px) - var(--icon-button-ghost-padding));
  margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
}

:where(.rt-IconButton:where(.rt-variant-ghost))>* {
  --margin-top-override: initial;
  --margin-right-override: initial;
  --margin-bottom-override: initial;
  --margin-left-override: initial
}

@media all {
  .rt-IconButton.rt-r-size-1:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-1)
  }

  .rt-IconButton.rt-r-size-2:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: calc(var(--space-1) * 1.5)
  }

  .rt-IconButton.rt-r-size-3:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-2)
  }

  .rt-IconButton.rt-r-size-4:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-3)
  }
}

@media (min-width:520px) {
  .rt-IconButton.xs\:rt-r-size-1:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-1)
  }

  .rt-IconButton.xs\:rt-r-size-2:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: calc(var(--space-1) * 1.5)
  }

  .rt-IconButton.xs\:rt-r-size-3:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-2)
  }

  .rt-IconButton.xs\:rt-r-size-4:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-3)
  }
}

@media (min-width:768px) {
  .rt-IconButton.sm\:rt-r-size-1:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-1)
  }

  .rt-IconButton.sm\:rt-r-size-2:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: calc(var(--space-1) * 1.5)
  }

  .rt-IconButton.sm\:rt-r-size-3:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-2)
  }

  .rt-IconButton.sm\:rt-r-size-4:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-3)
  }
}

@media (min-width:1024px) {
  .rt-IconButton.md\:rt-r-size-1:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-1)
  }

  .rt-IconButton.md\:rt-r-size-2:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: calc(var(--space-1) * 1.5)
  }

  .rt-IconButton.md\:rt-r-size-3:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-2)
  }

  .rt-IconButton.md\:rt-r-size-4:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-3)
  }
}

@media (min-width:1280px) {
  .rt-IconButton.lg\:rt-r-size-1:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-1)
  }

  .rt-IconButton.lg\:rt-r-size-2:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: calc(var(--space-1) * 1.5)
  }

  .rt-IconButton.lg\:rt-r-size-3:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-2)
  }

  .rt-IconButton.lg\:rt-r-size-4:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-3)
  }
}

@media (min-width:1640px) {
  .rt-IconButton.xl\:rt-r-size-1:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-1)
  }

  .rt-IconButton.xl\:rt-r-size-2:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: calc(var(--space-1) * 1.5)
  }

  .rt-IconButton.xl\:rt-r-size-3:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-2)
  }

  .rt-IconButton.xl\:rt-r-size-4:where(.rt-variant-ghost) {
    --icon-button-ghost-padding: var(--space-3)
  }
}

.rt-Inset {
  --margin-top: 0px;
  --margin-right: 0px;
  --margin-bottom: 0px;
  --margin-left: 0px
}

:where(.rt-Inset)>* {
  --margin-top-override: initial;
  --margin-right-override: initial;
  --margin-bottom-override: initial;
  --margin-left-override: initial
}

@media all {
  .rt-Inset.rt-r-side-top {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    margin-top: var(--margin-top-override)
  }

  .rt-Inset.rt-r-side-bottom,
  .rt-Inset.rt-r-side-top {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.rt-r-side-bottom {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.rt-r-side-left {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin-left: var(--margin-left-override)
  }

  .rt-Inset.rt-r-side-left,
  .rt-Inset.rt-r-side-right {
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.rt-r-side-right {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.rt-r-side-x {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.rt-r-side-y {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.rt-r-side-all,
  .rt-Inset.rt-r-side-y {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding))
  }

  .rt-Inset.rt-r-side-all {
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
  }
}

@media (min-width:520px) {
  .rt-Inset.xs\:rt-r-side-top {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    margin-top: var(--margin-top-override)
  }

  .rt-Inset.xs\:rt-r-side-bottom,
  .rt-Inset.xs\:rt-r-side-top {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.xs\:rt-r-side-bottom {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.xs\:rt-r-side-left {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin-left: var(--margin-left-override)
  }

  .rt-Inset.xs\:rt-r-side-left,
  .rt-Inset.xs\:rt-r-side-right {
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.xs\:rt-r-side-right {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.xs\:rt-r-side-x {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.xs\:rt-r-side-y {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.xs\:rt-r-side-all,
  .rt-Inset.xs\:rt-r-side-y {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding))
  }

  .rt-Inset.xs\:rt-r-side-all {
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
  }
}

@media (min-width:768px) {
  .rt-Inset.sm\:rt-r-side-top {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    margin-top: var(--margin-top-override)
  }

  .rt-Inset.sm\:rt-r-side-bottom,
  .rt-Inset.sm\:rt-r-side-top {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.sm\:rt-r-side-bottom {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.sm\:rt-r-side-left {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin-left: var(--margin-left-override)
  }

  .rt-Inset.sm\:rt-r-side-left,
  .rt-Inset.sm\:rt-r-side-right {
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.sm\:rt-r-side-right {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.sm\:rt-r-side-x {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.sm\:rt-r-side-y {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.sm\:rt-r-side-all,
  .rt-Inset.sm\:rt-r-side-y {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding))
  }

  .rt-Inset.sm\:rt-r-side-all {
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
  }
}

@media (min-width:1024px) {
  .rt-Inset.md\:rt-r-side-top {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    margin-top: var(--margin-top-override)
  }

  .rt-Inset.md\:rt-r-side-bottom,
  .rt-Inset.md\:rt-r-side-top {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.md\:rt-r-side-bottom {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.md\:rt-r-side-left {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin-left: var(--margin-left-override)
  }

  .rt-Inset.md\:rt-r-side-left,
  .rt-Inset.md\:rt-r-side-right {
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.md\:rt-r-side-right {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.md\:rt-r-side-x {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.md\:rt-r-side-y {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.md\:rt-r-side-all,
  .rt-Inset.md\:rt-r-side-y {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding))
  }

  .rt-Inset.md\:rt-r-side-all {
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
  }
}

@media (min-width:1280px) {
  .rt-Inset.lg\:rt-r-side-top {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    margin-top: var(--margin-top-override)
  }

  .rt-Inset.lg\:rt-r-side-bottom,
  .rt-Inset.lg\:rt-r-side-top {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.lg\:rt-r-side-bottom {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.lg\:rt-r-side-left {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin-left: var(--margin-left-override)
  }

  .rt-Inset.lg\:rt-r-side-left,
  .rt-Inset.lg\:rt-r-side-right {
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.lg\:rt-r-side-right {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.lg\:rt-r-side-x {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.lg\:rt-r-side-y {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.lg\:rt-r-side-all,
  .rt-Inset.lg\:rt-r-side-y {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding))
  }

  .rt-Inset.lg\:rt-r-side-all {
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
  }
}

@media (min-width:1640px) {
  .rt-Inset.xl\:rt-r-side-top {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    margin-top: var(--margin-top-override)
  }

  .rt-Inset.xl\:rt-r-side-bottom,
  .rt-Inset.xl\:rt-r-side-top {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.xl\:rt-r-side-bottom {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.xl\:rt-r-side-left {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin-left: var(--margin-left-override)
  }

  .rt-Inset.xl\:rt-r-side-left,
  .rt-Inset.xl\:rt-r-side-right {
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.xl\:rt-r-side-right {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.xl\:rt-r-side-x {
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    margin-left: var(--margin-left-override);
    margin-right: var(--margin-right-override)
  }

  .rt-Inset.xl\:rt-r-side-y {
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    margin-top: var(--margin-top-override);
    margin-bottom: var(--margin-bottom-override)
  }

  .rt-Inset.xl\:rt-r-side-all,
  .rt-Inset.xl\:rt-r-side-y {
    --margin-top-override: calc(var(--margin-top) - var(--inset-padding))
  }

  .rt-Inset.xl\:rt-r-side-all {
    --margin-right-override: calc(var(--margin-right) - var(--inset-padding));
    --margin-bottom-override: calc(var(--margin-bottom) - var(--inset-padding));
    --margin-left-override: calc(var(--margin-left) - var(--inset-padding));
    margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
  }
}

.radix-themes {
  --kbd-shadow: inset 0 0.05em var(--white-a12), inset 0 0.25em 0.5em var(--gray-a2), inset 0 -0.05em var(--gray-a6), 0 0 0 0.05em var(--gray-a6), 0 0.08em 0.17em var(--gray-a7)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --kbd-shadow: inset 0 0.05em var(--white-a9), inset 0 0.25em 0.5em var(--gray-a2), inset 0 -0.1em var(--black-a12), 0 0 0 0.075em var(--gray-a8), 0 0.08em 0.17em var(--black-a12)
}

.rt-Kbd {
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-family: var(--default-font-family);
  font-weight: 400;
  vertical-align: text-top;
  white-space: nowrap;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  cursor: default;
  position: relative;
  top: -.05em;
  font-size: .75em;
  min-width: 1.75em;
  line-height: 1.7em;
  padding-left: .5em;
  padding-right: .5em;
  padding-bottom: .05em;
  word-spacing: -.1em;
  border-radius: calc(var(--radius-factor) * .35em);
  letter-spacing: var(--letter-spacing, var(--default-letter-spacing));
  color: var(--gray-12);
  background-color: var(--gray-1);
  box-shadow: var(--kbd-shadow)
}

@media all {
  .rt-Kbd.rt-r-size-1 {
    font-size: calc(var(--font-size-1) * .8);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Kbd.rt-r-size-2 {
    font-size: calc(var(--font-size-2) * .8);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Kbd.rt-r-size-3 {
    font-size: calc(var(--font-size-3) * .8);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Kbd.rt-r-size-4 {
    font-size: calc(var(--font-size-4) * .8);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Kbd.rt-r-size-5 {
    font-size: calc(var(--font-size-5) * .8);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Kbd.rt-r-size-6 {
    font-size: calc(var(--font-size-6) * .8);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Kbd.rt-r-size-7 {
    font-size: calc(var(--font-size-7) * .8);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Kbd.rt-r-size-8 {
    font-size: calc(var(--font-size-8) * .8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Kbd.rt-r-size-9 {
    font-size: calc(var(--font-size-9) * .8);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:520px) {
  .rt-Kbd.xs\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * .8);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Kbd.xs\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * .8);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Kbd.xs\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * .8);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Kbd.xs\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * .8);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Kbd.xs\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * .8);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Kbd.xs\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * .8);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Kbd.xs\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * .8);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Kbd.xs\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * .8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Kbd.xs\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * .8);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:768px) {
  .rt-Kbd.sm\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * .8);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Kbd.sm\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * .8);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Kbd.sm\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * .8);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Kbd.sm\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * .8);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Kbd.sm\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * .8);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Kbd.sm\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * .8);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Kbd.sm\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * .8);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Kbd.sm\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * .8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Kbd.sm\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * .8);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1024px) {
  .rt-Kbd.md\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * .8);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Kbd.md\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * .8);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Kbd.md\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * .8);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Kbd.md\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * .8);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Kbd.md\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * .8);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Kbd.md\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * .8);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Kbd.md\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * .8);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Kbd.md\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * .8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Kbd.md\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * .8);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1280px) {
  .rt-Kbd.lg\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * .8);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Kbd.lg\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * .8);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Kbd.lg\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * .8);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Kbd.lg\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * .8);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Kbd.lg\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * .8);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Kbd.lg\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * .8);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Kbd.lg\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * .8);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Kbd.lg\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * .8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Kbd.lg\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * .8);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1640px) {
  .rt-Kbd.xl\:rt-r-size-1 {
    font-size: calc(var(--font-size-1) * .8);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Kbd.xl\:rt-r-size-2 {
    font-size: calc(var(--font-size-2) * .8);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Kbd.xl\:rt-r-size-3 {
    font-size: calc(var(--font-size-3) * .8);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Kbd.xl\:rt-r-size-4 {
    font-size: calc(var(--font-size-4) * .8);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Kbd.xl\:rt-r-size-5 {
    font-size: calc(var(--font-size-5) * .8);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Kbd.xl\:rt-r-size-6 {
    font-size: calc(var(--font-size-6) * .8);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Kbd.xl\:rt-r-size-7 {
    font-size: calc(var(--font-size-7) * .8);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Kbd.xl\:rt-r-size-8 {
    font-size: calc(var(--font-size-8) * .8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Kbd.xl\:rt-r-size-9 {
    font-size: calc(var(--font-size-9) * .8);
    --letter-spacing: var(--letter-spacing-9)
  }
}

.rt-Link {
  cursor: pointer;
  color: var(--accent-a11);
  border-radius: calc(.07em * var(--radius-factor))
}

.rt-Link:focus-visible {
  outline-color: var(--accent-a8);
  outline-width: 2px;
  outline-style: solid;
  outline-offset: 2px
}

.rt-Link.rt-high-contrast,
.rt-Text:where([data-accent-color]):not(.rt-high-contrast) .rt-Link {
  color: var(--accent-12)
}

@media all {

  .rt-Link.rt-r-size-7,
  .rt-Link.rt-r-size-8,
  .rt-Link.rt-r-size-9 {
    text-decoration-thickness: 2px
  }
}

@media (min-width:520px) {

  .rt-Link.xs\:rt-r-size-7,
  .rt-Link.xs\:rt-r-size-8,
  .rt-Link.xs\:rt-r-size-9 {
    text-decoration-thickness: 2px
  }
}

@media (min-width:768px) {

  .rt-Link.sm\:rt-r-size-7,
  .rt-Link.sm\:rt-r-size-8,
  .rt-Link.sm\:rt-r-size-9 {
    text-decoration-thickness: 2px
  }
}

@media (min-width:1024px) {

  .rt-Link.md\:rt-r-size-7,
  .rt-Link.md\:rt-r-size-8,
  .rt-Link.md\:rt-r-size-9 {
    text-decoration-thickness: 2px
  }
}

@media (min-width:1280px) {

  .rt-Link.lg\:rt-r-size-7,
  .rt-Link.lg\:rt-r-size-8,
  .rt-Link.lg\:rt-r-size-9 {
    text-decoration-thickness: 2px
  }
}

@media (min-width:1640px) {

  .rt-Link.xl\:rt-r-size-7,
  .rt-Link.xl\:rt-r-size-8,
  .rt-Link.xl\:rt-r-size-9 {
    text-decoration-thickness: 2px
  }
}

.rt-Link {
  text-decoration-line: none;
  text-decoration-style: solid;
  text-decoration-thickness: 1px;
  text-underline-offset: calc(.025em + 2px);
  text-decoration-color: var(--accent-a5)
}

@media (hover:hover) {
  .rt-Link:where(.rt-underline-auto):hover {
    text-decoration-line: underline
  }
}

.rt-Link.rt-high-contrast:where(.rt-underline-auto),
:where(.rt-Text:where([data-accent-color])):not(.rt-high-contrast) .rt-Link:where(.rt-underline-auto) {
  text-decoration-line: underline;
  text-decoration-color: var(--accent-a6)
}

@media (hover:hover) {
  .rt-Link:where(.rt-underline-hover):hover {
    text-decoration-line: underline
  }
}

.rt-Link:where(.rt-underline-always) {
  text-decoration-line: underline
}

.rt-Link:focus-visible {
  text-decoration-line: none
}

.rt-PopoverContent {
  background-color: var(--color-panel-solid);
  box-shadow: var(--shadow-5);
  min-width: var(--radix-popover-trigger-width);
  outline: 0;
  overflow: auto;
  --inset-padding: var(--popover-padding);
  padding: var(--inset-padding);
  transform-origin: var(--radix-popover-content-transform-origin)
}

@media all {
  .rt-PopoverContent.rt-r-size-1 {
    --popover-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.rt-r-size-2 {
    --popover-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.rt-r-size-3 {
    --popover-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-PopoverContent.rt-r-size-4 {
    --popover-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:520px) {
  .rt-PopoverContent.xs\:rt-r-size-1 {
    --popover-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.xs\:rt-r-size-2 {
    --popover-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.xs\:rt-r-size-3 {
    --popover-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-PopoverContent.xs\:rt-r-size-4 {
    --popover-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:768px) {
  .rt-PopoverContent.sm\:rt-r-size-1 {
    --popover-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.sm\:rt-r-size-2 {
    --popover-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.sm\:rt-r-size-3 {
    --popover-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-PopoverContent.sm\:rt-r-size-4 {
    --popover-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1024px) {
  .rt-PopoverContent.md\:rt-r-size-1 {
    --popover-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.md\:rt-r-size-2 {
    --popover-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.md\:rt-r-size-3 {
    --popover-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-PopoverContent.md\:rt-r-size-4 {
    --popover-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1280px) {
  .rt-PopoverContent.lg\:rt-r-size-1 {
    --popover-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.lg\:rt-r-size-2 {
    --popover-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.lg\:rt-r-size-3 {
    --popover-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-PopoverContent.lg\:rt-r-size-4 {
    --popover-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

@media (min-width:1640px) {
  .rt-PopoverContent.xl\:rt-r-size-1 {
    --popover-padding: var(--space-3);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.xl\:rt-r-size-2 {
    --popover-padding: var(--space-4);
    border-radius: var(--radius-4)
  }

  .rt-PopoverContent.xl\:rt-r-size-3 {
    --popover-padding: var(--space-5);
    border-radius: var(--radius-5)
  }

  .rt-PopoverContent.xl\:rt-r-size-4 {
    --popover-padding: var(--space-6);
    border-radius: var(--radius-5)
  }
}

.rt-Quote {
  box-sizing: border-box;
  font-family: var(--quote-font-family);
  font-size: calc(var(--quote-font-size-adjust) * 1em);
  font-style: var(--quote-font-style);
  font-weight: var(--quote-font-weight);
  line-height: 1.25;
  letter-spacing: calc(var(--quote-letter-spacing) + var(--letter-spacing, var(--default-letter-spacing)));
  color: inherit
}

.rt-RadioGroupItem {
  display: inline-flex;
  align-items: center;
  vertical-align: bottom;
  flex-shrink: 0;
  height: var(--line-height-2)
}

.rt-RadioGroupButton {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  height: var(--radio-group-item-size);
  width: var(--radio-group-item-size);
  border-radius: 100%
}

.rt-RadioGroupIndicator {
  background-color: currentColor;
  height: var(--radio-group-indicator-size);
  width: var(--radio-group-indicator-size);
  border-radius: 100%
}

@media all {
  .rt-RadioGroupRoot.rt-r-size-1 {
    --radio-group-item-size: var(--space-4);
    --radio-group-indicator-size: calc(6px * var(--scaling))
  }

  .rt-RadioGroupRoot.rt-r-size-2 {
    --radio-group-item-size: var(--space-5);
    --radio-group-indicator-size: calc(10px * var(--scaling))
  }
}

@media (min-width:520px) {
  .rt-RadioGroupRoot.xs\:rt-r-size-1 {
    --radio-group-item-size: var(--space-4);
    --radio-group-indicator-size: calc(6px * var(--scaling))
  }

  .rt-RadioGroupRoot.xs\:rt-r-size-2 {
    --radio-group-item-size: var(--space-5);
    --radio-group-indicator-size: calc(10px * var(--scaling))
  }
}

@media (min-width:768px) {
  .rt-RadioGroupRoot.sm\:rt-r-size-1 {
    --radio-group-item-size: var(--space-4);
    --radio-group-indicator-size: calc(6px * var(--scaling))
  }

  .rt-RadioGroupRoot.sm\:rt-r-size-2 {
    --radio-group-item-size: var(--space-5);
    --radio-group-indicator-size: calc(10px * var(--scaling))
  }
}

@media (min-width:1024px) {
  .rt-RadioGroupRoot.md\:rt-r-size-1 {
    --radio-group-item-size: var(--space-4);
    --radio-group-indicator-size: calc(6px * var(--scaling))
  }

  .rt-RadioGroupRoot.md\:rt-r-size-2 {
    --radio-group-item-size: var(--space-5);
    --radio-group-indicator-size: calc(10px * var(--scaling))
  }
}

@media (min-width:1280px) {
  .rt-RadioGroupRoot.lg\:rt-r-size-1 {
    --radio-group-item-size: var(--space-4);
    --radio-group-indicator-size: calc(6px * var(--scaling))
  }

  .rt-RadioGroupRoot.lg\:rt-r-size-2 {
    --radio-group-item-size: var(--space-5);
    --radio-group-indicator-size: calc(10px * var(--scaling))
  }
}

@media (min-width:1640px) {
  .rt-RadioGroupRoot.xl\:rt-r-size-1 {
    --radio-group-item-size: var(--space-4);
    --radio-group-indicator-size: calc(6px * var(--scaling))
  }

  .rt-RadioGroupRoot.xl\:rt-r-size-2 {
    --radio-group-item-size: var(--space-5);
    --radio-group-indicator-size: calc(10px * var(--scaling))
  }
}

.rt-RadioGroupRoot.rt-variant-surface .rt-RadioGroupButton:where([data-state=unchecked]) {
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a7)
}

.rt-RadioGroupRoot.rt-variant-surface .rt-RadioGroupButton:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--gray-a7), 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-RadioGroupRoot.rt-variant-surface .rt-RadioGroupButton:where([data-state=checked]) {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-RadioGroupRoot.rt-variant-surface:where(.rt-high-contrast) .rt-RadioGroupButton:where([data-state=checked]) {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-RadioGroupRoot.rt-variant-classic .rt-RadioGroupButton:where([data-state=unchecked]) {
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a3), var(--shadow-1)
}

.rt-RadioGroupRoot.rt-variant-classic .rt-RadioGroupButton:where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--gray-a3), var(--shadow-1), 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-RadioGroupRoot.rt-variant-classic .rt-RadioGroupButton:where([data-state=checked]) {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-RadioGroupRoot.rt-variant-classic:where(.rt-high-contrast) .rt-RadioGroupButton:where([data-state=checked]) {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-RadioGroupRoot.rt-variant-soft .rt-RadioGroupButton {
  background-color: var(--accent-a5)
}

.rt-RadioGroupRoot.rt-variant-soft .rt-RadioGroupButton:where(:focus-visible) {
  box-shadow: 0 0 0 2px var(--accent-1), 0 0 0 4px var(--accent-a8)
}

.rt-RadioGroupRoot.rt-variant-soft .rt-RadioGroupButton:where([data-state=checked]) {
  color: var(--accent-11)
}

.rt-RadioGroupRoot.rt-variant-soft:where(.rt-high-contrast) .rt-RadioGroupButton:where([data-state=checked]) {
  color: var(--accent-12)
}

.rt-RadioGroupRoot .rt-RadioGroupButton[data-disabled] {
  box-shadow: inset 0 0 0 1px var(--gray-a6);
  background-color: var(--gray-a3);
  cursor: not-allowed;
  color: var(--gray-a8)
}

.rt-ScrollAreaRoot {
  --scrollarea-scrollbar-margin-top: var(--space-1);
  --scrollarea-scrollbar-margin-bottom: var(--space-1);
  --scrollarea-scrollbar-margin-left: var(--space-1);
  --scrollarea-scrollbar-margin-right: var(--space-1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  width: 100%;
  height: 100%
}

.rt-ScrollAreaViewport {
  width: 100%;
  height: 100%;
  overscroll-behavior-x: contain
}

.rt-ScrollAreaViewport:focus-visible+.rt-ScrollAreaViewportFocusRing {
  position: absolute;
  inset: 0;
  pointer-events: none;
  box-shadow: inset 0 0 0 2px var(--accent-a8)
}

.rt-ScrollAreaScrollbar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  touch-action: none
}

.rt-ScrollAreaScrollbar[data-orientation=vertical] {
  flex-direction: column;
  width: var(--scrollarea-scrollbar-size)
}

.rt-ScrollAreaScrollbar[data-orientation=horizontal] {
  flex-direction: row;
  height: var(--scrollarea-scrollbar-size)
}

.rt-ScrollAreaThumb {
  position: relative
}

.rt-ScrollAreaThumb:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  min-width: 44px;
  min-height: 44px
}

@media all {
  .rt-ScrollAreaScrollbar.rt-r-size-1 {
    --scrollarea-scrollbar-size: var(--space-1);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.rt-r-size-2 {
    --scrollarea-scrollbar-size: var(--space-2);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.rt-r-size-3 {
    --scrollarea-scrollbar-size: var(--space-3);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }
}

@media (min-width:520px) {
  .rt-ScrollAreaScrollbar.xs\:rt-r-size-1 {
    --scrollarea-scrollbar-size: var(--space-1);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.xs\:rt-r-size-2 {
    --scrollarea-scrollbar-size: var(--space-2);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.xs\:rt-r-size-3 {
    --scrollarea-scrollbar-size: var(--space-3);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }
}

@media (min-width:768px) {
  .rt-ScrollAreaScrollbar.sm\:rt-r-size-1 {
    --scrollarea-scrollbar-size: var(--space-1);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.sm\:rt-r-size-2 {
    --scrollarea-scrollbar-size: var(--space-2);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.sm\:rt-r-size-3 {
    --scrollarea-scrollbar-size: var(--space-3);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }
}

@media (min-width:1024px) {
  .rt-ScrollAreaScrollbar.md\:rt-r-size-1 {
    --scrollarea-scrollbar-size: var(--space-1);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.md\:rt-r-size-2 {
    --scrollarea-scrollbar-size: var(--space-2);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.md\:rt-r-size-3 {
    --scrollarea-scrollbar-size: var(--space-3);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }
}

@media (min-width:1280px) {
  .rt-ScrollAreaScrollbar.lg\:rt-r-size-1 {
    --scrollarea-scrollbar-size: var(--space-1);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.lg\:rt-r-size-2 {
    --scrollarea-scrollbar-size: var(--space-2);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.lg\:rt-r-size-3 {
    --scrollarea-scrollbar-size: var(--space-3);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }
}

@media (min-width:1640px) {
  .rt-ScrollAreaScrollbar.xl\:rt-r-size-1 {
    --scrollarea-scrollbar-size: var(--space-1);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.xl\:rt-r-size-2 {
    --scrollarea-scrollbar-size: var(--space-2);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-ScrollAreaScrollbar.xl\:rt-r-size-3 {
    --scrollarea-scrollbar-size: var(--space-3);
    --scrollarea-scrollbar-radius: max(var(--radius-1), var(--radius-full))
  }
}

.rt-ScrollAreaScrollbar {
  background-color: var(--gray-a3);
  border-radius: var(--scrollarea-scrollbar-radius);
  margin: var(--scrollarea-scrollbar-margin-top) var(--scrollarea-scrollbar-margin-right) var(--scrollarea-scrollbar-margin-bottom) var(--scrollarea-scrollbar-margin-left);
  animation-duration: .15s;
  animation-timing-function: ease-out
}

.rt-ScrollAreaScrollbar[data-state=visible] {
  animation-name: fadeIn
}

.rt-ScrollAreaScrollbar[data-state=hidden] {
  animation-name: fadeOut
}

.rt-ScrollAreaThumb {
  background-color: var(--gray-a8);
  border-radius: inherit;
  transition: background-color .1s
}

@media (hover:hover) {
  .rt-ScrollAreaThumb:hover {
    background-color: var(--gray-a9)
  }
}

.rt-Section {
  box-sizing: border-box;
  flex-shrink: 0
}

@media all {
  .rt-Section:where(.rt-r-size-1) {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-Section:where(.rt-r-size-2) {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-Section:where(.rt-r-size-3) {
    padding-top: 80px;
    padding-bottom: 80px
  }
}

@media (min-width:520px) {
  .rt-Section:where(.xs\:rt-r-size-1) {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-Section:where(.xs\:rt-r-size-2) {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-Section:where(.xs\:rt-r-size-3) {
    padding-top: 80px;
    padding-bottom: 80px
  }
}

@media (min-width:768px) {
  .rt-Section:where(.sm\:rt-r-size-1) {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-Section:where(.sm\:rt-r-size-2) {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-Section:where(.sm\:rt-r-size-3) {
    padding-top: 80px;
    padding-bottom: 80px
  }
}

@media (min-width:1024px) {
  .rt-Section:where(.md\:rt-r-size-1) {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-Section:where(.md\:rt-r-size-2) {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-Section:where(.md\:rt-r-size-3) {
    padding-top: 80px;
    padding-bottom: 80px
  }
}

@media (min-width:1280px) {
  .rt-Section:where(.lg\:rt-r-size-1) {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-Section:where(.lg\:rt-r-size-2) {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-Section:where(.lg\:rt-r-size-3) {
    padding-top: 80px;
    padding-bottom: 80px
  }
}

@media (min-width:1640px) {
  .rt-Section:where(.xl\:rt-r-size-1) {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-Section:where(.xl\:rt-r-size-2) {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-Section:where(.xl\:rt-r-size-3) {
    padding-top: 80px;
    padding-bottom: 80px
  }
}

.rt-SelectTrigger {
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  box-sizing: border-box;
  flex-shrink: 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  vertical-align: top;
  line-height: var(--height)
}

.rt-SelectIcon {
  flex-shrink: 0
}

.rt-SelectTrigger:where(:not(.rt-variant-ghost)) .rt-SelectIcon {
  opacity: .9
}

.rt-SelectContent {
  overflow: hidden;
  background-color: var(--select-content-bg);
  --select-content-radius: min((var(--select-item-height)/2 + var(--select-content-padding)), max(var(--radius-3), var(--radius-full)));
  border-radius: var(--select-content-radius)
}

.rt-SelectContent[data-side] {
  min-width: var(--radix-select-trigger-width);
  max-height: var(--radix-select-content-available-height);
  transform-origin: var(--radix-select-content-transform-origin)
}

.rt-SelectContent .rt-ScrollAreaScrollbar {
  --select-content-scrollbar-margin: max(calc(var(--select-content-radius) / 1.5), var(--select-content-padding));
  margin-top: var(--select-content-scrollbar-margin);
  margin-bottom: var(--select-content-scrollbar-margin)
}

.rt-SelectViewport {
  box-sizing: border-box;
  padding: var(--select-content-padding)
}

.rt-SelectContent:has(.rt-ScrollAreaScrollbar[data-orientation=vertical]) .rt-SelectViewport {
  padding-right: 12px
}

.rt-SelectItem {
  display: flex;
  align-items: center;
  height: var(--select-item-height);
  border-radius: max(var(--radius-2), var(--radius-full));
  padding-left: var(--space-5);
  padding-right: var(--space-5);
  position: relative;
  box-sizing: border-box;
  outline: none;
  cursor: default;
  scroll-margin: var(--select-content-padding) 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none
}

.rt-SelectItemIndicator {
  position: absolute;
  left: 0;
  width: var(--space-5);
  display: inline-flex;
  align-items: center;
  justify-content: center
}

.rt-SelectSeparator {
  height: 1px;
  margin: var(--space-2)
}

.rt-SelectLabel {
  display: flex;
  align-items: center;
  height: var(--select-item-height);
  padding-left: var(--space-5);
  padding-right: var(--space-5);
  font-size: var(--font-size-1);
  line-height: var(--line-height-1);
  letter-spacing: var(--letter-spacing-1);
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  cursor: default
}

.rt-SelectLabel:not(:first-child) {
  margin-top: var(--space-2)
}

.rt-SelectTrigger {
  color: var(--gray-12)
}

.rt-SelectTrigger:where(:not(.rt-variant-ghost)) {
  height: var(--select-trigger-height)
}

.rt-SelectTrigger:where(.rt-variant-ghost) {
  box-sizing: content-box;
  height: -moz-fit-content;
  height: fit-content;
  padding: var(--select-trigger-ghost-padding-y) var(--select-trigger-ghost-padding-x);
  --margin-top: 0px;
  --margin-right: 0px;
  --margin-bottom: 0px;
  --margin-left: 0px;
  --margin-top-override: calc(var(--margin-top, 0px) - var(--select-trigger-ghost-padding-y));
  --margin-right-override: calc(var(--margin-right, 0px) - var(--select-trigger-ghost-padding-x));
  --margin-bottom-override: calc(var(--margin-bottom, 0px) - var(--select-trigger-ghost-padding-y));
  --margin-left-override: calc(var(--margin-left, 0px) - var(--select-trigger-ghost-padding-x));
  margin: var(--margin-top-override) var(--margin-right-override) var(--margin-bottom-override) var(--margin-left-override)
}

:where(.rt-SelectTrigger:where(.rt-variant-ghost))>* {
  --margin-top-override: initial;
  --margin-right-override: initial;
  --margin-bottom-override: initial;
  --margin-left-override: initial
}

@media all {
  .rt-SelectTrigger.rt-r-size-1 {
    --select-trigger-height: var(--space-5);
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SelectTrigger.rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-SelectTrigger.rt-r-size-1:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.rt-r-size-2 {
    --select-trigger-height: var(--space-6);
    gap: calc(var(--space-1) * 1.5);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SelectTrigger.rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-SelectTrigger.rt-r-size-2:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.rt-r-size-3 {
    --select-trigger-height: var(--space-7);
    gap: var(--space-2);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SelectTrigger.rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-SelectTrigger.rt-r-size-3:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-3);
    --select-trigger-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-SelectTrigger.rt-r-size-3 .rt-SelectIcon {
    width: 11px;
    height: 11px
  }
}

@media (min-width:520px) {
  .rt-SelectTrigger.xs\:rt-r-size-1 {
    --select-trigger-height: var(--space-5);
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SelectTrigger.xs\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-SelectTrigger.xs\:rt-r-size-1:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.xs\:rt-r-size-2 {
    --select-trigger-height: var(--space-6);
    gap: calc(var(--space-1) * 1.5);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SelectTrigger.xs\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-SelectTrigger.xs\:rt-r-size-2:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.xs\:rt-r-size-3 {
    --select-trigger-height: var(--space-7);
    gap: var(--space-2);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SelectTrigger.xs\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-SelectTrigger.xs\:rt-r-size-3:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-3);
    --select-trigger-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-SelectTrigger.xs\:rt-r-size-3 .rt-SelectIcon {
    width: 11px;
    height: 11px
  }
}

@media (min-width:768px) {
  .rt-SelectTrigger.sm\:rt-r-size-1 {
    --select-trigger-height: var(--space-5);
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SelectTrigger.sm\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-SelectTrigger.sm\:rt-r-size-1:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.sm\:rt-r-size-2 {
    --select-trigger-height: var(--space-6);
    gap: calc(var(--space-1) * 1.5);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SelectTrigger.sm\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-SelectTrigger.sm\:rt-r-size-2:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.sm\:rt-r-size-3 {
    --select-trigger-height: var(--space-7);
    gap: var(--space-2);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SelectTrigger.sm\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-SelectTrigger.sm\:rt-r-size-3:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-3);
    --select-trigger-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-SelectTrigger.sm\:rt-r-size-3 .rt-SelectIcon {
    width: 11px;
    height: 11px
  }
}

@media (min-width:1024px) {
  .rt-SelectTrigger.md\:rt-r-size-1 {
    --select-trigger-height: var(--space-5);
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SelectTrigger.md\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-SelectTrigger.md\:rt-r-size-1:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.md\:rt-r-size-2 {
    --select-trigger-height: var(--space-6);
    gap: calc(var(--space-1) * 1.5);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SelectTrigger.md\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-SelectTrigger.md\:rt-r-size-2:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.md\:rt-r-size-3 {
    --select-trigger-height: var(--space-7);
    gap: var(--space-2);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SelectTrigger.md\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-SelectTrigger.md\:rt-r-size-3:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-3);
    --select-trigger-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-SelectTrigger.md\:rt-r-size-3 .rt-SelectIcon {
    width: 11px;
    height: 11px
  }
}

@media (min-width:1280px) {
  .rt-SelectTrigger.lg\:rt-r-size-1 {
    --select-trigger-height: var(--space-5);
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SelectTrigger.lg\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-SelectTrigger.lg\:rt-r-size-1:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.lg\:rt-r-size-2 {
    --select-trigger-height: var(--space-6);
    gap: calc(var(--space-1) * 1.5);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SelectTrigger.lg\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-SelectTrigger.lg\:rt-r-size-2:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.lg\:rt-r-size-3 {
    --select-trigger-height: var(--space-7);
    gap: var(--space-2);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SelectTrigger.lg\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-SelectTrigger.lg\:rt-r-size-3:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-3);
    --select-trigger-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-SelectTrigger.lg\:rt-r-size-3 .rt-SelectIcon {
    width: 11px;
    height: 11px
  }
}

@media (min-width:1640px) {
  .rt-SelectTrigger.xl\:rt-r-size-1 {
    --select-trigger-height: var(--space-5);
    gap: var(--space-1);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    border-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SelectTrigger.xl\:rt-r-size-1:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-SelectTrigger.xl\:rt-r-size-1:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.xl\:rt-r-size-2 {
    --select-trigger-height: var(--space-6);
    gap: calc(var(--space-1) * 1.5);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SelectTrigger.xl\:rt-r-size-2:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-SelectTrigger.xl\:rt-r-size-2:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-2);
    --select-trigger-ghost-padding-y: var(--space-1)
  }

  .rt-SelectTrigger.xl\:rt-r-size-3 {
    --select-trigger-height: var(--space-7);
    gap: var(--space-2);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3);
    border-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SelectTrigger.xl\:rt-r-size-3:where(:not(.rt-variant-ghost)) {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-SelectTrigger.xl\:rt-r-size-3:where(.rt-variant-ghost) {
    --select-trigger-ghost-padding-x: var(--space-3);
    --select-trigger-ghost-padding-y: calc(var(--space-1) * 1.5)
  }

  .rt-SelectTrigger.xl\:rt-r-size-3 .rt-SelectIcon {
    width: 11px;
    height: 11px
  }
}

@media all {
  .rt-SelectContent.rt-r-size-1 {
    --select-content-padding: var(--space-1);
    --select-item-height: var(--space-5)
  }

  .rt-SelectContent.rt-r-size-1 .rt-SelectItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-SelectContent.rt-r-size-2 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-6)
  }

  .rt-SelectContent.rt-r-size-2 .rt-SelectItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.rt-r-size-3 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-7)
  }

  .rt-SelectContent.rt-r-size-3 .rt-SelectLabel {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.rt-r-size-3 .rt-SelectItem {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:520px) {
  .rt-SelectContent.xs\:rt-r-size-1 {
    --select-content-padding: var(--space-1);
    --select-item-height: var(--space-5)
  }

  .rt-SelectContent.xs\:rt-r-size-1 .rt-SelectItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-SelectContent.xs\:rt-r-size-2 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-6)
  }

  .rt-SelectContent.xs\:rt-r-size-2 .rt-SelectItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.xs\:rt-r-size-3 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-7)
  }

  .rt-SelectContent.xs\:rt-r-size-3 .rt-SelectLabel {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.xs\:rt-r-size-3 .rt-SelectItem {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:768px) {
  .rt-SelectContent.sm\:rt-r-size-1 {
    --select-content-padding: var(--space-1);
    --select-item-height: var(--space-5)
  }

  .rt-SelectContent.sm\:rt-r-size-1 .rt-SelectItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-SelectContent.sm\:rt-r-size-2 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-6)
  }

  .rt-SelectContent.sm\:rt-r-size-2 .rt-SelectItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.sm\:rt-r-size-3 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-7)
  }

  .rt-SelectContent.sm\:rt-r-size-3 .rt-SelectLabel {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.sm\:rt-r-size-3 .rt-SelectItem {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:1024px) {
  .rt-SelectContent.md\:rt-r-size-1 {
    --select-content-padding: var(--space-1);
    --select-item-height: var(--space-5)
  }

  .rt-SelectContent.md\:rt-r-size-1 .rt-SelectItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-SelectContent.md\:rt-r-size-2 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-6)
  }

  .rt-SelectContent.md\:rt-r-size-2 .rt-SelectItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.md\:rt-r-size-3 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-7)
  }

  .rt-SelectContent.md\:rt-r-size-3 .rt-SelectLabel {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.md\:rt-r-size-3 .rt-SelectItem {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:1280px) {
  .rt-SelectContent.lg\:rt-r-size-1 {
    --select-content-padding: var(--space-1);
    --select-item-height: var(--space-5)
  }

  .rt-SelectContent.lg\:rt-r-size-1 .rt-SelectItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-SelectContent.lg\:rt-r-size-2 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-6)
  }

  .rt-SelectContent.lg\:rt-r-size-2 .rt-SelectItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.lg\:rt-r-size-3 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-7)
  }

  .rt-SelectContent.lg\:rt-r-size-3 .rt-SelectLabel {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.lg\:rt-r-size-3 .rt-SelectItem {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:1640px) {
  .rt-SelectContent.xl\:rt-r-size-1 {
    --select-content-padding: var(--space-1);
    --select-item-height: var(--space-5)
  }

  .rt-SelectContent.xl\:rt-r-size-1 .rt-SelectItem {
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-SelectContent.xl\:rt-r-size-2 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-6)
  }

  .rt-SelectContent.xl\:rt-r-size-2 .rt-SelectItem {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.xl\:rt-r-size-3 {
    --select-content-padding: var(--space-2);
    --select-item-height: var(--space-7)
  }

  .rt-SelectContent.xl\:rt-r-size-3 .rt-SelectLabel {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-SelectContent.xl\:rt-r-size-3 .rt-SelectItem {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

.rt-SelectTrigger[data-placeholder]>span>span {
  color: var(--gray-a10)
}

.rt-SelectTrigger:where(.rt-variant-surface) {
  color: var(--gray-12);
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a7)
}

@media (hover:hover) {
  .rt-SelectTrigger:where(.rt-variant-surface):where(:hover) {
    box-shadow: inset 0 0 0 1px var(--gray-a8)
  }
}

.rt-SelectTrigger:where(.rt-variant-surface):where([data-state=open]) {
  box-shadow: inset 0 0 0 1px var(--gray-a8)
}

.rt-SelectTrigger:where(.rt-variant-surface):where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.radix-themes {
  --select-trigger__classic__box-shadow: inset 0 0 0 1px var(--gray-a6), inset 0 2px 0 0 var(--white-a12), inset 0 -2px 0 0 var(--gray-a5)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --select-trigger__classic__box-shadow: 0 0 0 1px var(--white-a5), 0 -1px 0 0 var(--white-a7), inset 0 -1px 0 0 var(--black-a11)
}

.rt-SelectTrigger:where(.rt-variant-classic) {
  color: var(--gray-12);
  background-color: var(--color-surface);
  background-image: linear-gradient(var(--gray-a2), var(--gray-a1));
  box-shadow: var(--select-trigger__classic__box-shadow);
  position: relative;
  z-index: 0
}

.rt-SelectTrigger:where(.rt-variant-classic):after,
.rt-SelectTrigger:where(.rt-variant-classic):before {
  content: "";
  position: absolute;
  inset: 2px;
  border-radius: 2px;
  pointer-events: none
}

.rt-SelectTrigger:where(.rt-variant-classic):before {
  z-index: 1;
  background-image: linear-gradient(var(--accent-a1), transparent 50%);
  mix-blend-mode: darken
}

.rt-SelectTrigger:where(.rt-variant-classic):after {
  z-index: 2;
  background-image: linear-gradient(transparent 50%, var(--white-a2));
  mix-blend-mode: soft-light
}

@media (hover:hover) {
  .rt-SelectTrigger:where(.rt-variant-classic):where(:hover) {
    background-image: linear-gradient(var(--black-a3), var(--black-a2) 50%)
  }
}

.rt-SelectTrigger:where(.rt-variant-classic):where([data-state=open]) {
  background-image: linear-gradient(var(--black-a3), var(--black-a2) 50%)
}

.rt-SelectTrigger:where(.rt-variant-classic):where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-SelectTrigger:where(.rt-variant-ghost),
.rt-SelectTrigger:where(.rt-variant-soft) {
  color: var(--accent-12)
}

.rt-SelectTrigger[data-placeholder]:where(.rt-variant-ghost)>span>span,
.rt-SelectTrigger[data-placeholder]:where(.rt-variant-soft)>span>span {
  color: var(--accent-12);
  opacity: .5
}

.rt-SelectTrigger:where(.rt-variant-ghost):where(:focus-visible),
.rt-SelectTrigger:where(.rt-variant-soft):where(:focus-visible) {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-SelectTrigger:where(.rt-variant-soft) {
  background-color: var(--accent-a3)
}

@media (hover:hover) {
  .rt-SelectTrigger:where(.rt-variant-soft):where(:hover) {
    background-color: var(--accent-a4)
  }
}

.rt-SelectTrigger:where(.rt-variant-soft):where([data-state=open]) {
  background-color: var(--accent-a4)
}

@media (hover:hover) {
  .rt-SelectTrigger:where(.rt-variant-ghost):where(:hover) {
    background-color: var(--accent-a3)
  }
}

.rt-SelectTrigger:where(.rt-variant-ghost):where([data-state=open]) {
  background-color: var(--accent-a3)
}

.rt-SelectTrigger:disabled {
  color: var(--gray-a8);
  cursor: not-allowed;
  box-shadow: none;
  background-color: transparent;
  background-image: none
}

.rt-SelectTrigger:disabled:after,
.rt-SelectTrigger:disabled:before {
  display: none
}

.rt-SelectTrigger:disabled:where(:not(.rt-variant-ghost)) {
  background-color: var(--gray-a3)
}

.rt-SelectContent {
  --select-content-bg: var(--color-panel-solid);
  box-shadow: var(--shadow-5)
}

.rt-SelectItem[data-disabled] {
  color: var(--gray-a8)
}

.rt-SelectLabel {
  color: var(--gray-a11)
}

.rt-SelectSeparator {
  background-color: var(--gray-a6)
}

.rt-SelectContent.rt-variant-solid .rt-SelectItem[data-highlighted] {
  background-color: var(--accent-9);
  color: var(--accent-9-contrast)
}

.rt-SelectContent.rt-variant-solid:where(.rt-high-contrast) .rt-SelectItem[data-highlighted] {
  background-color: var(--accent-12);
  color: var(--accent-1)
}

.rt-SelectContent.rt-variant-soft .rt-SelectItem[data-highlighted] {
  background-color: var(--accent-a5)
}

.rt-Separator {
  background-color: var(--accent-a6)
}

.rt-Separator[data-orientation=vertical] {
  width: 1px;
  height: var(--separator-size)
}

.rt-Separator[data-orientation=horizontal] {
  width: var(--separator-size);
  height: 1px
}

@media all {
  .rt-Separator.rt-r-size-1 {
    --separator-size: var(--space-4)
  }

  .rt-Separator.rt-r-size-2 {
    --separator-size: var(--space-6)
  }

  .rt-Separator.rt-r-size-3 {
    --separator-size: var(--space-9)
  }

  .rt-Separator.rt-r-size-4 {
    --separator-size: 100%
  }
}

@media (min-width:520px) {
  .rt-Separator.xs\:rt-r-size-1 {
    --separator-size: var(--space-4)
  }

  .rt-Separator.xs\:rt-r-size-2 {
    --separator-size: var(--space-6)
  }

  .rt-Separator.xs\:rt-r-size-3 {
    --separator-size: var(--space-9)
  }

  .rt-Separator.xs\:rt-r-size-4 {
    --separator-size: 100%
  }
}

@media (min-width:768px) {
  .rt-Separator.sm\:rt-r-size-1 {
    --separator-size: var(--space-4)
  }

  .rt-Separator.sm\:rt-r-size-2 {
    --separator-size: var(--space-6)
  }

  .rt-Separator.sm\:rt-r-size-3 {
    --separator-size: var(--space-9)
  }

  .rt-Separator.sm\:rt-r-size-4 {
    --separator-size: 100%
  }
}

@media (min-width:1024px) {
  .rt-Separator.md\:rt-r-size-1 {
    --separator-size: var(--space-4)
  }

  .rt-Separator.md\:rt-r-size-2 {
    --separator-size: var(--space-6)
  }

  .rt-Separator.md\:rt-r-size-3 {
    --separator-size: var(--space-9)
  }

  .rt-Separator.md\:rt-r-size-4 {
    --separator-size: 100%
  }
}

@media (min-width:1280px) {
  .rt-Separator.lg\:rt-r-size-1 {
    --separator-size: var(--space-4)
  }

  .rt-Separator.lg\:rt-r-size-2 {
    --separator-size: var(--space-6)
  }

  .rt-Separator.lg\:rt-r-size-3 {
    --separator-size: var(--space-9)
  }

  .rt-Separator.lg\:rt-r-size-4 {
    --separator-size: 100%
  }
}

@media (min-width:1640px) {
  .rt-Separator.xl\:rt-r-size-1 {
    --separator-size: var(--space-4)
  }

  .rt-Separator.xl\:rt-r-size-2 {
    --separator-size: var(--space-6)
  }

  .rt-Separator.xl\:rt-r-size-3 {
    --separator-size: var(--space-9)
  }

  .rt-Separator.xl\:rt-r-size-4 {
    --separator-size: 100%
  }
}

.rt-SliderRoot {
  --slider-thumb-size: calc(var(--slider-track-size) + var(--space-1));
  position: relative;
  display: flex;
  align-items: center;
  flex-shrink: 0;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  touch-action: none
}

.rt-SliderRoot[data-orientation=horizontal] {
  height: var(--slider-thumb-size)
}

.rt-SliderRoot[data-orientation=vertical] {
  height: 100%;
  flex-direction: column;
  width: var(--slider-thumb-size)
}

.rt-SliderTrack {
  position: relative;
  flex-grow: 1;
  border-radius: var(--radius-1);
  overflow: hidden
}

.rt-SliderTrack[data-orientation=horizontal] {
  height: var(--slider-track-size)
}

.rt-SliderTrack[data-orientation=vertical] {
  width: var(--slider-track-size)
}

.rt-SliderRange {
  position: absolute
}

.rt-SliderRange[data-orientation=horizontal] {
  height: 100%
}

.rt-SliderRange[data-orientation=vertical] {
  width: 100%
}

.rt-SliderThumb {
  display: block;
  width: var(--slider-thumb-size);
  height: var(--slider-thumb-size);
  border-radius: var(--slider-thumb-radius)
}

.rt-SliderThumb:before {
  content: "";
  position: absolute;
  z-index: -1;
  width: 44px;
  height: 44px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%)
}

.rt-SliderThumb:after {
  content: "";
  position: absolute;
  inset: calc(-1 * var(--space-1) / 2);
  background-color: #fff;
  border-radius: var(--slider-thumb-radius);
  box-shadow: var(--slider-thumb-shadow)
}

.rt-SliderThumb:where(:focus-visible):after {
  box-shadow: var(--slider-thumb-shadow), 0 0 0 3px var(--accent-3), 0 0 0 5px var(--accent-8)
}

@media all {
  .rt-SliderRoot.rt-r-size-1 {
    --slider-track-size: calc(var(--space-1) * 1.5);
    --slider-thumb-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SliderRoot.rt-r-size-2 {
    --slider-track-size: var(--space-2);
    --slider-thumb-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SliderRoot.rt-r-size-3 {
    --slider-track-size: var(--space-3);
    --slider-thumb-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:520px) {
  .rt-SliderRoot.xs\:rt-r-size-1 {
    --slider-track-size: calc(var(--space-1) * 1.5);
    --slider-thumb-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SliderRoot.xs\:rt-r-size-2 {
    --slider-track-size: var(--space-2);
    --slider-thumb-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SliderRoot.xs\:rt-r-size-3 {
    --slider-track-size: var(--space-3);
    --slider-thumb-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:768px) {
  .rt-SliderRoot.sm\:rt-r-size-1 {
    --slider-track-size: calc(var(--space-1) * 1.5);
    --slider-thumb-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SliderRoot.sm\:rt-r-size-2 {
    --slider-track-size: var(--space-2);
    --slider-thumb-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SliderRoot.sm\:rt-r-size-3 {
    --slider-track-size: var(--space-3);
    --slider-thumb-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:1024px) {
  .rt-SliderRoot.md\:rt-r-size-1 {
    --slider-track-size: calc(var(--space-1) * 1.5);
    --slider-thumb-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SliderRoot.md\:rt-r-size-2 {
    --slider-track-size: var(--space-2);
    --slider-thumb-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SliderRoot.md\:rt-r-size-3 {
    --slider-track-size: var(--space-3);
    --slider-thumb-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:1280px) {
  .rt-SliderRoot.lg\:rt-r-size-1 {
    --slider-track-size: calc(var(--space-1) * 1.5);
    --slider-thumb-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SliderRoot.lg\:rt-r-size-2 {
    --slider-track-size: var(--space-2);
    --slider-thumb-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SliderRoot.lg\:rt-r-size-3 {
    --slider-track-size: var(--space-3);
    --slider-thumb-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:1640px) {
  .rt-SliderRoot.xl\:rt-r-size-1 {
    --slider-track-size: calc(var(--space-1) * 1.5);
    --slider-thumb-radius: max(var(--radius-1), var(--radius-full))
  }

  .rt-SliderRoot.xl\:rt-r-size-2 {
    --slider-track-size: var(--space-2);
    --slider-thumb-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SliderRoot.xl\:rt-r-size-3 {
    --slider-track-size: var(--space-3);
    --slider-thumb-radius: max(var(--radius-3), var(--radius-full))
  }
}

.rt-SliderRoot.rt-variant-surface .rt-SliderTrack {
  background-color: var(--gray-a3);
  box-shadow: inset 0 0 0 1px var(--gray-a5)
}

.rt-SliderRoot.rt-variant-surface .rt-SliderRange {
  background-color: var(--accent-9);
  box-shadow: inset 0 0 0 1px var(--gray-a5)
}

.rt-SliderRoot.rt-variant-surface .rt-SliderThumb {
  --slider-thumb-shadow: 0 0 0 1px var(--black-a7)
}

.rt-SliderRoot.rt-variant-classic .rt-SliderTrack {
  background-color: var(--gray-a3);
  box-shadow: var(--shadow-1)
}

.rt-SliderRoot.rt-variant-classic .rt-SliderRange {
  background-color: var(--accent-9);
  box-shadow: inset 0 0 0 1px var(--gray-a6), inset 0 1.5px 2px 0 var(--black-a7)
}

.rt-SliderRoot.rt-variant-classic .rt-SliderThumb {
  --slider-thumb-shadow: 0 0 0 1px var(--black-a7), 0 1px 3px var(--black-a3), 0 2px 4px -1px var(--black-a3)
}

.rt-SliderRoot.rt-variant-soft .rt-SliderTrack {
  background-color: var(--gray-a3);
  background-image: linear-gradient(to right, var(--accent-a3), var(--accent-a3))
}

.rt-SliderRoot.rt-variant-soft .rt-SliderRange {
  background-color: var(--accent-a7)
}

.rt-SliderRoot.rt-variant-soft .rt-SliderThumb {
  --slider-thumb-shadow: 0 0 0 1px var(--black-a7), 0 0 0 1px var(--accent-a3), 0 1px 2px var(--accent-a4), 0 1px 3px -0.5px var(--accent-a3)
}

.radix-themes {
  --slider-range-background-image__high-contrast: linear-gradient(90deg, rgba(0, 0, 0, .62), rgba(0, 0, 0, .62))
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --slider-range-background-image__high-contrast: none
}

.rt-SliderRoot.rt-high-contrast .rt-SliderRange {
  background-image: var(--slider-range-background-image__high-contrast)
}

.radix-themes {
  --slider-blend-mode__disabled: multiply
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --slider-blend-mode__disabled: screen
}

.rt-SliderRoot[data-disabled] {
  cursor: not-allowed;
  mix-blend-mode: var(--slider-blend-mode__disabled)
}

.rt-SliderRoot[data-disabled] .rt-SliderTrack[data-disabled] {
  background-color: var(--gray-a3);
  background-image: none;
  box-shadow: inset 0 0 0 1px var(--gray-a5)
}

.rt-SliderRoot[data-disabled] .rt-SliderRange[data-disabled] {
  background-color: transparent;
  box-shadow: none
}

.rt-SliderRoot[data-disabled] .rt-SliderThumb[data-disabled]:after {
  background-color: var(--gray-2);
  box-shadow: 0 0 0 1px var(--gray-6)
}

.rt-Strong {
  font-family: var(--strong-font-family);
  font-size: calc(var(--strong-font-size-adjust) * 1em);
  font-style: var(--strong-font-style);
  font-weight: var(--strong-font-weight);
  letter-spacing: calc(var(--strong-letter-spacing) + var(--letter-spacing, var(--default-letter-spacing)))
}

.rt-SwitchRoot {
  vertical-align: bottom;
  flex-shrink: 0;
  height: var(--line-height-2);
  --switch-padding: 1px;
  --switch-width: calc(var(--switch-height) * 1.75);
  --switch-thumb-size: calc(var(--switch-height) - var(--switch-padding) * 2);
  --switch-thumb-translate: calc(var(--switch-width) - var(--switch-height))
}

.rt-SwitchButton,
.rt-SwitchRoot {
  display: inline-flex;
  align-items: center
}

.rt-SwitchButton {
  position: relative;
  width: var(--switch-width);
  height: var(--switch-height);
  padding: var(--switch-padding);
  border-radius: var(--switch-radius)
}

.rt-SwitchButton:before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
  transition: background-position, background-color, box-shadow, filter;
  transition-timing-function: linear, ease-in-out, ease-in-out, ease-in-out;
  background-repeat: no-repeat;
  background-size: calc(var(--switch-width) * 2 + var(--switch-height)) 100%
}

.rt-SwitchButton:where([data-state=unchecked]):before {
  transition-duration: .12s, .14s, .14s, .14s;
  background-position-x: 100%
}

.rt-SwitchButton:where([data-state=checked]):before {
  transition-duration: .16s, .14s, .14s, .14s;
  background-position: 0
}

.rt-SwitchButton:where(:active):before {
  transition-duration: 30ms
}

.rt-SwitchButton:where(:focus-visible):after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
  box-shadow: 0 0 0 2px var(--accent-3), 0 0 0 4px var(--accent-a8)
}

.rt-SwitchThumb {
  background-color: #fff;
  position: relative;
  width: var(--switch-thumb-size);
  height: var(--switch-thumb-size);
  border-radius: calc(var(--switch-radius) - var(--switch-padding));
  transition: transform .14s cubic-bezier(.45, .05, .55, .95), box-shadow .14s ease-in-out
}

.rt-SwitchThumb:where([data-state=checked]) {
  transform: translateX(var(--switch-thumb-translate))
}

@media all {
  .rt-SwitchRoot.rt-r-size-1 {
    --switch-height: var(--space-4);
    --switch-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SwitchRoot.rt-r-size-2 {
    --switch-height: var(--space-5);
    --switch-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SwitchRoot.rt-r-size-3 {
    --switch-height: var(--space-6);
    --switch-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:520px) {
  .rt-SwitchRoot.xs\:rt-r-size-1 {
    --switch-height: var(--space-4);
    --switch-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SwitchRoot.xs\:rt-r-size-2 {
    --switch-height: var(--space-5);
    --switch-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SwitchRoot.xs\:rt-r-size-3 {
    --switch-height: var(--space-6);
    --switch-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:768px) {
  .rt-SwitchRoot.sm\:rt-r-size-1 {
    --switch-height: var(--space-4);
    --switch-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SwitchRoot.sm\:rt-r-size-2 {
    --switch-height: var(--space-5);
    --switch-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SwitchRoot.sm\:rt-r-size-3 {
    --switch-height: var(--space-6);
    --switch-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:1024px) {
  .rt-SwitchRoot.md\:rt-r-size-1 {
    --switch-height: var(--space-4);
    --switch-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SwitchRoot.md\:rt-r-size-2 {
    --switch-height: var(--space-5);
    --switch-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SwitchRoot.md\:rt-r-size-3 {
    --switch-height: var(--space-6);
    --switch-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:1280px) {
  .rt-SwitchRoot.lg\:rt-r-size-1 {
    --switch-height: var(--space-4);
    --switch-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SwitchRoot.lg\:rt-r-size-2 {
    --switch-height: var(--space-5);
    --switch-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SwitchRoot.lg\:rt-r-size-3 {
    --switch-height: var(--space-6);
    --switch-radius: max(var(--radius-4), var(--radius-full))
  }
}

@media (min-width:1640px) {
  .rt-SwitchRoot.xl\:rt-r-size-1 {
    --switch-height: var(--space-4);
    --switch-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-SwitchRoot.xl\:rt-r-size-2 {
    --switch-height: var(--space-5);
    --switch-radius: max(var(--radius-3), var(--radius-full))
  }

  .rt-SwitchRoot.xl\:rt-r-size-3 {
    --switch-height: var(--space-6);
    --switch-radius: max(var(--radius-4), var(--radius-full))
  }
}

.rt-SwitchRoot.rt-variant-surface .rt-SwitchButton:before {
  background-color: var(--gray-a3);
  background-image: linear-gradient(to right, var(--accent-9) 40%, transparent 60%);
  box-shadow: inset 0 0 0 1px var(--gray-a7)
}

.rt-SwitchRoot.rt-variant-surface .rt-SwitchButton:where(:active):before {
  background-color: var(--gray-a4)
}

.rt-SwitchRoot.rt-variant-surface .rt-SwitchButton:where([data-state=checked]:active):before {
  filter: var(--switch-button-filter__surface-checked-active)
}

.rt-SwitchRoot.rt-variant-surface:where(.rt-high-contrast) .rt-SwitchButton:before {
  background-image: linear-gradient(to right, var(--switch-button-overlay__high-contrast-checked) 40%, transparent 60%), linear-gradient(to right, var(--accent-9) 40%, transparent 60%)
}

.rt-SwitchRoot.rt-variant-surface .rt-SwitchThumb:where([data-state=unchecked]) {
  box-shadow: 0 0 0 1px var(--gray-8), 0 1px 1px var(--black-a3), 0 2px 4px -1px var(--black-a3)
}

.rt-SwitchRoot.rt-variant-surface .rt-SwitchThumb:where([data-state=checked]) {
  box-shadow: 0 0 0 1px var(--black-a5), 0 1px 1px var(--black-a3), 0 2px 4px -1px var(--black-a3)
}

.radix-themes {
  --switch-button-filter__surface-checked-active: brightness(0.92) saturate(1.1)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --switch-button-filter__surface-checked-active: brightness(1.08)
}

.rt-SwitchRoot.rt-variant-classic .rt-SwitchButton:before {
  background-image: linear-gradient(to right, var(--accent-9) 40%, transparent 60%);
  background-color: var(--gray-a4);
  box-shadow: var(--shadow-1)
}

.rt-SwitchRoot.rt-variant-classic .rt-SwitchButton:where([data-state=unchecked]:active):before {
  background-color: var(--gray-a6)
}

.rt-SwitchRoot.rt-variant-classic .rt-SwitchButton:where([data-state=checked]):before {
  box-shadow: inset 0 0 0 1px var(--gray-a6), inset 0 1.5px 2px 0 var(--black-a7)
}

.rt-SwitchRoot.rt-variant-classic .rt-SwitchButton:where([data-state=checked]:active):before {
  filter: var(--switch-button-filter__surface-checked-active)
}

.rt-SwitchRoot.rt-variant-classic:where(.rt-high-contrast) .rt-SwitchButton:before {
  background-image: linear-gradient(to right, var(--switch-button-overlay__high-contrast-checked) 40%, transparent 60%), linear-gradient(to right, var(--accent-9) 40%, transparent 60%)
}

.rt-SwitchRoot.rt-variant-classic .rt-SwitchThumb {
  box-shadow: 0 0 0 1px var(--black-a4), 0 1px 3px var(--black-a7), 0 2px 4px -1px var(--black-a3)
}

.radix-themes {
  --switch-button-filter__soft-checked-active: contrast(1.2) brightness(0.75) saturate(1.1)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --switch-button-filter__soft-checked-active: brightness(1.08)
}

.rt-SwitchRoot.rt-variant-soft .rt-SwitchButton:before {
  background-image: linear-gradient(to right, var(--accent-a8) 40%, transparent 60%), linear-gradient(to right, var(--accent-a3), var(--accent-a3))
}

.rt-SwitchRoot.rt-variant-soft .rt-SwitchButton:where([data-state=unchecked]):before {
  background-color: var(--gray-a5)
}

.rt-SwitchRoot.rt-variant-soft .rt-SwitchButton:where([data-state=unchecked]:active):before {
  background-color: var(--gray-a7)
}

.rt-SwitchRoot.rt-variant-soft .rt-SwitchButton:where([data-state=checked]:active):before {
  filter: var(--switch-button-filter__soft-checked-active)
}

.rt-SwitchRoot.rt-variant-soft:where(.rt-high-contrast) .rt-SwitchButton:before {
  background-image: linear-gradient(to right, var(--switch-button-overlay__high-contrast-checked) 40%, transparent 60%), linear-gradient(to right, var(--accent-a8) 40%, transparent 60%), linear-gradient(to right, var(--accent-a3), var(--accent-a3))
}

.rt-SwitchRoot.rt-variant-soft .rt-SwitchThumb {
  box-shadow: 0 0 0 1px var(--accent-a3), 0 1px 3px var(--accent-a4), 0 2px 4px -1px var(--accent-a3);
  filter: saturate(.45)
}

.radix-themes {
  --switch-button-overlay__high-contrast-checked: var(--black-a11);
  --switch-button-filter__high-contrast-checked-active: contrast(0.82) saturate(1.2) brightness(1.16)
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --switch-button-overlay__high-contrast-checked: transparent;
  --switch-button-filter__high-contrast-checked-active: brightness(1.08)
}

.rt-SwitchRoot.rt-high-contrast .rt-SwitchButton:where([data-state=checked]:active):before {
  filter: var(--switch-button-filter__high-contrast-checked-active)
}

.radix-themes {
  --switch-thumb-shadow__disabled: 0 0 0 1px var(--gray-6);
  --switch-blend-mode__disabled: multiply
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --switch-thumb-shadow__disabled: 0 0 0 1px var(--gray-5);
  --switch-blend-mode__disabled: screen
}

.rt-SwitchRoot .rt-SwitchButton[data-disabled] {
  cursor: not-allowed;
  mix-blend-mode: var(--switch-blend-mode__disabled)
}

.rt-SwitchRoot .rt-SwitchButton[data-disabled]:before {
  background-image: none;
  background-color: var(--gray-a3);
  box-shadow: inset 0 0 0 1px var(--gray-a5)
}

.rt-SwitchRoot .rt-SwitchThumb[data-disabled] {
  background-color: var(--gray-2);
  box-shadow: var(--switch-thumb-shadow__disabled)
}

.rt-TabsList {
  display: flex;
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none
}

.rt-TabsList::-webkit-scrollbar {
  display: none
}

.rt-TabsTrigger {
  box-sizing: border-box;
  flex-shrink: 0;
  position: relative;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none
}

.rt-TabsTrigger,
.rt-TabsTriggerInner,
.rt-TabsTriggerInnerHidden {
  display: flex;
  align-items: center;
  justify-content: center
}

.rt-TabsTriggerInner {
  position: absolute
}

.rt-TabsTrigger[data-state=active] .rt-TabsTriggerInner {
  font-weight: var(--font-weight-medium);
  letter-spacing: -.01em
}

.rt-TabsTriggerInnerHidden {
  visibility: hidden;
  font-weight: var(--font-weight-medium)
}

.rt-TabsContent {
  position: relative;
  outline: 0
}

.rt-TabsTrigger {
  padding-left: var(--tabs-trigger-padding-x);
  padding-right: var(--tabs-trigger-padding-x)
}

.rt-TabsTriggerInner,
.rt-TabsTriggerInnerHidden {
  padding: var(--tabs-trigger-inner-padding-y) var(--tabs-trigger-inner-padding-x);
  border-radius: var(--tabs-trigger-inner-radius)
}

@media all {
  .rt-TabsList.rt-r-size-1 {
    height: var(--space-6);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    --tabs-trigger-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-y: calc(var(--space-1) * 0.5);
    --tabs-trigger-inner-radius: var(--radius-1)
  }

  .rt-TabsList.rt-r-size-2 {
    height: var(--space-7);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    --tabs-trigger-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-y: var(--space-1);
    --tabs-trigger-inner-radius: var(--radius-2)
  }
}

@media (min-width:520px) {
  .rt-TabsList.xs\:rt-r-size-1 {
    height: var(--space-6);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    --tabs-trigger-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-y: calc(var(--space-1) * 0.5);
    --tabs-trigger-inner-radius: var(--radius-1)
  }

  .rt-TabsList.xs\:rt-r-size-2 {
    height: var(--space-7);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    --tabs-trigger-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-y: var(--space-1);
    --tabs-trigger-inner-radius: var(--radius-2)
  }
}

@media (min-width:768px) {
  .rt-TabsList.sm\:rt-r-size-1 {
    height: var(--space-6);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    --tabs-trigger-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-y: calc(var(--space-1) * 0.5);
    --tabs-trigger-inner-radius: var(--radius-1)
  }

  .rt-TabsList.sm\:rt-r-size-2 {
    height: var(--space-7);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    --tabs-trigger-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-y: var(--space-1);
    --tabs-trigger-inner-radius: var(--radius-2)
  }
}

@media (min-width:1024px) {
  .rt-TabsList.md\:rt-r-size-1 {
    height: var(--space-6);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    --tabs-trigger-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-y: calc(var(--space-1) * 0.5);
    --tabs-trigger-inner-radius: var(--radius-1)
  }

  .rt-TabsList.md\:rt-r-size-2 {
    height: var(--space-7);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    --tabs-trigger-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-y: var(--space-1);
    --tabs-trigger-inner-radius: var(--radius-2)
  }
}

@media (min-width:1280px) {
  .rt-TabsList.lg\:rt-r-size-1 {
    height: var(--space-6);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    --tabs-trigger-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-y: calc(var(--space-1) * 0.5);
    --tabs-trigger-inner-radius: var(--radius-1)
  }

  .rt-TabsList.lg\:rt-r-size-2 {
    height: var(--space-7);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    --tabs-trigger-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-y: var(--space-1);
    --tabs-trigger-inner-radius: var(--radius-2)
  }
}

@media (min-width:1640px) {
  .rt-TabsList.xl\:rt-r-size-1 {
    height: var(--space-6);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1);
    --tabs-trigger-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-x: var(--space-1);
    --tabs-trigger-inner-padding-y: calc(var(--space-1) * 0.5);
    --tabs-trigger-inner-radius: var(--radius-1)
  }

  .rt-TabsList.xl\:rt-r-size-2 {
    height: var(--space-7);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2);
    --tabs-trigger-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-x: var(--space-2);
    --tabs-trigger-inner-padding-y: var(--space-1);
    --tabs-trigger-inner-radius: var(--radius-2)
  }
}

.rt-TabsList {
  box-shadow: inset 0 -1px 0 0 var(--gray-a5)
}

.rt-TabsTrigger {
  color: var(--gray-a11)
}

@media (hover:hover) {
  .rt-TabsTrigger:hover {
    color: var(--gray-12)
  }

  .rt-TabsTrigger:hover .rt-TabsTriggerInner {
    background-color: var(--gray-a3)
  }

  .rt-TabsTrigger:focus-visible:hover .rt-TabsTriggerInner {
    background-color: var(--accent-a3)
  }
}

.rt-TabsTrigger[data-state=active] {
  color: var(--gray-12)
}

.rt-TabsTrigger:focus-visible .rt-TabsTriggerInner {
  box-shadow: 0 0 0 2px var(--accent-a8)
}

.rt-TabsTrigger[data-state=active]:before {
  box-sizing: border-box;
  content: "";
  height: 2px;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: var(--accent-10)
}

.rt-TabsContent:focus-visible {
  box-shadow: 0 0 0 2px var(--accent-a8)
}

.rt-TableRootTable {
  --table-row-background: transparent;
  --table-row-border-bottom: inset 0 -1px var(--gray-a5);
  width: 100%;
  text-align: left;
  vertical-align: top;
  border-collapse: collapse;
  border-radius: calc(var(--table-border-radius) - 1px);
  border-spacing: 0;
  box-sizing: border-box;
  height: 0
}

.rt-TableBody,
.rt-TableHeader,
.rt-TableRow {
  vertical-align: inherit
}

.rt-TableRow {
  color: var(--gray-12)
}

.rt-TableCell {
  background-color: var(--table-row-background);
  box-shadow: var(--table-row-border-bottom);
  box-sizing: border-box;
  vertical-align: inherit;
  padding: var(--table-cell-padding);
  height: var(--table-cell-min-height)
}

.rt-TableColumnHeaderCell {
  font-weight: 700
}

.rt-TableRowHeaderCell {
  font-weight: 400
}

@media all {
  .rt-TableRoot.rt-r-size-1 {
    --table-border-radius: var(--radius-3);
    --table-cell-padding: var(--space-2);
    --table-cell-min-height: calc(36px * var(--scaling))
  }

  .rt-TableRoot.rt-r-size-1 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.rt-r-size-2 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3);
    --table-cell-min-height: calc(44px * var(--scaling))
  }

  .rt-TableRoot.rt-r-size-2 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.rt-r-size-3 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3) var(--space-4);
    --table-cell-min-height: calc(48px * var(--scaling))
  }

  .rt-TableRoot.rt-r-size-3 .rt-TableRootTable {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3)
  }
}

@media (min-width:520px) {
  .rt-TableRoot.xs\:rt-r-size-1 {
    --table-border-radius: var(--radius-3);
    --table-cell-padding: var(--space-2);
    --table-cell-min-height: calc(36px * var(--scaling))
  }

  .rt-TableRoot.xs\:rt-r-size-1 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.xs\:rt-r-size-2 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3);
    --table-cell-min-height: calc(44px * var(--scaling))
  }

  .rt-TableRoot.xs\:rt-r-size-2 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.xs\:rt-r-size-3 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3) var(--space-4);
    --table-cell-min-height: calc(48px * var(--scaling))
  }

  .rt-TableRoot.xs\:rt-r-size-3 .rt-TableRootTable {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3)
  }
}

@media (min-width:768px) {
  .rt-TableRoot.sm\:rt-r-size-1 {
    --table-border-radius: var(--radius-3);
    --table-cell-padding: var(--space-2);
    --table-cell-min-height: calc(36px * var(--scaling))
  }

  .rt-TableRoot.sm\:rt-r-size-1 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.sm\:rt-r-size-2 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3);
    --table-cell-min-height: calc(44px * var(--scaling))
  }

  .rt-TableRoot.sm\:rt-r-size-2 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.sm\:rt-r-size-3 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3) var(--space-4);
    --table-cell-min-height: calc(48px * var(--scaling))
  }

  .rt-TableRoot.sm\:rt-r-size-3 .rt-TableRootTable {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3)
  }
}

@media (min-width:1024px) {
  .rt-TableRoot.md\:rt-r-size-1 {
    --table-border-radius: var(--radius-3);
    --table-cell-padding: var(--space-2);
    --table-cell-min-height: calc(36px * var(--scaling))
  }

  .rt-TableRoot.md\:rt-r-size-1 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.md\:rt-r-size-2 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3);
    --table-cell-min-height: calc(44px * var(--scaling))
  }

  .rt-TableRoot.md\:rt-r-size-2 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.md\:rt-r-size-3 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3) var(--space-4);
    --table-cell-min-height: calc(48px * var(--scaling))
  }

  .rt-TableRoot.md\:rt-r-size-3 .rt-TableRootTable {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3)
  }
}

@media (min-width:1280px) {
  .rt-TableRoot.lg\:rt-r-size-1 {
    --table-border-radius: var(--radius-3);
    --table-cell-padding: var(--space-2);
    --table-cell-min-height: calc(36px * var(--scaling))
  }

  .rt-TableRoot.lg\:rt-r-size-1 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.lg\:rt-r-size-2 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3);
    --table-cell-min-height: calc(44px * var(--scaling))
  }

  .rt-TableRoot.lg\:rt-r-size-2 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.lg\:rt-r-size-3 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3) var(--space-4);
    --table-cell-min-height: calc(48px * var(--scaling))
  }

  .rt-TableRoot.lg\:rt-r-size-3 .rt-TableRootTable {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3)
  }
}

@media (min-width:1640px) {
  .rt-TableRoot.xl\:rt-r-size-1 {
    --table-border-radius: var(--radius-3);
    --table-cell-padding: var(--space-2);
    --table-cell-min-height: calc(36px * var(--scaling))
  }

  .rt-TableRoot.xl\:rt-r-size-1 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.xl\:rt-r-size-2 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3);
    --table-cell-min-height: calc(44px * var(--scaling))
  }

  .rt-TableRoot.xl\:rt-r-size-2 .rt-TableRootTable {
    font-size: var(--font-size-2);
    line-height: var(--line-height-2)
  }

  .rt-TableRoot.xl\:rt-r-size-3 {
    --table-border-radius: var(--radius-4);
    --table-cell-padding: var(--space-3) var(--space-4);
    --table-cell-min-height: calc(48px * var(--scaling))
  }

  .rt-TableRoot.xl\:rt-r-size-3 .rt-TableRootTable {
    font-size: var(--font-size-3);
    line-height: var(--line-height-3)
  }
}

.rt-TableRoot.rt-variant-surface {
  border: 1px solid var(--gray-a5);
  border-radius: var(--table-border-radius);
  background-color: var(--color-panel);
  position: relative
}

.rt-TableRoot.rt-variant-surface .rt-TableRootTable {
  overflow: hidden
}

.rt-TableRoot.rt-variant-surface .rt-TableRootTable :where(.rt-TableHeader) {
  --table-row-background: var(--gray-a2)
}

.rt-TableRoot.rt-variant-surface .rt-TableRootTable :where(.rt-TableBody .rt-TableRow:last-child) {
  --table-row-border-bottom: none
}

.rt-TableRoot.rt-variant-ghost .rt-ScrollAreaScrollbar[data-orientation=horizontal] {
  --scrollarea-scrollbar-margin-left: 0;
  --scrollarea-scrollbar-margin-right: 0
}

.rt-Inset>.rt-TableRootTable .rt-TableCell:first-child {
  padding-left: var(--inset-padding)
}

.rt-Inset>.rt-TableRootTable .rt-TableCell:last-child {
  padding-right: var(--inset-padding)
}

.rt-TextArea {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-width: 0;
  font-family: inherit;
  -webkit-tap-highlight-color: transparent;
  outline: none;
  box-sizing: border-box;
  display: block;
  width: 100%;
  flex-shrink: 0;
  flex-grow: 1;
  resize: none;
  cursor: auto;
  scrollbar-width: thin
}

.rt-TextArea::-webkit-scrollbar {
  width: 12px;
  height: 12px
}

.rt-TextArea::-webkit-scrollbar-thumb,
.rt-TextArea::-webkit-scrollbar-track {
  background-clip: content-box;
  border: 4px solid transparent;
  border-radius: 12px
}

.rt-TextArea::-webkit-scrollbar-track {
  background-color: var(--gray-a3)
}

.rt-TextArea::-webkit-scrollbar-thumb {
  background-color: var(--gray-a8)
}

@media (hover:hover) {
  .rt-TextArea:not(:disabled)::-webkit-scrollbar-thumb:hover {
    background-color: var(--gray-a9)
  }
}

@media all {
  .rt-TextArea.rt-r-size-1 {
    min-height: var(--space-8);
    padding: var(--space-1);
    border-radius: var(--radius-2);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextArea.rt-r-size-2 {
    min-height: var(--space-9);
    padding: var(--space-2);
    border-radius: var(--radius-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextArea.rt-r-size-3 {
    min-height: 80px;
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:520px) {
  .rt-TextArea.xs\:rt-r-size-1 {
    min-height: var(--space-8);
    padding: var(--space-1);
    border-radius: var(--radius-2);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextArea.xs\:rt-r-size-2 {
    min-height: var(--space-9);
    padding: var(--space-2);
    border-radius: var(--radius-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextArea.xs\:rt-r-size-3 {
    min-height: 80px;
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:768px) {
  .rt-TextArea.sm\:rt-r-size-1 {
    min-height: var(--space-8);
    padding: var(--space-1);
    border-radius: var(--radius-2);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextArea.sm\:rt-r-size-2 {
    min-height: var(--space-9);
    padding: var(--space-2);
    border-radius: var(--radius-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextArea.sm\:rt-r-size-3 {
    min-height: 80px;
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:1024px) {
  .rt-TextArea.md\:rt-r-size-1 {
    min-height: var(--space-8);
    padding: var(--space-1);
    border-radius: var(--radius-2);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextArea.md\:rt-r-size-2 {
    min-height: var(--space-9);
    padding: var(--space-2);
    border-radius: var(--radius-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextArea.md\:rt-r-size-3 {
    min-height: 80px;
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:1280px) {
  .rt-TextArea.lg\:rt-r-size-1 {
    min-height: var(--space-8);
    padding: var(--space-1);
    border-radius: var(--radius-2);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextArea.lg\:rt-r-size-2 {
    min-height: var(--space-9);
    padding: var(--space-2);
    border-radius: var(--radius-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextArea.lg\:rt-r-size-3 {
    min-height: 80px;
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

@media (min-width:1640px) {
  .rt-TextArea.xl\:rt-r-size-1 {
    min-height: var(--space-8);
    padding: var(--space-1);
    border-radius: var(--radius-2);
    font-size: var(--font-size-1);
    line-height: var(--line-height-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextArea.xl\:rt-r-size-2 {
    min-height: var(--space-9);
    padding: var(--space-2);
    border-radius: var(--radius-2);
    font-size: var(--font-size-2);
    line-height: var(--line-height-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextArea.xl\:rt-r-size-3 {
    min-height: 80px;
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-3);
    font-size: var(--font-size-3);
    line-height: var(--line-height-3);
    letter-spacing: var(--letter-spacing-3)
  }
}

.rt-TextArea::-moz-placeholder {
  color: var(--gray-a10);
  opacity: 1
}

.rt-TextArea::placeholder {
  color: var(--gray-a10);
  opacity: 1
}

.rt-TextArea:-webkit-autofill {
  -webkit-text-fill-color: var(--gray-12);
  box-shadow: var(--shadow-1), inset 0 0 0 100px var(--accent-3)
}

.rt-TextArea:autofill {
  -webkit-text-fill-color: var(--gray-12);
  box-shadow: var(--shadow-1), inset 0 0 0 100px var(--accent-3)
}

.rt-TextArea:-webkit-autofill:focus {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8), inset 0 0 0 100px var(--accent-3)
}

.rt-TextArea:autofill:focus {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8), inset 0 0 0 100px var(--accent-3)
}

.rt-TextArea:-moz-read-only::-moz-placeholder {
  color: var(--gray-a7)
}

.rt-TextArea:read-only::-moz-placeholder {
  color: var(--gray-a7)
}

.rt-TextArea:-moz-read-only::placeholder {
  color: var(--gray-a7)
}

.rt-TextArea:read-only::placeholder {
  color: var(--gray-a7)
}

.rt-TextArea:-moz-read-only::-moz-selection {
  background-color: var(--gray-a5)
}

.rt-TextArea:read-only::-moz-selection {
  background-color: var(--gray-a5)
}

.rt-TextArea:-moz-read-only::selection {
  background-color: var(--gray-a5)
}

.rt-TextArea:read-only::selection {
  background-color: var(--gray-a5)
}

.rt-TextArea.rt-variant-surface {
  color: var(--gray-12);
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a7)
}

.rt-TextArea.rt-variant-surface:focus {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-TextArea.rt-variant-classic {
  color: var(--gray-12);
  background-color: var(--color-surface);
  box-shadow: var(--shadow-1)
}

.rt-TextArea.rt-variant-classic:focus {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8), var(--shadow-1)
}

.rt-TextArea.rt-variant-soft {
  color: var(--accent-12);
  background-color: var(--accent-a3)
}

.rt-TextArea.rt-variant-soft:focus {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-TextArea.rt-variant-soft:-moz-read-only {
  color: var(--gray-12)
}

.rt-TextArea.rt-variant-soft:read-only {
  color: var(--gray-12)
}

.rt-TextArea.rt-variant-soft::-moz-placeholder {
  color: var(--accent-12);
  opacity: .5
}

.rt-TextArea.rt-variant-soft::placeholder {
  color: var(--accent-12);
  opacity: .5
}

.rt-TextArea.rt-variant-soft::-moz-selection {
  background-color: var(--accent-a5)
}

.rt-TextArea.rt-variant-soft::selection {
  background-color: var(--accent-a5)
}

.rt-TextArea:disabled {
  color: var(--gray-a9);
  box-shadow: inset 0 0 0 1px var(--gray-a6);
  background-color: var(--gray-a3);
  cursor: not-allowed
}

.rt-TextArea:-moz-read-only {
  background-color: var(--gray-a3)
}

.rt-TextArea:read-only {
  background-color: var(--gray-a3)
}

.rt-TextArea:-moz-read-only:not(:focus) {
  box-shadow: inset 0 0 0 1px var(--gray-a6)
}

.rt-TextArea:read-only:not(:focus) {
  box-shadow: inset 0 0 0 1px var(--gray-a6)
}

.rt-TextArea:-moz-read-only:focus {
  box-shadow: inset 0 0 0 1px var(--gray-8), 0 0 0 1px var(--gray-a8)
}

.rt-TextArea:read-only:focus {
  box-shadow: inset 0 0 0 1px var(--gray-8), 0 0 0 1px var(--gray-a8)
}

.rt-TextFieldRoot {
  position: relative;
  cursor: text
}

.rt-TextFieldInput {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-width: 0;
  -webkit-tap-highlight-color: transparent;
  outline: none;
  font-family: inherit;
  text-overflow: ellipsis;
  background-color: transparent;
  position: relative;
  z-index: 1
}

.rt-TextFieldChrome {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none
}

.rt-TextFieldSlot {
  position: relative;
  z-index: 1;
  color: var(--gray-a11)
}

.rt-TextFieldSlot[data-accent-color] {
  color: var(--accent-a11)
}

.rt-TextFieldSlot:empty {
  display: none
}

.rt-TextFieldRoot {
  display: flex;
  box-sizing: border-box
}

.rt-TextFieldSlot {
  flex-shrink: 0;
  display: flex;
  align-items: center
}

.rt-TextFieldInput {
  display: block;
  box-sizing: border-box;
  padding: 0;
  width: 100%
}

.rt-TextFieldRoot .rt-TextFieldSlot+.rt-TextFieldInput {
  padding-left: 0
}

@media all {
  .rt-TextFieldSlot:where(.rt-r-size-1) {
    gap: var(--space-2);
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-TextFieldSlot:where(.rt-r-size-2) {
    gap: var(--space-2);
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-TextFieldSlot:where(.rt-r-size-3) {
    gap: var(--space-3);
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-TextFieldInput:where(.rt-r-size-1) {
    height: var(--space-5);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-1);
    font-size: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextFieldInput:where(.rt-r-size-1)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.rt-r-size-2) {
    height: var(--space-6);
    padding-top: 0;
    padding-bottom: 1px;
    padding-left: var(--space-2);
    font-size: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextFieldInput:where(.rt-r-size-2)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.rt-r-size-3) {
    height: var(--space-7);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-3);
    font-size: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-TextFieldInput:where(.rt-r-size-3)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:520px) {
  .rt-TextFieldSlot:where(.xs\:rt-r-size-1) {
    gap: var(--space-2);
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-TextFieldSlot:where(.xs\:rt-r-size-2) {
    gap: var(--space-2);
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-TextFieldSlot:where(.xs\:rt-r-size-3) {
    gap: var(--space-3);
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-TextFieldInput:where(.xs\:rt-r-size-1) {
    height: var(--space-5);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-1);
    font-size: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextFieldInput:where(.xs\:rt-r-size-1)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.xs\:rt-r-size-2) {
    height: var(--space-6);
    padding-top: 0;
    padding-bottom: 1px;
    padding-left: var(--space-2);
    font-size: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextFieldInput:where(.xs\:rt-r-size-2)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.xs\:rt-r-size-3) {
    height: var(--space-7);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-3);
    font-size: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-TextFieldInput:where(.xs\:rt-r-size-3)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:768px) {
  .rt-TextFieldSlot:where(.sm\:rt-r-size-1) {
    gap: var(--space-2);
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-TextFieldSlot:where(.sm\:rt-r-size-2) {
    gap: var(--space-2);
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-TextFieldSlot:where(.sm\:rt-r-size-3) {
    gap: var(--space-3);
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-TextFieldInput:where(.sm\:rt-r-size-1) {
    height: var(--space-5);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-1);
    font-size: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextFieldInput:where(.sm\:rt-r-size-1)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.sm\:rt-r-size-2) {
    height: var(--space-6);
    padding-top: 0;
    padding-bottom: 1px;
    padding-left: var(--space-2);
    font-size: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextFieldInput:where(.sm\:rt-r-size-2)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.sm\:rt-r-size-3) {
    height: var(--space-7);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-3);
    font-size: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-TextFieldInput:where(.sm\:rt-r-size-3)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:1024px) {
  .rt-TextFieldSlot:where(.md\:rt-r-size-1) {
    gap: var(--space-2);
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-TextFieldSlot:where(.md\:rt-r-size-2) {
    gap: var(--space-2);
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-TextFieldSlot:where(.md\:rt-r-size-3) {
    gap: var(--space-3);
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-TextFieldInput:where(.md\:rt-r-size-1) {
    height: var(--space-5);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-1);
    font-size: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextFieldInput:where(.md\:rt-r-size-1)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.md\:rt-r-size-2) {
    height: var(--space-6);
    padding-top: 0;
    padding-bottom: 1px;
    padding-left: var(--space-2);
    font-size: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextFieldInput:where(.md\:rt-r-size-2)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.md\:rt-r-size-3) {
    height: var(--space-7);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-3);
    font-size: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-TextFieldInput:where(.md\:rt-r-size-3)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:1280px) {
  .rt-TextFieldSlot:where(.lg\:rt-r-size-1) {
    gap: var(--space-2);
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-TextFieldSlot:where(.lg\:rt-r-size-2) {
    gap: var(--space-2);
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-TextFieldSlot:where(.lg\:rt-r-size-3) {
    gap: var(--space-3);
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-TextFieldInput:where(.lg\:rt-r-size-1) {
    height: var(--space-5);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-1);
    font-size: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextFieldInput:where(.lg\:rt-r-size-1)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.lg\:rt-r-size-2) {
    height: var(--space-6);
    padding-top: 0;
    padding-bottom: 1px;
    padding-left: var(--space-2);
    font-size: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextFieldInput:where(.lg\:rt-r-size-2)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.lg\:rt-r-size-3) {
    height: var(--space-7);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-3);
    font-size: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-TextFieldInput:where(.lg\:rt-r-size-3)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-3), var(--radius-full))
  }
}

@media (min-width:1640px) {
  .rt-TextFieldSlot:where(.xl\:rt-r-size-1) {
    gap: var(--space-2);
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-TextFieldSlot:where(.xl\:rt-r-size-2) {
    gap: var(--space-2);
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-TextFieldSlot:where(.xl\:rt-r-size-3) {
    gap: var(--space-3);
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-TextFieldInput:where(.xl\:rt-r-size-1) {
    height: var(--space-5);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-1);
    font-size: var(--font-size-1);
    letter-spacing: var(--letter-spacing-1)
  }

  .rt-TextFieldInput:where(.xl\:rt-r-size-1)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.xl\:rt-r-size-2) {
    height: var(--space-6);
    padding-top: 0;
    padding-bottom: 1px;
    padding-left: var(--space-2);
    font-size: var(--font-size-2);
    letter-spacing: var(--letter-spacing-2)
  }

  .rt-TextFieldInput:where(.xl\:rt-r-size-2)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-2), var(--radius-full))
  }

  .rt-TextFieldInput:where(.xl\:rt-r-size-3) {
    height: var(--space-7);
    padding-top: .5px;
    padding-bottom: 1px;
    padding-left: var(--space-3);
    font-size: var(--font-size-3);
    letter-spacing: var(--letter-spacing-3)
  }

  .rt-TextFieldInput:where(.xl\:rt-r-size-3)+.rt-TextFieldChrome {
    border-radius: max(var(--radius-3), var(--radius-full))
  }
}

.rt-TextFieldInput::-moz-placeholder {
  color: var(--gray-a10);
  opacity: 1
}

.rt-TextFieldInput::placeholder {
  color: var(--gray-a10);
  opacity: 1
}

.rt-TextFieldInput:-webkit-autofill+.rt-TextFieldChrome {
  -webkit-text-fill-color: var(--gray-12);
  box-shadow: var(--shadow-1), inset 0 0 0 100px var(--accent-3)
}

.rt-TextFieldInput:autofill+.rt-TextFieldChrome {
  -webkit-text-fill-color: var(--gray-12);
  box-shadow: var(--shadow-1), inset 0 0 0 100px var(--accent-3)
}

.rt-TextFieldInput:-webkit-autofill:focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8), inset 0 0 0 100px var(--accent-3)
}

.rt-TextFieldInput:autofill:focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8), inset 0 0 0 100px var(--accent-3)
}

.rt-TextFieldInput:-moz-read-only::-moz-placeholder {
  color: var(--gray-a7)
}

.rt-TextFieldInput:read-only::-moz-placeholder {
  color: var(--gray-a7)
}

.rt-TextFieldInput:-moz-read-only::placeholder {
  color: var(--gray-a7)
}

.rt-TextFieldInput:read-only::placeholder {
  color: var(--gray-a7)
}

.rt-TextFieldInput:-moz-read-only::-moz-selection {
  background-color: var(--gray-a5)
}

.rt-TextFieldInput:read-only::-moz-selection {
  background-color: var(--gray-a5)
}

.rt-TextFieldInput:-moz-read-only::selection {
  background-color: var(--gray-a5)
}

.rt-TextFieldInput:read-only::selection {
  background-color: var(--gray-a5)
}

.rt-TextFieldInput:where(.rt-variant-surface) {
  color: var(--gray-12)
}

.rt-TextFieldInput:where(.rt-variant-surface)+.rt-TextFieldChrome {
  background-color: var(--color-surface);
  box-shadow: inset 0 0 0 1px var(--gray-a7)
}

.rt-TextFieldInput:where(.rt-variant-surface):focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-TextFieldInput:where(.rt-variant-classic) {
  color: var(--gray-12)
}

.rt-TextFieldInput:where(.rt-variant-classic)+.rt-TextFieldChrome {
  background-color: var(--color-surface);
  box-shadow: var(--shadow-1)
}

.rt-TextFieldInput:where(.rt-variant-classic):focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8), var(--shadow-1)
}

.rt-TextFieldInput:where(.rt-variant-soft) {
  color: var(--accent-12)
}

.rt-TextFieldInput:where(.rt-variant-soft)+.rt-TextFieldChrome {
  background-color: var(--accent-a3)
}

.rt-TextFieldInput:where(.rt-variant-soft):focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--accent-8), 0 0 0 1px var(--accent-a8)
}

.rt-TextFieldInput:where(.rt-variant-soft):-moz-read-only {
  color: var(--gray-12)
}

.rt-TextFieldInput:where(.rt-variant-soft):read-only {
  color: var(--gray-12)
}

.rt-TextFieldInput:where(.rt-variant-soft)::-moz-placeholder {
  color: var(--accent-12);
  opacity: .5
}

.rt-TextFieldInput:where(.rt-variant-soft)::placeholder {
  color: var(--accent-12);
  opacity: .5
}

.rt-TextFieldInput:where(.rt-variant-soft)::-moz-selection {
  background-color: var(--accent-a5)
}

.rt-TextFieldInput:where(.rt-variant-soft)::selection {
  background-color: var(--accent-a5)
}

.rt-TextFieldInput:disabled {
  color: var(--gray-a9);
  cursor: not-allowed
}

.rt-TextFieldInput:disabled+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--gray-a6);
  background-color: var(--gray-a3);
  cursor: not-allowed
}

.rt-TextFieldRoot:has(.rt-TextFieldInput:disabled) {
  cursor: not-allowed
}

.rt-TextFieldInput:-moz-read-only+.rt-TextFieldChrome {
  background-color: var(--gray-a3)
}

.rt-TextFieldInput:read-only+.rt-TextFieldChrome {
  background-color: var(--gray-a3)
}

.rt-TextFieldInput:-moz-read-only:not(:focus)+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--gray-a6)
}

.rt-TextFieldInput:read-only:not(:focus)+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--gray-a6)
}

.rt-TextFieldInput:-moz-read-only:focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--gray-8), 0 0 0 1px var(--gray-a8)
}

.rt-TextFieldInput:read-only:focus+.rt-TextFieldChrome {
  box-shadow: inset 0 0 0 1px var(--gray-8), 0 0 0 1px var(--gray-a8)
}

.rt-Text {
  margin: 0;
  line-height: var(--line-height, var(--default-line-height));
  letter-spacing: var(--letter-spacing, inherit)
}

.rt-Text:where([data-accent-color]) {
  color: var(--accent-a11)
}

.rt-Text:where([data-accent-color]) .rt-Text:where(.rt-high-contrast),
.rt-Text:where([data-accent-color]):where(.rt-high-contrast) {
  color: var(--accent-a12)
}

@media all {
  .rt-Text.rt-r-size-1 {
    font-size: var(--font-size-1);
    --line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Text.rt-r-size-2 {
    font-size: var(--font-size-2);
    --line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Text.rt-r-size-3 {
    font-size: var(--font-size-3);
    --line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Text.rt-r-size-4 {
    font-size: var(--font-size-4);
    --line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Text.rt-r-size-5 {
    font-size: var(--font-size-5);
    --line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Text.rt-r-size-6 {
    font-size: var(--font-size-6);
    --line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Text.rt-r-size-7 {
    font-size: var(--font-size-7);
    --line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Text.rt-r-size-8 {
    font-size: var(--font-size-8);
    --line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Text.rt-r-size-9 {
    font-size: var(--font-size-9);
    --line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:520px) {
  .rt-Text.xs\:rt-r-size-1 {
    font-size: var(--font-size-1);
    --line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Text.xs\:rt-r-size-2 {
    font-size: var(--font-size-2);
    --line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Text.xs\:rt-r-size-3 {
    font-size: var(--font-size-3);
    --line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Text.xs\:rt-r-size-4 {
    font-size: var(--font-size-4);
    --line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Text.xs\:rt-r-size-5 {
    font-size: var(--font-size-5);
    --line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Text.xs\:rt-r-size-6 {
    font-size: var(--font-size-6);
    --line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Text.xs\:rt-r-size-7 {
    font-size: var(--font-size-7);
    --line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Text.xs\:rt-r-size-8 {
    font-size: var(--font-size-8);
    --line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Text.xs\:rt-r-size-9 {
    font-size: var(--font-size-9);
    --line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:768px) {
  .rt-Text.sm\:rt-r-size-1 {
    font-size: var(--font-size-1);
    --line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Text.sm\:rt-r-size-2 {
    font-size: var(--font-size-2);
    --line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Text.sm\:rt-r-size-3 {
    font-size: var(--font-size-3);
    --line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Text.sm\:rt-r-size-4 {
    font-size: var(--font-size-4);
    --line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Text.sm\:rt-r-size-5 {
    font-size: var(--font-size-5);
    --line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Text.sm\:rt-r-size-6 {
    font-size: var(--font-size-6);
    --line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Text.sm\:rt-r-size-7 {
    font-size: var(--font-size-7);
    --line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Text.sm\:rt-r-size-8 {
    font-size: var(--font-size-8);
    --line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Text.sm\:rt-r-size-9 {
    font-size: var(--font-size-9);
    --line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1024px) {
  .rt-Text.md\:rt-r-size-1 {
    font-size: var(--font-size-1);
    --line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Text.md\:rt-r-size-2 {
    font-size: var(--font-size-2);
    --line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Text.md\:rt-r-size-3 {
    font-size: var(--font-size-3);
    --line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Text.md\:rt-r-size-4 {
    font-size: var(--font-size-4);
    --line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Text.md\:rt-r-size-5 {
    font-size: var(--font-size-5);
    --line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Text.md\:rt-r-size-6 {
    font-size: var(--font-size-6);
    --line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Text.md\:rt-r-size-7 {
    font-size: var(--font-size-7);
    --line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Text.md\:rt-r-size-8 {
    font-size: var(--font-size-8);
    --line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Text.md\:rt-r-size-9 {
    font-size: var(--font-size-9);
    --line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1280px) {
  .rt-Text.lg\:rt-r-size-1 {
    font-size: var(--font-size-1);
    --line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Text.lg\:rt-r-size-2 {
    font-size: var(--font-size-2);
    --line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Text.lg\:rt-r-size-3 {
    font-size: var(--font-size-3);
    --line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Text.lg\:rt-r-size-4 {
    font-size: var(--font-size-4);
    --line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Text.lg\:rt-r-size-5 {
    font-size: var(--font-size-5);
    --line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Text.lg\:rt-r-size-6 {
    font-size: var(--font-size-6);
    --line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Text.lg\:rt-r-size-7 {
    font-size: var(--font-size-7);
    --line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Text.lg\:rt-r-size-8 {
    font-size: var(--font-size-8);
    --line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Text.lg\:rt-r-size-9 {
    font-size: var(--font-size-9);
    --line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

@media (min-width:1640px) {
  .rt-Text.xl\:rt-r-size-1 {
    font-size: var(--font-size-1);
    --line-height: var(--line-height-1);
    --letter-spacing: var(--letter-spacing-1)
  }

  .rt-Text.xl\:rt-r-size-2 {
    font-size: var(--font-size-2);
    --line-height: var(--line-height-2);
    --letter-spacing: var(--letter-spacing-2)
  }

  .rt-Text.xl\:rt-r-size-3 {
    font-size: var(--font-size-3);
    --line-height: var(--line-height-3);
    --letter-spacing: var(--letter-spacing-3)
  }

  .rt-Text.xl\:rt-r-size-4 {
    font-size: var(--font-size-4);
    --line-height: var(--line-height-4);
    --letter-spacing: var(--letter-spacing-4)
  }

  .rt-Text.xl\:rt-r-size-5 {
    font-size: var(--font-size-5);
    --line-height: var(--line-height-5);
    --letter-spacing: var(--letter-spacing-5)
  }

  .rt-Text.xl\:rt-r-size-6 {
    font-size: var(--font-size-6);
    --line-height: var(--line-height-6);
    --letter-spacing: var(--letter-spacing-6)
  }

  .rt-Text.xl\:rt-r-size-7 {
    font-size: var(--font-size-7);
    --line-height: var(--line-height-7);
    --letter-spacing: var(--letter-spacing-7)
  }

  .rt-Text.xl\:rt-r-size-8 {
    font-size: var(--font-size-8);
    --line-height: var(--line-height-8);
    --letter-spacing: var(--letter-spacing-8)
  }

  .rt-Text.xl\:rt-r-size-9 {
    font-size: var(--font-size-9);
    --line-height: var(--line-height-9);
    --letter-spacing: var(--letter-spacing-9)
  }
}

.rt-TooltipContent {
  padding: var(--space-1) var(--space-2);
  --tooltip-bg: var(--gray-12);
  background-color: var(--tooltip-bg);
  border-radius: max(var(--radius-2), var(--radius-full));
  transform-origin: var(--radix-tooltip-content-transform-origin);
  animation-duration: .2s;
  animation-timing-function: cubic-bezier(.16, 1, .3, 1)
}

.rt-TooltipContent[data-state=delayed-open][data-side=top] {
  animation-name: slideUpAndFadeIn
}

.rt-TooltipContent[data-state=delayed-open][data-side=bottom] {
  animation-name: slideDownAndFadeIn
}

.rt-TooltipContent[data-state=delayed-open][data-side=left] {
  animation-name: slideLeftAndFadeIn
}

.rt-TooltipContent[data-state=delayed-open][data-side=right] {
  animation-name: slideRightAndFadeIn
}

.rt-TooltipText {
  color: var(--gray-1);
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  cursor: default
}

.rt-TooltipArrow {
  fill: var(--tooltip-bg)
}

.rt-TooltipContent.rt-multiline {
  max-width: 250px;
  border-radius: var(--radius-2)
}

.rt-TooltipContent.rt-multiline .rt-TooltipText {
  line-height: var(--default-line-height)
}

@media all {
  .rt-r-ai-start {
    align-items: flex-start
  }

  .rt-r-ai-center {
    align-items: center
  }

  .rt-r-ai-end {
    align-items: flex-end
  }

  .rt-r-ai-baseline {
    align-items: baseline
  }

  .rt-r-ai-stretch {
    align-items: stretch
  }
}

@media (min-width:520px) {
  .xs\:rt-r-ai-start {
    align-items: flex-start
  }

  .xs\:rt-r-ai-center {
    align-items: center
  }

  .xs\:rt-r-ai-end {
    align-items: flex-end
  }

  .xs\:rt-r-ai-baseline {
    align-items: baseline
  }

  .xs\:rt-r-ai-stretch {
    align-items: stretch
  }
}

@media (min-width:768px) {
  .sm\:rt-r-ai-start {
    align-items: flex-start
  }

  .sm\:rt-r-ai-center {
    align-items: center
  }

  .sm\:rt-r-ai-end {
    align-items: flex-end
  }

  .sm\:rt-r-ai-baseline {
    align-items: baseline
  }

  .sm\:rt-r-ai-stretch {
    align-items: stretch
  }
}

@media (min-width:1024px) {
  .md\:rt-r-ai-start {
    align-items: flex-start
  }

  .md\:rt-r-ai-center {
    align-items: center
  }

  .md\:rt-r-ai-end {
    align-items: flex-end
  }

  .md\:rt-r-ai-baseline {
    align-items: baseline
  }

  .md\:rt-r-ai-stretch {
    align-items: stretch
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-ai-start {
    align-items: flex-start
  }

  .lg\:rt-r-ai-center {
    align-items: center
  }

  .lg\:rt-r-ai-end {
    align-items: flex-end
  }

  .lg\:rt-r-ai-baseline {
    align-items: baseline
  }

  .lg\:rt-r-ai-stretch {
    align-items: stretch
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-ai-start {
    align-items: flex-start
  }

  .xl\:rt-r-ai-center {
    align-items: center
  }

  .xl\:rt-r-ai-end {
    align-items: flex-end
  }

  .xl\:rt-r-ai-baseline {
    align-items: baseline
  }

  .xl\:rt-r-ai-stretch {
    align-items: stretch
  }
}

@media all {
  .rt-r-as-start {
    align-self: flex-start
  }

  .rt-r-as-center {
    align-self: center
  }

  .rt-r-as-end {
    align-self: flex-end
  }

  .rt-r-as-baseline {
    align-self: baseline
  }

  .rt-r-as-stretch {
    align-self: stretch
  }
}

@media (min-width:520px) {
  .xs\:rt-r-as-start {
    align-self: flex-start
  }

  .xs\:rt-r-as-center {
    align-self: center
  }

  .xs\:rt-r-as-end {
    align-self: flex-end
  }

  .xs\:rt-r-as-baseline {
    align-self: baseline
  }

  .xs\:rt-r-as-stretch {
    align-self: stretch
  }
}

@media (min-width:768px) {
  .sm\:rt-r-as-start {
    align-self: flex-start
  }

  .sm\:rt-r-as-center {
    align-self: center
  }

  .sm\:rt-r-as-end {
    align-self: flex-end
  }

  .sm\:rt-r-as-baseline {
    align-self: baseline
  }

  .sm\:rt-r-as-stretch {
    align-self: stretch
  }
}

@media (min-width:1024px) {
  .md\:rt-r-as-start {
    align-self: flex-start
  }

  .md\:rt-r-as-center {
    align-self: center
  }

  .md\:rt-r-as-end {
    align-self: flex-end
  }

  .md\:rt-r-as-baseline {
    align-self: baseline
  }

  .md\:rt-r-as-stretch {
    align-self: stretch
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-as-start {
    align-self: flex-start
  }

  .lg\:rt-r-as-center {
    align-self: center
  }

  .lg\:rt-r-as-end {
    align-self: flex-end
  }

  .lg\:rt-r-as-baseline {
    align-self: baseline
  }

  .lg\:rt-r-as-stretch {
    align-self: stretch
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-as-start {
    align-self: flex-start
  }

  .xl\:rt-r-as-center {
    align-self: center
  }

  .xl\:rt-r-as-end {
    align-self: flex-end
  }

  .xl\:rt-r-as-baseline {
    align-self: baseline
  }

  .xl\:rt-r-as-stretch {
    align-self: stretch
  }
}

@media all {
  .rt-r-display-block {
    display: block
  }

  .rt-r-display-inline {
    display: inline
  }

  .rt-r-display-inline-block {
    display: inline-block
  }

  .rt-r-display-flex {
    display: flex
  }

  .rt-r-display-inline-flex {
    display: inline-flex
  }

  .rt-r-display-grid {
    display: grid
  }

  .rt-r-display-inline-grid {
    display: inline-grid
  }

  .rt-r-display-none {
    display: none
  }
}

@media (min-width:520px) {
  .xs\:rt-r-display-block {
    display: block
  }

  .xs\:rt-r-display-inline {
    display: inline
  }

  .xs\:rt-r-display-inline-block {
    display: inline-block
  }

  .xs\:rt-r-display-flex {
    display: flex
  }

  .xs\:rt-r-display-inline-flex {
    display: inline-flex
  }

  .xs\:rt-r-display-grid {
    display: grid
  }

  .xs\:rt-r-display-inline-grid {
    display: inline-grid
  }

  .xs\:rt-r-display-none {
    display: none
  }
}

@media (min-width:768px) {
  .sm\:rt-r-display-block {
    display: block
  }

  .sm\:rt-r-display-inline {
    display: inline
  }

  .sm\:rt-r-display-inline-block {
    display: inline-block
  }

  .sm\:rt-r-display-flex {
    display: flex
  }

  .sm\:rt-r-display-inline-flex {
    display: inline-flex
  }

  .sm\:rt-r-display-grid {
    display: grid
  }

  .sm\:rt-r-display-inline-grid {
    display: inline-grid
  }

  .sm\:rt-r-display-none {
    display: none
  }
}

@media (min-width:1024px) {
  .md\:rt-r-display-block {
    display: block
  }

  .md\:rt-r-display-inline {
    display: inline
  }

  .md\:rt-r-display-inline-block {
    display: inline-block
  }

  .md\:rt-r-display-flex {
    display: flex
  }

  .md\:rt-r-display-inline-flex {
    display: inline-flex
  }

  .md\:rt-r-display-grid {
    display: grid
  }

  .md\:rt-r-display-inline-grid {
    display: inline-grid
  }

  .md\:rt-r-display-none {
    display: none
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-display-block {
    display: block
  }

  .lg\:rt-r-display-inline {
    display: inline
  }

  .lg\:rt-r-display-inline-block {
    display: inline-block
  }

  .lg\:rt-r-display-flex {
    display: flex
  }

  .lg\:rt-r-display-inline-flex {
    display: inline-flex
  }

  .lg\:rt-r-display-grid {
    display: grid
  }

  .lg\:rt-r-display-inline-grid {
    display: inline-grid
  }

  .lg\:rt-r-display-none {
    display: none
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-display-block {
    display: block
  }

  .xl\:rt-r-display-inline {
    display: inline
  }

  .xl\:rt-r-display-inline-block {
    display: inline-block
  }

  .xl\:rt-r-display-flex {
    display: flex
  }

  .xl\:rt-r-display-inline-flex {
    display: inline-flex
  }

  .xl\:rt-r-display-grid {
    display: grid
  }

  .xl\:rt-r-display-inline-grid {
    display: inline-grid
  }

  .xl\:rt-r-display-none {
    display: none
  }
}

@media all {
  .rt-r-fd-row {
    flex-direction: row
  }

  .rt-r-fd-column {
    flex-direction: column
  }

  .rt-r-fd-row-reverse {
    flex-direction: row-reverse
  }

  .rt-r-fd-column-reverse {
    flex-direction: column-reverse
  }
}

@media (min-width:520px) {
  .xs\:rt-r-fd-row {
    flex-direction: row
  }

  .xs\:rt-r-fd-column {
    flex-direction: column
  }

  .xs\:rt-r-fd-row-reverse {
    flex-direction: row-reverse
  }

  .xs\:rt-r-fd-column-reverse {
    flex-direction: column-reverse
  }
}

@media (min-width:768px) {
  .sm\:rt-r-fd-row {
    flex-direction: row
  }

  .sm\:rt-r-fd-column {
    flex-direction: column
  }

  .sm\:rt-r-fd-row-reverse {
    flex-direction: row-reverse
  }

  .sm\:rt-r-fd-column-reverse {
    flex-direction: column-reverse
  }
}

@media (min-width:1024px) {
  .md\:rt-r-fd-row {
    flex-direction: row
  }

  .md\:rt-r-fd-column {
    flex-direction: column
  }

  .md\:rt-r-fd-row-reverse {
    flex-direction: row-reverse
  }

  .md\:rt-r-fd-column-reverse {
    flex-direction: column-reverse
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-fd-row {
    flex-direction: row
  }

  .lg\:rt-r-fd-column {
    flex-direction: column
  }

  .lg\:rt-r-fd-row-reverse {
    flex-direction: row-reverse
  }

  .lg\:rt-r-fd-column-reverse {
    flex-direction: column-reverse
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-fd-row {
    flex-direction: row
  }

  .xl\:rt-r-fd-column {
    flex-direction: column
  }

  .xl\:rt-r-fd-row-reverse {
    flex-direction: row-reverse
  }

  .xl\:rt-r-fd-column-reverse {
    flex-direction: column-reverse
  }
}

@media all {
  .rt-r-fg-0 {
    flex-grow: 0
  }

  .rt-r-fg-1 {
    flex-grow: 1
  }
}

@media (min-width:520px) {
  .xs\:rt-r-fg-0 {
    flex-grow: 0
  }

  .xs\:rt-r-fg-1 {
    flex-grow: 1
  }
}

@media (min-width:768px) {
  .sm\:rt-r-fg-0 {
    flex-grow: 0
  }

  .sm\:rt-r-fg-1 {
    flex-grow: 1
  }
}

@media (min-width:1024px) {
  .md\:rt-r-fg-0 {
    flex-grow: 0
  }

  .md\:rt-r-fg-1 {
    flex-grow: 1
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-fg-0 {
    flex-grow: 0
  }

  .lg\:rt-r-fg-1 {
    flex-grow: 1
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-fg-0 {
    flex-grow: 0
  }

  .xl\:rt-r-fg-1 {
    flex-grow: 1
  }
}

@media all {
  .rt-r-fs-0 {
    flex-shrink: 0
  }

  .rt-r-fs-1 {
    flex-shrink: 1
  }
}

@media (min-width:520px) {
  .xs\:rt-r-fs-0 {
    flex-shrink: 0
  }

  .xs\:rt-r-fs-1 {
    flex-shrink: 1
  }
}

@media (min-width:768px) {
  .sm\:rt-r-fs-0 {
    flex-shrink: 0
  }

  .sm\:rt-r-fs-1 {
    flex-shrink: 1
  }
}

@media (min-width:1024px) {
  .md\:rt-r-fs-0 {
    flex-shrink: 0
  }

  .md\:rt-r-fs-1 {
    flex-shrink: 1
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-fs-0 {
    flex-shrink: 0
  }

  .lg\:rt-r-fs-1 {
    flex-shrink: 1
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-fs-0 {
    flex-shrink: 0
  }

  .xl\:rt-r-fs-1 {
    flex-shrink: 1
  }
}

@media all {
  .rt-r-fw-nowrap {
    flex-wrap: nowrap
  }

  .rt-r-fw-wrap {
    flex-wrap: wrap
  }

  .rt-r-fw-wrap-reverse {
    flex-wrap: wrap-reverse
  }
}

@media (min-width:520px) {
  .xs\:rt-r-fw-nowrap {
    flex-wrap: nowrap
  }

  .xs\:rt-r-fw-wrap {
    flex-wrap: wrap
  }

  .xs\:rt-r-fw-wrap-reverse {
    flex-wrap: wrap-reverse
  }
}

@media (min-width:768px) {
  .sm\:rt-r-fw-nowrap {
    flex-wrap: nowrap
  }

  .sm\:rt-r-fw-wrap {
    flex-wrap: wrap
  }

  .sm\:rt-r-fw-wrap-reverse {
    flex-wrap: wrap-reverse
  }
}

@media (min-width:1024px) {
  .md\:rt-r-fw-nowrap {
    flex-wrap: nowrap
  }

  .md\:rt-r-fw-wrap {
    flex-wrap: wrap
  }

  .md\:rt-r-fw-wrap-reverse {
    flex-wrap: wrap-reverse
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-fw-nowrap {
    flex-wrap: nowrap
  }

  .lg\:rt-r-fw-wrap {
    flex-wrap: wrap
  }

  .lg\:rt-r-fw-wrap-reverse {
    flex-wrap: wrap-reverse
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-fw-nowrap {
    flex-wrap: nowrap
  }

  .xl\:rt-r-fw-wrap {
    flex-wrap: wrap
  }

  .xl\:rt-r-fw-wrap-reverse {
    flex-wrap: wrap-reverse
  }
}

@media all {
  .rt-r-weight-light {
    font-weight: var(--font-weight-light)
  }

  .rt-r-weight-regular {
    font-weight: var(--font-weight-regular)
  }

  .rt-r-weight-medium {
    font-weight: var(--font-weight-medium)
  }

  .rt-r-weight-bold {
    font-weight: var(--font-weight-bold)
  }
}

@media (min-width:520px) {
  .xs\:rt-r-weight-light {
    font-weight: var(--font-weight-light)
  }

  .xs\:rt-r-weight-regular {
    font-weight: var(--font-weight-regular)
  }

  .xs\:rt-r-weight-medium {
    font-weight: var(--font-weight-medium)
  }

  .xs\:rt-r-weight-bold {
    font-weight: var(--font-weight-bold)
  }
}

@media (min-width:768px) {
  .sm\:rt-r-weight-light {
    font-weight: var(--font-weight-light)
  }

  .sm\:rt-r-weight-regular {
    font-weight: var(--font-weight-regular)
  }

  .sm\:rt-r-weight-medium {
    font-weight: var(--font-weight-medium)
  }

  .sm\:rt-r-weight-bold {
    font-weight: var(--font-weight-bold)
  }
}

@media (min-width:1024px) {
  .md\:rt-r-weight-light {
    font-weight: var(--font-weight-light)
  }

  .md\:rt-r-weight-regular {
    font-weight: var(--font-weight-regular)
  }

  .md\:rt-r-weight-medium {
    font-weight: var(--font-weight-medium)
  }

  .md\:rt-r-weight-bold {
    font-weight: var(--font-weight-bold)
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-weight-light {
    font-weight: var(--font-weight-light)
  }

  .lg\:rt-r-weight-regular {
    font-weight: var(--font-weight-regular)
  }

  .lg\:rt-r-weight-medium {
    font-weight: var(--font-weight-medium)
  }

  .lg\:rt-r-weight-bold {
    font-weight: var(--font-weight-bold)
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-weight-light {
    font-weight: var(--font-weight-light)
  }

  .xl\:rt-r-weight-regular {
    font-weight: var(--font-weight-regular)
  }

  .xl\:rt-r-weight-medium {
    font-weight: var(--font-weight-medium)
  }

  .xl\:rt-r-weight-bold {
    font-weight: var(--font-weight-bold)
  }
}

@media all {
  .rt-r-gap-0 {
    gap: 0
  }

  .rt-r-gap-1 {
    gap: var(--space-1)
  }

  .rt-r-gap-2 {
    gap: var(--space-2)
  }

  .rt-r-gap-3 {
    gap: var(--space-3)
  }

  .rt-r-gap-4 {
    gap: var(--space-4)
  }

  .rt-r-gap-5 {
    gap: var(--space-5)
  }

  .rt-r-gap-6 {
    gap: var(--space-6)
  }

  .rt-r-gap-7 {
    gap: var(--space-7)
  }

  .rt-r-gap-8 {
    gap: var(--space-8)
  }

  .rt-r-gap-9 {
    gap: var(--space-9)
  }

  .rt-r-cg-0 {
    -moz-column-gap: 0;
    column-gap: 0
  }

  .rt-r-cg-1 {
    -moz-column-gap: var(--space-1);
    column-gap: var(--space-1)
  }

  .rt-r-cg-2 {
    -moz-column-gap: var(--space-2);
    column-gap: var(--space-2)
  }

  .rt-r-cg-3 {
    -moz-column-gap: var(--space-3);
    column-gap: var(--space-3)
  }

  .rt-r-cg-4 {
    -moz-column-gap: var(--space-4);
    column-gap: var(--space-4)
  }

  .rt-r-cg-5 {
    -moz-column-gap: var(--space-5);
    column-gap: var(--space-5)
  }

  .rt-r-cg-6 {
    -moz-column-gap: var(--space-6);
    column-gap: var(--space-6)
  }

  .rt-r-cg-7 {
    -moz-column-gap: var(--space-7);
    column-gap: var(--space-7)
  }

  .rt-r-cg-8 {
    -moz-column-gap: var(--space-8);
    column-gap: var(--space-8)
  }

  .rt-r-cg-9 {
    -moz-column-gap: var(--space-9);
    column-gap: var(--space-9)
  }

  .rt-r-rg-0 {
    row-gap: 0
  }

  .rt-r-rg-1 {
    row-gap: var(--space-1)
  }

  .rt-r-rg-2 {
    row-gap: var(--space-2)
  }

  .rt-r-rg-3 {
    row-gap: var(--space-3)
  }

  .rt-r-rg-4 {
    row-gap: var(--space-4)
  }

  .rt-r-rg-5 {
    row-gap: var(--space-5)
  }

  .rt-r-rg-6 {
    row-gap: var(--space-6)
  }

  .rt-r-rg-7 {
    row-gap: var(--space-7)
  }

  .rt-r-rg-8 {
    row-gap: var(--space-8)
  }

  .rt-r-rg-9 {
    row-gap: var(--space-9)
  }
}

@media (min-width:520px) {
  .xs\:rt-r-gap-0 {
    gap: 0
  }

  .xs\:rt-r-gap-1 {
    gap: var(--space-1)
  }

  .xs\:rt-r-gap-2 {
    gap: var(--space-2)
  }

  .xs\:rt-r-gap-3 {
    gap: var(--space-3)
  }

  .xs\:rt-r-gap-4 {
    gap: var(--space-4)
  }

  .xs\:rt-r-gap-5 {
    gap: var(--space-5)
  }

  .xs\:rt-r-gap-6 {
    gap: var(--space-6)
  }

  .xs\:rt-r-gap-7 {
    gap: var(--space-7)
  }

  .xs\:rt-r-gap-8 {
    gap: var(--space-8)
  }

  .xs\:rt-r-gap-9 {
    gap: var(--space-9)
  }

  .xs\:rt-r-cg-0 {
    -moz-column-gap: 0;
    column-gap: 0
  }

  .xs\:rt-r-cg-1 {
    -moz-column-gap: var(--space-1);
    column-gap: var(--space-1)
  }

  .xs\:rt-r-cg-2 {
    -moz-column-gap: var(--space-2);
    column-gap: var(--space-2)
  }

  .xs\:rt-r-cg-3 {
    -moz-column-gap: var(--space-3);
    column-gap: var(--space-3)
  }

  .xs\:rt-r-cg-4 {
    -moz-column-gap: var(--space-4);
    column-gap: var(--space-4)
  }

  .xs\:rt-r-cg-5 {
    -moz-column-gap: var(--space-5);
    column-gap: var(--space-5)
  }

  .xs\:rt-r-cg-6 {
    -moz-column-gap: var(--space-6);
    column-gap: var(--space-6)
  }

  .xs\:rt-r-cg-7 {
    -moz-column-gap: var(--space-7);
    column-gap: var(--space-7)
  }

  .xs\:rt-r-cg-8 {
    -moz-column-gap: var(--space-8);
    column-gap: var(--space-8)
  }

  .xs\:rt-r-cg-9 {
    -moz-column-gap: var(--space-9);
    column-gap: var(--space-9)
  }

  .xs\:rt-r-rg-0 {
    row-gap: 0
  }

  .xs\:rt-r-rg-1 {
    row-gap: var(--space-1)
  }

  .xs\:rt-r-rg-2 {
    row-gap: var(--space-2)
  }

  .xs\:rt-r-rg-3 {
    row-gap: var(--space-3)
  }

  .xs\:rt-r-rg-4 {
    row-gap: var(--space-4)
  }

  .xs\:rt-r-rg-5 {
    row-gap: var(--space-5)
  }

  .xs\:rt-r-rg-6 {
    row-gap: var(--space-6)
  }

  .xs\:rt-r-rg-7 {
    row-gap: var(--space-7)
  }

  .xs\:rt-r-rg-8 {
    row-gap: var(--space-8)
  }

  .xs\:rt-r-rg-9 {
    row-gap: var(--space-9)
  }
}

@media (min-width:768px) {
  .sm\:rt-r-gap-0 {
    gap: 0
  }

  .sm\:rt-r-gap-1 {
    gap: var(--space-1)
  }

  .sm\:rt-r-gap-2 {
    gap: var(--space-2)
  }

  .sm\:rt-r-gap-3 {
    gap: var(--space-3)
  }

  .sm\:rt-r-gap-4 {
    gap: var(--space-4)
  }

  .sm\:rt-r-gap-5 {
    gap: var(--space-5)
  }

  .sm\:rt-r-gap-6 {
    gap: var(--space-6)
  }

  .sm\:rt-r-gap-7 {
    gap: var(--space-7)
  }

  .sm\:rt-r-gap-8 {
    gap: var(--space-8)
  }

  .sm\:rt-r-gap-9 {
    gap: var(--space-9)
  }

  .sm\:rt-r-cg-0 {
    -moz-column-gap: 0;
    column-gap: 0
  }

  .sm\:rt-r-cg-1 {
    -moz-column-gap: var(--space-1);
    column-gap: var(--space-1)
  }

  .sm\:rt-r-cg-2 {
    -moz-column-gap: var(--space-2);
    column-gap: var(--space-2)
  }

  .sm\:rt-r-cg-3 {
    -moz-column-gap: var(--space-3);
    column-gap: var(--space-3)
  }

  .sm\:rt-r-cg-4 {
    -moz-column-gap: var(--space-4);
    column-gap: var(--space-4)
  }

  .sm\:rt-r-cg-5 {
    -moz-column-gap: var(--space-5);
    column-gap: var(--space-5)
  }

  .sm\:rt-r-cg-6 {
    -moz-column-gap: var(--space-6);
    column-gap: var(--space-6)
  }

  .sm\:rt-r-cg-7 {
    -moz-column-gap: var(--space-7);
    column-gap: var(--space-7)
  }

  .sm\:rt-r-cg-8 {
    -moz-column-gap: var(--space-8);
    column-gap: var(--space-8)
  }

  .sm\:rt-r-cg-9 {
    -moz-column-gap: var(--space-9);
    column-gap: var(--space-9)
  }

  .sm\:rt-r-rg-0 {
    row-gap: 0
  }

  .sm\:rt-r-rg-1 {
    row-gap: var(--space-1)
  }

  .sm\:rt-r-rg-2 {
    row-gap: var(--space-2)
  }

  .sm\:rt-r-rg-3 {
    row-gap: var(--space-3)
  }

  .sm\:rt-r-rg-4 {
    row-gap: var(--space-4)
  }

  .sm\:rt-r-rg-5 {
    row-gap: var(--space-5)
  }

  .sm\:rt-r-rg-6 {
    row-gap: var(--space-6)
  }

  .sm\:rt-r-rg-7 {
    row-gap: var(--space-7)
  }

  .sm\:rt-r-rg-8 {
    row-gap: var(--space-8)
  }

  .sm\:rt-r-rg-9 {
    row-gap: var(--space-9)
  }
}

@media (min-width:1024px) {
  .md\:rt-r-gap-0 {
    gap: 0
  }

  .md\:rt-r-gap-1 {
    gap: var(--space-1)
  }

  .md\:rt-r-gap-2 {
    gap: var(--space-2)
  }

  .md\:rt-r-gap-3 {
    gap: var(--space-3)
  }

  .md\:rt-r-gap-4 {
    gap: var(--space-4)
  }

  .md\:rt-r-gap-5 {
    gap: var(--space-5)
  }

  .md\:rt-r-gap-6 {
    gap: var(--space-6)
  }

  .md\:rt-r-gap-7 {
    gap: var(--space-7)
  }

  .md\:rt-r-gap-8 {
    gap: var(--space-8)
  }

  .md\:rt-r-gap-9 {
    gap: var(--space-9)
  }

  .md\:rt-r-cg-0 {
    -moz-column-gap: 0;
    column-gap: 0
  }

  .md\:rt-r-cg-1 {
    -moz-column-gap: var(--space-1);
    column-gap: var(--space-1)
  }

  .md\:rt-r-cg-2 {
    -moz-column-gap: var(--space-2);
    column-gap: var(--space-2)
  }

  .md\:rt-r-cg-3 {
    -moz-column-gap: var(--space-3);
    column-gap: var(--space-3)
  }

  .md\:rt-r-cg-4 {
    -moz-column-gap: var(--space-4);
    column-gap: var(--space-4)
  }

  .md\:rt-r-cg-5 {
    -moz-column-gap: var(--space-5);
    column-gap: var(--space-5)
  }

  .md\:rt-r-cg-6 {
    -moz-column-gap: var(--space-6);
    column-gap: var(--space-6)
  }

  .md\:rt-r-cg-7 {
    -moz-column-gap: var(--space-7);
    column-gap: var(--space-7)
  }

  .md\:rt-r-cg-8 {
    -moz-column-gap: var(--space-8);
    column-gap: var(--space-8)
  }

  .md\:rt-r-cg-9 {
    -moz-column-gap: var(--space-9);
    column-gap: var(--space-9)
  }

  .md\:rt-r-rg-0 {
    row-gap: 0
  }

  .md\:rt-r-rg-1 {
    row-gap: var(--space-1)
  }

  .md\:rt-r-rg-2 {
    row-gap: var(--space-2)
  }

  .md\:rt-r-rg-3 {
    row-gap: var(--space-3)
  }

  .md\:rt-r-rg-4 {
    row-gap: var(--space-4)
  }

  .md\:rt-r-rg-5 {
    row-gap: var(--space-5)
  }

  .md\:rt-r-rg-6 {
    row-gap: var(--space-6)
  }

  .md\:rt-r-rg-7 {
    row-gap: var(--space-7)
  }

  .md\:rt-r-rg-8 {
    row-gap: var(--space-8)
  }

  .md\:rt-r-rg-9 {
    row-gap: var(--space-9)
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-gap-0 {
    gap: 0
  }

  .lg\:rt-r-gap-1 {
    gap: var(--space-1)
  }

  .lg\:rt-r-gap-2 {
    gap: var(--space-2)
  }

  .lg\:rt-r-gap-3 {
    gap: var(--space-3)
  }

  .lg\:rt-r-gap-4 {
    gap: var(--space-4)
  }

  .lg\:rt-r-gap-5 {
    gap: var(--space-5)
  }

  .lg\:rt-r-gap-6 {
    gap: var(--space-6)
  }

  .lg\:rt-r-gap-7 {
    gap: var(--space-7)
  }

  .lg\:rt-r-gap-8 {
    gap: var(--space-8)
  }

  .lg\:rt-r-gap-9 {
    gap: var(--space-9)
  }

  .lg\:rt-r-cg-0 {
    -moz-column-gap: 0;
    column-gap: 0
  }

  .lg\:rt-r-cg-1 {
    -moz-column-gap: var(--space-1);
    column-gap: var(--space-1)
  }

  .lg\:rt-r-cg-2 {
    -moz-column-gap: var(--space-2);
    column-gap: var(--space-2)
  }

  .lg\:rt-r-cg-3 {
    -moz-column-gap: var(--space-3);
    column-gap: var(--space-3)
  }

  .lg\:rt-r-cg-4 {
    -moz-column-gap: var(--space-4);
    column-gap: var(--space-4)
  }

  .lg\:rt-r-cg-5 {
    -moz-column-gap: var(--space-5);
    column-gap: var(--space-5)
  }

  .lg\:rt-r-cg-6 {
    -moz-column-gap: var(--space-6);
    column-gap: var(--space-6)
  }

  .lg\:rt-r-cg-7 {
    -moz-column-gap: var(--space-7);
    column-gap: var(--space-7)
  }

  .lg\:rt-r-cg-8 {
    -moz-column-gap: var(--space-8);
    column-gap: var(--space-8)
  }

  .lg\:rt-r-cg-9 {
    -moz-column-gap: var(--space-9);
    column-gap: var(--space-9)
  }

  .lg\:rt-r-rg-0 {
    row-gap: 0
  }

  .lg\:rt-r-rg-1 {
    row-gap: var(--space-1)
  }

  .lg\:rt-r-rg-2 {
    row-gap: var(--space-2)
  }

  .lg\:rt-r-rg-3 {
    row-gap: var(--space-3)
  }

  .lg\:rt-r-rg-4 {
    row-gap: var(--space-4)
  }

  .lg\:rt-r-rg-5 {
    row-gap: var(--space-5)
  }

  .lg\:rt-r-rg-6 {
    row-gap: var(--space-6)
  }

  .lg\:rt-r-rg-7 {
    row-gap: var(--space-7)
  }

  .lg\:rt-r-rg-8 {
    row-gap: var(--space-8)
  }

  .lg\:rt-r-rg-9 {
    row-gap: var(--space-9)
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-gap-0 {
    gap: 0
  }

  .xl\:rt-r-gap-1 {
    gap: var(--space-1)
  }

  .xl\:rt-r-gap-2 {
    gap: var(--space-2)
  }

  .xl\:rt-r-gap-3 {
    gap: var(--space-3)
  }

  .xl\:rt-r-gap-4 {
    gap: var(--space-4)
  }

  .xl\:rt-r-gap-5 {
    gap: var(--space-5)
  }

  .xl\:rt-r-gap-6 {
    gap: var(--space-6)
  }

  .xl\:rt-r-gap-7 {
    gap: var(--space-7)
  }

  .xl\:rt-r-gap-8 {
    gap: var(--space-8)
  }

  .xl\:rt-r-gap-9 {
    gap: var(--space-9)
  }

  .xl\:rt-r-cg-0 {
    -moz-column-gap: 0;
    column-gap: 0
  }

  .xl\:rt-r-cg-1 {
    -moz-column-gap: var(--space-1);
    column-gap: var(--space-1)
  }

  .xl\:rt-r-cg-2 {
    -moz-column-gap: var(--space-2);
    column-gap: var(--space-2)
  }

  .xl\:rt-r-cg-3 {
    -moz-column-gap: var(--space-3);
    column-gap: var(--space-3)
  }

  .xl\:rt-r-cg-4 {
    -moz-column-gap: var(--space-4);
    column-gap: var(--space-4)
  }

  .xl\:rt-r-cg-5 {
    -moz-column-gap: var(--space-5);
    column-gap: var(--space-5)
  }

  .xl\:rt-r-cg-6 {
    -moz-column-gap: var(--space-6);
    column-gap: var(--space-6)
  }

  .xl\:rt-r-cg-7 {
    -moz-column-gap: var(--space-7);
    column-gap: var(--space-7)
  }

  .xl\:rt-r-cg-8 {
    -moz-column-gap: var(--space-8);
    column-gap: var(--space-8)
  }

  .xl\:rt-r-cg-9 {
    -moz-column-gap: var(--space-9);
    column-gap: var(--space-9)
  }

  .xl\:rt-r-rg-0 {
    row-gap: 0
  }

  .xl\:rt-r-rg-1 {
    row-gap: var(--space-1)
  }

  .xl\:rt-r-rg-2 {
    row-gap: var(--space-2)
  }

  .xl\:rt-r-rg-3 {
    row-gap: var(--space-3)
  }

  .xl\:rt-r-rg-4 {
    row-gap: var(--space-4)
  }

  .xl\:rt-r-rg-5 {
    row-gap: var(--space-5)
  }

  .xl\:rt-r-rg-6 {
    row-gap: var(--space-6)
  }

  .xl\:rt-r-rg-7 {
    row-gap: var(--space-7)
  }

  .xl\:rt-r-rg-8 {
    row-gap: var(--space-8)
  }

  .xl\:rt-r-rg-9 {
    row-gap: var(--space-9)
  }
}

@media all {
  .rt-r-gaf-row {
    grid-auto-flow: row
  }

  .rt-r-gaf-column {
    grid-auto-flow: column
  }

  .rt-r-gaf-dense {
    grid-auto-flow: dense
  }

  .rt-r-gaf-row-dense {
    grid-auto-flow: row dense
  }

  .rt-r-gaf-column-dense {
    grid-auto-flow: column dense
  }
}

@media (min-width:520px) {
  .xs\:rt-r-gaf-row {
    grid-auto-flow: row
  }

  .xs\:rt-r-gaf-column {
    grid-auto-flow: column
  }

  .xs\:rt-r-gaf-dense {
    grid-auto-flow: dense
  }

  .xs\:rt-r-gaf-row-dense {
    grid-auto-flow: row dense
  }

  .xs\:rt-r-gaf-column-dense {
    grid-auto-flow: column dense
  }
}

@media (min-width:768px) {
  .sm\:rt-r-gaf-row {
    grid-auto-flow: row
  }

  .sm\:rt-r-gaf-column {
    grid-auto-flow: column
  }

  .sm\:rt-r-gaf-dense {
    grid-auto-flow: dense
  }

  .sm\:rt-r-gaf-row-dense {
    grid-auto-flow: row dense
  }

  .sm\:rt-r-gaf-column-dense {
    grid-auto-flow: column dense
  }
}

@media (min-width:1024px) {
  .md\:rt-r-gaf-row {
    grid-auto-flow: row
  }

  .md\:rt-r-gaf-column {
    grid-auto-flow: column
  }

  .md\:rt-r-gaf-dense {
    grid-auto-flow: dense
  }

  .md\:rt-r-gaf-row-dense {
    grid-auto-flow: row dense
  }

  .md\:rt-r-gaf-column-dense {
    grid-auto-flow: column dense
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-gaf-row {
    grid-auto-flow: row
  }

  .lg\:rt-r-gaf-column {
    grid-auto-flow: column
  }

  .lg\:rt-r-gaf-dense {
    grid-auto-flow: dense
  }

  .lg\:rt-r-gaf-row-dense {
    grid-auto-flow: row dense
  }

  .lg\:rt-r-gaf-column-dense {
    grid-auto-flow: column dense
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-gaf-row {
    grid-auto-flow: row
  }

  .xl\:rt-r-gaf-column {
    grid-auto-flow: column
  }

  .xl\:rt-r-gaf-dense {
    grid-auto-flow: dense
  }

  .xl\:rt-r-gaf-row-dense {
    grid-auto-flow: row dense
  }

  .xl\:rt-r-gaf-column-dense {
    grid-auto-flow: column dense
  }
}

@media all {
  .rt-r-h-auto {
    height: auto
  }

  .rt-r-h-max-content {
    height: -moz-max-content;
    height: max-content
  }

  .rt-r-h-min-content {
    height: -moz-min-content;
    height: min-content
  }

  .rt-r-h-0 {
    height: 0
  }

  .rt-r-h-1 {
    height: var(--space-1)
  }

  .rt-r-h-2 {
    height: var(--space-2)
  }

  .rt-r-h-3 {
    height: var(--space-3)
  }

  .rt-r-h-4 {
    height: var(--space-4)
  }

  .rt-r-h-5 {
    height: var(--space-5)
  }

  .rt-r-h-6 {
    height: var(--space-6)
  }

  .rt-r-h-7 {
    height: var(--space-7)
  }

  .rt-r-h-8 {
    height: var(--space-8)
  }

  .rt-r-h-9 {
    height: var(--space-9)
  }

  .rt-r-h-50\% {
    height: 50%
  }

  .rt-r-h-100\% {
    height: 100%
  }
}

@media (min-width:520px) {
  .xs\:rt-r-h-auto {
    height: auto
  }

  .xs\:rt-r-h-max-content {
    height: -moz-max-content;
    height: max-content
  }

  .xs\:rt-r-h-min-content {
    height: -moz-min-content;
    height: min-content
  }

  .xs\:rt-r-h-0 {
    height: 0
  }

  .xs\:rt-r-h-1 {
    height: var(--space-1)
  }

  .xs\:rt-r-h-2 {
    height: var(--space-2)
  }

  .xs\:rt-r-h-3 {
    height: var(--space-3)
  }

  .xs\:rt-r-h-4 {
    height: var(--space-4)
  }

  .xs\:rt-r-h-5 {
    height: var(--space-5)
  }

  .xs\:rt-r-h-6 {
    height: var(--space-6)
  }

  .xs\:rt-r-h-7 {
    height: var(--space-7)
  }

  .xs\:rt-r-h-8 {
    height: var(--space-8)
  }

  .xs\:rt-r-h-9 {
    height: var(--space-9)
  }

  .xs\:rt-r-h-50\% {
    height: 50%
  }

  .xs\:rt-r-h-100\% {
    height: 100%
  }
}

@media (min-width:768px) {
  .sm\:rt-r-h-auto {
    height: auto
  }

  .sm\:rt-r-h-max-content {
    height: -moz-max-content;
    height: max-content
  }

  .sm\:rt-r-h-min-content {
    height: -moz-min-content;
    height: min-content
  }

  .sm\:rt-r-h-0 {
    height: 0
  }

  .sm\:rt-r-h-1 {
    height: var(--space-1)
  }

  .sm\:rt-r-h-2 {
    height: var(--space-2)
  }

  .sm\:rt-r-h-3 {
    height: var(--space-3)
  }

  .sm\:rt-r-h-4 {
    height: var(--space-4)
  }

  .sm\:rt-r-h-5 {
    height: var(--space-5)
  }

  .sm\:rt-r-h-6 {
    height: var(--space-6)
  }

  .sm\:rt-r-h-7 {
    height: var(--space-7)
  }

  .sm\:rt-r-h-8 {
    height: var(--space-8)
  }

  .sm\:rt-r-h-9 {
    height: var(--space-9)
  }

  .sm\:rt-r-h-50\% {
    height: 50%
  }

  .sm\:rt-r-h-100\% {
    height: 100%
  }
}

@media (min-width:1024px) {
  .md\:rt-r-h-auto {
    height: auto
  }

  .md\:rt-r-h-max-content {
    height: -moz-max-content;
    height: max-content
  }

  .md\:rt-r-h-min-content {
    height: -moz-min-content;
    height: min-content
  }

  .md\:rt-r-h-0 {
    height: 0
  }

  .md\:rt-r-h-1 {
    height: var(--space-1)
  }

  .md\:rt-r-h-2 {
    height: var(--space-2)
  }

  .md\:rt-r-h-3 {
    height: var(--space-3)
  }

  .md\:rt-r-h-4 {
    height: var(--space-4)
  }

  .md\:rt-r-h-5 {
    height: var(--space-5)
  }

  .md\:rt-r-h-6 {
    height: var(--space-6)
  }

  .md\:rt-r-h-7 {
    height: var(--space-7)
  }

  .md\:rt-r-h-8 {
    height: var(--space-8)
  }

  .md\:rt-r-h-9 {
    height: var(--space-9)
  }

  .md\:rt-r-h-50\% {
    height: 50%
  }

  .md\:rt-r-h-100\% {
    height: 100%
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-h-auto {
    height: auto
  }

  .lg\:rt-r-h-max-content {
    height: -moz-max-content;
    height: max-content
  }

  .lg\:rt-r-h-min-content {
    height: -moz-min-content;
    height: min-content
  }

  .lg\:rt-r-h-0 {
    height: 0
  }

  .lg\:rt-r-h-1 {
    height: var(--space-1)
  }

  .lg\:rt-r-h-2 {
    height: var(--space-2)
  }

  .lg\:rt-r-h-3 {
    height: var(--space-3)
  }

  .lg\:rt-r-h-4 {
    height: var(--space-4)
  }

  .lg\:rt-r-h-5 {
    height: var(--space-5)
  }

  .lg\:rt-r-h-6 {
    height: var(--space-6)
  }

  .lg\:rt-r-h-7 {
    height: var(--space-7)
  }

  .lg\:rt-r-h-8 {
    height: var(--space-8)
  }

  .lg\:rt-r-h-9 {
    height: var(--space-9)
  }

  .lg\:rt-r-h-50\% {
    height: 50%
  }

  .lg\:rt-r-h-100\% {
    height: 100%
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-h-auto {
    height: auto
  }

  .xl\:rt-r-h-max-content {
    height: -moz-max-content;
    height: max-content
  }

  .xl\:rt-r-h-min-content {
    height: -moz-min-content;
    height: min-content
  }

  .xl\:rt-r-h-0 {
    height: 0
  }

  .xl\:rt-r-h-1 {
    height: var(--space-1)
  }

  .xl\:rt-r-h-2 {
    height: var(--space-2)
  }

  .xl\:rt-r-h-3 {
    height: var(--space-3)
  }

  .xl\:rt-r-h-4 {
    height: var(--space-4)
  }

  .xl\:rt-r-h-5 {
    height: var(--space-5)
  }

  .xl\:rt-r-h-6 {
    height: var(--space-6)
  }

  .xl\:rt-r-h-7 {
    height: var(--space-7)
  }

  .xl\:rt-r-h-8 {
    height: var(--space-8)
  }

  .xl\:rt-r-h-9 {
    height: var(--space-9)
  }

  .xl\:rt-r-h-50\% {
    height: 50%
  }

  .xl\:rt-r-h-100\% {
    height: 100%
  }
}

@media all {
  .rt-r-inset-auto {
    inset: auto
  }

  .rt-r-top-auto {
    top: auto
  }

  .rt-r-right-auto {
    right: auto
  }

  .rt-r-bottom-auto {
    bottom: auto
  }

  .rt-r-left-auto {
    left: auto
  }

  .rt-r-inset-0 {
    inset: 0
  }

  .rt-r-top-0 {
    top: 0
  }

  .rt-r-right-0 {
    right: 0
  }

  .rt-r-bottom-0 {
    bottom: 0
  }

  .rt-r-left-0 {
    left: 0
  }

  .rt-r-inset-50\% {
    inset: 50%
  }

  .rt-r-top-50\% {
    top: 50%
  }

  .rt-r-right-50\% {
    right: 50%
  }

  .rt-r-bottom-50\% {
    bottom: 50%
  }

  .rt-r-left-50\% {
    left: 50%
  }

  .rt-r-inset-100\% {
    inset: 100%
  }

  .rt-r-top-100\% {
    top: 100%
  }

  .rt-r-right-100\% {
    right: 100%
  }

  .rt-r-bottom-100\% {
    bottom: 100%
  }

  .rt-r-left-100\% {
    left: 100%
  }
}

@media (min-width:520px) {
  .xs\:rt-r-inset-auto {
    inset: auto
  }

  .xs\:rt-r-top-auto {
    top: auto
  }

  .xs\:rt-r-right-auto {
    right: auto
  }

  .xs\:rt-r-bottom-auto {
    bottom: auto
  }

  .xs\:rt-r-left-auto {
    left: auto
  }

  .xs\:rt-r-inset-0 {
    inset: 0
  }

  .xs\:rt-r-top-0 {
    top: 0
  }

  .xs\:rt-r-right-0 {
    right: 0
  }

  .xs\:rt-r-bottom-0 {
    bottom: 0
  }

  .xs\:rt-r-left-0 {
    left: 0
  }

  .xs\:rt-r-inset-50\% {
    inset: 50%
  }

  .xs\:rt-r-top-50\% {
    top: 50%
  }

  .xs\:rt-r-right-50\% {
    right: 50%
  }

  .xs\:rt-r-bottom-50\% {
    bottom: 50%
  }

  .xs\:rt-r-left-50\% {
    left: 50%
  }

  .xs\:rt-r-inset-100\% {
    inset: 100%
  }

  .xs\:rt-r-top-100\% {
    top: 100%
  }

  .xs\:rt-r-right-100\% {
    right: 100%
  }

  .xs\:rt-r-bottom-100\% {
    bottom: 100%
  }

  .xs\:rt-r-left-100\% {
    left: 100%
  }
}

@media (min-width:768px) {
  .sm\:rt-r-inset-auto {
    inset: auto
  }

  .sm\:rt-r-top-auto {
    top: auto
  }

  .sm\:rt-r-right-auto {
    right: auto
  }

  .sm\:rt-r-bottom-auto {
    bottom: auto
  }

  .sm\:rt-r-left-auto {
    left: auto
  }

  .sm\:rt-r-inset-0 {
    inset: 0
  }

  .sm\:rt-r-top-0 {
    top: 0
  }

  .sm\:rt-r-right-0 {
    right: 0
  }

  .sm\:rt-r-bottom-0 {
    bottom: 0
  }

  .sm\:rt-r-left-0 {
    left: 0
  }

  .sm\:rt-r-inset-50\% {
    inset: 50%
  }

  .sm\:rt-r-top-50\% {
    top: 50%
  }

  .sm\:rt-r-right-50\% {
    right: 50%
  }

  .sm\:rt-r-bottom-50\% {
    bottom: 50%
  }

  .sm\:rt-r-left-50\% {
    left: 50%
  }

  .sm\:rt-r-inset-100\% {
    inset: 100%
  }

  .sm\:rt-r-top-100\% {
    top: 100%
  }

  .sm\:rt-r-right-100\% {
    right: 100%
  }

  .sm\:rt-r-bottom-100\% {
    bottom: 100%
  }

  .sm\:rt-r-left-100\% {
    left: 100%
  }
}

@media (min-width:1024px) {
  .md\:rt-r-inset-auto {
    inset: auto
  }

  .md\:rt-r-top-auto {
    top: auto
  }

  .md\:rt-r-right-auto {
    right: auto
  }

  .md\:rt-r-bottom-auto {
    bottom: auto
  }

  .md\:rt-r-left-auto {
    left: auto
  }

  .md\:rt-r-inset-0 {
    inset: 0
  }

  .md\:rt-r-top-0 {
    top: 0
  }

  .md\:rt-r-right-0 {
    right: 0
  }

  .md\:rt-r-bottom-0 {
    bottom: 0
  }

  .md\:rt-r-left-0 {
    left: 0
  }

  .md\:rt-r-inset-50\% {
    inset: 50%
  }

  .md\:rt-r-top-50\% {
    top: 50%
  }

  .md\:rt-r-right-50\% {
    right: 50%
  }

  .md\:rt-r-bottom-50\% {
    bottom: 50%
  }

  .md\:rt-r-left-50\% {
    left: 50%
  }

  .md\:rt-r-inset-100\% {
    inset: 100%
  }

  .md\:rt-r-top-100\% {
    top: 100%
  }

  .md\:rt-r-right-100\% {
    right: 100%
  }

  .md\:rt-r-bottom-100\% {
    bottom: 100%
  }

  .md\:rt-r-left-100\% {
    left: 100%
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-inset-auto {
    inset: auto
  }

  .lg\:rt-r-top-auto {
    top: auto
  }

  .lg\:rt-r-right-auto {
    right: auto
  }

  .lg\:rt-r-bottom-auto {
    bottom: auto
  }

  .lg\:rt-r-left-auto {
    left: auto
  }

  .lg\:rt-r-inset-0 {
    inset: 0
  }

  .lg\:rt-r-top-0 {
    top: 0
  }

  .lg\:rt-r-right-0 {
    right: 0
  }

  .lg\:rt-r-bottom-0 {
    bottom: 0
  }

  .lg\:rt-r-left-0 {
    left: 0
  }

  .lg\:rt-r-inset-50\% {
    inset: 50%
  }

  .lg\:rt-r-top-50\% {
    top: 50%
  }

  .lg\:rt-r-right-50\% {
    right: 50%
  }

  .lg\:rt-r-bottom-50\% {
    bottom: 50%
  }

  .lg\:rt-r-left-50\% {
    left: 50%
  }

  .lg\:rt-r-inset-100\% {
    inset: 100%
  }

  .lg\:rt-r-top-100\% {
    top: 100%
  }

  .lg\:rt-r-right-100\% {
    right: 100%
  }

  .lg\:rt-r-bottom-100\% {
    bottom: 100%
  }

  .lg\:rt-r-left-100\% {
    left: 100%
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-inset-auto {
    inset: auto
  }

  .xl\:rt-r-top-auto {
    top: auto
  }

  .xl\:rt-r-right-auto {
    right: auto
  }

  .xl\:rt-r-bottom-auto {
    bottom: auto
  }

  .xl\:rt-r-left-auto {
    left: auto
  }

  .xl\:rt-r-inset-0 {
    inset: 0
  }

  .xl\:rt-r-top-0 {
    top: 0
  }

  .xl\:rt-r-right-0 {
    right: 0
  }

  .xl\:rt-r-bottom-0 {
    bottom: 0
  }

  .xl\:rt-r-left-0 {
    left: 0
  }

  .xl\:rt-r-inset-50\% {
    inset: 50%
  }

  .xl\:rt-r-top-50\% {
    top: 50%
  }

  .xl\:rt-r-right-50\% {
    right: 50%
  }

  .xl\:rt-r-bottom-50\% {
    bottom: 50%
  }

  .xl\:rt-r-left-50\% {
    left: 50%
  }

  .xl\:rt-r-inset-100\% {
    inset: 100%
  }

  .xl\:rt-r-top-100\% {
    top: 100%
  }

  .xl\:rt-r-right-100\% {
    right: 100%
  }

  .xl\:rt-r-bottom-100\% {
    bottom: 100%
  }

  .xl\:rt-r-left-100\% {
    left: 100%
  }
}

@media all {
  .rt-r-jc-start {
    justify-content: flex-start
  }

  .rt-r-jc-center {
    justify-content: center
  }

  .rt-r-jc-end {
    justify-content: flex-end
  }

  .rt-r-jc-space-between {
    justify-content: space-between
  }
}

@media (min-width:520px) {
  .xs\:rt-r-jc-start {
    justify-content: flex-start
  }

  .xs\:rt-r-jc-center {
    justify-content: center
  }

  .xs\:rt-r-jc-end {
    justify-content: flex-end
  }

  .xs\:rt-r-jc-space-between {
    justify-content: space-between
  }
}

@media (min-width:768px) {
  .sm\:rt-r-jc-start {
    justify-content: flex-start
  }

  .sm\:rt-r-jc-center {
    justify-content: center
  }

  .sm\:rt-r-jc-end {
    justify-content: flex-end
  }

  .sm\:rt-r-jc-space-between {
    justify-content: space-between
  }
}

@media (min-width:1024px) {
  .md\:rt-r-jc-start {
    justify-content: flex-start
  }

  .md\:rt-r-jc-center {
    justify-content: center
  }

  .md\:rt-r-jc-end {
    justify-content: flex-end
  }

  .md\:rt-r-jc-space-between {
    justify-content: space-between
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-jc-start {
    justify-content: flex-start
  }

  .lg\:rt-r-jc-center {
    justify-content: center
  }

  .lg\:rt-r-jc-end {
    justify-content: flex-end
  }

  .lg\:rt-r-jc-space-between {
    justify-content: space-between
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-jc-start {
    justify-content: flex-start
  }

  .xl\:rt-r-jc-center {
    justify-content: center
  }

  .xl\:rt-r-jc-end {
    justify-content: flex-end
  }

  .xl\:rt-r-jc-space-between {
    justify-content: space-between
  }
}

@media all {

  .rt-r-lt-end:before,
  .rt-r-lt-normal:after,
  .rt-r-lt-normal:before,
  .rt-r-lt-start:after {
    content: none
  }

  .rt-r-lt-both:after,
  .rt-r-lt-both:before,
  .rt-r-lt-end:after,
  .rt-r-lt-start:before {
    content: "";
    display: table
  }

  .rt-r-lt-both:before,
  .rt-r-lt-start:before {
    margin-bottom: calc(var(--leading-trim-start, var(--default-leading-trim-start)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }

  .rt-r-lt-both:after,
  .rt-r-lt-end:after {
    margin-top: calc(var(--leading-trim-end, var(--default-leading-trim-end)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }
}

@media (min-width:520px) {

  .xs\:rt-r-lt-end:before,
  .xs\:rt-r-lt-normal:after,
  .xs\:rt-r-lt-normal:before,
  .xs\:rt-r-lt-start:after {
    content: none
  }

  .xs\:rt-r-lt-both:after,
  .xs\:rt-r-lt-both:before,
  .xs\:rt-r-lt-end:after,
  .xs\:rt-r-lt-start:before {
    content: "";
    display: table
  }

  .xs\:rt-r-lt-both:before,
  .xs\:rt-r-lt-start:before {
    margin-bottom: calc(var(--leading-trim-start, var(--default-leading-trim-start)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }

  .xs\:rt-r-lt-both:after,
  .xs\:rt-r-lt-end:after {
    margin-top: calc(var(--leading-trim-end, var(--default-leading-trim-end)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }
}

@media (min-width:768px) {

  .sm\:rt-r-lt-end:before,
  .sm\:rt-r-lt-normal:after,
  .sm\:rt-r-lt-normal:before,
  .sm\:rt-r-lt-start:after {
    content: none
  }

  .sm\:rt-r-lt-both:after,
  .sm\:rt-r-lt-both:before,
  .sm\:rt-r-lt-end:after,
  .sm\:rt-r-lt-start:before {
    content: "";
    display: table
  }

  .sm\:rt-r-lt-both:before,
  .sm\:rt-r-lt-start:before {
    margin-bottom: calc(var(--leading-trim-start, var(--default-leading-trim-start)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }

  .sm\:rt-r-lt-both:after,
  .sm\:rt-r-lt-end:after {
    margin-top: calc(var(--leading-trim-end, var(--default-leading-trim-end)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }
}

@media (min-width:1024px) {

  .md\:rt-r-lt-end:before,
  .md\:rt-r-lt-normal:after,
  .md\:rt-r-lt-normal:before,
  .md\:rt-r-lt-start:after {
    content: none
  }

  .md\:rt-r-lt-both:after,
  .md\:rt-r-lt-both:before,
  .md\:rt-r-lt-end:after,
  .md\:rt-r-lt-start:before {
    content: "";
    display: table
  }

  .md\:rt-r-lt-both:before,
  .md\:rt-r-lt-start:before {
    margin-bottom: calc(var(--leading-trim-start, var(--default-leading-trim-start)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }

  .md\:rt-r-lt-both:after,
  .md\:rt-r-lt-end:after {
    margin-top: calc(var(--leading-trim-end, var(--default-leading-trim-end)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }
}

@media (min-width:1280px) {

  .lg\:rt-r-lt-end:before,
  .lg\:rt-r-lt-normal:after,
  .lg\:rt-r-lt-normal:before,
  .lg\:rt-r-lt-start:after {
    content: none
  }

  .lg\:rt-r-lt-both:after,
  .lg\:rt-r-lt-both:before,
  .lg\:rt-r-lt-end:after,
  .lg\:rt-r-lt-start:before {
    content: "";
    display: table
  }

  .lg\:rt-r-lt-both:before,
  .lg\:rt-r-lt-start:before {
    margin-bottom: calc(var(--leading-trim-start, var(--default-leading-trim-start)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }

  .lg\:rt-r-lt-both:after,
  .lg\:rt-r-lt-end:after {
    margin-top: calc(var(--leading-trim-end, var(--default-leading-trim-end)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }
}

@media (min-width:1640px) {

  .xl\:rt-r-lt-end:before,
  .xl\:rt-r-lt-normal:after,
  .xl\:rt-r-lt-normal:before,
  .xl\:rt-r-lt-start:after {
    content: none
  }

  .xl\:rt-r-lt-both:after,
  .xl\:rt-r-lt-both:before,
  .xl\:rt-r-lt-end:after,
  .xl\:rt-r-lt-start:before {
    content: "";
    display: table
  }

  .xl\:rt-r-lt-both:before,
  .xl\:rt-r-lt-start:before {
    margin-bottom: calc(var(--leading-trim-start, var(--default-leading-trim-start)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }

  .xl\:rt-r-lt-both:after,
  .xl\:rt-r-lt-end:after {
    margin-top: calc(var(--leading-trim-end, var(--default-leading-trim-end)) - var(--line-height, calc(1em * var(--default-line-height))) / 2)
  }
}

@media all {
  .rt-r-m-auto {
    margin: auto
  }

  .rt-r-m-0 {
    --margin-top: 0px;
    --margin-right: 0px;
    --margin-bottom: 0px;
    --margin-left: 0px
  }

  .rt-r-m-0,
  .rt-r-m-1 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .rt-r-m-1 {
    --margin-top: var(--space-1);
    --margin-right: var(--space-1);
    --margin-bottom: var(--space-1);
    --margin-left: var(--space-1)
  }

  .rt-r-m-2 {
    --margin-top: var(--space-2);
    --margin-right: var(--space-2);
    --margin-bottom: var(--space-2);
    --margin-left: var(--space-2)
  }

  .rt-r-m-2,
  .rt-r-m-3 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .rt-r-m-3 {
    --margin-top: var(--space-3);
    --margin-right: var(--space-3);
    --margin-bottom: var(--space-3);
    --margin-left: var(--space-3)
  }

  .rt-r-m-4 {
    --margin-top: var(--space-4);
    --margin-right: var(--space-4);
    --margin-bottom: var(--space-4);
    --margin-left: var(--space-4)
  }

  .rt-r-m-4,
  .rt-r-m-5 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .rt-r-m-5 {
    --margin-top: var(--space-5);
    --margin-right: var(--space-5);
    --margin-bottom: var(--space-5);
    --margin-left: var(--space-5)
  }

  .rt-r-m-6 {
    --margin-top: var(--space-6);
    --margin-right: var(--space-6);
    --margin-bottom: var(--space-6);
    --margin-left: var(--space-6)
  }

  .rt-r-m-6,
  .rt-r-m-7 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .rt-r-m-7 {
    --margin-top: var(--space-7);
    --margin-right: var(--space-7);
    --margin-bottom: var(--space-7);
    --margin-left: var(--space-7)
  }

  .rt-r-m-8 {
    --margin-top: var(--space-8);
    --margin-right: var(--space-8);
    --margin-bottom: var(--space-8);
    --margin-left: var(--space-8)
  }

  .rt-r-m-8,
  .rt-r-m-9 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .rt-r-m-9 {
    --margin-top: var(--space-9);
    --margin-right: var(--space-9);
    --margin-bottom: var(--space-9);
    --margin-left: var(--space-9)
  }

  .-rt-r-m-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1));
    --margin-left: calc(-1 * var(--space-1))
  }

  .-rt-r-m-1,
  .-rt-r-m-2 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-m-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2));
    --margin-left: calc(-1 * var(--space-2))
  }

  .-rt-r-m-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3));
    --margin-left: calc(-1 * var(--space-3))
  }

  .-rt-r-m-3,
  .-rt-r-m-4 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-m-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4));
    --margin-left: calc(-1 * var(--space-4))
  }

  .-rt-r-m-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5));
    --margin-left: calc(-1 * var(--space-5))
  }

  .-rt-r-m-5,
  .-rt-r-m-6 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-m-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6));
    --margin-left: calc(-1 * var(--space-6))
  }

  .-rt-r-m-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7));
    --margin-left: calc(-1 * var(--space-7))
  }

  .-rt-r-m-7,
  .-rt-r-m-8 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-m-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8));
    --margin-left: calc(-1 * var(--space-8))
  }

  .-rt-r-m-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    --margin-left: calc(-1 * var(--space-9));
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .rt-r-mx-auto {
    margin-left: auto;
    margin-right: auto
  }

  .rt-r-mx-0 {
    --margin-left: 0px;
    --margin-right: 0px
  }

  .rt-r-mx-0,
  .rt-r-mx-1 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mx-1 {
    --margin-left: var(--space-1);
    --margin-right: var(--space-1)
  }

  .rt-r-mx-2 {
    --margin-left: var(--space-2);
    --margin-right: var(--space-2)
  }

  .rt-r-mx-2,
  .rt-r-mx-3 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mx-3 {
    --margin-left: var(--space-3);
    --margin-right: var(--space-3)
  }

  .rt-r-mx-4 {
    --margin-left: var(--space-4);
    --margin-right: var(--space-4)
  }

  .rt-r-mx-4,
  .rt-r-mx-5 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mx-5 {
    --margin-left: var(--space-5);
    --margin-right: var(--space-5)
  }

  .rt-r-mx-6 {
    --margin-left: var(--space-6);
    --margin-right: var(--space-6)
  }

  .rt-r-mx-6,
  .rt-r-mx-7 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mx-7 {
    --margin-left: var(--space-7);
    --margin-right: var(--space-7)
  }

  .rt-r-mx-8 {
    --margin-left: var(--space-8);
    --margin-right: var(--space-8)
  }

  .rt-r-mx-8,
  .rt-r-mx-9 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mx-9 {
    --margin-left: var(--space-9);
    --margin-right: var(--space-9)
  }

  .-rt-r-mx-1 {
    --margin-left: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1))
  }

  .-rt-r-mx-1,
  .-rt-r-mx-2 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mx-2 {
    --margin-left: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2))
  }

  .-rt-r-mx-3 {
    --margin-left: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3))
  }

  .-rt-r-mx-3,
  .-rt-r-mx-4 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mx-4 {
    --margin-left: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4))
  }

  .-rt-r-mx-5 {
    --margin-left: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5))
  }

  .-rt-r-mx-5,
  .-rt-r-mx-6 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mx-6 {
    --margin-left: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6))
  }

  .-rt-r-mx-7 {
    --margin-left: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7))
  }

  .-rt-r-mx-7,
  .-rt-r-mx-8 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mx-8 {
    --margin-left: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8))
  }

  .-rt-r-mx-9 {
    --margin-left: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-my-auto {
    margin-top: auto;
    margin-bottom: auto
  }

  .rt-r-my-0 {
    --margin-top: 0px;
    --margin-bottom: 0px
  }

  .rt-r-my-0,
  .rt-r-my-1 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-my-1 {
    --margin-top: var(--space-1);
    --margin-bottom: var(--space-1)
  }

  .rt-r-my-2 {
    --margin-top: var(--space-2);
    --margin-bottom: var(--space-2)
  }

  .rt-r-my-2,
  .rt-r-my-3 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-my-3 {
    --margin-top: var(--space-3);
    --margin-bottom: var(--space-3)
  }

  .rt-r-my-4 {
    --margin-top: var(--space-4);
    --margin-bottom: var(--space-4)
  }

  .rt-r-my-4,
  .rt-r-my-5 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-my-5 {
    --margin-top: var(--space-5);
    --margin-bottom: var(--space-5)
  }

  .rt-r-my-6 {
    --margin-top: var(--space-6);
    --margin-bottom: var(--space-6)
  }

  .rt-r-my-6,
  .rt-r-my-7 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-my-7 {
    --margin-top: var(--space-7);
    --margin-bottom: var(--space-7)
  }

  .rt-r-my-8 {
    --margin-top: var(--space-8);
    --margin-bottom: var(--space-8)
  }

  .rt-r-my-8,
  .rt-r-my-9 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-my-9 {
    --margin-top: var(--space-9);
    --margin-bottom: var(--space-9)
  }

  .-rt-r-my-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .-rt-r-my-1,
  .-rt-r-my-2 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-my-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .-rt-r-my-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .-rt-r-my-3,
  .-rt-r-my-4 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-my-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .-rt-r-my-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .-rt-r-my-5,
  .-rt-r-my-6 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-my-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .-rt-r-my-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .-rt-r-my-7,
  .-rt-r-my-8 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-my-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .-rt-r-my-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-mt-auto {
    margin-top: auto
  }

  .rt-r-mt-0 {
    --margin-top: 0px
  }

  .rt-r-mt-0,
  .rt-r-mt-1 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .rt-r-mt-1 {
    --margin-top: var(--space-1)
  }

  .rt-r-mt-2 {
    --margin-top: var(--space-2)
  }

  .rt-r-mt-2,
  .rt-r-mt-3 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .rt-r-mt-3 {
    --margin-top: var(--space-3)
  }

  .rt-r-mt-4 {
    --margin-top: var(--space-4)
  }

  .rt-r-mt-4,
  .rt-r-mt-5 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .rt-r-mt-5 {
    --margin-top: var(--space-5)
  }

  .rt-r-mt-6 {
    --margin-top: var(--space-6)
  }

  .rt-r-mt-6,
  .rt-r-mt-7 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .rt-r-mt-7 {
    --margin-top: var(--space-7)
  }

  .rt-r-mt-8 {
    --margin-top: var(--space-8)
  }

  .rt-r-mt-8,
  .rt-r-mt-9 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .rt-r-mt-9 {
    --margin-top: var(--space-9)
  }

  .-rt-r-mt-1 {
    --margin-top: calc(-1 * var(--space-1))
  }

  .-rt-r-mt-1,
  .-rt-r-mt-2 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .-rt-r-mt-2 {
    --margin-top: calc(-1 * var(--space-2))
  }

  .-rt-r-mt-3 {
    --margin-top: calc(-1 * var(--space-3))
  }

  .-rt-r-mt-3,
  .-rt-r-mt-4 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .-rt-r-mt-4 {
    --margin-top: calc(-1 * var(--space-4))
  }

  .-rt-r-mt-5 {
    --margin-top: calc(-1 * var(--space-5))
  }

  .-rt-r-mt-5,
  .-rt-r-mt-6 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .-rt-r-mt-6 {
    --margin-top: calc(-1 * var(--space-6))
  }

  .-rt-r-mt-7 {
    --margin-top: calc(-1 * var(--space-7))
  }

  .-rt-r-mt-7,
  .-rt-r-mt-8 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .-rt-r-mt-8 {
    --margin-top: calc(-1 * var(--space-8))
  }

  .-rt-r-mt-9 {
    --margin-top: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .rt-r-mr-auto {
    margin-right: auto
  }

  .rt-r-mr-0 {
    --margin-right: 0px
  }

  .rt-r-mr-0,
  .rt-r-mr-1 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mr-1 {
    --margin-right: var(--space-1)
  }

  .rt-r-mr-2 {
    --margin-right: var(--space-2)
  }

  .rt-r-mr-2,
  .rt-r-mr-3 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mr-3 {
    --margin-right: var(--space-3)
  }

  .rt-r-mr-4 {
    --margin-right: var(--space-4)
  }

  .rt-r-mr-4,
  .rt-r-mr-5 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mr-5 {
    --margin-right: var(--space-5)
  }

  .rt-r-mr-6 {
    --margin-right: var(--space-6)
  }

  .rt-r-mr-6,
  .rt-r-mr-7 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mr-7 {
    --margin-right: var(--space-7)
  }

  .rt-r-mr-8 {
    --margin-right: var(--space-8)
  }

  .rt-r-mr-8,
  .rt-r-mr-9 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mr-9 {
    --margin-right: var(--space-9)
  }

  .-rt-r-mr-1 {
    --margin-right: calc(-1 * var(--space-1))
  }

  .-rt-r-mr-1,
  .-rt-r-mr-2 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mr-2 {
    --margin-right: calc(-1 * var(--space-2))
  }

  .-rt-r-mr-3 {
    --margin-right: calc(-1 * var(--space-3))
  }

  .-rt-r-mr-3,
  .-rt-r-mr-4 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mr-4 {
    --margin-right: calc(-1 * var(--space-4))
  }

  .-rt-r-mr-5 {
    --margin-right: calc(-1 * var(--space-5))
  }

  .-rt-r-mr-5,
  .-rt-r-mr-6 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mr-6 {
    --margin-right: calc(-1 * var(--space-6))
  }

  .-rt-r-mr-7 {
    --margin-right: calc(-1 * var(--space-7))
  }

  .-rt-r-mr-7,
  .-rt-r-mr-8 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .-rt-r-mr-8 {
    --margin-right: calc(-1 * var(--space-8))
  }

  .-rt-r-mr-9 {
    --margin-right: calc(-1 * var(--space-9));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .rt-r-mb-auto {
    margin-bottom: auto
  }

  .rt-r-mb-0 {
    --margin-bottom: 0px
  }

  .rt-r-mb-0,
  .rt-r-mb-1 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-mb-1 {
    --margin-bottom: var(--space-1)
  }

  .rt-r-mb-2 {
    --margin-bottom: var(--space-2)
  }

  .rt-r-mb-2,
  .rt-r-mb-3 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-mb-3 {
    --margin-bottom: var(--space-3)
  }

  .rt-r-mb-4 {
    --margin-bottom: var(--space-4)
  }

  .rt-r-mb-4,
  .rt-r-mb-5 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-mb-5 {
    --margin-bottom: var(--space-5)
  }

  .rt-r-mb-6 {
    --margin-bottom: var(--space-6)
  }

  .rt-r-mb-6,
  .rt-r-mb-7 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-mb-7 {
    --margin-bottom: var(--space-7)
  }

  .rt-r-mb-8 {
    --margin-bottom: var(--space-8)
  }

  .rt-r-mb-8,
  .rt-r-mb-9 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-mb-9 {
    --margin-bottom: var(--space-9)
  }

  .-rt-r-mb-1 {
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .-rt-r-mb-1,
  .-rt-r-mb-2 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-mb-2 {
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .-rt-r-mb-3 {
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .-rt-r-mb-3,
  .-rt-r-mb-4 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-mb-4 {
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .-rt-r-mb-5 {
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .-rt-r-mb-5,
  .-rt-r-mb-6 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-mb-6 {
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .-rt-r-mb-7 {
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .-rt-r-mb-7,
  .-rt-r-mb-8 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .-rt-r-mb-8 {
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .-rt-r-mb-9 {
    --margin-bottom: calc(-1 * var(--space-9));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .rt-r-ml-auto {
    margin-left: auto
  }

  .rt-r-ml-0 {
    --margin-left: 0px
  }

  .rt-r-ml-0,
  .rt-r-ml-1 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .rt-r-ml-1 {
    --margin-left: var(--space-1)
  }

  .rt-r-ml-2 {
    --margin-left: var(--space-2)
  }

  .rt-r-ml-2,
  .rt-r-ml-3 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .rt-r-ml-3 {
    --margin-left: var(--space-3)
  }

  .rt-r-ml-4 {
    --margin-left: var(--space-4)
  }

  .rt-r-ml-4,
  .rt-r-ml-5 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .rt-r-ml-5 {
    --margin-left: var(--space-5)
  }

  .rt-r-ml-6 {
    --margin-left: var(--space-6)
  }

  .rt-r-ml-6,
  .rt-r-ml-7 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .rt-r-ml-7 {
    --margin-left: var(--space-7)
  }

  .rt-r-ml-8 {
    --margin-left: var(--space-8)
  }

  .rt-r-ml-8,
  .rt-r-ml-9 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .rt-r-ml-9 {
    --margin-left: var(--space-9)
  }

  .-rt-r-ml-1 {
    --margin-left: calc(-1 * var(--space-1))
  }

  .-rt-r-ml-1,
  .-rt-r-ml-2 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-ml-2 {
    --margin-left: calc(-1 * var(--space-2))
  }

  .-rt-r-ml-3 {
    --margin-left: calc(-1 * var(--space-3))
  }

  .-rt-r-ml-3,
  .-rt-r-ml-4 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-ml-4 {
    --margin-left: calc(-1 * var(--space-4))
  }

  .-rt-r-ml-5 {
    --margin-left: calc(-1 * var(--space-5))
  }

  .-rt-r-ml-5,
  .-rt-r-ml-6 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-ml-6 {
    --margin-left: calc(-1 * var(--space-6))
  }

  .-rt-r-ml-7 {
    --margin-left: calc(-1 * var(--space-7))
  }

  .-rt-r-ml-7,
  .-rt-r-ml-8 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .-rt-r-ml-8 {
    --margin-left: calc(-1 * var(--space-8))
  }

  .-rt-r-ml-9 {
    --margin-left: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left))
  }
}

@media (min-width:520px) {
  .xs\:rt-r-m-auto {
    margin: auto
  }

  .xs\:rt-r-m-0 {
    --margin-top: 0px;
    --margin-right: 0px;
    --margin-bottom: 0px;
    --margin-left: 0px
  }

  .xs\:rt-r-m-0,
  .xs\:rt-r-m-1 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-m-1 {
    --margin-top: var(--space-1);
    --margin-right: var(--space-1);
    --margin-bottom: var(--space-1);
    --margin-left: var(--space-1)
  }

  .xs\:rt-r-m-2 {
    --margin-top: var(--space-2);
    --margin-right: var(--space-2);
    --margin-bottom: var(--space-2);
    --margin-left: var(--space-2)
  }

  .xs\:rt-r-m-2,
  .xs\:rt-r-m-3 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-m-3 {
    --margin-top: var(--space-3);
    --margin-right: var(--space-3);
    --margin-bottom: var(--space-3);
    --margin-left: var(--space-3)
  }

  .xs\:rt-r-m-4 {
    --margin-top: var(--space-4);
    --margin-right: var(--space-4);
    --margin-bottom: var(--space-4);
    --margin-left: var(--space-4)
  }

  .xs\:rt-r-m-4,
  .xs\:rt-r-m-5 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-m-5 {
    --margin-top: var(--space-5);
    --margin-right: var(--space-5);
    --margin-bottom: var(--space-5);
    --margin-left: var(--space-5)
  }

  .xs\:rt-r-m-6 {
    --margin-top: var(--space-6);
    --margin-right: var(--space-6);
    --margin-bottom: var(--space-6);
    --margin-left: var(--space-6)
  }

  .xs\:rt-r-m-6,
  .xs\:rt-r-m-7 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-m-7 {
    --margin-top: var(--space-7);
    --margin-right: var(--space-7);
    --margin-bottom: var(--space-7);
    --margin-left: var(--space-7)
  }

  .xs\:rt-r-m-8 {
    --margin-top: var(--space-8);
    --margin-right: var(--space-8);
    --margin-bottom: var(--space-8);
    --margin-left: var(--space-8)
  }

  .xs\:rt-r-m-8,
  .xs\:rt-r-m-9 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-m-9 {
    --margin-top: var(--space-9);
    --margin-right: var(--space-9);
    --margin-bottom: var(--space-9);
    --margin-left: var(--space-9)
  }

  .xs\:-rt-r-m-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1));
    --margin-left: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-m-1,
  .xs\:-rt-r-m-2 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-m-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2));
    --margin-left: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-m-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3));
    --margin-left: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-m-3,
  .xs\:-rt-r-m-4 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-m-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4));
    --margin-left: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-m-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5));
    --margin-left: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-m-5,
  .xs\:-rt-r-m-6 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-m-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6));
    --margin-left: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-m-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7));
    --margin-left: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-m-7,
  .xs\:-rt-r-m-8 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-m-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8));
    --margin-left: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-m-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    --margin-left: calc(-1 * var(--space-9));
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-mx-auto {
    margin-left: auto;
    margin-right: auto
  }

  .xs\:rt-r-mx-0 {
    --margin-left: 0px;
    --margin-right: 0px
  }

  .xs\:rt-r-mx-0,
  .xs\:rt-r-mx-1 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mx-1 {
    --margin-left: var(--space-1);
    --margin-right: var(--space-1)
  }

  .xs\:rt-r-mx-2 {
    --margin-left: var(--space-2);
    --margin-right: var(--space-2)
  }

  .xs\:rt-r-mx-2,
  .xs\:rt-r-mx-3 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mx-3 {
    --margin-left: var(--space-3);
    --margin-right: var(--space-3)
  }

  .xs\:rt-r-mx-4 {
    --margin-left: var(--space-4);
    --margin-right: var(--space-4)
  }

  .xs\:rt-r-mx-4,
  .xs\:rt-r-mx-5 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mx-5 {
    --margin-left: var(--space-5);
    --margin-right: var(--space-5)
  }

  .xs\:rt-r-mx-6 {
    --margin-left: var(--space-6);
    --margin-right: var(--space-6)
  }

  .xs\:rt-r-mx-6,
  .xs\:rt-r-mx-7 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mx-7 {
    --margin-left: var(--space-7);
    --margin-right: var(--space-7)
  }

  .xs\:rt-r-mx-8 {
    --margin-left: var(--space-8);
    --margin-right: var(--space-8)
  }

  .xs\:rt-r-mx-8,
  .xs\:rt-r-mx-9 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mx-9 {
    --margin-left: var(--space-9);
    --margin-right: var(--space-9)
  }

  .xs\:-rt-r-mx-1 {
    --margin-left: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-mx-1,
  .xs\:-rt-r-mx-2 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mx-2 {
    --margin-left: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-mx-3 {
    --margin-left: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-mx-3,
  .xs\:-rt-r-mx-4 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mx-4 {
    --margin-left: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-mx-5 {
    --margin-left: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-mx-5,
  .xs\:-rt-r-mx-6 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mx-6 {
    --margin-left: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-mx-7 {
    --margin-left: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-mx-7,
  .xs\:-rt-r-mx-8 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mx-8 {
    --margin-left: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-mx-9 {
    --margin-left: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-my-auto {
    margin-top: auto;
    margin-bottom: auto
  }

  .xs\:rt-r-my-0 {
    --margin-top: 0px;
    --margin-bottom: 0px
  }

  .xs\:rt-r-my-0,
  .xs\:rt-r-my-1 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-my-1 {
    --margin-top: var(--space-1);
    --margin-bottom: var(--space-1)
  }

  .xs\:rt-r-my-2 {
    --margin-top: var(--space-2);
    --margin-bottom: var(--space-2)
  }

  .xs\:rt-r-my-2,
  .xs\:rt-r-my-3 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-my-3 {
    --margin-top: var(--space-3);
    --margin-bottom: var(--space-3)
  }

  .xs\:rt-r-my-4 {
    --margin-top: var(--space-4);
    --margin-bottom: var(--space-4)
  }

  .xs\:rt-r-my-4,
  .xs\:rt-r-my-5 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-my-5 {
    --margin-top: var(--space-5);
    --margin-bottom: var(--space-5)
  }

  .xs\:rt-r-my-6 {
    --margin-top: var(--space-6);
    --margin-bottom: var(--space-6)
  }

  .xs\:rt-r-my-6,
  .xs\:rt-r-my-7 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-my-7 {
    --margin-top: var(--space-7);
    --margin-bottom: var(--space-7)
  }

  .xs\:rt-r-my-8 {
    --margin-top: var(--space-8);
    --margin-bottom: var(--space-8)
  }

  .xs\:rt-r-my-8,
  .xs\:rt-r-my-9 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-my-9 {
    --margin-top: var(--space-9);
    --margin-bottom: var(--space-9)
  }

  .xs\:-rt-r-my-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-my-1,
  .xs\:-rt-r-my-2 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-my-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-my-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-my-3,
  .xs\:-rt-r-my-4 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-my-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-my-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-my-5,
  .xs\:-rt-r-my-6 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-my-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-my-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-my-7,
  .xs\:-rt-r-my-8 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-my-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-my-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-mt-auto {
    margin-top: auto
  }

  .xs\:rt-r-mt-0 {
    --margin-top: 0px
  }

  .xs\:rt-r-mt-0,
  .xs\:rt-r-mt-1 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:rt-r-mt-1 {
    --margin-top: var(--space-1)
  }

  .xs\:rt-r-mt-2 {
    --margin-top: var(--space-2)
  }

  .xs\:rt-r-mt-2,
  .xs\:rt-r-mt-3 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:rt-r-mt-3 {
    --margin-top: var(--space-3)
  }

  .xs\:rt-r-mt-4 {
    --margin-top: var(--space-4)
  }

  .xs\:rt-r-mt-4,
  .xs\:rt-r-mt-5 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:rt-r-mt-5 {
    --margin-top: var(--space-5)
  }

  .xs\:rt-r-mt-6 {
    --margin-top: var(--space-6)
  }

  .xs\:rt-r-mt-6,
  .xs\:rt-r-mt-7 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:rt-r-mt-7 {
    --margin-top: var(--space-7)
  }

  .xs\:rt-r-mt-8 {
    --margin-top: var(--space-8)
  }

  .xs\:rt-r-mt-8,
  .xs\:rt-r-mt-9 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:rt-r-mt-9 {
    --margin-top: var(--space-9)
  }

  .xs\:-rt-r-mt-1 {
    --margin-top: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-mt-1,
  .xs\:-rt-r-mt-2 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:-rt-r-mt-2 {
    --margin-top: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-mt-3 {
    --margin-top: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-mt-3,
  .xs\:-rt-r-mt-4 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:-rt-r-mt-4 {
    --margin-top: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-mt-5 {
    --margin-top: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-mt-5,
  .xs\:-rt-r-mt-6 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:-rt-r-mt-6 {
    --margin-top: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-mt-7 {
    --margin-top: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-mt-7,
  .xs\:-rt-r-mt-8 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:-rt-r-mt-8 {
    --margin-top: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-mt-9 {
    --margin-top: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xs\:rt-r-mr-auto {
    margin-right: auto
  }

  .xs\:rt-r-mr-0 {
    --margin-right: 0px
  }

  .xs\:rt-r-mr-0,
  .xs\:rt-r-mr-1 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mr-1 {
    --margin-right: var(--space-1)
  }

  .xs\:rt-r-mr-2 {
    --margin-right: var(--space-2)
  }

  .xs\:rt-r-mr-2,
  .xs\:rt-r-mr-3 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mr-3 {
    --margin-right: var(--space-3)
  }

  .xs\:rt-r-mr-4 {
    --margin-right: var(--space-4)
  }

  .xs\:rt-r-mr-4,
  .xs\:rt-r-mr-5 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mr-5 {
    --margin-right: var(--space-5)
  }

  .xs\:rt-r-mr-6 {
    --margin-right: var(--space-6)
  }

  .xs\:rt-r-mr-6,
  .xs\:rt-r-mr-7 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mr-7 {
    --margin-right: var(--space-7)
  }

  .xs\:rt-r-mr-8 {
    --margin-right: var(--space-8)
  }

  .xs\:rt-r-mr-8,
  .xs\:rt-r-mr-9 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mr-9 {
    --margin-right: var(--space-9)
  }

  .xs\:-rt-r-mr-1 {
    --margin-right: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-mr-1,
  .xs\:-rt-r-mr-2 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mr-2 {
    --margin-right: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-mr-3 {
    --margin-right: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-mr-3,
  .xs\:-rt-r-mr-4 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mr-4 {
    --margin-right: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-mr-5 {
    --margin-right: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-mr-5,
  .xs\:-rt-r-mr-6 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mr-6 {
    --margin-right: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-mr-7 {
    --margin-right: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-mr-7,
  .xs\:-rt-r-mr-8 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:-rt-r-mr-8 {
    --margin-right: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-mr-9 {
    --margin-right: calc(-1 * var(--space-9));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xs\:rt-r-mb-auto {
    margin-bottom: auto
  }

  .xs\:rt-r-mb-0 {
    --margin-bottom: 0px
  }

  .xs\:rt-r-mb-0,
  .xs\:rt-r-mb-1 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-mb-1 {
    --margin-bottom: var(--space-1)
  }

  .xs\:rt-r-mb-2 {
    --margin-bottom: var(--space-2)
  }

  .xs\:rt-r-mb-2,
  .xs\:rt-r-mb-3 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-mb-3 {
    --margin-bottom: var(--space-3)
  }

  .xs\:rt-r-mb-4 {
    --margin-bottom: var(--space-4)
  }

  .xs\:rt-r-mb-4,
  .xs\:rt-r-mb-5 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-mb-5 {
    --margin-bottom: var(--space-5)
  }

  .xs\:rt-r-mb-6 {
    --margin-bottom: var(--space-6)
  }

  .xs\:rt-r-mb-6,
  .xs\:rt-r-mb-7 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-mb-7 {
    --margin-bottom: var(--space-7)
  }

  .xs\:rt-r-mb-8 {
    --margin-bottom: var(--space-8)
  }

  .xs\:rt-r-mb-8,
  .xs\:rt-r-mb-9 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-mb-9 {
    --margin-bottom: var(--space-9)
  }

  .xs\:-rt-r-mb-1 {
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-mb-1,
  .xs\:-rt-r-mb-2 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-mb-2 {
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-mb-3 {
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-mb-3,
  .xs\:-rt-r-mb-4 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-mb-4 {
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-mb-5 {
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-mb-5,
  .xs\:-rt-r-mb-6 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-mb-6 {
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-mb-7 {
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-mb-7,
  .xs\:-rt-r-mb-8 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:-rt-r-mb-8 {
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-mb-9 {
    --margin-bottom: calc(-1 * var(--space-9));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xs\:rt-r-ml-auto {
    margin-left: auto
  }

  .xs\:rt-r-ml-0 {
    --margin-left: 0px
  }

  .xs\:rt-r-ml-0,
  .xs\:rt-r-ml-1 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-ml-1 {
    --margin-left: var(--space-1)
  }

  .xs\:rt-r-ml-2 {
    --margin-left: var(--space-2)
  }

  .xs\:rt-r-ml-2,
  .xs\:rt-r-ml-3 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-ml-3 {
    --margin-left: var(--space-3)
  }

  .xs\:rt-r-ml-4 {
    --margin-left: var(--space-4)
  }

  .xs\:rt-r-ml-4,
  .xs\:rt-r-ml-5 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-ml-5 {
    --margin-left: var(--space-5)
  }

  .xs\:rt-r-ml-6 {
    --margin-left: var(--space-6)
  }

  .xs\:rt-r-ml-6,
  .xs\:rt-r-ml-7 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-ml-7 {
    --margin-left: var(--space-7)
  }

  .xs\:rt-r-ml-8 {
    --margin-left: var(--space-8)
  }

  .xs\:rt-r-ml-8,
  .xs\:rt-r-ml-9 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:rt-r-ml-9 {
    --margin-left: var(--space-9)
  }

  .xs\:-rt-r-ml-1 {
    --margin-left: calc(-1 * var(--space-1))
  }

  .xs\:-rt-r-ml-1,
  .xs\:-rt-r-ml-2 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-ml-2 {
    --margin-left: calc(-1 * var(--space-2))
  }

  .xs\:-rt-r-ml-3 {
    --margin-left: calc(-1 * var(--space-3))
  }

  .xs\:-rt-r-ml-3,
  .xs\:-rt-r-ml-4 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-ml-4 {
    --margin-left: calc(-1 * var(--space-4))
  }

  .xs\:-rt-r-ml-5 {
    --margin-left: calc(-1 * var(--space-5))
  }

  .xs\:-rt-r-ml-5,
  .xs\:-rt-r-ml-6 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-ml-6 {
    --margin-left: calc(-1 * var(--space-6))
  }

  .xs\:-rt-r-ml-7 {
    --margin-left: calc(-1 * var(--space-7))
  }

  .xs\:-rt-r-ml-7,
  .xs\:-rt-r-ml-8 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xs\:-rt-r-ml-8 {
    --margin-left: calc(-1 * var(--space-8))
  }

  .xs\:-rt-r-ml-9 {
    --margin-left: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left))
  }
}

@media (min-width:768px) {
  .sm\:rt-r-m-auto {
    margin: auto
  }

  .sm\:rt-r-m-0 {
    --margin-top: 0px;
    --margin-right: 0px;
    --margin-bottom: 0px;
    --margin-left: 0px
  }

  .sm\:rt-r-m-0,
  .sm\:rt-r-m-1 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-m-1 {
    --margin-top: var(--space-1);
    --margin-right: var(--space-1);
    --margin-bottom: var(--space-1);
    --margin-left: var(--space-1)
  }

  .sm\:rt-r-m-2 {
    --margin-top: var(--space-2);
    --margin-right: var(--space-2);
    --margin-bottom: var(--space-2);
    --margin-left: var(--space-2)
  }

  .sm\:rt-r-m-2,
  .sm\:rt-r-m-3 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-m-3 {
    --margin-top: var(--space-3);
    --margin-right: var(--space-3);
    --margin-bottom: var(--space-3);
    --margin-left: var(--space-3)
  }

  .sm\:rt-r-m-4 {
    --margin-top: var(--space-4);
    --margin-right: var(--space-4);
    --margin-bottom: var(--space-4);
    --margin-left: var(--space-4)
  }

  .sm\:rt-r-m-4,
  .sm\:rt-r-m-5 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-m-5 {
    --margin-top: var(--space-5);
    --margin-right: var(--space-5);
    --margin-bottom: var(--space-5);
    --margin-left: var(--space-5)
  }

  .sm\:rt-r-m-6 {
    --margin-top: var(--space-6);
    --margin-right: var(--space-6);
    --margin-bottom: var(--space-6);
    --margin-left: var(--space-6)
  }

  .sm\:rt-r-m-6,
  .sm\:rt-r-m-7 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-m-7 {
    --margin-top: var(--space-7);
    --margin-right: var(--space-7);
    --margin-bottom: var(--space-7);
    --margin-left: var(--space-7)
  }

  .sm\:rt-r-m-8 {
    --margin-top: var(--space-8);
    --margin-right: var(--space-8);
    --margin-bottom: var(--space-8);
    --margin-left: var(--space-8)
  }

  .sm\:rt-r-m-8,
  .sm\:rt-r-m-9 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-m-9 {
    --margin-top: var(--space-9);
    --margin-right: var(--space-9);
    --margin-bottom: var(--space-9);
    --margin-left: var(--space-9)
  }

  .sm\:-rt-r-m-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1));
    --margin-left: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-m-1,
  .sm\:-rt-r-m-2 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-m-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2));
    --margin-left: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-m-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3));
    --margin-left: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-m-3,
  .sm\:-rt-r-m-4 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-m-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4));
    --margin-left: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-m-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5));
    --margin-left: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-m-5,
  .sm\:-rt-r-m-6 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-m-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6));
    --margin-left: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-m-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7));
    --margin-left: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-m-7,
  .sm\:-rt-r-m-8 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-m-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8));
    --margin-left: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-m-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    --margin-left: calc(-1 * var(--space-9));
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-mx-auto {
    margin-left: auto;
    margin-right: auto
  }

  .sm\:rt-r-mx-0 {
    --margin-left: 0px;
    --margin-right: 0px
  }

  .sm\:rt-r-mx-0,
  .sm\:rt-r-mx-1 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mx-1 {
    --margin-left: var(--space-1);
    --margin-right: var(--space-1)
  }

  .sm\:rt-r-mx-2 {
    --margin-left: var(--space-2);
    --margin-right: var(--space-2)
  }

  .sm\:rt-r-mx-2,
  .sm\:rt-r-mx-3 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mx-3 {
    --margin-left: var(--space-3);
    --margin-right: var(--space-3)
  }

  .sm\:rt-r-mx-4 {
    --margin-left: var(--space-4);
    --margin-right: var(--space-4)
  }

  .sm\:rt-r-mx-4,
  .sm\:rt-r-mx-5 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mx-5 {
    --margin-left: var(--space-5);
    --margin-right: var(--space-5)
  }

  .sm\:rt-r-mx-6 {
    --margin-left: var(--space-6);
    --margin-right: var(--space-6)
  }

  .sm\:rt-r-mx-6,
  .sm\:rt-r-mx-7 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mx-7 {
    --margin-left: var(--space-7);
    --margin-right: var(--space-7)
  }

  .sm\:rt-r-mx-8 {
    --margin-left: var(--space-8);
    --margin-right: var(--space-8)
  }

  .sm\:rt-r-mx-8,
  .sm\:rt-r-mx-9 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mx-9 {
    --margin-left: var(--space-9);
    --margin-right: var(--space-9)
  }

  .sm\:-rt-r-mx-1 {
    --margin-left: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-mx-1,
  .sm\:-rt-r-mx-2 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mx-2 {
    --margin-left: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-mx-3 {
    --margin-left: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-mx-3,
  .sm\:-rt-r-mx-4 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mx-4 {
    --margin-left: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-mx-5 {
    --margin-left: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-mx-5,
  .sm\:-rt-r-mx-6 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mx-6 {
    --margin-left: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-mx-7 {
    --margin-left: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-mx-7,
  .sm\:-rt-r-mx-8 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mx-8 {
    --margin-left: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-mx-9 {
    --margin-left: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-my-auto {
    margin-top: auto;
    margin-bottom: auto
  }

  .sm\:rt-r-my-0 {
    --margin-top: 0px;
    --margin-bottom: 0px
  }

  .sm\:rt-r-my-0,
  .sm\:rt-r-my-1 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-my-1 {
    --margin-top: var(--space-1);
    --margin-bottom: var(--space-1)
  }

  .sm\:rt-r-my-2 {
    --margin-top: var(--space-2);
    --margin-bottom: var(--space-2)
  }

  .sm\:rt-r-my-2,
  .sm\:rt-r-my-3 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-my-3 {
    --margin-top: var(--space-3);
    --margin-bottom: var(--space-3)
  }

  .sm\:rt-r-my-4 {
    --margin-top: var(--space-4);
    --margin-bottom: var(--space-4)
  }

  .sm\:rt-r-my-4,
  .sm\:rt-r-my-5 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-my-5 {
    --margin-top: var(--space-5);
    --margin-bottom: var(--space-5)
  }

  .sm\:rt-r-my-6 {
    --margin-top: var(--space-6);
    --margin-bottom: var(--space-6)
  }

  .sm\:rt-r-my-6,
  .sm\:rt-r-my-7 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-my-7 {
    --margin-top: var(--space-7);
    --margin-bottom: var(--space-7)
  }

  .sm\:rt-r-my-8 {
    --margin-top: var(--space-8);
    --margin-bottom: var(--space-8)
  }

  .sm\:rt-r-my-8,
  .sm\:rt-r-my-9 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-my-9 {
    --margin-top: var(--space-9);
    --margin-bottom: var(--space-9)
  }

  .sm\:-rt-r-my-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-my-1,
  .sm\:-rt-r-my-2 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-my-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-my-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-my-3,
  .sm\:-rt-r-my-4 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-my-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-my-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-my-5,
  .sm\:-rt-r-my-6 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-my-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-my-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-my-7,
  .sm\:-rt-r-my-8 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-my-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-my-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-mt-auto {
    margin-top: auto
  }

  .sm\:rt-r-mt-0 {
    --margin-top: 0px
  }

  .sm\:rt-r-mt-0,
  .sm\:rt-r-mt-1 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:rt-r-mt-1 {
    --margin-top: var(--space-1)
  }

  .sm\:rt-r-mt-2 {
    --margin-top: var(--space-2)
  }

  .sm\:rt-r-mt-2,
  .sm\:rt-r-mt-3 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:rt-r-mt-3 {
    --margin-top: var(--space-3)
  }

  .sm\:rt-r-mt-4 {
    --margin-top: var(--space-4)
  }

  .sm\:rt-r-mt-4,
  .sm\:rt-r-mt-5 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:rt-r-mt-5 {
    --margin-top: var(--space-5)
  }

  .sm\:rt-r-mt-6 {
    --margin-top: var(--space-6)
  }

  .sm\:rt-r-mt-6,
  .sm\:rt-r-mt-7 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:rt-r-mt-7 {
    --margin-top: var(--space-7)
  }

  .sm\:rt-r-mt-8 {
    --margin-top: var(--space-8)
  }

  .sm\:rt-r-mt-8,
  .sm\:rt-r-mt-9 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:rt-r-mt-9 {
    --margin-top: var(--space-9)
  }

  .sm\:-rt-r-mt-1 {
    --margin-top: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-mt-1,
  .sm\:-rt-r-mt-2 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:-rt-r-mt-2 {
    --margin-top: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-mt-3 {
    --margin-top: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-mt-3,
  .sm\:-rt-r-mt-4 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:-rt-r-mt-4 {
    --margin-top: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-mt-5 {
    --margin-top: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-mt-5,
  .sm\:-rt-r-mt-6 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:-rt-r-mt-6 {
    --margin-top: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-mt-7 {
    --margin-top: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-mt-7,
  .sm\:-rt-r-mt-8 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:-rt-r-mt-8 {
    --margin-top: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-mt-9 {
    --margin-top: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .sm\:rt-r-mr-auto {
    margin-right: auto
  }

  .sm\:rt-r-mr-0 {
    --margin-right: 0px
  }

  .sm\:rt-r-mr-0,
  .sm\:rt-r-mr-1 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mr-1 {
    --margin-right: var(--space-1)
  }

  .sm\:rt-r-mr-2 {
    --margin-right: var(--space-2)
  }

  .sm\:rt-r-mr-2,
  .sm\:rt-r-mr-3 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mr-3 {
    --margin-right: var(--space-3)
  }

  .sm\:rt-r-mr-4 {
    --margin-right: var(--space-4)
  }

  .sm\:rt-r-mr-4,
  .sm\:rt-r-mr-5 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mr-5 {
    --margin-right: var(--space-5)
  }

  .sm\:rt-r-mr-6 {
    --margin-right: var(--space-6)
  }

  .sm\:rt-r-mr-6,
  .sm\:rt-r-mr-7 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mr-7 {
    --margin-right: var(--space-7)
  }

  .sm\:rt-r-mr-8 {
    --margin-right: var(--space-8)
  }

  .sm\:rt-r-mr-8,
  .sm\:rt-r-mr-9 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mr-9 {
    --margin-right: var(--space-9)
  }

  .sm\:-rt-r-mr-1 {
    --margin-right: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-mr-1,
  .sm\:-rt-r-mr-2 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mr-2 {
    --margin-right: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-mr-3 {
    --margin-right: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-mr-3,
  .sm\:-rt-r-mr-4 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mr-4 {
    --margin-right: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-mr-5 {
    --margin-right: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-mr-5,
  .sm\:-rt-r-mr-6 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mr-6 {
    --margin-right: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-mr-7 {
    --margin-right: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-mr-7,
  .sm\:-rt-r-mr-8 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:-rt-r-mr-8 {
    --margin-right: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-mr-9 {
    --margin-right: calc(-1 * var(--space-9));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .sm\:rt-r-mb-auto {
    margin-bottom: auto
  }

  .sm\:rt-r-mb-0 {
    --margin-bottom: 0px
  }

  .sm\:rt-r-mb-0,
  .sm\:rt-r-mb-1 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-mb-1 {
    --margin-bottom: var(--space-1)
  }

  .sm\:rt-r-mb-2 {
    --margin-bottom: var(--space-2)
  }

  .sm\:rt-r-mb-2,
  .sm\:rt-r-mb-3 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-mb-3 {
    --margin-bottom: var(--space-3)
  }

  .sm\:rt-r-mb-4 {
    --margin-bottom: var(--space-4)
  }

  .sm\:rt-r-mb-4,
  .sm\:rt-r-mb-5 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-mb-5 {
    --margin-bottom: var(--space-5)
  }

  .sm\:rt-r-mb-6 {
    --margin-bottom: var(--space-6)
  }

  .sm\:rt-r-mb-6,
  .sm\:rt-r-mb-7 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-mb-7 {
    --margin-bottom: var(--space-7)
  }

  .sm\:rt-r-mb-8 {
    --margin-bottom: var(--space-8)
  }

  .sm\:rt-r-mb-8,
  .sm\:rt-r-mb-9 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-mb-9 {
    --margin-bottom: var(--space-9)
  }

  .sm\:-rt-r-mb-1 {
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-mb-1,
  .sm\:-rt-r-mb-2 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-mb-2 {
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-mb-3 {
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-mb-3,
  .sm\:-rt-r-mb-4 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-mb-4 {
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-mb-5 {
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-mb-5,
  .sm\:-rt-r-mb-6 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-mb-6 {
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-mb-7 {
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-mb-7,
  .sm\:-rt-r-mb-8 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:-rt-r-mb-8 {
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-mb-9 {
    --margin-bottom: calc(-1 * var(--space-9));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .sm\:rt-r-ml-auto {
    margin-left: auto
  }

  .sm\:rt-r-ml-0 {
    --margin-left: 0px
  }

  .sm\:rt-r-ml-0,
  .sm\:rt-r-ml-1 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-ml-1 {
    --margin-left: var(--space-1)
  }

  .sm\:rt-r-ml-2 {
    --margin-left: var(--space-2)
  }

  .sm\:rt-r-ml-2,
  .sm\:rt-r-ml-3 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-ml-3 {
    --margin-left: var(--space-3)
  }

  .sm\:rt-r-ml-4 {
    --margin-left: var(--space-4)
  }

  .sm\:rt-r-ml-4,
  .sm\:rt-r-ml-5 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-ml-5 {
    --margin-left: var(--space-5)
  }

  .sm\:rt-r-ml-6 {
    --margin-left: var(--space-6)
  }

  .sm\:rt-r-ml-6,
  .sm\:rt-r-ml-7 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-ml-7 {
    --margin-left: var(--space-7)
  }

  .sm\:rt-r-ml-8 {
    --margin-left: var(--space-8)
  }

  .sm\:rt-r-ml-8,
  .sm\:rt-r-ml-9 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:rt-r-ml-9 {
    --margin-left: var(--space-9)
  }

  .sm\:-rt-r-ml-1 {
    --margin-left: calc(-1 * var(--space-1))
  }

  .sm\:-rt-r-ml-1,
  .sm\:-rt-r-ml-2 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-ml-2 {
    --margin-left: calc(-1 * var(--space-2))
  }

  .sm\:-rt-r-ml-3 {
    --margin-left: calc(-1 * var(--space-3))
  }

  .sm\:-rt-r-ml-3,
  .sm\:-rt-r-ml-4 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-ml-4 {
    --margin-left: calc(-1 * var(--space-4))
  }

  .sm\:-rt-r-ml-5 {
    --margin-left: calc(-1 * var(--space-5))
  }

  .sm\:-rt-r-ml-5,
  .sm\:-rt-r-ml-6 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-ml-6 {
    --margin-left: calc(-1 * var(--space-6))
  }

  .sm\:-rt-r-ml-7 {
    --margin-left: calc(-1 * var(--space-7))
  }

  .sm\:-rt-r-ml-7,
  .sm\:-rt-r-ml-8 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .sm\:-rt-r-ml-8 {
    --margin-left: calc(-1 * var(--space-8))
  }

  .sm\:-rt-r-ml-9 {
    --margin-left: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left))
  }
}

@media (min-width:1024px) {
  .md\:rt-r-m-auto {
    margin: auto
  }

  .md\:rt-r-m-0 {
    --margin-top: 0px;
    --margin-right: 0px;
    --margin-bottom: 0px;
    --margin-left: 0px
  }

  .md\:rt-r-m-0,
  .md\:rt-r-m-1 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-m-1 {
    --margin-top: var(--space-1);
    --margin-right: var(--space-1);
    --margin-bottom: var(--space-1);
    --margin-left: var(--space-1)
  }

  .md\:rt-r-m-2 {
    --margin-top: var(--space-2);
    --margin-right: var(--space-2);
    --margin-bottom: var(--space-2);
    --margin-left: var(--space-2)
  }

  .md\:rt-r-m-2,
  .md\:rt-r-m-3 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-m-3 {
    --margin-top: var(--space-3);
    --margin-right: var(--space-3);
    --margin-bottom: var(--space-3);
    --margin-left: var(--space-3)
  }

  .md\:rt-r-m-4 {
    --margin-top: var(--space-4);
    --margin-right: var(--space-4);
    --margin-bottom: var(--space-4);
    --margin-left: var(--space-4)
  }

  .md\:rt-r-m-4,
  .md\:rt-r-m-5 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-m-5 {
    --margin-top: var(--space-5);
    --margin-right: var(--space-5);
    --margin-bottom: var(--space-5);
    --margin-left: var(--space-5)
  }

  .md\:rt-r-m-6 {
    --margin-top: var(--space-6);
    --margin-right: var(--space-6);
    --margin-bottom: var(--space-6);
    --margin-left: var(--space-6)
  }

  .md\:rt-r-m-6,
  .md\:rt-r-m-7 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-m-7 {
    --margin-top: var(--space-7);
    --margin-right: var(--space-7);
    --margin-bottom: var(--space-7);
    --margin-left: var(--space-7)
  }

  .md\:rt-r-m-8 {
    --margin-top: var(--space-8);
    --margin-right: var(--space-8);
    --margin-bottom: var(--space-8);
    --margin-left: var(--space-8)
  }

  .md\:rt-r-m-8,
  .md\:rt-r-m-9 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-m-9 {
    --margin-top: var(--space-9);
    --margin-right: var(--space-9);
    --margin-bottom: var(--space-9);
    --margin-left: var(--space-9)
  }

  .md\:-rt-r-m-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1));
    --margin-left: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-m-1,
  .md\:-rt-r-m-2 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-m-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2));
    --margin-left: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-m-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3));
    --margin-left: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-m-3,
  .md\:-rt-r-m-4 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-m-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4));
    --margin-left: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-m-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5));
    --margin-left: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-m-5,
  .md\:-rt-r-m-6 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-m-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6));
    --margin-left: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-m-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7));
    --margin-left: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-m-7,
  .md\:-rt-r-m-8 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-m-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8));
    --margin-left: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-m-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    --margin-left: calc(-1 * var(--space-9));
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-mx-auto {
    margin-left: auto;
    margin-right: auto
  }

  .md\:rt-r-mx-0 {
    --margin-left: 0px;
    --margin-right: 0px
  }

  .md\:rt-r-mx-0,
  .md\:rt-r-mx-1 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mx-1 {
    --margin-left: var(--space-1);
    --margin-right: var(--space-1)
  }

  .md\:rt-r-mx-2 {
    --margin-left: var(--space-2);
    --margin-right: var(--space-2)
  }

  .md\:rt-r-mx-2,
  .md\:rt-r-mx-3 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mx-3 {
    --margin-left: var(--space-3);
    --margin-right: var(--space-3)
  }

  .md\:rt-r-mx-4 {
    --margin-left: var(--space-4);
    --margin-right: var(--space-4)
  }

  .md\:rt-r-mx-4,
  .md\:rt-r-mx-5 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mx-5 {
    --margin-left: var(--space-5);
    --margin-right: var(--space-5)
  }

  .md\:rt-r-mx-6 {
    --margin-left: var(--space-6);
    --margin-right: var(--space-6)
  }

  .md\:rt-r-mx-6,
  .md\:rt-r-mx-7 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mx-7 {
    --margin-left: var(--space-7);
    --margin-right: var(--space-7)
  }

  .md\:rt-r-mx-8 {
    --margin-left: var(--space-8);
    --margin-right: var(--space-8)
  }

  .md\:rt-r-mx-8,
  .md\:rt-r-mx-9 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mx-9 {
    --margin-left: var(--space-9);
    --margin-right: var(--space-9)
  }

  .md\:-rt-r-mx-1 {
    --margin-left: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-mx-1,
  .md\:-rt-r-mx-2 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mx-2 {
    --margin-left: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-mx-3 {
    --margin-left: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-mx-3,
  .md\:-rt-r-mx-4 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mx-4 {
    --margin-left: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-mx-5 {
    --margin-left: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-mx-5,
  .md\:-rt-r-mx-6 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mx-6 {
    --margin-left: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-mx-7 {
    --margin-left: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-mx-7,
  .md\:-rt-r-mx-8 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mx-8 {
    --margin-left: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-mx-9 {
    --margin-left: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-my-auto {
    margin-top: auto;
    margin-bottom: auto
  }

  .md\:rt-r-my-0 {
    --margin-top: 0px;
    --margin-bottom: 0px
  }

  .md\:rt-r-my-0,
  .md\:rt-r-my-1 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-my-1 {
    --margin-top: var(--space-1);
    --margin-bottom: var(--space-1)
  }

  .md\:rt-r-my-2 {
    --margin-top: var(--space-2);
    --margin-bottom: var(--space-2)
  }

  .md\:rt-r-my-2,
  .md\:rt-r-my-3 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-my-3 {
    --margin-top: var(--space-3);
    --margin-bottom: var(--space-3)
  }

  .md\:rt-r-my-4 {
    --margin-top: var(--space-4);
    --margin-bottom: var(--space-4)
  }

  .md\:rt-r-my-4,
  .md\:rt-r-my-5 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-my-5 {
    --margin-top: var(--space-5);
    --margin-bottom: var(--space-5)
  }

  .md\:rt-r-my-6 {
    --margin-top: var(--space-6);
    --margin-bottom: var(--space-6)
  }

  .md\:rt-r-my-6,
  .md\:rt-r-my-7 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-my-7 {
    --margin-top: var(--space-7);
    --margin-bottom: var(--space-7)
  }

  .md\:rt-r-my-8 {
    --margin-top: var(--space-8);
    --margin-bottom: var(--space-8)
  }

  .md\:rt-r-my-8,
  .md\:rt-r-my-9 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-my-9 {
    --margin-top: var(--space-9);
    --margin-bottom: var(--space-9)
  }

  .md\:-rt-r-my-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-my-1,
  .md\:-rt-r-my-2 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-my-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-my-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-my-3,
  .md\:-rt-r-my-4 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-my-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-my-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-my-5,
  .md\:-rt-r-my-6 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-my-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-my-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-my-7,
  .md\:-rt-r-my-8 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-my-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-my-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-mt-auto {
    margin-top: auto
  }

  .md\:rt-r-mt-0 {
    --margin-top: 0px
  }

  .md\:rt-r-mt-0,
  .md\:rt-r-mt-1 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:rt-r-mt-1 {
    --margin-top: var(--space-1)
  }

  .md\:rt-r-mt-2 {
    --margin-top: var(--space-2)
  }

  .md\:rt-r-mt-2,
  .md\:rt-r-mt-3 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:rt-r-mt-3 {
    --margin-top: var(--space-3)
  }

  .md\:rt-r-mt-4 {
    --margin-top: var(--space-4)
  }

  .md\:rt-r-mt-4,
  .md\:rt-r-mt-5 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:rt-r-mt-5 {
    --margin-top: var(--space-5)
  }

  .md\:rt-r-mt-6 {
    --margin-top: var(--space-6)
  }

  .md\:rt-r-mt-6,
  .md\:rt-r-mt-7 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:rt-r-mt-7 {
    --margin-top: var(--space-7)
  }

  .md\:rt-r-mt-8 {
    --margin-top: var(--space-8)
  }

  .md\:rt-r-mt-8,
  .md\:rt-r-mt-9 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:rt-r-mt-9 {
    --margin-top: var(--space-9)
  }

  .md\:-rt-r-mt-1 {
    --margin-top: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-mt-1,
  .md\:-rt-r-mt-2 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:-rt-r-mt-2 {
    --margin-top: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-mt-3 {
    --margin-top: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-mt-3,
  .md\:-rt-r-mt-4 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:-rt-r-mt-4 {
    --margin-top: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-mt-5 {
    --margin-top: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-mt-5,
  .md\:-rt-r-mt-6 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:-rt-r-mt-6 {
    --margin-top: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-mt-7 {
    --margin-top: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-mt-7,
  .md\:-rt-r-mt-8 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:-rt-r-mt-8 {
    --margin-top: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-mt-9 {
    --margin-top: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .md\:rt-r-mr-auto {
    margin-right: auto
  }

  .md\:rt-r-mr-0 {
    --margin-right: 0px
  }

  .md\:rt-r-mr-0,
  .md\:rt-r-mr-1 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mr-1 {
    --margin-right: var(--space-1)
  }

  .md\:rt-r-mr-2 {
    --margin-right: var(--space-2)
  }

  .md\:rt-r-mr-2,
  .md\:rt-r-mr-3 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mr-3 {
    --margin-right: var(--space-3)
  }

  .md\:rt-r-mr-4 {
    --margin-right: var(--space-4)
  }

  .md\:rt-r-mr-4,
  .md\:rt-r-mr-5 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mr-5 {
    --margin-right: var(--space-5)
  }

  .md\:rt-r-mr-6 {
    --margin-right: var(--space-6)
  }

  .md\:rt-r-mr-6,
  .md\:rt-r-mr-7 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mr-7 {
    --margin-right: var(--space-7)
  }

  .md\:rt-r-mr-8 {
    --margin-right: var(--space-8)
  }

  .md\:rt-r-mr-8,
  .md\:rt-r-mr-9 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mr-9 {
    --margin-right: var(--space-9)
  }

  .md\:-rt-r-mr-1 {
    --margin-right: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-mr-1,
  .md\:-rt-r-mr-2 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mr-2 {
    --margin-right: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-mr-3 {
    --margin-right: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-mr-3,
  .md\:-rt-r-mr-4 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mr-4 {
    --margin-right: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-mr-5 {
    --margin-right: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-mr-5,
  .md\:-rt-r-mr-6 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mr-6 {
    --margin-right: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-mr-7 {
    --margin-right: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-mr-7,
  .md\:-rt-r-mr-8 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:-rt-r-mr-8 {
    --margin-right: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-mr-9 {
    --margin-right: calc(-1 * var(--space-9));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .md\:rt-r-mb-auto {
    margin-bottom: auto
  }

  .md\:rt-r-mb-0 {
    --margin-bottom: 0px
  }

  .md\:rt-r-mb-0,
  .md\:rt-r-mb-1 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-mb-1 {
    --margin-bottom: var(--space-1)
  }

  .md\:rt-r-mb-2 {
    --margin-bottom: var(--space-2)
  }

  .md\:rt-r-mb-2,
  .md\:rt-r-mb-3 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-mb-3 {
    --margin-bottom: var(--space-3)
  }

  .md\:rt-r-mb-4 {
    --margin-bottom: var(--space-4)
  }

  .md\:rt-r-mb-4,
  .md\:rt-r-mb-5 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-mb-5 {
    --margin-bottom: var(--space-5)
  }

  .md\:rt-r-mb-6 {
    --margin-bottom: var(--space-6)
  }

  .md\:rt-r-mb-6,
  .md\:rt-r-mb-7 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-mb-7 {
    --margin-bottom: var(--space-7)
  }

  .md\:rt-r-mb-8 {
    --margin-bottom: var(--space-8)
  }

  .md\:rt-r-mb-8,
  .md\:rt-r-mb-9 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-mb-9 {
    --margin-bottom: var(--space-9)
  }

  .md\:-rt-r-mb-1 {
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-mb-1,
  .md\:-rt-r-mb-2 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-mb-2 {
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-mb-3 {
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-mb-3,
  .md\:-rt-r-mb-4 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-mb-4 {
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-mb-5 {
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-mb-5,
  .md\:-rt-r-mb-6 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-mb-6 {
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-mb-7 {
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-mb-7,
  .md\:-rt-r-mb-8 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:-rt-r-mb-8 {
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-mb-9 {
    --margin-bottom: calc(-1 * var(--space-9));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .md\:rt-r-ml-auto {
    margin-left: auto
  }

  .md\:rt-r-ml-0 {
    --margin-left: 0px
  }

  .md\:rt-r-ml-0,
  .md\:rt-r-ml-1 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-ml-1 {
    --margin-left: var(--space-1)
  }

  .md\:rt-r-ml-2 {
    --margin-left: var(--space-2)
  }

  .md\:rt-r-ml-2,
  .md\:rt-r-ml-3 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-ml-3 {
    --margin-left: var(--space-3)
  }

  .md\:rt-r-ml-4 {
    --margin-left: var(--space-4)
  }

  .md\:rt-r-ml-4,
  .md\:rt-r-ml-5 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-ml-5 {
    --margin-left: var(--space-5)
  }

  .md\:rt-r-ml-6 {
    --margin-left: var(--space-6)
  }

  .md\:rt-r-ml-6,
  .md\:rt-r-ml-7 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-ml-7 {
    --margin-left: var(--space-7)
  }

  .md\:rt-r-ml-8 {
    --margin-left: var(--space-8)
  }

  .md\:rt-r-ml-8,
  .md\:rt-r-ml-9 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:rt-r-ml-9 {
    --margin-left: var(--space-9)
  }

  .md\:-rt-r-ml-1 {
    --margin-left: calc(-1 * var(--space-1))
  }

  .md\:-rt-r-ml-1,
  .md\:-rt-r-ml-2 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-ml-2 {
    --margin-left: calc(-1 * var(--space-2))
  }

  .md\:-rt-r-ml-3 {
    --margin-left: calc(-1 * var(--space-3))
  }

  .md\:-rt-r-ml-3,
  .md\:-rt-r-ml-4 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-ml-4 {
    --margin-left: calc(-1 * var(--space-4))
  }

  .md\:-rt-r-ml-5 {
    --margin-left: calc(-1 * var(--space-5))
  }

  .md\:-rt-r-ml-5,
  .md\:-rt-r-ml-6 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-ml-6 {
    --margin-left: calc(-1 * var(--space-6))
  }

  .md\:-rt-r-ml-7 {
    --margin-left: calc(-1 * var(--space-7))
  }

  .md\:-rt-r-ml-7,
  .md\:-rt-r-ml-8 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .md\:-rt-r-ml-8 {
    --margin-left: calc(-1 * var(--space-8))
  }

  .md\:-rt-r-ml-9 {
    --margin-left: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left))
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-m-auto {
    margin: auto
  }

  .lg\:rt-r-m-0 {
    --margin-top: 0px;
    --margin-right: 0px;
    --margin-bottom: 0px;
    --margin-left: 0px
  }

  .lg\:rt-r-m-0,
  .lg\:rt-r-m-1 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-m-1 {
    --margin-top: var(--space-1);
    --margin-right: var(--space-1);
    --margin-bottom: var(--space-1);
    --margin-left: var(--space-1)
  }

  .lg\:rt-r-m-2 {
    --margin-top: var(--space-2);
    --margin-right: var(--space-2);
    --margin-bottom: var(--space-2);
    --margin-left: var(--space-2)
  }

  .lg\:rt-r-m-2,
  .lg\:rt-r-m-3 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-m-3 {
    --margin-top: var(--space-3);
    --margin-right: var(--space-3);
    --margin-bottom: var(--space-3);
    --margin-left: var(--space-3)
  }

  .lg\:rt-r-m-4 {
    --margin-top: var(--space-4);
    --margin-right: var(--space-4);
    --margin-bottom: var(--space-4);
    --margin-left: var(--space-4)
  }

  .lg\:rt-r-m-4,
  .lg\:rt-r-m-5 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-m-5 {
    --margin-top: var(--space-5);
    --margin-right: var(--space-5);
    --margin-bottom: var(--space-5);
    --margin-left: var(--space-5)
  }

  .lg\:rt-r-m-6 {
    --margin-top: var(--space-6);
    --margin-right: var(--space-6);
    --margin-bottom: var(--space-6);
    --margin-left: var(--space-6)
  }

  .lg\:rt-r-m-6,
  .lg\:rt-r-m-7 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-m-7 {
    --margin-top: var(--space-7);
    --margin-right: var(--space-7);
    --margin-bottom: var(--space-7);
    --margin-left: var(--space-7)
  }

  .lg\:rt-r-m-8 {
    --margin-top: var(--space-8);
    --margin-right: var(--space-8);
    --margin-bottom: var(--space-8);
    --margin-left: var(--space-8)
  }

  .lg\:rt-r-m-8,
  .lg\:rt-r-m-9 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-m-9 {
    --margin-top: var(--space-9);
    --margin-right: var(--space-9);
    --margin-bottom: var(--space-9);
    --margin-left: var(--space-9)
  }

  .lg\:-rt-r-m-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1));
    --margin-left: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-m-1,
  .lg\:-rt-r-m-2 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-m-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2));
    --margin-left: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-m-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3));
    --margin-left: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-m-3,
  .lg\:-rt-r-m-4 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-m-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4));
    --margin-left: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-m-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5));
    --margin-left: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-m-5,
  .lg\:-rt-r-m-6 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-m-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6));
    --margin-left: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-m-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7));
    --margin-left: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-m-7,
  .lg\:-rt-r-m-8 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-m-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8));
    --margin-left: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-m-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    --margin-left: calc(-1 * var(--space-9));
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-mx-auto {
    margin-left: auto;
    margin-right: auto
  }

  .lg\:rt-r-mx-0 {
    --margin-left: 0px;
    --margin-right: 0px
  }

  .lg\:rt-r-mx-0,
  .lg\:rt-r-mx-1 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mx-1 {
    --margin-left: var(--space-1);
    --margin-right: var(--space-1)
  }

  .lg\:rt-r-mx-2 {
    --margin-left: var(--space-2);
    --margin-right: var(--space-2)
  }

  .lg\:rt-r-mx-2,
  .lg\:rt-r-mx-3 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mx-3 {
    --margin-left: var(--space-3);
    --margin-right: var(--space-3)
  }

  .lg\:rt-r-mx-4 {
    --margin-left: var(--space-4);
    --margin-right: var(--space-4)
  }

  .lg\:rt-r-mx-4,
  .lg\:rt-r-mx-5 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mx-5 {
    --margin-left: var(--space-5);
    --margin-right: var(--space-5)
  }

  .lg\:rt-r-mx-6 {
    --margin-left: var(--space-6);
    --margin-right: var(--space-6)
  }

  .lg\:rt-r-mx-6,
  .lg\:rt-r-mx-7 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mx-7 {
    --margin-left: var(--space-7);
    --margin-right: var(--space-7)
  }

  .lg\:rt-r-mx-8 {
    --margin-left: var(--space-8);
    --margin-right: var(--space-8)
  }

  .lg\:rt-r-mx-8,
  .lg\:rt-r-mx-9 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mx-9 {
    --margin-left: var(--space-9);
    --margin-right: var(--space-9)
  }

  .lg\:-rt-r-mx-1 {
    --margin-left: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-mx-1,
  .lg\:-rt-r-mx-2 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mx-2 {
    --margin-left: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-mx-3 {
    --margin-left: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-mx-3,
  .lg\:-rt-r-mx-4 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mx-4 {
    --margin-left: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-mx-5 {
    --margin-left: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-mx-5,
  .lg\:-rt-r-mx-6 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mx-6 {
    --margin-left: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-mx-7 {
    --margin-left: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-mx-7,
  .lg\:-rt-r-mx-8 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mx-8 {
    --margin-left: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-mx-9 {
    --margin-left: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-my-auto {
    margin-top: auto;
    margin-bottom: auto
  }

  .lg\:rt-r-my-0 {
    --margin-top: 0px;
    --margin-bottom: 0px
  }

  .lg\:rt-r-my-0,
  .lg\:rt-r-my-1 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-my-1 {
    --margin-top: var(--space-1);
    --margin-bottom: var(--space-1)
  }

  .lg\:rt-r-my-2 {
    --margin-top: var(--space-2);
    --margin-bottom: var(--space-2)
  }

  .lg\:rt-r-my-2,
  .lg\:rt-r-my-3 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-my-3 {
    --margin-top: var(--space-3);
    --margin-bottom: var(--space-3)
  }

  .lg\:rt-r-my-4 {
    --margin-top: var(--space-4);
    --margin-bottom: var(--space-4)
  }

  .lg\:rt-r-my-4,
  .lg\:rt-r-my-5 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-my-5 {
    --margin-top: var(--space-5);
    --margin-bottom: var(--space-5)
  }

  .lg\:rt-r-my-6 {
    --margin-top: var(--space-6);
    --margin-bottom: var(--space-6)
  }

  .lg\:rt-r-my-6,
  .lg\:rt-r-my-7 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-my-7 {
    --margin-top: var(--space-7);
    --margin-bottom: var(--space-7)
  }

  .lg\:rt-r-my-8 {
    --margin-top: var(--space-8);
    --margin-bottom: var(--space-8)
  }

  .lg\:rt-r-my-8,
  .lg\:rt-r-my-9 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-my-9 {
    --margin-top: var(--space-9);
    --margin-bottom: var(--space-9)
  }

  .lg\:-rt-r-my-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-my-1,
  .lg\:-rt-r-my-2 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-my-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-my-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-my-3,
  .lg\:-rt-r-my-4 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-my-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-my-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-my-5,
  .lg\:-rt-r-my-6 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-my-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-my-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-my-7,
  .lg\:-rt-r-my-8 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-my-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-my-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-mt-auto {
    margin-top: auto
  }

  .lg\:rt-r-mt-0 {
    --margin-top: 0px
  }

  .lg\:rt-r-mt-0,
  .lg\:rt-r-mt-1 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:rt-r-mt-1 {
    --margin-top: var(--space-1)
  }

  .lg\:rt-r-mt-2 {
    --margin-top: var(--space-2)
  }

  .lg\:rt-r-mt-2,
  .lg\:rt-r-mt-3 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:rt-r-mt-3 {
    --margin-top: var(--space-3)
  }

  .lg\:rt-r-mt-4 {
    --margin-top: var(--space-4)
  }

  .lg\:rt-r-mt-4,
  .lg\:rt-r-mt-5 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:rt-r-mt-5 {
    --margin-top: var(--space-5)
  }

  .lg\:rt-r-mt-6 {
    --margin-top: var(--space-6)
  }

  .lg\:rt-r-mt-6,
  .lg\:rt-r-mt-7 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:rt-r-mt-7 {
    --margin-top: var(--space-7)
  }

  .lg\:rt-r-mt-8 {
    --margin-top: var(--space-8)
  }

  .lg\:rt-r-mt-8,
  .lg\:rt-r-mt-9 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:rt-r-mt-9 {
    --margin-top: var(--space-9)
  }

  .lg\:-rt-r-mt-1 {
    --margin-top: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-mt-1,
  .lg\:-rt-r-mt-2 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:-rt-r-mt-2 {
    --margin-top: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-mt-3 {
    --margin-top: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-mt-3,
  .lg\:-rt-r-mt-4 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:-rt-r-mt-4 {
    --margin-top: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-mt-5 {
    --margin-top: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-mt-5,
  .lg\:-rt-r-mt-6 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:-rt-r-mt-6 {
    --margin-top: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-mt-7 {
    --margin-top: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-mt-7,
  .lg\:-rt-r-mt-8 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:-rt-r-mt-8 {
    --margin-top: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-mt-9 {
    --margin-top: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .lg\:rt-r-mr-auto {
    margin-right: auto
  }

  .lg\:rt-r-mr-0 {
    --margin-right: 0px
  }

  .lg\:rt-r-mr-0,
  .lg\:rt-r-mr-1 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mr-1 {
    --margin-right: var(--space-1)
  }

  .lg\:rt-r-mr-2 {
    --margin-right: var(--space-2)
  }

  .lg\:rt-r-mr-2,
  .lg\:rt-r-mr-3 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mr-3 {
    --margin-right: var(--space-3)
  }

  .lg\:rt-r-mr-4 {
    --margin-right: var(--space-4)
  }

  .lg\:rt-r-mr-4,
  .lg\:rt-r-mr-5 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mr-5 {
    --margin-right: var(--space-5)
  }

  .lg\:rt-r-mr-6 {
    --margin-right: var(--space-6)
  }

  .lg\:rt-r-mr-6,
  .lg\:rt-r-mr-7 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mr-7 {
    --margin-right: var(--space-7)
  }

  .lg\:rt-r-mr-8 {
    --margin-right: var(--space-8)
  }

  .lg\:rt-r-mr-8,
  .lg\:rt-r-mr-9 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mr-9 {
    --margin-right: var(--space-9)
  }

  .lg\:-rt-r-mr-1 {
    --margin-right: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-mr-1,
  .lg\:-rt-r-mr-2 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mr-2 {
    --margin-right: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-mr-3 {
    --margin-right: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-mr-3,
  .lg\:-rt-r-mr-4 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mr-4 {
    --margin-right: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-mr-5 {
    --margin-right: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-mr-5,
  .lg\:-rt-r-mr-6 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mr-6 {
    --margin-right: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-mr-7 {
    --margin-right: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-mr-7,
  .lg\:-rt-r-mr-8 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:-rt-r-mr-8 {
    --margin-right: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-mr-9 {
    --margin-right: calc(-1 * var(--space-9));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .lg\:rt-r-mb-auto {
    margin-bottom: auto
  }

  .lg\:rt-r-mb-0 {
    --margin-bottom: 0px
  }

  .lg\:rt-r-mb-0,
  .lg\:rt-r-mb-1 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-mb-1 {
    --margin-bottom: var(--space-1)
  }

  .lg\:rt-r-mb-2 {
    --margin-bottom: var(--space-2)
  }

  .lg\:rt-r-mb-2,
  .lg\:rt-r-mb-3 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-mb-3 {
    --margin-bottom: var(--space-3)
  }

  .lg\:rt-r-mb-4 {
    --margin-bottom: var(--space-4)
  }

  .lg\:rt-r-mb-4,
  .lg\:rt-r-mb-5 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-mb-5 {
    --margin-bottom: var(--space-5)
  }

  .lg\:rt-r-mb-6 {
    --margin-bottom: var(--space-6)
  }

  .lg\:rt-r-mb-6,
  .lg\:rt-r-mb-7 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-mb-7 {
    --margin-bottom: var(--space-7)
  }

  .lg\:rt-r-mb-8 {
    --margin-bottom: var(--space-8)
  }

  .lg\:rt-r-mb-8,
  .lg\:rt-r-mb-9 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-mb-9 {
    --margin-bottom: var(--space-9)
  }

  .lg\:-rt-r-mb-1 {
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-mb-1,
  .lg\:-rt-r-mb-2 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-mb-2 {
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-mb-3 {
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-mb-3,
  .lg\:-rt-r-mb-4 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-mb-4 {
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-mb-5 {
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-mb-5,
  .lg\:-rt-r-mb-6 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-mb-6 {
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-mb-7 {
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-mb-7,
  .lg\:-rt-r-mb-8 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:-rt-r-mb-8 {
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-mb-9 {
    --margin-bottom: calc(-1 * var(--space-9));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .lg\:rt-r-ml-auto {
    margin-left: auto
  }

  .lg\:rt-r-ml-0 {
    --margin-left: 0px
  }

  .lg\:rt-r-ml-0,
  .lg\:rt-r-ml-1 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-ml-1 {
    --margin-left: var(--space-1)
  }

  .lg\:rt-r-ml-2 {
    --margin-left: var(--space-2)
  }

  .lg\:rt-r-ml-2,
  .lg\:rt-r-ml-3 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-ml-3 {
    --margin-left: var(--space-3)
  }

  .lg\:rt-r-ml-4 {
    --margin-left: var(--space-4)
  }

  .lg\:rt-r-ml-4,
  .lg\:rt-r-ml-5 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-ml-5 {
    --margin-left: var(--space-5)
  }

  .lg\:rt-r-ml-6 {
    --margin-left: var(--space-6)
  }

  .lg\:rt-r-ml-6,
  .lg\:rt-r-ml-7 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-ml-7 {
    --margin-left: var(--space-7)
  }

  .lg\:rt-r-ml-8 {
    --margin-left: var(--space-8)
  }

  .lg\:rt-r-ml-8,
  .lg\:rt-r-ml-9 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:rt-r-ml-9 {
    --margin-left: var(--space-9)
  }

  .lg\:-rt-r-ml-1 {
    --margin-left: calc(-1 * var(--space-1))
  }

  .lg\:-rt-r-ml-1,
  .lg\:-rt-r-ml-2 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-ml-2 {
    --margin-left: calc(-1 * var(--space-2))
  }

  .lg\:-rt-r-ml-3 {
    --margin-left: calc(-1 * var(--space-3))
  }

  .lg\:-rt-r-ml-3,
  .lg\:-rt-r-ml-4 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-ml-4 {
    --margin-left: calc(-1 * var(--space-4))
  }

  .lg\:-rt-r-ml-5 {
    --margin-left: calc(-1 * var(--space-5))
  }

  .lg\:-rt-r-ml-5,
  .lg\:-rt-r-ml-6 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-ml-6 {
    --margin-left: calc(-1 * var(--space-6))
  }

  .lg\:-rt-r-ml-7 {
    --margin-left: calc(-1 * var(--space-7))
  }

  .lg\:-rt-r-ml-7,
  .lg\:-rt-r-ml-8 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .lg\:-rt-r-ml-8 {
    --margin-left: calc(-1 * var(--space-8))
  }

  .lg\:-rt-r-ml-9 {
    --margin-left: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left))
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-m-auto {
    margin: auto
  }

  .xl\:rt-r-m-0 {
    --margin-top: 0px;
    --margin-right: 0px;
    --margin-bottom: 0px;
    --margin-left: 0px
  }

  .xl\:rt-r-m-0,
  .xl\:rt-r-m-1 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-m-1 {
    --margin-top: var(--space-1);
    --margin-right: var(--space-1);
    --margin-bottom: var(--space-1);
    --margin-left: var(--space-1)
  }

  .xl\:rt-r-m-2 {
    --margin-top: var(--space-2);
    --margin-right: var(--space-2);
    --margin-bottom: var(--space-2);
    --margin-left: var(--space-2)
  }

  .xl\:rt-r-m-2,
  .xl\:rt-r-m-3 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-m-3 {
    --margin-top: var(--space-3);
    --margin-right: var(--space-3);
    --margin-bottom: var(--space-3);
    --margin-left: var(--space-3)
  }

  .xl\:rt-r-m-4 {
    --margin-top: var(--space-4);
    --margin-right: var(--space-4);
    --margin-bottom: var(--space-4);
    --margin-left: var(--space-4)
  }

  .xl\:rt-r-m-4,
  .xl\:rt-r-m-5 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-m-5 {
    --margin-top: var(--space-5);
    --margin-right: var(--space-5);
    --margin-bottom: var(--space-5);
    --margin-left: var(--space-5)
  }

  .xl\:rt-r-m-6 {
    --margin-top: var(--space-6);
    --margin-right: var(--space-6);
    --margin-bottom: var(--space-6);
    --margin-left: var(--space-6)
  }

  .xl\:rt-r-m-6,
  .xl\:rt-r-m-7 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-m-7 {
    --margin-top: var(--space-7);
    --margin-right: var(--space-7);
    --margin-bottom: var(--space-7);
    --margin-left: var(--space-7)
  }

  .xl\:rt-r-m-8 {
    --margin-top: var(--space-8);
    --margin-right: var(--space-8);
    --margin-bottom: var(--space-8);
    --margin-left: var(--space-8)
  }

  .xl\:rt-r-m-8,
  .xl\:rt-r-m-9 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-m-9 {
    --margin-top: var(--space-9);
    --margin-right: var(--space-9);
    --margin-bottom: var(--space-9);
    --margin-left: var(--space-9)
  }

  .xl\:-rt-r-m-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1));
    --margin-left: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-m-1,
  .xl\:-rt-r-m-2 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-m-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2));
    --margin-left: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-m-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3));
    --margin-left: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-m-3,
  .xl\:-rt-r-m-4 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-m-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4));
    --margin-left: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-m-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5));
    --margin-left: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-m-5,
  .xl\:-rt-r-m-6 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-m-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6));
    --margin-left: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-m-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7));
    --margin-left: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-m-7,
  .xl\:-rt-r-m-8 {
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-m-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8));
    --margin-left: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-m-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    --margin-left: calc(-1 * var(--space-9));
    margin: var(--margin-top-override, var(--margin-top)) var(--margin-right-override, var(--margin-right)) var(--margin-bottom-override, var(--margin-bottom)) var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-mx-auto {
    margin-left: auto;
    margin-right: auto
  }

  .xl\:rt-r-mx-0 {
    --margin-left: 0px;
    --margin-right: 0px
  }

  .xl\:rt-r-mx-0,
  .xl\:rt-r-mx-1 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mx-1 {
    --margin-left: var(--space-1);
    --margin-right: var(--space-1)
  }

  .xl\:rt-r-mx-2 {
    --margin-left: var(--space-2);
    --margin-right: var(--space-2)
  }

  .xl\:rt-r-mx-2,
  .xl\:rt-r-mx-3 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mx-3 {
    --margin-left: var(--space-3);
    --margin-right: var(--space-3)
  }

  .xl\:rt-r-mx-4 {
    --margin-left: var(--space-4);
    --margin-right: var(--space-4)
  }

  .xl\:rt-r-mx-4,
  .xl\:rt-r-mx-5 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mx-5 {
    --margin-left: var(--space-5);
    --margin-right: var(--space-5)
  }

  .xl\:rt-r-mx-6 {
    --margin-left: var(--space-6);
    --margin-right: var(--space-6)
  }

  .xl\:rt-r-mx-6,
  .xl\:rt-r-mx-7 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mx-7 {
    --margin-left: var(--space-7);
    --margin-right: var(--space-7)
  }

  .xl\:rt-r-mx-8 {
    --margin-left: var(--space-8);
    --margin-right: var(--space-8)
  }

  .xl\:rt-r-mx-8,
  .xl\:rt-r-mx-9 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mx-9 {
    --margin-left: var(--space-9);
    --margin-right: var(--space-9)
  }

  .xl\:-rt-r-mx-1 {
    --margin-left: calc(-1 * var(--space-1));
    --margin-right: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-mx-1,
  .xl\:-rt-r-mx-2 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mx-2 {
    --margin-left: calc(-1 * var(--space-2));
    --margin-right: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-mx-3 {
    --margin-left: calc(-1 * var(--space-3));
    --margin-right: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-mx-3,
  .xl\:-rt-r-mx-4 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mx-4 {
    --margin-left: calc(-1 * var(--space-4));
    --margin-right: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-mx-5 {
    --margin-left: calc(-1 * var(--space-5));
    --margin-right: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-mx-5,
  .xl\:-rt-r-mx-6 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mx-6 {
    --margin-left: calc(-1 * var(--space-6));
    --margin-right: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-mx-7 {
    --margin-left: calc(-1 * var(--space-7));
    --margin-right: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-mx-7,
  .xl\:-rt-r-mx-8 {
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mx-8 {
    --margin-left: calc(-1 * var(--space-8));
    --margin-right: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-mx-9 {
    --margin-left: calc(-1 * var(--space-9));
    --margin-right: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-my-auto {
    margin-top: auto;
    margin-bottom: auto
  }

  .xl\:rt-r-my-0 {
    --margin-top: 0px;
    --margin-bottom: 0px
  }

  .xl\:rt-r-my-0,
  .xl\:rt-r-my-1 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-my-1 {
    --margin-top: var(--space-1);
    --margin-bottom: var(--space-1)
  }

  .xl\:rt-r-my-2 {
    --margin-top: var(--space-2);
    --margin-bottom: var(--space-2)
  }

  .xl\:rt-r-my-2,
  .xl\:rt-r-my-3 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-my-3 {
    --margin-top: var(--space-3);
    --margin-bottom: var(--space-3)
  }

  .xl\:rt-r-my-4 {
    --margin-top: var(--space-4);
    --margin-bottom: var(--space-4)
  }

  .xl\:rt-r-my-4,
  .xl\:rt-r-my-5 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-my-5 {
    --margin-top: var(--space-5);
    --margin-bottom: var(--space-5)
  }

  .xl\:rt-r-my-6 {
    --margin-top: var(--space-6);
    --margin-bottom: var(--space-6)
  }

  .xl\:rt-r-my-6,
  .xl\:rt-r-my-7 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-my-7 {
    --margin-top: var(--space-7);
    --margin-bottom: var(--space-7)
  }

  .xl\:rt-r-my-8 {
    --margin-top: var(--space-8);
    --margin-bottom: var(--space-8)
  }

  .xl\:rt-r-my-8,
  .xl\:rt-r-my-9 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-my-9 {
    --margin-top: var(--space-9);
    --margin-bottom: var(--space-9)
  }

  .xl\:-rt-r-my-1 {
    --margin-top: calc(-1 * var(--space-1));
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-my-1,
  .xl\:-rt-r-my-2 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-my-2 {
    --margin-top: calc(-1 * var(--space-2));
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-my-3 {
    --margin-top: calc(-1 * var(--space-3));
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-my-3,
  .xl\:-rt-r-my-4 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-my-4 {
    --margin-top: calc(-1 * var(--space-4));
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-my-5 {
    --margin-top: calc(-1 * var(--space-5));
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-my-5,
  .xl\:-rt-r-my-6 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-my-6 {
    --margin-top: calc(-1 * var(--space-6));
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-my-7 {
    --margin-top: calc(-1 * var(--space-7));
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-my-7,
  .xl\:-rt-r-my-8 {
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-my-8 {
    --margin-top: calc(-1 * var(--space-8));
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-my-9 {
    --margin-top: calc(-1 * var(--space-9));
    --margin-bottom: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-mt-auto {
    margin-top: auto
  }

  .xl\:rt-r-mt-0 {
    --margin-top: 0px
  }

  .xl\:rt-r-mt-0,
  .xl\:rt-r-mt-1 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:rt-r-mt-1 {
    --margin-top: var(--space-1)
  }

  .xl\:rt-r-mt-2 {
    --margin-top: var(--space-2)
  }

  .xl\:rt-r-mt-2,
  .xl\:rt-r-mt-3 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:rt-r-mt-3 {
    --margin-top: var(--space-3)
  }

  .xl\:rt-r-mt-4 {
    --margin-top: var(--space-4)
  }

  .xl\:rt-r-mt-4,
  .xl\:rt-r-mt-5 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:rt-r-mt-5 {
    --margin-top: var(--space-5)
  }

  .xl\:rt-r-mt-6 {
    --margin-top: var(--space-6)
  }

  .xl\:rt-r-mt-6,
  .xl\:rt-r-mt-7 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:rt-r-mt-7 {
    --margin-top: var(--space-7)
  }

  .xl\:rt-r-mt-8 {
    --margin-top: var(--space-8)
  }

  .xl\:rt-r-mt-8,
  .xl\:rt-r-mt-9 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:rt-r-mt-9 {
    --margin-top: var(--space-9)
  }

  .xl\:-rt-r-mt-1 {
    --margin-top: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-mt-1,
  .xl\:-rt-r-mt-2 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:-rt-r-mt-2 {
    --margin-top: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-mt-3 {
    --margin-top: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-mt-3,
  .xl\:-rt-r-mt-4 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:-rt-r-mt-4 {
    --margin-top: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-mt-5 {
    --margin-top: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-mt-5,
  .xl\:-rt-r-mt-6 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:-rt-r-mt-6 {
    --margin-top: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-mt-7 {
    --margin-top: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-mt-7,
  .xl\:-rt-r-mt-8 {
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:-rt-r-mt-8 {
    --margin-top: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-mt-9 {
    --margin-top: calc(-1 * var(--space-9));
    margin-top: var(--margin-top-override, var(--margin-top))
  }

  .xl\:rt-r-mr-auto {
    margin-right: auto
  }

  .xl\:rt-r-mr-0 {
    --margin-right: 0px
  }

  .xl\:rt-r-mr-0,
  .xl\:rt-r-mr-1 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mr-1 {
    --margin-right: var(--space-1)
  }

  .xl\:rt-r-mr-2 {
    --margin-right: var(--space-2)
  }

  .xl\:rt-r-mr-2,
  .xl\:rt-r-mr-3 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mr-3 {
    --margin-right: var(--space-3)
  }

  .xl\:rt-r-mr-4 {
    --margin-right: var(--space-4)
  }

  .xl\:rt-r-mr-4,
  .xl\:rt-r-mr-5 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mr-5 {
    --margin-right: var(--space-5)
  }

  .xl\:rt-r-mr-6 {
    --margin-right: var(--space-6)
  }

  .xl\:rt-r-mr-6,
  .xl\:rt-r-mr-7 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mr-7 {
    --margin-right: var(--space-7)
  }

  .xl\:rt-r-mr-8 {
    --margin-right: var(--space-8)
  }

  .xl\:rt-r-mr-8,
  .xl\:rt-r-mr-9 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mr-9 {
    --margin-right: var(--space-9)
  }

  .xl\:-rt-r-mr-1 {
    --margin-right: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-mr-1,
  .xl\:-rt-r-mr-2 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mr-2 {
    --margin-right: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-mr-3 {
    --margin-right: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-mr-3,
  .xl\:-rt-r-mr-4 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mr-4 {
    --margin-right: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-mr-5 {
    --margin-right: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-mr-5,
  .xl\:-rt-r-mr-6 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mr-6 {
    --margin-right: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-mr-7 {
    --margin-right: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-mr-7,
  .xl\:-rt-r-mr-8 {
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:-rt-r-mr-8 {
    --margin-right: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-mr-9 {
    --margin-right: calc(-1 * var(--space-9));
    margin-right: var(--margin-right-override, var(--margin-right))
  }

  .xl\:rt-r-mb-auto {
    margin-bottom: auto
  }

  .xl\:rt-r-mb-0 {
    --margin-bottom: 0px
  }

  .xl\:rt-r-mb-0,
  .xl\:rt-r-mb-1 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-mb-1 {
    --margin-bottom: var(--space-1)
  }

  .xl\:rt-r-mb-2 {
    --margin-bottom: var(--space-2)
  }

  .xl\:rt-r-mb-2,
  .xl\:rt-r-mb-3 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-mb-3 {
    --margin-bottom: var(--space-3)
  }

  .xl\:rt-r-mb-4 {
    --margin-bottom: var(--space-4)
  }

  .xl\:rt-r-mb-4,
  .xl\:rt-r-mb-5 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-mb-5 {
    --margin-bottom: var(--space-5)
  }

  .xl\:rt-r-mb-6 {
    --margin-bottom: var(--space-6)
  }

  .xl\:rt-r-mb-6,
  .xl\:rt-r-mb-7 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-mb-7 {
    --margin-bottom: var(--space-7)
  }

  .xl\:rt-r-mb-8 {
    --margin-bottom: var(--space-8)
  }

  .xl\:rt-r-mb-8,
  .xl\:rt-r-mb-9 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-mb-9 {
    --margin-bottom: var(--space-9)
  }

  .xl\:-rt-r-mb-1 {
    --margin-bottom: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-mb-1,
  .xl\:-rt-r-mb-2 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-mb-2 {
    --margin-bottom: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-mb-3 {
    --margin-bottom: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-mb-3,
  .xl\:-rt-r-mb-4 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-mb-4 {
    --margin-bottom: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-mb-5 {
    --margin-bottom: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-mb-5,
  .xl\:-rt-r-mb-6 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-mb-6 {
    --margin-bottom: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-mb-7 {
    --margin-bottom: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-mb-7,
  .xl\:-rt-r-mb-8 {
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:-rt-r-mb-8 {
    --margin-bottom: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-mb-9 {
    --margin-bottom: calc(-1 * var(--space-9));
    margin-bottom: var(--margin-bottom-override, var(--margin-bottom))
  }

  .xl\:rt-r-ml-auto {
    margin-left: auto
  }

  .xl\:rt-r-ml-0 {
    --margin-left: 0px
  }

  .xl\:rt-r-ml-0,
  .xl\:rt-r-ml-1 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-ml-1 {
    --margin-left: var(--space-1)
  }

  .xl\:rt-r-ml-2 {
    --margin-left: var(--space-2)
  }

  .xl\:rt-r-ml-2,
  .xl\:rt-r-ml-3 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-ml-3 {
    --margin-left: var(--space-3)
  }

  .xl\:rt-r-ml-4 {
    --margin-left: var(--space-4)
  }

  .xl\:rt-r-ml-4,
  .xl\:rt-r-ml-5 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-ml-5 {
    --margin-left: var(--space-5)
  }

  .xl\:rt-r-ml-6 {
    --margin-left: var(--space-6)
  }

  .xl\:rt-r-ml-6,
  .xl\:rt-r-ml-7 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-ml-7 {
    --margin-left: var(--space-7)
  }

  .xl\:rt-r-ml-8 {
    --margin-left: var(--space-8)
  }

  .xl\:rt-r-ml-8,
  .xl\:rt-r-ml-9 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:rt-r-ml-9 {
    --margin-left: var(--space-9)
  }

  .xl\:-rt-r-ml-1 {
    --margin-left: calc(-1 * var(--space-1))
  }

  .xl\:-rt-r-ml-1,
  .xl\:-rt-r-ml-2 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-ml-2 {
    --margin-left: calc(-1 * var(--space-2))
  }

  .xl\:-rt-r-ml-3 {
    --margin-left: calc(-1 * var(--space-3))
  }

  .xl\:-rt-r-ml-3,
  .xl\:-rt-r-ml-4 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-ml-4 {
    --margin-left: calc(-1 * var(--space-4))
  }

  .xl\:-rt-r-ml-5 {
    --margin-left: calc(-1 * var(--space-5))
  }

  .xl\:-rt-r-ml-5,
  .xl\:-rt-r-ml-6 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-ml-6 {
    --margin-left: calc(-1 * var(--space-6))
  }

  .xl\:-rt-r-ml-7 {
    --margin-left: calc(-1 * var(--space-7))
  }

  .xl\:-rt-r-ml-7,
  .xl\:-rt-r-ml-8 {
    margin-left: var(--margin-left-override, var(--margin-left))
  }

  .xl\:-rt-r-ml-8 {
    --margin-left: calc(-1 * var(--space-8))
  }

  .xl\:-rt-r-ml-9 {
    --margin-left: calc(-1 * var(--space-9));
    margin-left: var(--margin-left-override, var(--margin-left))
  }
}

@media all {
  .rt-r-p-0 {
    padding: 0
  }

  .rt-r-p-1 {
    padding: var(--space-1)
  }

  .rt-r-p-2 {
    padding: var(--space-2)
  }

  .rt-r-p-3 {
    padding: var(--space-3)
  }

  .rt-r-p-4 {
    padding: var(--space-4)
  }

  .rt-r-p-5 {
    padding: var(--space-5)
  }

  .rt-r-p-6 {
    padding: var(--space-6)
  }

  .rt-r-p-7 {
    padding: var(--space-7)
  }

  .rt-r-p-8 {
    padding: var(--space-8)
  }

  .rt-r-p-9 {
    padding: var(--space-9)
  }

  .rt-r-p-current {
    padding: var(--inset-padding)
  }

  .rt-r-px-0 {
    padding-left: 0;
    padding-right: 0
  }

  .rt-r-px-1 {
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .rt-r-px-2 {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .rt-r-px-3 {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .rt-r-px-4 {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .rt-r-px-5 {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .rt-r-px-6 {
    padding-left: var(--space-6);
    padding-right: var(--space-6)
  }

  .rt-r-px-7 {
    padding-left: var(--space-7);
    padding-right: var(--space-7)
  }

  .rt-r-px-8 {
    padding-left: var(--space-8);
    padding-right: var(--space-8)
  }

  .rt-r-px-9 {
    padding-left: var(--space-9);
    padding-right: var(--space-9)
  }

  .rt-r-px-current {
    padding-left: var(--inset-padding);
    padding-right: var(--inset-padding)
  }

  .rt-r-py-0 {
    padding-top: 0;
    padding-bottom: 0
  }

  .rt-r-py-1 {
    padding-top: var(--space-1);
    padding-bottom: var(--space-1)
  }

  .rt-r-py-2 {
    padding-top: var(--space-2);
    padding-bottom: var(--space-2)
  }

  .rt-r-py-3 {
    padding-top: var(--space-3);
    padding-bottom: var(--space-3)
  }

  .rt-r-py-4 {
    padding-top: var(--space-4);
    padding-bottom: var(--space-4)
  }

  .rt-r-py-5 {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .rt-r-py-6 {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6)
  }

  .rt-r-py-7 {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .rt-r-py-8 {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8)
  }

  .rt-r-py-9 {
    padding-top: var(--space-9);
    padding-bottom: var(--space-9)
  }

  .rt-r-py-current {
    padding-top: var(--inset-padding);
    padding-bottom: var(--inset-padding)
  }

  .rt-r-pt-0 {
    padding-top: 0
  }

  .rt-r-pt-1 {
    padding-top: var(--space-1)
  }

  .rt-r-pt-2 {
    padding-top: var(--space-2)
  }

  .rt-r-pt-3 {
    padding-top: var(--space-3)
  }

  .rt-r-pt-4 {
    padding-top: var(--space-4)
  }

  .rt-r-pt-5 {
    padding-top: var(--space-5)
  }

  .rt-r-pt-6 {
    padding-top: var(--space-6)
  }

  .rt-r-pt-7 {
    padding-top: var(--space-7)
  }

  .rt-r-pt-8 {
    padding-top: var(--space-8)
  }

  .rt-r-pt-9 {
    padding-top: var(--space-9)
  }

  .rt-r-pt-current {
    padding-top: var(--inset-padding)
  }

  .rt-r-pr-0 {
    padding-right: 0
  }

  .rt-r-pr-1 {
    padding-right: var(--space-1)
  }

  .rt-r-pr-2 {
    padding-right: var(--space-2)
  }

  .rt-r-pr-3 {
    padding-right: var(--space-3)
  }

  .rt-r-pr-4 {
    padding-right: var(--space-4)
  }

  .rt-r-pr-5 {
    padding-right: var(--space-5)
  }

  .rt-r-pr-6 {
    padding-right: var(--space-6)
  }

  .rt-r-pr-7 {
    padding-right: var(--space-7)
  }

  .rt-r-pr-8 {
    padding-right: var(--space-8)
  }

  .rt-r-pr-9 {
    padding-right: var(--space-9)
  }

  .rt-r-pr-current {
    padding-right: var(--inset-padding)
  }

  .rt-r-pb-0 {
    padding-bottom: 0
  }

  .rt-r-pb-1 {
    padding-bottom: var(--space-1)
  }

  .rt-r-pb-2 {
    padding-bottom: var(--space-2)
  }

  .rt-r-pb-3 {
    padding-bottom: var(--space-3)
  }

  .rt-r-pb-4 {
    padding-bottom: var(--space-4)
  }

  .rt-r-pb-5 {
    padding-bottom: var(--space-5)
  }

  .rt-r-pb-6 {
    padding-bottom: var(--space-6)
  }

  .rt-r-pb-7 {
    padding-bottom: var(--space-7)
  }

  .rt-r-pb-8 {
    padding-bottom: var(--space-8)
  }

  .rt-r-pb-9 {
    padding-bottom: var(--space-9)
  }

  .rt-r-pb-current {
    padding-bottom: var(--inset-padding)
  }

  .rt-r-pl-0 {
    padding-left: 0
  }

  .rt-r-pl-1 {
    padding-left: var(--space-1)
  }

  .rt-r-pl-2 {
    padding-left: var(--space-2)
  }

  .rt-r-pl-3 {
    padding-left: var(--space-3)
  }

  .rt-r-pl-4 {
    padding-left: var(--space-4)
  }

  .rt-r-pl-5 {
    padding-left: var(--space-5)
  }

  .rt-r-pl-6 {
    padding-left: var(--space-6)
  }

  .rt-r-pl-7 {
    padding-left: var(--space-7)
  }

  .rt-r-pl-8 {
    padding-left: var(--space-8)
  }

  .rt-r-pl-9 {
    padding-left: var(--space-9)
  }

  .rt-r-pl-current {
    padding-left: var(--inset-padding)
  }
}

@media (min-width:520px) {
  .xs\:rt-r-p-0 {
    padding: 0
  }

  .xs\:rt-r-p-1 {
    padding: var(--space-1)
  }

  .xs\:rt-r-p-2 {
    padding: var(--space-2)
  }

  .xs\:rt-r-p-3 {
    padding: var(--space-3)
  }

  .xs\:rt-r-p-4 {
    padding: var(--space-4)
  }

  .xs\:rt-r-p-5 {
    padding: var(--space-5)
  }

  .xs\:rt-r-p-6 {
    padding: var(--space-6)
  }

  .xs\:rt-r-p-7 {
    padding: var(--space-7)
  }

  .xs\:rt-r-p-8 {
    padding: var(--space-8)
  }

  .xs\:rt-r-p-9 {
    padding: var(--space-9)
  }

  .xs\:rt-r-p-current {
    padding: var(--inset-padding)
  }

  .xs\:rt-r-px-0 {
    padding-left: 0;
    padding-right: 0
  }

  .xs\:rt-r-px-1 {
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .xs\:rt-r-px-2 {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .xs\:rt-r-px-3 {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .xs\:rt-r-px-4 {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .xs\:rt-r-px-5 {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .xs\:rt-r-px-6 {
    padding-left: var(--space-6);
    padding-right: var(--space-6)
  }

  .xs\:rt-r-px-7 {
    padding-left: var(--space-7);
    padding-right: var(--space-7)
  }

  .xs\:rt-r-px-8 {
    padding-left: var(--space-8);
    padding-right: var(--space-8)
  }

  .xs\:rt-r-px-9 {
    padding-left: var(--space-9);
    padding-right: var(--space-9)
  }

  .xs\:rt-r-px-current {
    padding-left: var(--inset-padding);
    padding-right: var(--inset-padding)
  }

  .xs\:rt-r-py-0 {
    padding-top: 0;
    padding-bottom: 0
  }

  .xs\:rt-r-py-1 {
    padding-top: var(--space-1);
    padding-bottom: var(--space-1)
  }

  .xs\:rt-r-py-2 {
    padding-top: var(--space-2);
    padding-bottom: var(--space-2)
  }

  .xs\:rt-r-py-3 {
    padding-top: var(--space-3);
    padding-bottom: var(--space-3)
  }

  .xs\:rt-r-py-4 {
    padding-top: var(--space-4);
    padding-bottom: var(--space-4)
  }

  .xs\:rt-r-py-5 {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .xs\:rt-r-py-6 {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6)
  }

  .xs\:rt-r-py-7 {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .xs\:rt-r-py-8 {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8)
  }

  .xs\:rt-r-py-9 {
    padding-top: var(--space-9);
    padding-bottom: var(--space-9)
  }

  .xs\:rt-r-py-current {
    padding-top: var(--inset-padding);
    padding-bottom: var(--inset-padding)
  }

  .xs\:rt-r-pt-0 {
    padding-top: 0
  }

  .xs\:rt-r-pt-1 {
    padding-top: var(--space-1)
  }

  .xs\:rt-r-pt-2 {
    padding-top: var(--space-2)
  }

  .xs\:rt-r-pt-3 {
    padding-top: var(--space-3)
  }

  .xs\:rt-r-pt-4 {
    padding-top: var(--space-4)
  }

  .xs\:rt-r-pt-5 {
    padding-top: var(--space-5)
  }

  .xs\:rt-r-pt-6 {
    padding-top: var(--space-6)
  }

  .xs\:rt-r-pt-7 {
    padding-top: var(--space-7)
  }

  .xs\:rt-r-pt-8 {
    padding-top: var(--space-8)
  }

  .xs\:rt-r-pt-9 {
    padding-top: var(--space-9)
  }

  .xs\:rt-r-pt-current {
    padding-top: var(--inset-padding)
  }

  .xs\:rt-r-pr-0 {
    padding-right: 0
  }

  .xs\:rt-r-pr-1 {
    padding-right: var(--space-1)
  }

  .xs\:rt-r-pr-2 {
    padding-right: var(--space-2)
  }

  .xs\:rt-r-pr-3 {
    padding-right: var(--space-3)
  }

  .xs\:rt-r-pr-4 {
    padding-right: var(--space-4)
  }

  .xs\:rt-r-pr-5 {
    padding-right: var(--space-5)
  }

  .xs\:rt-r-pr-6 {
    padding-right: var(--space-6)
  }

  .xs\:rt-r-pr-7 {
    padding-right: var(--space-7)
  }

  .xs\:rt-r-pr-8 {
    padding-right: var(--space-8)
  }

  .xs\:rt-r-pr-9 {
    padding-right: var(--space-9)
  }

  .xs\:rt-r-pr-current {
    padding-right: var(--inset-padding)
  }

  .xs\:rt-r-pb-0 {
    padding-bottom: 0
  }

  .xs\:rt-r-pb-1 {
    padding-bottom: var(--space-1)
  }

  .xs\:rt-r-pb-2 {
    padding-bottom: var(--space-2)
  }

  .xs\:rt-r-pb-3 {
    padding-bottom: var(--space-3)
  }

  .xs\:rt-r-pb-4 {
    padding-bottom: var(--space-4)
  }

  .xs\:rt-r-pb-5 {
    padding-bottom: var(--space-5)
  }

  .xs\:rt-r-pb-6 {
    padding-bottom: var(--space-6)
  }

  .xs\:rt-r-pb-7 {
    padding-bottom: var(--space-7)
  }

  .xs\:rt-r-pb-8 {
    padding-bottom: var(--space-8)
  }

  .xs\:rt-r-pb-9 {
    padding-bottom: var(--space-9)
  }

  .xs\:rt-r-pb-current {
    padding-bottom: var(--inset-padding)
  }

  .xs\:rt-r-pl-0 {
    padding-left: 0
  }

  .xs\:rt-r-pl-1 {
    padding-left: var(--space-1)
  }

  .xs\:rt-r-pl-2 {
    padding-left: var(--space-2)
  }

  .xs\:rt-r-pl-3 {
    padding-left: var(--space-3)
  }

  .xs\:rt-r-pl-4 {
    padding-left: var(--space-4)
  }

  .xs\:rt-r-pl-5 {
    padding-left: var(--space-5)
  }

  .xs\:rt-r-pl-6 {
    padding-left: var(--space-6)
  }

  .xs\:rt-r-pl-7 {
    padding-left: var(--space-7)
  }

  .xs\:rt-r-pl-8 {
    padding-left: var(--space-8)
  }

  .xs\:rt-r-pl-9 {
    padding-left: var(--space-9)
  }

  .xs\:rt-r-pl-current {
    padding-left: var(--inset-padding)
  }
}

@media (min-width:768px) {
  .sm\:rt-r-p-0 {
    padding: 0
  }

  .sm\:rt-r-p-1 {
    padding: var(--space-1)
  }

  .sm\:rt-r-p-2 {
    padding: var(--space-2)
  }

  .sm\:rt-r-p-3 {
    padding: var(--space-3)
  }

  .sm\:rt-r-p-4 {
    padding: var(--space-4)
  }

  .sm\:rt-r-p-5 {
    padding: var(--space-5)
  }

  .sm\:rt-r-p-6 {
    padding: var(--space-6)
  }

  .sm\:rt-r-p-7 {
    padding: var(--space-7)
  }

  .sm\:rt-r-p-8 {
    padding: var(--space-8)
  }

  .sm\:rt-r-p-9 {
    padding: var(--space-9)
  }

  .sm\:rt-r-p-current {
    padding: var(--inset-padding)
  }

  .sm\:rt-r-px-0 {
    padding-left: 0;
    padding-right: 0
  }

  .sm\:rt-r-px-1 {
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .sm\:rt-r-px-2 {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .sm\:rt-r-px-3 {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .sm\:rt-r-px-4 {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .sm\:rt-r-px-5 {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .sm\:rt-r-px-6 {
    padding-left: var(--space-6);
    padding-right: var(--space-6)
  }

  .sm\:rt-r-px-7 {
    padding-left: var(--space-7);
    padding-right: var(--space-7)
  }

  .sm\:rt-r-px-8 {
    padding-left: var(--space-8);
    padding-right: var(--space-8)
  }

  .sm\:rt-r-px-9 {
    padding-left: var(--space-9);
    padding-right: var(--space-9)
  }

  .sm\:rt-r-px-current {
    padding-left: var(--inset-padding);
    padding-right: var(--inset-padding)
  }

  .sm\:rt-r-py-0 {
    padding-top: 0;
    padding-bottom: 0
  }

  .sm\:rt-r-py-1 {
    padding-top: var(--space-1);
    padding-bottom: var(--space-1)
  }

  .sm\:rt-r-py-2 {
    padding-top: var(--space-2);
    padding-bottom: var(--space-2)
  }

  .sm\:rt-r-py-3 {
    padding-top: var(--space-3);
    padding-bottom: var(--space-3)
  }

  .sm\:rt-r-py-4 {
    padding-top: var(--space-4);
    padding-bottom: var(--space-4)
  }

  .sm\:rt-r-py-5 {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .sm\:rt-r-py-6 {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6)
  }

  .sm\:rt-r-py-7 {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .sm\:rt-r-py-8 {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8)
  }

  .sm\:rt-r-py-9 {
    padding-top: var(--space-9);
    padding-bottom: var(--space-9)
  }

  .sm\:rt-r-py-current {
    padding-top: var(--inset-padding);
    padding-bottom: var(--inset-padding)
  }

  .sm\:rt-r-pt-0 {
    padding-top: 0
  }

  .sm\:rt-r-pt-1 {
    padding-top: var(--space-1)
  }

  .sm\:rt-r-pt-2 {
    padding-top: var(--space-2)
  }

  .sm\:rt-r-pt-3 {
    padding-top: var(--space-3)
  }

  .sm\:rt-r-pt-4 {
    padding-top: var(--space-4)
  }

  .sm\:rt-r-pt-5 {
    padding-top: var(--space-5)
  }

  .sm\:rt-r-pt-6 {
    padding-top: var(--space-6)
  }

  .sm\:rt-r-pt-7 {
    padding-top: var(--space-7)
  }

  .sm\:rt-r-pt-8 {
    padding-top: var(--space-8)
  }

  .sm\:rt-r-pt-9 {
    padding-top: var(--space-9)
  }

  .sm\:rt-r-pt-current {
    padding-top: var(--inset-padding)
  }

  .sm\:rt-r-pr-0 {
    padding-right: 0
  }

  .sm\:rt-r-pr-1 {
    padding-right: var(--space-1)
  }

  .sm\:rt-r-pr-2 {
    padding-right: var(--space-2)
  }

  .sm\:rt-r-pr-3 {
    padding-right: var(--space-3)
  }

  .sm\:rt-r-pr-4 {
    padding-right: var(--space-4)
  }

  .sm\:rt-r-pr-5 {
    padding-right: var(--space-5)
  }

  .sm\:rt-r-pr-6 {
    padding-right: var(--space-6)
  }

  .sm\:rt-r-pr-7 {
    padding-right: var(--space-7)
  }

  .sm\:rt-r-pr-8 {
    padding-right: var(--space-8)
  }

  .sm\:rt-r-pr-9 {
    padding-right: var(--space-9)
  }

  .sm\:rt-r-pr-current {
    padding-right: var(--inset-padding)
  }

  .sm\:rt-r-pb-0 {
    padding-bottom: 0
  }

  .sm\:rt-r-pb-1 {
    padding-bottom: var(--space-1)
  }

  .sm\:rt-r-pb-2 {
    padding-bottom: var(--space-2)
  }

  .sm\:rt-r-pb-3 {
    padding-bottom: var(--space-3)
  }

  .sm\:rt-r-pb-4 {
    padding-bottom: var(--space-4)
  }

  .sm\:rt-r-pb-5 {
    padding-bottom: var(--space-5)
  }

  .sm\:rt-r-pb-6 {
    padding-bottom: var(--space-6)
  }

  .sm\:rt-r-pb-7 {
    padding-bottom: var(--space-7)
  }

  .sm\:rt-r-pb-8 {
    padding-bottom: var(--space-8)
  }

  .sm\:rt-r-pb-9 {
    padding-bottom: var(--space-9)
  }

  .sm\:rt-r-pb-current {
    padding-bottom: var(--inset-padding)
  }

  .sm\:rt-r-pl-0 {
    padding-left: 0
  }

  .sm\:rt-r-pl-1 {
    padding-left: var(--space-1)
  }

  .sm\:rt-r-pl-2 {
    padding-left: var(--space-2)
  }

  .sm\:rt-r-pl-3 {
    padding-left: var(--space-3)
  }

  .sm\:rt-r-pl-4 {
    padding-left: var(--space-4)
  }

  .sm\:rt-r-pl-5 {
    padding-left: var(--space-5)
  }

  .sm\:rt-r-pl-6 {
    padding-left: var(--space-6)
  }

  .sm\:rt-r-pl-7 {
    padding-left: var(--space-7)
  }

  .sm\:rt-r-pl-8 {
    padding-left: var(--space-8)
  }

  .sm\:rt-r-pl-9 {
    padding-left: var(--space-9)
  }

  .sm\:rt-r-pl-current {
    padding-left: var(--inset-padding)
  }
}

@media (min-width:1024px) {
  .md\:rt-r-p-0 {
    padding: 0
  }

  .md\:rt-r-p-1 {
    padding: var(--space-1)
  }

  .md\:rt-r-p-2 {
    padding: var(--space-2)
  }

  .md\:rt-r-p-3 {
    padding: var(--space-3)
  }

  .md\:rt-r-p-4 {
    padding: var(--space-4)
  }

  .md\:rt-r-p-5 {
    padding: var(--space-5)
  }

  .md\:rt-r-p-6 {
    padding: var(--space-6)
  }

  .md\:rt-r-p-7 {
    padding: var(--space-7)
  }

  .md\:rt-r-p-8 {
    padding: var(--space-8)
  }

  .md\:rt-r-p-9 {
    padding: var(--space-9)
  }

  .md\:rt-r-p-current {
    padding: var(--inset-padding)
  }

  .md\:rt-r-px-0 {
    padding-left: 0;
    padding-right: 0
  }

  .md\:rt-r-px-1 {
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .md\:rt-r-px-2 {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .md\:rt-r-px-3 {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .md\:rt-r-px-4 {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .md\:rt-r-px-5 {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .md\:rt-r-px-6 {
    padding-left: var(--space-6);
    padding-right: var(--space-6)
  }

  .md\:rt-r-px-7 {
    padding-left: var(--space-7);
    padding-right: var(--space-7)
  }

  .md\:rt-r-px-8 {
    padding-left: var(--space-8);
    padding-right: var(--space-8)
  }

  .md\:rt-r-px-9 {
    padding-left: var(--space-9);
    padding-right: var(--space-9)
  }

  .md\:rt-r-px-current {
    padding-left: var(--inset-padding);
    padding-right: var(--inset-padding)
  }

  .md\:rt-r-py-0 {
    padding-top: 0;
    padding-bottom: 0
  }

  .md\:rt-r-py-1 {
    padding-top: var(--space-1);
    padding-bottom: var(--space-1)
  }

  .md\:rt-r-py-2 {
    padding-top: var(--space-2);
    padding-bottom: var(--space-2)
  }

  .md\:rt-r-py-3 {
    padding-top: var(--space-3);
    padding-bottom: var(--space-3)
  }

  .md\:rt-r-py-4 {
    padding-top: var(--space-4);
    padding-bottom: var(--space-4)
  }

  .md\:rt-r-py-5 {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .md\:rt-r-py-6 {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6)
  }

  .md\:rt-r-py-7 {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .md\:rt-r-py-8 {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8)
  }

  .md\:rt-r-py-9 {
    padding-top: var(--space-9);
    padding-bottom: var(--space-9)
  }

  .md\:rt-r-py-current {
    padding-top: var(--inset-padding);
    padding-bottom: var(--inset-padding)
  }

  .md\:rt-r-pt-0 {
    padding-top: 0
  }

  .md\:rt-r-pt-1 {
    padding-top: var(--space-1)
  }

  .md\:rt-r-pt-2 {
    padding-top: var(--space-2)
  }

  .md\:rt-r-pt-3 {
    padding-top: var(--space-3)
  }

  .md\:rt-r-pt-4 {
    padding-top: var(--space-4)
  }

  .md\:rt-r-pt-5 {
    padding-top: var(--space-5)
  }

  .md\:rt-r-pt-6 {
    padding-top: var(--space-6)
  }

  .md\:rt-r-pt-7 {
    padding-top: var(--space-7)
  }

  .md\:rt-r-pt-8 {
    padding-top: var(--space-8)
  }

  .md\:rt-r-pt-9 {
    padding-top: var(--space-9)
  }

  .md\:rt-r-pt-current {
    padding-top: var(--inset-padding)
  }

  .md\:rt-r-pr-0 {
    padding-right: 0
  }

  .md\:rt-r-pr-1 {
    padding-right: var(--space-1)
  }

  .md\:rt-r-pr-2 {
    padding-right: var(--space-2)
  }

  .md\:rt-r-pr-3 {
    padding-right: var(--space-3)
  }

  .md\:rt-r-pr-4 {
    padding-right: var(--space-4)
  }

  .md\:rt-r-pr-5 {
    padding-right: var(--space-5)
  }

  .md\:rt-r-pr-6 {
    padding-right: var(--space-6)
  }

  .md\:rt-r-pr-7 {
    padding-right: var(--space-7)
  }

  .md\:rt-r-pr-8 {
    padding-right: var(--space-8)
  }

  .md\:rt-r-pr-9 {
    padding-right: var(--space-9)
  }

  .md\:rt-r-pr-current {
    padding-right: var(--inset-padding)
  }

  .md\:rt-r-pb-0 {
    padding-bottom: 0
  }

  .md\:rt-r-pb-1 {
    padding-bottom: var(--space-1)
  }

  .md\:rt-r-pb-2 {
    padding-bottom: var(--space-2)
  }

  .md\:rt-r-pb-3 {
    padding-bottom: var(--space-3)
  }

  .md\:rt-r-pb-4 {
    padding-bottom: var(--space-4)
  }

  .md\:rt-r-pb-5 {
    padding-bottom: var(--space-5)
  }

  .md\:rt-r-pb-6 {
    padding-bottom: var(--space-6)
  }

  .md\:rt-r-pb-7 {
    padding-bottom: var(--space-7)
  }

  .md\:rt-r-pb-8 {
    padding-bottom: var(--space-8)
  }

  .md\:rt-r-pb-9 {
    padding-bottom: var(--space-9)
  }

  .md\:rt-r-pb-current {
    padding-bottom: var(--inset-padding)
  }

  .md\:rt-r-pl-0 {
    padding-left: 0
  }

  .md\:rt-r-pl-1 {
    padding-left: var(--space-1)
  }

  .md\:rt-r-pl-2 {
    padding-left: var(--space-2)
  }

  .md\:rt-r-pl-3 {
    padding-left: var(--space-3)
  }

  .md\:rt-r-pl-4 {
    padding-left: var(--space-4)
  }

  .md\:rt-r-pl-5 {
    padding-left: var(--space-5)
  }

  .md\:rt-r-pl-6 {
    padding-left: var(--space-6)
  }

  .md\:rt-r-pl-7 {
    padding-left: var(--space-7)
  }

  .md\:rt-r-pl-8 {
    padding-left: var(--space-8)
  }

  .md\:rt-r-pl-9 {
    padding-left: var(--space-9)
  }

  .md\:rt-r-pl-current {
    padding-left: var(--inset-padding)
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-p-0 {
    padding: 0
  }

  .lg\:rt-r-p-1 {
    padding: var(--space-1)
  }

  .lg\:rt-r-p-2 {
    padding: var(--space-2)
  }

  .lg\:rt-r-p-3 {
    padding: var(--space-3)
  }

  .lg\:rt-r-p-4 {
    padding: var(--space-4)
  }

  .lg\:rt-r-p-5 {
    padding: var(--space-5)
  }

  .lg\:rt-r-p-6 {
    padding: var(--space-6)
  }

  .lg\:rt-r-p-7 {
    padding: var(--space-7)
  }

  .lg\:rt-r-p-8 {
    padding: var(--space-8)
  }

  .lg\:rt-r-p-9 {
    padding: var(--space-9)
  }

  .lg\:rt-r-p-current {
    padding: var(--inset-padding)
  }

  .lg\:rt-r-px-0 {
    padding-left: 0;
    padding-right: 0
  }

  .lg\:rt-r-px-1 {
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .lg\:rt-r-px-2 {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .lg\:rt-r-px-3 {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .lg\:rt-r-px-4 {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .lg\:rt-r-px-5 {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .lg\:rt-r-px-6 {
    padding-left: var(--space-6);
    padding-right: var(--space-6)
  }

  .lg\:rt-r-px-7 {
    padding-left: var(--space-7);
    padding-right: var(--space-7)
  }

  .lg\:rt-r-px-8 {
    padding-left: var(--space-8);
    padding-right: var(--space-8)
  }

  .lg\:rt-r-px-9 {
    padding-left: var(--space-9);
    padding-right: var(--space-9)
  }

  .lg\:rt-r-px-current {
    padding-left: var(--inset-padding);
    padding-right: var(--inset-padding)
  }

  .lg\:rt-r-py-0 {
    padding-top: 0;
    padding-bottom: 0
  }

  .lg\:rt-r-py-1 {
    padding-top: var(--space-1);
    padding-bottom: var(--space-1)
  }

  .lg\:rt-r-py-2 {
    padding-top: var(--space-2);
    padding-bottom: var(--space-2)
  }

  .lg\:rt-r-py-3 {
    padding-top: var(--space-3);
    padding-bottom: var(--space-3)
  }

  .lg\:rt-r-py-4 {
    padding-top: var(--space-4);
    padding-bottom: var(--space-4)
  }

  .lg\:rt-r-py-5 {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .lg\:rt-r-py-6 {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6)
  }

  .lg\:rt-r-py-7 {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .lg\:rt-r-py-8 {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8)
  }

  .lg\:rt-r-py-9 {
    padding-top: var(--space-9);
    padding-bottom: var(--space-9)
  }

  .lg\:rt-r-py-current {
    padding-top: var(--inset-padding);
    padding-bottom: var(--inset-padding)
  }

  .lg\:rt-r-pt-0 {
    padding-top: 0
  }

  .lg\:rt-r-pt-1 {
    padding-top: var(--space-1)
  }

  .lg\:rt-r-pt-2 {
    padding-top: var(--space-2)
  }

  .lg\:rt-r-pt-3 {
    padding-top: var(--space-3)
  }

  .lg\:rt-r-pt-4 {
    padding-top: var(--space-4)
  }

  .lg\:rt-r-pt-5 {
    padding-top: var(--space-5)
  }

  .lg\:rt-r-pt-6 {
    padding-top: var(--space-6)
  }

  .lg\:rt-r-pt-7 {
    padding-top: var(--space-7)
  }

  .lg\:rt-r-pt-8 {
    padding-top: var(--space-8)
  }

  .lg\:rt-r-pt-9 {
    padding-top: var(--space-9)
  }

  .lg\:rt-r-pt-current {
    padding-top: var(--inset-padding)
  }

  .lg\:rt-r-pr-0 {
    padding-right: 0
  }

  .lg\:rt-r-pr-1 {
    padding-right: var(--space-1)
  }

  .lg\:rt-r-pr-2 {
    padding-right: var(--space-2)
  }

  .lg\:rt-r-pr-3 {
    padding-right: var(--space-3)
  }

  .lg\:rt-r-pr-4 {
    padding-right: var(--space-4)
  }

  .lg\:rt-r-pr-5 {
    padding-right: var(--space-5)
  }

  .lg\:rt-r-pr-6 {
    padding-right: var(--space-6)
  }

  .lg\:rt-r-pr-7 {
    padding-right: var(--space-7)
  }

  .lg\:rt-r-pr-8 {
    padding-right: var(--space-8)
  }

  .lg\:rt-r-pr-9 {
    padding-right: var(--space-9)
  }

  .lg\:rt-r-pr-current {
    padding-right: var(--inset-padding)
  }

  .lg\:rt-r-pb-0 {
    padding-bottom: 0
  }

  .lg\:rt-r-pb-1 {
    padding-bottom: var(--space-1)
  }

  .lg\:rt-r-pb-2 {
    padding-bottom: var(--space-2)
  }

  .lg\:rt-r-pb-3 {
    padding-bottom: var(--space-3)
  }

  .lg\:rt-r-pb-4 {
    padding-bottom: var(--space-4)
  }

  .lg\:rt-r-pb-5 {
    padding-bottom: var(--space-5)
  }

  .lg\:rt-r-pb-6 {
    padding-bottom: var(--space-6)
  }

  .lg\:rt-r-pb-7 {
    padding-bottom: var(--space-7)
  }

  .lg\:rt-r-pb-8 {
    padding-bottom: var(--space-8)
  }

  .lg\:rt-r-pb-9 {
    padding-bottom: var(--space-9)
  }

  .lg\:rt-r-pb-current {
    padding-bottom: var(--inset-padding)
  }

  .lg\:rt-r-pl-0 {
    padding-left: 0
  }

  .lg\:rt-r-pl-1 {
    padding-left: var(--space-1)
  }

  .lg\:rt-r-pl-2 {
    padding-left: var(--space-2)
  }

  .lg\:rt-r-pl-3 {
    padding-left: var(--space-3)
  }

  .lg\:rt-r-pl-4 {
    padding-left: var(--space-4)
  }

  .lg\:rt-r-pl-5 {
    padding-left: var(--space-5)
  }

  .lg\:rt-r-pl-6 {
    padding-left: var(--space-6)
  }

  .lg\:rt-r-pl-7 {
    padding-left: var(--space-7)
  }

  .lg\:rt-r-pl-8 {
    padding-left: var(--space-8)
  }

  .lg\:rt-r-pl-9 {
    padding-left: var(--space-9)
  }

  .lg\:rt-r-pl-current {
    padding-left: var(--inset-padding)
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-p-0 {
    padding: 0
  }

  .xl\:rt-r-p-1 {
    padding: var(--space-1)
  }

  .xl\:rt-r-p-2 {
    padding: var(--space-2)
  }

  .xl\:rt-r-p-3 {
    padding: var(--space-3)
  }

  .xl\:rt-r-p-4 {
    padding: var(--space-4)
  }

  .xl\:rt-r-p-5 {
    padding: var(--space-5)
  }

  .xl\:rt-r-p-6 {
    padding: var(--space-6)
  }

  .xl\:rt-r-p-7 {
    padding: var(--space-7)
  }

  .xl\:rt-r-p-8 {
    padding: var(--space-8)
  }

  .xl\:rt-r-p-9 {
    padding: var(--space-9)
  }

  .xl\:rt-r-p-current {
    padding: var(--inset-padding)
  }

  .xl\:rt-r-px-0 {
    padding-left: 0;
    padding-right: 0
  }

  .xl\:rt-r-px-1 {
    padding-left: var(--space-1);
    padding-right: var(--space-1)
  }

  .xl\:rt-r-px-2 {
    padding-left: var(--space-2);
    padding-right: var(--space-2)
  }

  .xl\:rt-r-px-3 {
    padding-left: var(--space-3);
    padding-right: var(--space-3)
  }

  .xl\:rt-r-px-4 {
    padding-left: var(--space-4);
    padding-right: var(--space-4)
  }

  .xl\:rt-r-px-5 {
    padding-left: var(--space-5);
    padding-right: var(--space-5)
  }

  .xl\:rt-r-px-6 {
    padding-left: var(--space-6);
    padding-right: var(--space-6)
  }

  .xl\:rt-r-px-7 {
    padding-left: var(--space-7);
    padding-right: var(--space-7)
  }

  .xl\:rt-r-px-8 {
    padding-left: var(--space-8);
    padding-right: var(--space-8)
  }

  .xl\:rt-r-px-9 {
    padding-left: var(--space-9);
    padding-right: var(--space-9)
  }

  .xl\:rt-r-px-current {
    padding-left: var(--inset-padding);
    padding-right: var(--inset-padding)
  }

  .xl\:rt-r-py-0 {
    padding-top: 0;
    padding-bottom: 0
  }

  .xl\:rt-r-py-1 {
    padding-top: var(--space-1);
    padding-bottom: var(--space-1)
  }

  .xl\:rt-r-py-2 {
    padding-top: var(--space-2);
    padding-bottom: var(--space-2)
  }

  .xl\:rt-r-py-3 {
    padding-top: var(--space-3);
    padding-bottom: var(--space-3)
  }

  .xl\:rt-r-py-4 {
    padding-top: var(--space-4);
    padding-bottom: var(--space-4)
  }

  .xl\:rt-r-py-5 {
    padding-top: var(--space-5);
    padding-bottom: var(--space-5)
  }

  .xl\:rt-r-py-6 {
    padding-top: var(--space-6);
    padding-bottom: var(--space-6)
  }

  .xl\:rt-r-py-7 {
    padding-top: var(--space-7);
    padding-bottom: var(--space-7)
  }

  .xl\:rt-r-py-8 {
    padding-top: var(--space-8);
    padding-bottom: var(--space-8)
  }

  .xl\:rt-r-py-9 {
    padding-top: var(--space-9);
    padding-bottom: var(--space-9)
  }

  .xl\:rt-r-py-current {
    padding-top: var(--inset-padding);
    padding-bottom: var(--inset-padding)
  }

  .xl\:rt-r-pt-0 {
    padding-top: 0
  }

  .xl\:rt-r-pt-1 {
    padding-top: var(--space-1)
  }

  .xl\:rt-r-pt-2 {
    padding-top: var(--space-2)
  }

  .xl\:rt-r-pt-3 {
    padding-top: var(--space-3)
  }

  .xl\:rt-r-pt-4 {
    padding-top: var(--space-4)
  }

  .xl\:rt-r-pt-5 {
    padding-top: var(--space-5)
  }

  .xl\:rt-r-pt-6 {
    padding-top: var(--space-6)
  }

  .xl\:rt-r-pt-7 {
    padding-top: var(--space-7)
  }

  .xl\:rt-r-pt-8 {
    padding-top: var(--space-8)
  }

  .xl\:rt-r-pt-9 {
    padding-top: var(--space-9)
  }

  .xl\:rt-r-pt-current {
    padding-top: var(--inset-padding)
  }

  .xl\:rt-r-pr-0 {
    padding-right: 0
  }

  .xl\:rt-r-pr-1 {
    padding-right: var(--space-1)
  }

  .xl\:rt-r-pr-2 {
    padding-right: var(--space-2)
  }

  .xl\:rt-r-pr-3 {
    padding-right: var(--space-3)
  }

  .xl\:rt-r-pr-4 {
    padding-right: var(--space-4)
  }

  .xl\:rt-r-pr-5 {
    padding-right: var(--space-5)
  }

  .xl\:rt-r-pr-6 {
    padding-right: var(--space-6)
  }

  .xl\:rt-r-pr-7 {
    padding-right: var(--space-7)
  }

  .xl\:rt-r-pr-8 {
    padding-right: var(--space-8)
  }

  .xl\:rt-r-pr-9 {
    padding-right: var(--space-9)
  }

  .xl\:rt-r-pr-current {
    padding-right: var(--inset-padding)
  }

  .xl\:rt-r-pb-0 {
    padding-bottom: 0
  }

  .xl\:rt-r-pb-1 {
    padding-bottom: var(--space-1)
  }

  .xl\:rt-r-pb-2 {
    padding-bottom: var(--space-2)
  }

  .xl\:rt-r-pb-3 {
    padding-bottom: var(--space-3)
  }

  .xl\:rt-r-pb-4 {
    padding-bottom: var(--space-4)
  }

  .xl\:rt-r-pb-5 {
    padding-bottom: var(--space-5)
  }

  .xl\:rt-r-pb-6 {
    padding-bottom: var(--space-6)
  }

  .xl\:rt-r-pb-7 {
    padding-bottom: var(--space-7)
  }

  .xl\:rt-r-pb-8 {
    padding-bottom: var(--space-8)
  }

  .xl\:rt-r-pb-9 {
    padding-bottom: var(--space-9)
  }

  .xl\:rt-r-pb-current {
    padding-bottom: var(--inset-padding)
  }

  .xl\:rt-r-pl-0 {
    padding-left: 0
  }

  .xl\:rt-r-pl-1 {
    padding-left: var(--space-1)
  }

  .xl\:rt-r-pl-2 {
    padding-left: var(--space-2)
  }

  .xl\:rt-r-pl-3 {
    padding-left: var(--space-3)
  }

  .xl\:rt-r-pl-4 {
    padding-left: var(--space-4)
  }

  .xl\:rt-r-pl-5 {
    padding-left: var(--space-5)
  }

  .xl\:rt-r-pl-6 {
    padding-left: var(--space-6)
  }

  .xl\:rt-r-pl-7 {
    padding-left: var(--space-7)
  }

  .xl\:rt-r-pl-8 {
    padding-left: var(--space-8)
  }

  .xl\:rt-r-pl-9 {
    padding-left: var(--space-9)
  }

  .xl\:rt-r-pl-current {
    padding-left: var(--inset-padding)
  }
}

@media all {
  .rt-r-position-static {
    position: static
  }

  .rt-r-position-absolute {
    position: absolute
  }

  .rt-r-position-relative {
    position: relative
  }

  .rt-r-position-fixed {
    position: fixed
  }

  .rt-r-position-sticky {
    position: sticky
  }
}

@media (min-width:520px) {
  .xs\:rt-r-position-static {
    position: static
  }

  .xs\:rt-r-position-absolute {
    position: absolute
  }

  .xs\:rt-r-position-relative {
    position: relative
  }

  .xs\:rt-r-position-fixed {
    position: fixed
  }

  .xs\:rt-r-position-sticky {
    position: sticky
  }
}

@media (min-width:768px) {
  .sm\:rt-r-position-static {
    position: static
  }

  .sm\:rt-r-position-absolute {
    position: absolute
  }

  .sm\:rt-r-position-relative {
    position: relative
  }

  .sm\:rt-r-position-fixed {
    position: fixed
  }

  .sm\:rt-r-position-sticky {
    position: sticky
  }
}

@media (min-width:1024px) {
  .md\:rt-r-position-static {
    position: static
  }

  .md\:rt-r-position-absolute {
    position: absolute
  }

  .md\:rt-r-position-relative {
    position: relative
  }

  .md\:rt-r-position-fixed {
    position: fixed
  }

  .md\:rt-r-position-sticky {
    position: sticky
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-position-static {
    position: static
  }

  .lg\:rt-r-position-absolute {
    position: absolute
  }

  .lg\:rt-r-position-relative {
    position: relative
  }

  .lg\:rt-r-position-fixed {
    position: fixed
  }

  .lg\:rt-r-position-sticky {
    position: sticky
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-position-static {
    position: static
  }

  .xl\:rt-r-position-absolute {
    position: absolute
  }

  .xl\:rt-r-position-relative {
    position: relative
  }

  .xl\:rt-r-position-fixed {
    position: fixed
  }

  .xl\:rt-r-position-sticky {
    position: sticky
  }
}

@media all {
  .rt-r-ta-left {
    text-align: left
  }

  .rt-r-ta-center {
    text-align: center
  }

  .rt-r-ta-right {
    text-align: right
  }
}

@media (min-width:520px) {
  .xs\:rt-r-ta-left {
    text-align: left
  }

  .xs\:rt-r-ta-center {
    text-align: center
  }

  .xs\:rt-r-ta-right {
    text-align: right
  }
}

@media (min-width:768px) {
  .sm\:rt-r-ta-left {
    text-align: left
  }

  .sm\:rt-r-ta-center {
    text-align: center
  }

  .sm\:rt-r-ta-right {
    text-align: right
  }
}

@media (min-width:1024px) {
  .md\:rt-r-ta-left {
    text-align: left
  }

  .md\:rt-r-ta-center {
    text-align: center
  }

  .md\:rt-r-ta-right {
    text-align: right
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-ta-left {
    text-align: left
  }

  .lg\:rt-r-ta-center {
    text-align: center
  }

  .lg\:rt-r-ta-right {
    text-align: right
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-ta-left {
    text-align: left
  }

  .xl\:rt-r-ta-center {
    text-align: center
  }

  .xl\:rt-r-ta-right {
    text-align: right
  }
}

@media all {
  .rt-r-va-baseline {
    vertical-align: baseline
  }

  .rt-r-va-top {
    vertical-align: top
  }

  .rt-r-va-middle {
    vertical-align: middle
  }

  .rt-r-va-bottom {
    vertical-align: bottom
  }
}

@media (min-width:520px) {
  .xs\:rt-r-va-baseline {
    vertical-align: baseline
  }

  .xs\:rt-r-va-top {
    vertical-align: top
  }

  .xs\:rt-r-va-middle {
    vertical-align: middle
  }

  .xs\:rt-r-va-bottom {
    vertical-align: bottom
  }
}

@media (min-width:768px) {
  .sm\:rt-r-va-baseline {
    vertical-align: baseline
  }

  .sm\:rt-r-va-top {
    vertical-align: top
  }

  .sm\:rt-r-va-middle {
    vertical-align: middle
  }

  .sm\:rt-r-va-bottom {
    vertical-align: bottom
  }
}

@media (min-width:1024px) {
  .md\:rt-r-va-baseline {
    vertical-align: baseline
  }

  .md\:rt-r-va-top {
    vertical-align: top
  }

  .md\:rt-r-va-middle {
    vertical-align: middle
  }

  .md\:rt-r-va-bottom {
    vertical-align: bottom
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-va-baseline {
    vertical-align: baseline
  }

  .lg\:rt-r-va-top {
    vertical-align: top
  }

  .lg\:rt-r-va-middle {
    vertical-align: middle
  }

  .lg\:rt-r-va-bottom {
    vertical-align: bottom
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-va-baseline {
    vertical-align: baseline
  }

  .xl\:rt-r-va-top {
    vertical-align: top
  }

  .xl\:rt-r-va-middle {
    vertical-align: middle
  }

  .xl\:rt-r-va-bottom {
    vertical-align: bottom
  }
}

@media all {
  .rt-r-w-auto {
    width: auto
  }

  .rt-r-w-max-content {
    width: -moz-max-content;
    width: max-content
  }

  .rt-r-w-min-content {
    width: -moz-min-content;
    width: min-content
  }

  .rt-r-w-0 {
    width: 0
  }

  .rt-r-w-1 {
    width: var(--space-1)
  }

  .rt-r-w-2 {
    width: var(--space-2)
  }

  .rt-r-w-3 {
    width: var(--space-3)
  }

  .rt-r-w-4 {
    width: var(--space-4)
  }

  .rt-r-w-5 {
    width: var(--space-5)
  }

  .rt-r-w-6 {
    width: var(--space-6)
  }

  .rt-r-w-7 {
    width: var(--space-7)
  }

  .rt-r-w-8 {
    width: var(--space-8)
  }

  .rt-r-w-9 {
    width: var(--space-9)
  }

  .rt-r-w-50\% {
    width: 50%
  }

  .rt-r-w-100\% {
    width: 100%
  }
}

@media (min-width:520px) {
  .xs\:rt-r-w-auto {
    width: auto
  }

  .xs\:rt-r-w-max-content {
    width: -moz-max-content;
    width: max-content
  }

  .xs\:rt-r-w-min-content {
    width: -moz-min-content;
    width: min-content
  }

  .xs\:rt-r-w-0 {
    width: 0
  }

  .xs\:rt-r-w-1 {
    width: var(--space-1)
  }

  .xs\:rt-r-w-2 {
    width: var(--space-2)
  }

  .xs\:rt-r-w-3 {
    width: var(--space-3)
  }

  .xs\:rt-r-w-4 {
    width: var(--space-4)
  }

  .xs\:rt-r-w-5 {
    width: var(--space-5)
  }

  .xs\:rt-r-w-6 {
    width: var(--space-6)
  }

  .xs\:rt-r-w-7 {
    width: var(--space-7)
  }

  .xs\:rt-r-w-8 {
    width: var(--space-8)
  }

  .xs\:rt-r-w-9 {
    width: var(--space-9)
  }

  .xs\:rt-r-w-50\% {
    width: 50%
  }

  .xs\:rt-r-w-100\% {
    width: 100%
  }
}

@media (min-width:768px) {
  .sm\:rt-r-w-auto {
    width: auto
  }

  .sm\:rt-r-w-max-content {
    width: -moz-max-content;
    width: max-content
  }

  .sm\:rt-r-w-min-content {
    width: -moz-min-content;
    width: min-content
  }

  .sm\:rt-r-w-0 {
    width: 0
  }

  .sm\:rt-r-w-1 {
    width: var(--space-1)
  }

  .sm\:rt-r-w-2 {
    width: var(--space-2)
  }

  .sm\:rt-r-w-3 {
    width: var(--space-3)
  }

  .sm\:rt-r-w-4 {
    width: var(--space-4)
  }

  .sm\:rt-r-w-5 {
    width: var(--space-5)
  }

  .sm\:rt-r-w-6 {
    width: var(--space-6)
  }

  .sm\:rt-r-w-7 {
    width: var(--space-7)
  }

  .sm\:rt-r-w-8 {
    width: var(--space-8)
  }

  .sm\:rt-r-w-9 {
    width: var(--space-9)
  }

  .sm\:rt-r-w-50\% {
    width: 50%
  }

  .sm\:rt-r-w-100\% {
    width: 100%
  }
}

@media (min-width:1024px) {
  .md\:rt-r-w-auto {
    width: auto
  }

  .md\:rt-r-w-max-content {
    width: -moz-max-content;
    width: max-content
  }

  .md\:rt-r-w-min-content {
    width: -moz-min-content;
    width: min-content
  }

  .md\:rt-r-w-0 {
    width: 0
  }

  .md\:rt-r-w-1 {
    width: var(--space-1)
  }

  .md\:rt-r-w-2 {
    width: var(--space-2)
  }

  .md\:rt-r-w-3 {
    width: var(--space-3)
  }

  .md\:rt-r-w-4 {
    width: var(--space-4)
  }

  .md\:rt-r-w-5 {
    width: var(--space-5)
  }

  .md\:rt-r-w-6 {
    width: var(--space-6)
  }

  .md\:rt-r-w-7 {
    width: var(--space-7)
  }

  .md\:rt-r-w-8 {
    width: var(--space-8)
  }

  .md\:rt-r-w-9 {
    width: var(--space-9)
  }

  .md\:rt-r-w-50\% {
    width: 50%
  }

  .md\:rt-r-w-100\% {
    width: 100%
  }
}

@media (min-width:1280px) {
  .lg\:rt-r-w-auto {
    width: auto
  }

  .lg\:rt-r-w-max-content {
    width: -moz-max-content;
    width: max-content
  }

  .lg\:rt-r-w-min-content {
    width: -moz-min-content;
    width: min-content
  }

  .lg\:rt-r-w-0 {
    width: 0
  }

  .lg\:rt-r-w-1 {
    width: var(--space-1)
  }

  .lg\:rt-r-w-2 {
    width: var(--space-2)
  }

  .lg\:rt-r-w-3 {
    width: var(--space-3)
  }

  .lg\:rt-r-w-4 {
    width: var(--space-4)
  }

  .lg\:rt-r-w-5 {
    width: var(--space-5)
  }

  .lg\:rt-r-w-6 {
    width: var(--space-6)
  }

  .lg\:rt-r-w-7 {
    width: var(--space-7)
  }

  .lg\:rt-r-w-8 {
    width: var(--space-8)
  }

  .lg\:rt-r-w-9 {
    width: var(--space-9)
  }

  .lg\:rt-r-w-50\% {
    width: 50%
  }

  .lg\:rt-r-w-100\% {
    width: 100%
  }
}

@media (min-width:1640px) {
  .xl\:rt-r-w-auto {
    width: auto
  }

  .xl\:rt-r-w-max-content {
    width: -moz-max-content;
    width: max-content
  }

  .xl\:rt-r-w-min-content {
    width: -moz-min-content;
    width: min-content
  }

  .xl\:rt-r-w-0 {
    width: 0
  }

  .xl\:rt-r-w-1 {
    width: var(--space-1)
  }

  .xl\:rt-r-w-2 {
    width: var(--space-2)
  }

  .xl\:rt-r-w-3 {
    width: var(--space-3)
  }

  .xl\:rt-r-w-4 {
    width: var(--space-4)
  }

  .xl\:rt-r-w-5 {
    width: var(--space-5)
  }

  .xl\:rt-r-w-6 {
    width: var(--space-6)
  }

  .xl\:rt-r-w-7 {
    width: var(--space-7)
  }

  .xl\:rt-r-w-8 {
    width: var(--space-8)
  }

  .xl\:rt-r-w-9 {
    width: var(--space-9)
  }

  .xl\:rt-r-w-50\% {
    width: 50%
  }

  .xl\:rt-r-w-100\% {
    width: 100%
  }
}

.radix-themes {
  --theme-panel--focus-ring-color: #000
}

:is(.dark, .dark-theme),
:is(.dark, .dark-theme) .radix-themes:not(.light, .light-theme) {
  --theme-panel--focus-ring-color: #fff
}

.rt-ThemePanelShortcut:focus-visible {
  outline-style: solid;
  outline-width: 2px;
  outline-offset: 2px;
  outline-color: var(--accent-9)
}

.rt-ThemePanelRadioCard,
.rt-ThemePanelSwatch {
  position: relative
}

.rt-ThemePanelRadioCard input,
.rt-ThemePanelSwatch input {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  margin: 0;
  outline: none;
  outline-width: 2px;
  outline-offset: 2px;
  position: absolute;
  inset: 0;
  border-radius: inherit
}

.rt-ThemePanelSwatch {
  width: var(--space-5);
  height: var(--space-5);
  border-radius: 100%
}

.rt-ThemePanelSwatch input:checked {
  outline-style: solid;
  outline-color: var(--theme-panel--focus-ring-color)
}

.rt-ThemePanelSwatch input:focus-visible {
  outline-style: solid;
  outline-color: var(--accent-9)
}

.rt-ThemePanelRadioCard {
  border-radius: var(--radius-1);
  box-shadow: 0 0 0 1px var(--gray-7)
}

.rt-ThemePanelRadioCard input:checked {
  box-shadow: inset 0 0 0 1px var(--theme-panel--focus-ring-color), 0 0 0 1px var(--theme-panel--focus-ring-color)
}

.rt-ThemePanelRadioCard input:focus-visible {
  background-color: var(--accent-a3);
  box-shadow: inset 0 0 0 1px var(--accent-9), 0 0 0 1px var(--accent-9)
}
</style>
<style>
@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/d1d9458b69004127-s.woff2) format("woff2");
    unicode-range: U+0460-052f, U+1c80-1c88, U+20b4, U+2de0-2dff, U+a640-a69f, U+fe2e-fe2f
}

@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/b967158bc7d7a9fb-s.woff2) format("woff2");
    unicode-range: U+0301, U+0400-045f, U+0490-0491, U+04b0-04b1, U+2116
}

@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/ae9ae6716d4f8bf8-s.woff2) format("woff2");
    unicode-range: U+1f??
}

@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/c0f5ec5bbf5913b7-s.woff2) format("woff2");
    unicode-range: U+0370-03ff
}

@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/b1db3e28af9ef94a-s.woff2) format("woff2");
    unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01a0-01a1, U+01af-01b0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1ea0-1ef9, U+20ab
}

@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/9c4f34569c9b36ca-s.woff2) format("woff2");
    unicode-range: U+0100-02af, U+0304, U+0308, U+0329, U+1e00-1e9f, U+1ef2-1eff, U+2020, U+20a0-20ab, U+20ad-20cf, U+2113, U+2c60-2c7f, U+a720-a7ff
}

@font-face {
    font-family: __Inter_20951f;
    font-style: normal;
    font-weight: 100 900;
    font-display: swap;
    src: url(/app/static/2aaf0723e720e8b9-s.p.woff2) format("woff2");
    unicode-range: U+00??, U+0131, U+0152-0153, U+02bb-02bc, U+02c6, U+02da, U+02dc, U+0304, U+0308, U+0329, U+2000-206f, U+2074, U+20ac, U+2122, U+2191, U+2193, U+2212, U+2215, U+feff, U+fffd
}

@font-face {
    font-family: __Inter_Fallback_20951f;
    src: local("Arial");
    ascent-override: 90.20%;
    descent-override: 22.48%;
    line-gap-override: 0.00%;
    size-adjust: 107.40%
}

.__className_20951f {
    font-family: __Inter_20951f, __Inter_Fallback_20951f;
    font-style: normal
}

.__variable_20951f {
    --font-inter: "__Inter_20951f", "__Inter_Fallback_20951f"
}

@font-face {
    font-family: __Roboto_Mono_bbf4d0;
    font-style: normal;
    font-weight: 100 700;
    font-display: swap;
    src: url(/app/static/88ba9021cc1d0e98-s.woff2) format("woff2");
    unicode-range: U+0460-052f, U+1c80-1c88, U+20b4, U+2de0-2dff, U+a640-a69f, U+fe2e-fe2f
}

@font-face {
    font-family: __Roboto_Mono_bbf4d0;
    font-style: normal;
    font-weight: 100 700;
    font-display: swap;
    src: url(/app/static/104274daeea7a91a-s.woff2) format("woff2");
    unicode-range: U+0301, U+0400-045f, U+0490-0491, U+04b0-04b1, U+2116
}

@font-face {
    font-family: __Roboto_Mono_bbf4d0;
    font-style: normal;
    font-weight: 100 700;
    font-display: swap;
    src: url(/app/static/7e380d3170051f13-s.woff2) format("woff2");
    unicode-range: U+0370-03ff
}

@font-face {
    font-family: __Roboto_Mono_bbf4d0;
    font-style: normal;
    font-weight: 100 700;
    font-display: swap;
    src: url(/app/static/e653d759d3cc808f-s.woff2) format("woff2");
    unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01a0-01a1, U+01af-01b0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1ea0-1ef9, U+20ab
}

@font-face {
    font-family: __Roboto_Mono_bbf4d0;
    font-style: normal;
    font-weight: 100 700;
    font-display: swap;
    src: url(/app/static/a913ea2790b1a249-s.woff2) format("woff2");
    unicode-range: U+0100-02af, U+0304, U+0308, U+0329, U+1e00-1e9f, U+1ef2-1eff, U+2020, U+20a0-20ab, U+20ad-20cf, U+2113, U+2c60-2c7f, U+a720-a7ff
}

@font-face {
    font-family: __Roboto_Mono_bbf4d0;
    font-style: normal;
    font-weight: 100 700;
    font-display: swap;
    src: url(/app/static/8e992d4bd80b0720-s.p.woff2) format("woff2");
    unicode-range: U+00??, U+0131, U+0152-0153, U+02bb-02bc, U+02c6, U+02da, U+02dc, U+0304, U+0308, U+0329, U+2000-206f, U+2074, U+20ac, U+2122, U+2191, U+2193, U+2212, U+2215, U+feff, U+fffd
}

@font-face {
    font-family: __Roboto_Mono_Fallback_bbf4d0;
    src: local("Arial");
    ascent-override: 77.08%;
    descent-override: 19.93%;
    line-gap-override: 0.00%;
    size-adjust: 135.95%
}

.__className_bbf4d0 {
    font-family: __Roboto_Mono_bbf4d0, __Roboto_Mono_Fallback_bbf4d0;
    font-style: normal
}

.__variable_bbf4d0 {
    --font-roboto-mono: "__Roboto_Mono_bbf4d0", "__Roboto_Mono_Fallback_bbf4d0"
}

/*
! tailwindcss v3.3.3 | MIT License | https://tailwindcss.com
*/
*,
:after,
:before {
    box-sizing: border-box;
    border: 0 solid #e5e7eb
}

:after,
:before {
    --tw-content: ""
}

html {
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;
    font-family: var(--font-inter), ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    font-feature-settings: normal;
    font-variation-settings: normal
}

body {
    margin: 0;
    line-height: inherit
}

hr {
    height: 0;
    color: inherit;
    border-top-width: 1px
}

abbr:where([title]) {
    -webkit-text-decoration: underline dotted;
    text-decoration: underline dotted
}

h1,
h2,
h3,
h4,
h5,
h6 {
    font-size: inherit;
    font-weight: inherit
}

a {
    color: inherit;
    text-decoration: inherit
}

b,
strong {
    font-weight: bolder
}

code,
kbd,
pre,
samp {
    font-family: var(--font-roboto-mono), ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 1em
}

small {
    font-size: 80%
}

sub,
sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline
}

sub {
    bottom: -.25em
}

sup {
    top: -.5em
}

table {
    text-indent: 0;
    border-color: inherit;
    border-collapse: collapse
}

button,
input,
optgroup,
select,
textarea {
    font-family: inherit;
    font-feature-settings: inherit;
    font-variation-settings: inherit;
    font-size: 100%;
    font-weight: inherit;
    line-height: inherit;
    color: inherit;
    margin: 0;
    padding: 0
}

button,
select {
    text-transform: none
}

[type=button],
[type=reset],
[type=submit],
button {
    -webkit-appearance: button;
    background-color: transparent;
    background-image: none
}

:-moz-focusring {
    outline: auto
}

:-moz-ui-invalid {
    box-shadow: none
}

progress {
    vertical-align: baseline
}

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
    height: auto
}

[type=search] {
    -webkit-appearance: textfield;
    outline-offset: -2px
}

::-webkit-search-decoration {
    -webkit-appearance: none
}

::-webkit-file-upload-button {
    -webkit-appearance: button;
    font: inherit
}

summary {
    display: list-item
}

blockquote,
dd,
dl,
figure,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
p,
pre {
    margin: 0
}

fieldset {
    margin: 0
}

fieldset,
legend {
    padding: 0
}

menu,
ol,
ul {
    list-style: none;
    margin: 0;
    padding: 0
}

dialog {
    padding: 0
}

textarea {
    resize: vertical
}

input::-moz-placeholder,
textarea::-moz-placeholder {
    opacity: 1;
    color: #9ca3af
}

input::placeholder,
textarea::placeholder {
    opacity: 1;
    color: #9ca3af
}

[role=button],
button {
    cursor: pointer
}

:disabled {
    cursor: default
}

audio,
canvas,
embed,
iframe,
img,
object,
svg,
video {
    display: block;
    vertical-align: middle
}

img,
video {
    max-width: 100%;
    height: auto
}

[hidden] {
    display: none
}

*,
:after,
:before {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, .5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia:
}

::backdrop {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59, 130, 246, .5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia:
}

.prose {
    color: var(--tw-prose-body);
    max-width: 65ch
}

.prose :where(p):not(:where([class~=not-prose] *)) {
    margin-top: 1.25em;
    margin-bottom: 1.25em
}

.prose :where([class~=lead]):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-lead);
    font-size: 1.25em;
    line-height: 1.6;
    margin-top: 1.2em;
    margin-bottom: 1.2em
}

.prose :where(a):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-links);
    text-decoration: underline;
    font-weight: 500
}

.prose :where(strong):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-bold);
    font-weight: 600
}

.prose :where(a strong):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(blockquote strong):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(thead th strong):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(ol):not(:where([class~=not-prose] *)) {
    list-style-type: decimal;
    margin-top: 1.25em;
    margin-bottom: 1.25em;
    padding-left: 1.625em
}

.prose :where(ol[type=A]):not(:where([class~=not-prose] *)) {
    list-style-type: upper-alpha
}

.prose :where(ol[type=a]):not(:where([class~=not-prose] *)) {
    list-style-type: lower-alpha
}

.prose :where(ol[type=A s]):not(:where([class~=not-prose] *)) {
    list-style-type: upper-alpha
}

.prose :where(ol[type=a s]):not(:where([class~=not-prose] *)) {
    list-style-type: lower-alpha
}

.prose :where(ol[type=I]):not(:where([class~=not-prose] *)) {
    list-style-type: upper-roman
}

.prose :where(ol[type=i]):not(:where([class~=not-prose] *)) {
    list-style-type: lower-roman
}

.prose :where(ol[type=I s]):not(:where([class~=not-prose] *)) {
    list-style-type: upper-roman
}

.prose :where(ol[type=i s]):not(:where([class~=not-prose] *)) {
    list-style-type: lower-roman
}

.prose :where(ol[type="1"]):not(:where([class~=not-prose] *)) {
    list-style-type: decimal
}

.prose :where(ul):not(:where([class~=not-prose] *)) {
    list-style-type: disc;
    margin-top: 1.25em;
    margin-bottom: 1.25em;
    padding-left: 1.625em
}

.prose :where(ol>li):not(:where([class~=not-prose] *))::marker {
    font-weight: 400;
    color: var(--tw-prose-counters)
}

.prose :where(ul>li):not(:where([class~=not-prose] *))::marker {
    color: var(--tw-prose-bullets)
}

.prose :where(hr):not(:where([class~=not-prose] *)) {
    border-color: var(--tw-prose-hr);
    border-top-width: 1px;
    margin-top: 3em;
    margin-bottom: 3em
}

.prose :where(blockquote):not(:where([class~=not-prose] *)) {
    font-weight: 500;
    font-style: italic;
    color: var(--tw-prose-quotes);
    border-left-width: .25rem;
    border-left-color: var(--tw-prose-quote-borders);
    quotes: "\201C" "\201D" "\2018" "\2019";
    margin-top: 1.6em;
    margin-bottom: 1.6em;
    padding-left: 1em
}

.prose :where(blockquote p:first-of-type):not(:where([class~=not-prose] *)):before {
    content: open-quote
}

.prose :where(blockquote p:last-of-type):not(:where([class~=not-prose] *)):after {
    content: close-quote
}

.prose :where(h1):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-headings);
    font-weight: 800;
    font-size: 2.25em;
    margin-top: 0;
    margin-bottom: .8888889em;
    line-height: 1.1111111
}

.prose :where(h1 strong):not(:where([class~=not-prose] *)) {
    font-weight: 900;
    color: inherit
}

.prose :where(h2):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-headings);
    font-weight: 700;
    font-size: 1.5em;
    margin-top: 2em;
    margin-bottom: 1em;
    line-height: 1.3333333
}

.prose :where(h2 strong):not(:where([class~=not-prose] *)) {
    font-weight: 800;
    color: inherit
}

.prose :where(h3):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-headings);
    font-weight: 600;
    font-size: 1.25em;
    margin-top: 1.6em;
    margin-bottom: .6em;
    line-height: 1.6
}

.prose :where(h3 strong):not(:where([class~=not-prose] *)) {
    font-weight: 700;
    color: inherit
}

.prose :where(h4):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-headings);
    font-weight: 600;
    margin-top: 1.5em;
    margin-bottom: .5em;
    line-height: 1.5
}

.prose :where(h4 strong):not(:where([class~=not-prose] *)) {
    font-weight: 700;
    color: inherit
}

.prose :where(img):not(:where([class~=not-prose] *)) {
    margin-top: 2em;
    margin-bottom: 2em
}

.prose :where(figure>*):not(:where([class~=not-prose] *)) {
    margin-top: 0;
    margin-bottom: 0
}

.prose :where(figcaption):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-captions);
    font-size: .875em;
    line-height: 1.4285714;
    margin-top: .8571429em
}

.prose :where(code):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-code);
    font-weight: 600;
    font-size: .875em
}

.prose :where(code):not(:where([class~=not-prose] *)):before {
    content: "`"
}

.prose :where(code):not(:where([class~=not-prose] *)):after {
    content: "`"
}

.prose :where(a code):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(h1 code):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(h2 code):not(:where([class~=not-prose] *)) {
    color: inherit;
    font-size: .875em
}

.prose :where(h3 code):not(:where([class~=not-prose] *)) {
    color: inherit;
    font-size: .9em
}

.prose :where(h4 code):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(blockquote code):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(thead th code):not(:where([class~=not-prose] *)) {
    color: inherit
}

.prose :where(pre):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-pre-code);
    background-color: var(--tw-prose-pre-bg);
    overflow-x: auto;
    font-weight: 400;
    font-size: .875em;
    line-height: 1.7142857;
    margin-top: 1.7142857em;
    margin-bottom: 1.7142857em;
    border-radius: .375rem;
    padding: .8571429em 1.1428571em
}

.prose :where(pre code):not(:where([class~=not-prose] *)) {
    background-color: transparent;
    border-width: 0;
    border-radius: 0;
    padding: 0;
    font-weight: inherit;
    color: inherit;
    font-size: inherit;
    font-family: inherit;
    line-height: inherit
}

.prose :where(pre code):not(:where([class~=not-prose] *)):before {
    content: none
}

.prose :where(pre code):not(:where([class~=not-prose] *)):after {
    content: none
}

.prose :where(table):not(:where([class~=not-prose] *)) {
    width: 100%;
    table-layout: auto;
    text-align: left;
    margin-top: 2em;
    margin-bottom: 2em;
    font-size: .875em;
    line-height: 1.7142857
}

.prose :where(thead):not(:where([class~=not-prose] *)) {
    border-bottom-width: 1px;
    border-bottom-color: var(--tw-prose-th-borders)
}

.prose :where(thead th):not(:where([class~=not-prose] *)) {
    color: var(--tw-prose-headings);
    font-weight: 600;
    vertical-align: bottom;
    padding-right: .5714286em;
    padding-bottom: .5714286em;
    padding-left: .5714286em
}

.prose :where(tbody tr):not(:where([class~=not-prose] *)) {
    border-bottom-width: 1px;
    border-bottom-color: var(--tw-prose-td-borders)
}

.prose :where(tbody tr:last-child):not(:where([class~=not-prose] *)) {
    border-bottom-width: 0
}

.prose :where(tbody td):not(:where([class~=not-prose] *)) {
    vertical-align: baseline
}

.prose :where(tfoot):not(:where([class~=not-prose] *)) {
    border-top-width: 1px;
    border-top-color: var(--tw-prose-th-borders)
}

.prose :where(tfoot td):not(:where([class~=not-prose] *)) {
    vertical-align: top
}

.prose {
    --tw-prose-body: #374151;
    --tw-prose-headings: #111827;
    --tw-prose-lead: #4b5563;
    --tw-prose-links: #111827;
    --tw-prose-bold: #111827;
    --tw-prose-counters: #6b7280;
    --tw-prose-bullets: #d1d5db;
    --tw-prose-hr: #e5e7eb;
    --tw-prose-quotes: #111827;
    --tw-prose-quote-borders: #e5e7eb;
    --tw-prose-captions: #6b7280;
    --tw-prose-code: #111827;
    --tw-prose-pre-code: #e5e7eb;
    --tw-prose-pre-bg: #1f2937;
    --tw-prose-th-borders: #d1d5db;
    --tw-prose-td-borders: #e5e7eb;
    --tw-prose-invert-body: #d1d5db;
    --tw-prose-invert-headings: #fff;
    --tw-prose-invert-lead: #9ca3af;
    --tw-prose-invert-links: #fff;
    --tw-prose-invert-bold: #fff;
    --tw-prose-invert-counters: #9ca3af;
    --tw-prose-invert-bullets: #4b5563;
    --tw-prose-invert-hr: #374151;
    --tw-prose-invert-quotes: #f3f4f6;
    --tw-prose-invert-quote-borders: #374151;
    --tw-prose-invert-captions: #9ca3af;
    --tw-prose-invert-code: #fff;
    --tw-prose-invert-pre-code: #d1d5db;
    --tw-prose-invert-pre-bg: rgba(0, 0, 0, .5);
    --tw-prose-invert-th-borders: #4b5563;
    --tw-prose-invert-td-borders: #374151;
    font-size: 1rem;
    line-height: 1.75
}

.prose :where(video):not(:where([class~=not-prose] *)) {
    margin-top: 2em;
    margin-bottom: 2em
}

.prose :where(figure):not(:where([class~=not-prose] *)) {
    margin-top: 2em;
    margin-bottom: 2em
}

.prose :where(li):not(:where([class~=not-prose] *)) {
    margin-top: .5em;
    margin-bottom: .5em
}

.prose :where(ol>li):not(:where([class~=not-prose] *)) {
    padding-left: .375em
}

.prose :where(ul>li):not(:where([class~=not-prose] *)) {
    padding-left: .375em
}

.prose :where(.prose>ul>li p):not(:where([class~=not-prose] *)) {
    margin-top: .75em;
    margin-bottom: .75em
}

.prose :where(.prose>ul>li>:first-child):not(:where([class~=not-prose] *)) {
    margin-top: 1.25em
}

.prose :where(.prose>ul>li>:last-child):not(:where([class~=not-prose] *)) {
    margin-bottom: 1.25em
}

.prose :where(.prose>ol>li>:first-child):not(:where([class~=not-prose] *)) {
    margin-top: 1.25em
}

.prose :where(.prose>ol>li>:last-child):not(:where([class~=not-prose] *)) {
    margin-bottom: 1.25em
}

.prose :where(ul ul, ul ol, ol ul, ol ol):not(:where([class~=not-prose] *)) {
    margin-top: .75em;
    margin-bottom: .75em
}

.prose :where(hr+*):not(:where([class~=not-prose] *)) {
    margin-top: 0
}

.prose :where(h2+*):not(:where([class~=not-prose] *)) {
    margin-top: 0
}

.prose :where(h3+*):not(:where([class~=not-prose] *)) {
    margin-top: 0
}

.prose :where(h4+*):not(:where([class~=not-prose] *)) {
    margin-top: 0
}

.prose :where(thead th:first-child):not(:where([class~=not-prose] *)) {
    padding-left: 0
}

.prose :where(thead th:last-child):not(:where([class~=not-prose] *)) {
    padding-right: 0
}

.prose :where(tbody td, tfoot td):not(:where([class~=not-prose] *)) {
    padding: .5714286em
}

.prose :where(tbody td:first-child, tfoot td:first-child):not(:where([class~=not-prose] *)) {
    padding-left: 0
}

.prose :where(tbody td:last-child, tfoot td:last-child):not(:where([class~=not-prose] *)) {
    padding-right: 0
}

.prose :where(.prose>:first-child):not(:where([class~=not-prose] *)) {
    margin-top: 0
}

.prose :where(.prose>:last-child):not(:where([class~=not-prose] *)) {
    margin-bottom: 0
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0
}

.fixed {
    position: fixed
}

.absolute {
    position: absolute
}

.relative {
    position: relative
}

.left-0 {
    left: 0
}

.top-0 {
    top: 0
}

.-z-10 {
    z-index: -10
}

.mx-2 {
    margin-left: .5rem;
    margin-right: .5rem
}

.my-8 {
    margin-top: 2rem;
    margin-bottom: 2rem
}

.-mb-3 {
    margin-bottom: -.75rem
}

.ml-1 {
    margin-left: .25rem
}

.ml-2 {
    margin-left: .5rem
}

.mr-0 {
    margin-right: 0
}

.mr-1 {
    margin-right: .25rem
}

.mr-2 {
    margin-right: .5rem
}

.mt-2 {
    margin-top: .5rem
}

.mt-4 {
    margin-top: 1rem
}

.box-border {
    box-sizing: border-box
}

.flex {
    display: flex
}

.grid {
    display: grid
}

.h-10 {
    height: 2.5rem
}

.h-2 {
    height: .5rem
}

.h-20 {
    height: 5rem
}

.h-4 {
    height: 1rem
}

.h-5 {
    height: 1.25rem
}

.h-6 {
    height: 1.5rem
}

.h-8 {
    height: 2rem
}

.h-\[600px\] {
    height: 600px
}

.h-full {
    height: 100%
}

.h-screen {
    height: 100vh
}

.w-10 {
    width: 2.5rem
}

.w-12 {
    width: 3rem
}

.w-20 {
    width: 5rem
}

.w-4 {
    width: 1rem
}

.w-5 {
    width: 1.25rem
}

.w-8 {
    width: 2rem
}

.w-9 {
    width: 2.25rem
}

.w-\[450px\] {
    width: 450px
}

.w-auto {
    width: auto
}

.w-full {
    width: 100%
}

.w-screen {
    width: 100vw
}

.max-w-none {
    max-width: none
}

.shrink-0 {
    flex-shrink: 0
}

.grow {
    flex-grow: 1
}

.rotate-0 {
    --tw-rotate: 0deg
}

.rotate-0,
.rotate-90 {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.rotate-90 {
    --tw-rotate: 90deg
}

.scale-0 {
    --tw-scale-x: 0;
    --tw-scale-y: 0
}

.scale-0,
.scale-100 {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.scale-100 {
    --tw-scale-x: 1;
    --tw-scale-y: 1
}

.transform {
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

@keyframes circle-appear {
    0% {
        opacity: 0;
        transform: rotate(-70deg) scale(1)
    }

    70% {
        opacity: 1;
        transform: rotate(0deg) scale(1.2)
    }

    to {
        opacity: 1;
        transform: rotate(0deg) scale(1)
    }
}

.animate-circle-appear {
    animation: circle-appear .2s linear
}

.grid-flow-col {
    grid-auto-flow: column
}

.grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr))
}

.grid-cols-6 {
    grid-template-columns: repeat(6, minmax(0, 1fr))
}

.grid-cols-8 {
    grid-template-columns: repeat(8, minmax(0, 1fr))
}

.grid-rows-4 {
    grid-template-rows: repeat(4, minmax(0, 1fr))
}

.flex-col {
    flex-direction: column
}

.flex-wrap {
    flex-wrap: wrap
}

.items-start {
    align-items: flex-start
}

.items-center {
    align-items: center
}

.items-stretch {
    align-items: stretch
}

.justify-start {
    justify-content: flex-start
}

.justify-center {
    justify-content: center
}

.justify-between {
    justify-content: space-between
}

.gap-1 {
    gap: .25rem
}

.gap-4 {
    gap: 1rem
}

.gap-\[1px\] {
    gap: 1px
}

.gap-x-2 {
    -moz-column-gap: .5rem;
    column-gap: .5rem
}

.gap-x-4 {
    -moz-column-gap: 1rem;
    column-gap: 1rem
}

.gap-y-2 {
    row-gap: .5rem
}

.gap-y-4 {
    row-gap: 1rem
}

.gap-y-8 {
    row-gap: 2rem
}

.self-center {
    align-self: center
}

.self-stretch {
    align-self: stretch
}

.overflow-hidden {
    overflow: hidden
}

.overflow-x-auto {
    overflow-x: auto
}

.rounded {
    border-radius: .25rem
}

.rounded-md {
    border-radius: .375rem
}

.rounded-sm {
    border-radius: .125rem
}

.border-\[2px\] {
    border-width: 2px
}

.border-\[var\(--accent-9\)\] {
    border-color: var(--accent-9)
}

.border-\[var\(--gray-10\)\] {
    border-color: var(--gray-10)
}

.bg-black\/40 {
    background-color: rgba(0, 0, 0, .4)
}

.bg-white\/80 {
    background-color: hsla(0, 0%, 100%, .8)
}

.bg-gradient-to-br {
    background-image: linear-gradient(to bottom right, var(--tw-gradient-stops))
}

.bg-gradient-to-r {
    background-image: linear-gradient(to right, var(--tw-gradient-stops))
}

.from-\[\#f59e0b\] {
    --tw-gradient-from: #f59e0b var(--tw-gradient-from-position);
    --tw-gradient-to: rgba(245, 158, 11, 0) var(--tw-gradient-to-position);
    --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to)
}

.from-\[\#fde68a\] {
    --tw-gradient-from: #fde68a var(--tw-gradient-from-position);
    --tw-gradient-to: hsla(48, 97%, 77%, 0) var(--tw-gradient-to-position);
    --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to)
}

.from-\[var\(--gray-4\)\] {
    --tw-gradient-from: var(--gray-4) var(--tw-gradient-from-position);
    --tw-gradient-to: hsla(0, 0%, 100%, 0) var(--tw-gradient-to-position);
    --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to)
}

.to-\[\#d97706\] {
    --tw-gradient-to: #d97706 var(--tw-gradient-to-position)
}

.to-\[\#fecaca\] {
    --tw-gradient-to: #fecaca var(--tw-gradient-to-position)
}

.to-\[var\(--gray-8\)\] {
    --tw-gradient-to: var(--gray-8) var(--tw-gradient-to-position)
}

.p-4 {
    padding: 1rem
}

.px-3 {
    padding-left: .75rem;
    padding-right: .75rem
}

.pb-4 {
    padding-bottom: 1rem
}

.pb-5 {
    padding-bottom: 1.25rem
}

.pb-6 {
    padding-bottom: 1.5rem
}

.pt-20 {
    padding-top: 5rem
}

.pt-4 {
    padding-top: 1rem
}

.text-4xl {
    font-size: 2.25rem;
    line-height: 2.5rem
}

.text-sm {
    font-size: .875rem;
    line-height: 1.25rem
}

.text-xl {
    font-size: 1.25rem;
    line-height: 1.75rem
}

.font-medium {
    font-weight: 500
}

.italic {
    font-style: italic
}

.leading-none {
    line-height: 1
}

.text-\[var\(--accent-10\)\] {
    color: var(--accent-10)
}

.text-\[var\(--accent-9\)\] {
    color: var(--accent-9)
}

.text-\[var\(--gray-11\)\] {
    color: var(--gray-11)
}

.text-\[var\(--gray-9\)\] {
    color: var(--gray-9)
}

.text-neutral-950 {
    --tw-text-opacity: 1;
    color: rgb(10 10 10/var(--tw-text-opacity))
}

.opacity-25 {
    opacity: .25
}

.opacity-75 {
    opacity: .75
}

.shadow {
    --tw-shadow: 0 1px 3px 0 rgba(0, 0, 0, .1), 0 1px 2px -1px rgba(0, 0, 0, .1);
    --tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color)
}

.shadow,
.shadow-md {
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)
}

.shadow-md {
    --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, .1), 0 2px 4px -2px rgba(0, 0, 0, .1);
    --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color)
}

.outline {
    outline-style: solid
}

.transition-all {
    transition-property: all;
    transition-timing-function: cubic-bezier(.4, 0, .2, 1);
    transition-duration: .15s
}

:is(.dark .dark\:-rotate-90) {
    --tw-rotate: -90deg;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

:is(.dark .dark\:rotate-0) {
    --tw-rotate: 0deg;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

:is(.dark .dark\:scale-0) {
    --tw-scale-x: 0;
    --tw-scale-y: 0;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

:is(.dark .dark\:scale-100) {
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

:is(.dark .dark\:text-neutral-950) {
    --tw-text-opacity: 1;
    color: rgb(10 10 10/var(--tw-text-opacity))
}

@media (min-width:640px) {
    .sm\:px-12 {
        padding-left: 3rem;
        padding-right: 3rem
    }
}

@media (min-width:1024px) {
    .lg\:px-24 {
        padding-left: 6rem;
        padding-right: 6rem
    }
}

@media (min-width:1280px) {
    .xl\:w-96 {
        width: 24rem
    }

    .xl\:flex-row {
        flex-direction: row
    }
}

@keyframes smallwave {
    0% {
        transform: rotate(0deg) scale(1);
        opacity: .8
    }

    50% {
        transform: rotate(180deg) scale(.95);
        opacity: .25
    }

    to {
        transform: rotate(1turn) scale(1);
        opacity: .8
    }
}

.coral-waves {
    position: relative
}

.coral-waves .Coralwave {
    position: absolute;
    content: "";
    top: 1rem;
    left: 50%;
    width: 10rem;
    height: 10rem;
    margin-left: -5rem;
    border-radius: 42.5%;
    transform-origin: 50% 50%;
    transition: all 1s ease, top 1.5s ease
}

.coral-waves .Coralwave1 {
    background-color: var(--green-8);
    animation: smallwave 3s linear infinite
}

.coral-waves .Coralwave2 {
    background: var(--red-8);
    animation: smallwave 4s linear infinite
}

.coral-waves .Coralwave3 {
    background: var(--blue-8);
    animation: smallwave 5s linear infinite
}

.coral-waves:hover .Coralwave {
    top: .5rem
}
</style>
</head>
<body class="__className_20951f" >
<div data-is-root-theme="true" data-accent-color="violet" data-gray-color="mauve" data-has-background="false" data-panel-background="translucent" data-radius="medium" data-scaling="100%" class="radix-themes">
<div class="flex gap-x-4 rt-r-ai-center">
    <button id="renderAndDownloadBtn" class="rt-reset-button rt-reset-a rt-BaseButton rt-Button rt-r-size-2 rt-variant-surface">
        <svg width="15" height="15" viewBox="0 0 15 15" fill="none"
            xmlns="http://www.w3.org/2000/svg">
            <path d="M7.50005 1.04999C7.74858 1.04999 7.95005 1.25146 7.95005 1.49999V8.41359L10.1819 6.18179C10.3576 6.00605 10.6425 6.00605 10.8182 6.18179C10.994 6.35753 10.994 6.64245 10.8182 6.81819L7.81825 9.81819C7.64251 9.99392 7.35759 9.99392 7.18185 9.81819L4.18185 6.81819C4.00611 6.64245 4.00611 6.35753 4.18185 6.18179C4.35759 6.00605 4.64251 6.00605 4.81825 6.18179L7.05005 8.41359V1.49999C7.05005 1.25146 7.25152 1.04999 7.50005 1.04999ZM2.5 10C2.77614 10 3 10.2239 3 10.5V12C3 12.5539 3.44565 13 3.99635 13H11.0012C11.5529 13 12 12.5528 12 12V10.5C12 10.2239 12.2239 10 12.5 10C12.7761 10 13 10.2239 13 10.5V12C13 13.1041 12.1062 14 11.0012 14H3.99635C2.89019 14 2 13.103 2 12V10.5C2 10.2239 2.22386 10 2.5 10Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path>
        </svg>Download</button>
    <div id="downloadMessage"></div>
</div>
<div class="mt-4 rt-reset-a rt-reset-button w-full overflow-x-auto undefined rt-r-size-1 rt-variant-surface">
    <div class="rt-CardInner">
        <div class="flex flex-col items-stretch gap-y-4 -mb-3">
            <div dir="ltr" class="rt-ScrollAreaRoot"
                style="position: relative; --radix-scroll-area-corner-width: 0px; --radix-scroll-area-corner-height: 0px;">
                <style>
                    [data-radix-scroll-area-viewport] {
                        scrollbar-width: none;
                        -ms-overflow-style: none;
                        -webkit-overflow-scrolling: touch;
                    }

                    [data-radix-scroll-area-viewport]::-webkit-scrollbar {
                        display: none
                    }
                </style>
                <div data-radix-scroll-area-viewport="" class="rt-ScrollAreaViewport" style="overflow: scroll hidden;">
                    <div style="min-width: 100%; display: table">
                        <div class="flex gap-4 pb-5">
'''

page_begin = '''
                            <div class="md-page">
                                <div class="to-image-section">
                                    <div class="box-border p-4"
                                        style="background-image: linear-gradient(to right bottom, {}, {}); width: {}px; height: {}px;">
                                        <div class="p-4 rounded bg-white/80 shadow h-full box-border">
                                            <div class="prose w-full max-w-none undefined"
                                                style="--tw-prose-headings: {}; --tw-prose-body: {}; --tw-prose-quotes: #6b7280; --tw-prose-bold: {}; --tw-prose-code: {}; --tw-prose-bullets: {}; --tw-prose-quote-borders: {}; --tw-prose-hr: {};">
'''

page_end = '''
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
'''

html_end = '''
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
<script>
    document.getElementById('renderAndDownloadBtn').addEventListener('click', function() {
        const pages = document.querySelectorAll('.md-page');
        const downloadMessage = document.getElementById('downloadMessage');
        downloadMessage.innerHTML = '正在下载...';
        
        let downloadCount = 0;
        let completedCount = 0;

        const prefix = generateRandomPrefix();
        function downloadPage(page, index) {
            return new Promise((resolve, reject) => {
                domtoimage.toBlob(page)
                    .then(function(blob) {
                        const filename = `${prefix}_${index + 1}.png`;
                        const link = document.createElement('a');
                        link.download = filename;
                        link.href = URL.createObjectURL(blob);
                        document.body.appendChild(link);
                        link.click();
                        document.body.removeChild(link);

                        completedCount++;
                        const progress = `正在下载 ${completedCount} / ${pages.length} 图片...`;
                        downloadMessage.innerHTML = progress;

                        resolve(); // Resolve the promise once download completes
                    })
                    .catch(function(error) {
                        console.error('Error rendering page to image:', error);
                        reject(error); // Reject the promise if an error occurs
                    });
            });
        }

        // Sequentially download each page
        function downloadAllPages() {
            downloadPage(pages[downloadCount], downloadCount)
                .then(function() {
                    downloadCount++;
                    if (downloadCount < pages.length) {
                        downloadAllPages(); // Recursively download next page
                    } else {
                        // All downloads completed
                        downloadMessage.innerHTML = `共下载 ${completedCount} 张图片`;
                        setTimeout(() => {
                            downloadMessage.innerHTML = ''; // Clear message after 3 seconds
                        }, 3000);
                    }
                })
                .catch(function(error) {
                    console.error('Error downloading page:', error);
                });
        }

        // Function to generate a random 4-character alphanumeric prefix
        function generateRandomPrefix() {
            const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
            let result = '';
            for (let i = 0; i < 4; i++) {
                result += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            return result;
        }

        // Start downloading pages
        downloadAllPages();
    });
</script>
</html>
'''

editor_prompt = '''# 在这里输入文本，开始吧！'''

st.sidebar.title('设置')

width = st.sidebar.number_input('图片宽度', min_value=100, value=600, step=1)
height = st.sidebar.number_input('图片高度', min_value=100, value=800, step=1)

bg_gradient = st.sidebar.checkbox('使用渐变背景', True)
if bg_gradient:
    c1, c2 = st.sidebar.columns(2)
    bg_color = c1.color_picker('左上颜色', '#ffecd2', key='bg_color')
    bg_color2 = c2.color_picker('右下颜色', '#fcb69f', key='bg_color2')
else:
    bg_color = st.sidebar.color_picker('背景颜色', '#fcb69f', key='bg_color')
    bg_color2 = bg_color

accent_color = st.sidebar.color_picker('主色调', '#f97316', key='accent_color')
text_color = st.sidebar.color_picker('文本颜色', '#111827', key='text_color')

page_begin = page_begin.format(bg_color, bg_color2, width, height, accent_color, text_color, accent_color, accent_color, accent_color, accent_color, accent_color)

st.subheader('Markdown文章编辑和图片生成器')

if st.sidebar.button('生成随机内容'):
    random_str = requests.get('https://jaspervdj.be/lorem-markdownum/markdown.txt').text
    with st.expander('**展开查看随机生成的内容**'):
        st.code(random_str, language='markdown')

with st.expander('**编辑使用说明：** "---" 分页，按 ”Ctrl-Enter“ 或 ”Command-Enter“ 预览效果', expanded=True):
    md_str = st.text_area('Markdown', placeholder=editor_prompt, height=400, label_visibility='collapsed')

md_pages = md_str.split('\n---')
page_str = [
    md.markdown(
        page_str,
        extensions=['extra', 'abbr', 'attr_list', 'def_list', 'fenced_code', 'footnotes', 'tables',
                    'admonition', 'codehilite', 'meta', 'nl2br', 'sane_lists', 'smarty', 'toc', 'wikilinks',
                    'pymdownx.arithmatex', 'pymdownx.betterem', 'pymdownx.caret', 'pymdownx.details',
                    'pymdownx.emoji', 'pymdownx.keys', 'pymdownx.magiclink', 'pymdownx.mark',
                    'pymdownx.smartsymbols', 'pymdownx.superfences', 'pymdownx.tasklist', 'pymdownx.tilde'])
    for page_str in md_pages
]
html_str = ['\n'.join([page_begin, x, page_end]) for x in page_str]
html_str = '\n'.join([html_begin, *html_str, html_end])

html(html_str, height=height+50)

st.markdown('---')
st.markdown('**Credit:** This tool is inspired by https://breditor.vercel.app, and the random markdown content is generated by [lorem-markdownum](https://jaspervdj.be/lorem-markdownum/).')