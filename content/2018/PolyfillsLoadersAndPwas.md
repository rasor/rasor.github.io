Title: Using js polyfills, dependency managers and PWAs
Date: 2099-01-01 00:00
Category: Develop
Tags: #polyfills, #loader, #webcomponents, #pwa, #polymer, #ionic, #stencil, #preact

# Polyfills

Using new cool javascript features and frameworks requires polyfills for the browsers, that don't support them.

And how do you then do it?

There can be several strategies.  
I am currently looking at this

1. Add Global Fallback for non-supported browsers
2. Use polyfills.io to determine which polyfills to return to the browser based on the browser agent - with a swich
3. Load a framework including what it includes of polyfills
4. Load my own code

## Ad 1.

IE is often target for fallbacks. You can use [IE conditional comments].(https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/HTML_and_CSS#IE_conditional_comments)

## Ad 2. 

With the IE condition above you can load special polyfils using polyfill.io and [overriding the user-agent](https://polyfill.io/v2/docs/examples#override-ua).  
Otherwise then just use [basic case](https://polyfill.io/v2/docs/examples#basic).  

## Ad 3

When using polyfill.io [her are two ways of loading polyfills.io](https://polyfill.io/v2/docs/examples#feature-detection) before you code

* Using a callback or perhasp an [onload event on script tag](https://stackoverflow.com/questions/16230886/trying-to-fire-the-onload-event-on-script-tag) or a [Script Loader](https://davidwalsh.name/javascript-loader)
* Pre-specify needed features in  [client-side feature detection](https://output.jsbin.com/sufiboz/)
* But recommended is to use [server-side feature detection](https://webplatform.github.io/docs/concepts/Detecting_device_and_browser/)
 using the user-agent to serve different pages and polifills according to browser

## Read More

* [Internet Explorer Conditional Comments](https://www.sitepoint.com/internet-explorer-conditional-comments/)
* MooTools can be used on top of JQuery as polyfill for HTML and CSS: [mdn/learning-area](https://github.com/mdn/learning-area/blob/master/tools-testing/cross-browser-testing/html-css/selectivizr-example.html)
* Check which features you can use in a certain browser: [HTML5 Please - Use the new and shiny responsibly](http://html5please.com/)
* Load js from a server: [jQuery.getScript()](http://api.jquery.com/jQuery.getScript/)
* ES5 polyfill: [es-shims/es5-shim](https://github.com/es-shims/es5-shim) for IE7
* ES5 polyfill: [@babel/polyfill · Babel](https://babeljs.io/docs/en/babel-polyfill/) for IE7

# Frameworks and tools

## Polyfills and PWA

PWA's delivers [progressive enhancement](https://ionicframework.com/docs/developer-resources/progressive-web-apps/) meaning they provide some sort of fallback for unsupported features. But if your PWA don't support a feature, you might still want to enable the feature using extra polyfills.

Demo PWA's: [HNPWA](https://hnpwa.com/)

## Stencil (WebComponent and PWA compiler)

[Browser Support](https://github.com/ionic-team/stencil#browser-support)

* Chrome (and all Chromium based browsers)
* Safari
* Edge
* Firefox
* IE 11

PWA Demo code:[ionic-team/ionic-stencil-hn-app](https://github.com/ionic-team/ionic-stencil-hn-app)

### Ionic V4 Beta

[Browser Support](https://beta.ionicframework.com/docs/intro/browser-support)

* Mobile
    * iOS 10+
    * Android 4.4+
* Browser
    * Safari
    * Chrome
    * Edge
    * Firefox

PWA:  
* [Ionic PWA Toolkit Beta](https://blog.ionicframework.com/announcing-the-ionic-pwa-toolkit-beta/)
* [Ionic Framework - Pwa-toolkit](https://ionicframework.com/pwa/toolkit)
* [ionic-team/ionic-pwa-toolkit](https://github.com/ionic-team/ionic-pwa-toolkit)

## Ionic V3

[Browser Support](https://ionicframework.com/docs/intro/browser-support/)

* Mobile
    * iOS 8+
    * Windows 10 Universal App
    * Android 4.4+
* Browser
    * Safari
    * Chrome
    * Edge

## WebComponets

[webcomponents.org](https://www.webcomponents.org/polyfills)  
[Browser Support](https://github.com/WebComponents/webcomponentsjs#browser-support)
* Edge
* IE11+
* Chrome
* Firefox
* Safari 9+
* Chrome Android
* Mobile Safari

### Polymer V1

[Browser Support](https://www.polymer-project.org/1.0/docs/browsers)

* Chrome
* Firefox
* IE 11+/Edge
* Safari 7+
* Chrome (Android)
* Safari (iOS 7.1)

### Polymer V3

PWA:  
* [Polymer App Toolbox - Polymer Project](https://www.polymer-project.org/3.0/toolbox/)
* [Polymer 3.0 released at I/O, accelerates PWA development](https://react-etc.net/entry/polymer-3-0-released-io-accelerates-pwa-development)
* [Polymer/pwa-starter-kit](https://github.com/Polymer/pwa-starter-kit/blob/master/README.md)

## Preact

[Browser Support](https://preactjs.com/about/browser-support)

* Chrome 10
* Firefox 10
* IE 7+
* Edge 10
* Safari 10.11

PWA:  
* [Overiew](https://preactjs.com/guide/progressive-web-apps)
* [developit/preact-cli](https://github.com/developit/preact-cli)

# Testing

* [WebPagetest - Website Performance and Optimization Test](https://www.webpagetest.org/easy) with the `Run Lighthouse Audit` option turned on.
* Using above: [Guide to Web Performance Using WebPageTest - Zoompf Web Performance](https://zoompf.com/blog/2015/07/the-seo-experts-guide-to-web-performance-using-webpagetest-2/)
* [Lighthouse ](https://developers.google.com/web/tools/lighthouse/)

The End.