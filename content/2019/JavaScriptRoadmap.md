Title:  JavaScript Roadmap
Date: 2099-01-01 00:00
Category: Develop
Tags: #javascript

## JavaScript Roadmap

|JavaScript versions - tsconfig - lib, target||Comment|
|---|---|---|
|es3(1999)|||
|es5||Still current in 2019|
|es6/es2015|||
|es2016|||
|es2017|||
|es2018|||
|es2019|||
|esnext|||

## Which module loaders to support

|tsconfig - module||Comment|
|---|---|---|
|none|||
|commonjs||NodeJs - sync loading|
|amd||AMD - async loading|
|system||Both CommonJs and AMD|
|umd||Both CommonJs and AMD|
|es6/es2015||type="module" - can use import in js - build into modern browsers|
|esnext||Comming features|

## Links

* [ECMAScript 6 modules: the final syntax](http://2ality.com/2014/09/es6-modules-final.html)
* [ES6 In Depth: Modules – Mozilla Hacks - the Web developer blog](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/)
* Ref: [Microsoft/TypeScript - Import Declarations](https://github.com/Microsoft/TypeScript/blob/master/doc/spec.md#1132-import-declarations)
* Ref: [Microsoft/TypeScript - Export Declarations](https://github.com/Microsoft/TypeScript/blob/master/doc/spec.md#11342-export-default-declarations)
* Ref: [Compiler Options - TypeScript](https://www.typescriptlang.org/docs/handbook/compiler-options.html)
* Ref: [tsconfig.json - @types, typeRoots and types](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html#types-typeroots-and-types)
* Ref - TS Libs: [Microsoft/TypeScript](https://github.com/Microsoft/TypeScript/tree/master/lib)
* Blog - 2015 [ES5, ES6, ES2016, ES.Next: What's going on with JavaScript versioning?](https://benmccormick.org/2015/09/14/es5-es6-es2016-es-next-whats-going-on-with-javascript-versioning)
* [Learn ES2015 · Babel](https://babeljs.io/docs/en/learn)
* 2016: [A Dive into SystemJS &#8211; Part 1](https://superdevelopment.com/2016/03/16/a-dive-into-systemjs-part-1/)
* [Understanding Module loaders using SystemJs - LearnAngularJS](http://www.learnangularjs.net/understanding-module-loaders-using-systemjs.php)
* [What are differences between SystemJS and Webpack?](https://stackoverflow.com/questions/38263406/what-are-differences-between-systemjs-and-webpack)

Inline modules in <script>

* [ECMAScript modules in browsers](https://jakearchibald.com/2017/es-modules-in-browsers/)
* [The Script element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
* [Inlining ECMAScript Modules in HTML](https://stackoverflow.com/questions/43817297/inlining-ecmascript-modules-in-html)

## Books

* 2017-02: [Mastering TypeScript - Second Edition | PACKT Books](https://www.packtpub.com/application-development/mastering-typescript-second-edition)
* 2015-08: [Learning ECMAScript 6 | PACKT Books](https://www.packtpub.com/web-development/learning-ecmascript-6)
* 2014-07 - Seen from .NET: [Syncfusion Free Ebooks | TypeScript Succinctly](https://www.syncfusion.com/ebooks/typescript)

The End