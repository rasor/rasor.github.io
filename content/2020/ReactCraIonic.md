Title: React CRA with Ionic and Stencil WebComponents
Date: 2099-01-01 00:00
Category: Develop
Tags: #react, #cra, #ionic, #stencil, #webcomponents, #typescript

# Intro

* **CRA** is create-react-app, which is a React starter template CLI tool.
* **Ionic** is a webcomponet library, which can be used by JS and TypeScript apps in modern browsers.
* **Stencil** is a webcomponet builder tool using TypeScript. It can also can build apps.

## CRA with Ionic

Why is this cool?  
* Ionic is a great mobile-first component lib
* Ionic has great PWA features
* Ionic can be build for native deployments

## CRA with Stencil WebComponents

Why is this cool?  
* You can within CRA use TypeScript to discover properties (attributes)
* You can set typed objects to properties

Why is it not so cool? (compared to using Stencil (or Angular) app as a webcomponent host)
* In Stencil a typed object on an attribute will both be settable and gettable from the host directly in the custom element
* Debugging webcomponents is not a good experience compared to debugging React components

# Starter templates

```bash
# CRA using TypeScript:
npx create-react-app my-cra-typescript-app --template typescript
# More: https://www.pluralsight.com/guides/typescript-react-getting-started

# CRA using TypeScript and Ionic components:
npm install -g ionic
ionic start my-ionic-react-app
# More: https://ionicframework.com/blog/announcing-ionic-react/

# Clone an existing starter template
ionic start my-cloned-app https://github.com/ionic-team/ionic-conference-app

# Stencil Typescript-App - without React:
npm init stencil # – Select app
# More: https://stenciljs.com/docs/getting-started

# Stencil Typescript-App with Ionic components - without React:
npm init stencil # – Select ionic-pwa
# More: https://stenciljs.com/docs/getting-started

# Stencil Typescript-webcomponents:
npm init stencil # – Select component
# More: https://stenciljs.com/docs/getting-started

```

The end
