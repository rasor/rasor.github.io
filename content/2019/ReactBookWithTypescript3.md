Title: Notes from book 'Learn React with TypeScript 3'
Date: 2099-01-01 00:00
Category: Develop
Tags: #react

Notes from 

* Vid 2019-10: [React Hooks](https://subscription.packtpub.com/video/web_development/9781839210075)
    * [PacktPublishing/React-Hooks](https://github.com/PacktPublishing/React-Hooks)
* Vid 2019-10: [Awesome Apps with React Hooks and Firebase](https://subscription.packtpub.com/video/web_development/9781839211348)
    * [PacktPublishing/Awesome-Apps-with-React-Hooks-and-Firebase](https://github.com/PacktPublishing/Awesome-Apps-with-React-Hooks-and-Firebase)
* Book 2018-11: [Learn React with TypeScript 3](https://www.packtpub.com/web-development/learn-react-typescript-3)  
    * [PacktPublishing/Learn-React-with-TypeScript-3](https://github.com/PacktPublishing/Learn-React-with-TypeScript-3)

I have pushed some code to 

* [rasor/react-stencil-poc](https://github.com/rasor/react-stencil-poc)
* [rasor/my-react-ts-app](https://github.com/rasor/my-react-ts-app)

```bash
# running on
node -v
# v10.16.2

# create react code
npx create-react-app my-react-ts-app --typescript
# We detected TypeScript in your project (src/App.test.tsx) and created a tsconfig.json file for you.
# Your tsconfig.json has been populated with default values.
# Success! Created my-react-ts-app at /home/rasor/e-toshiba/projs-react/my-react-ts-app
# Inside that directory, you can run several commands:
#   npm start        #     Starts the development server.
#   npm run build    #     Bundles the app into static files for production.
#   npm test         #     Starts the test runner.
#   npm run eject    #     Removes this tool and copies build dependencies, configuration files and scripts into the app directory. If you do this, you can’t go back!

# Enter the project folder
cd my-react-ts-app

# 1st run - incl download and build
npm start

# Commit locally
git add .
git commit -m "first commit"

# push to new empty repo
git remote add origin git@github.com:yourgithub/my-react-ts-app.git
git push -u origin master

# add lint
npm install tslint tslint-react tslint-config-prettier --save-dev

# open editor
code .
```

Add file `tslint.json`

```json
{
    "extends": ["tslint:recommended", "tslint-react", "tslint-config-prettier"],
    "rules": {
      "ordered-imports": false,
      "object-literal-sort-keys": false,
      "no-debugger": false,
      "no-console": false
    },
    "linterOptions": {
      "exclude": [
        "config/**/*.js",
        "node_modules/**/*.ts",
        "coverage/lcov-report/*.js"
      ]
    }
  }
```

## Using WebComponents in React

index.tsx:
```ts
import { defineCustomElements } from 'my-stencil-components/loader';

ReactDOM.render(<App />, document.getElementById('root'));

defineCustomElements(window);
```

declarations.d.ts:
```ts
// Load my-component for untyped elements
import 'my-stencil-components'

// Load my-component for typed elements
import { JSX as ExtJSX } from 'my-stencil-components'

export declare global {
    namespace JSX {
        // From /my-stencil-app/node_modules/@stencil/core/dist/index.d.ts
        // Untyped elements
        interface IntrinsicElements extends d.JSX.IntrinsicElements, d.JSXBase.IntrinsicElements {
            [tagName: string]: any;
        }
        // Typed elements from imported webcomponent
        interface IntrinsicElements extends ExtJSX.IntrinsicElements{}
    }
}
```

Home.tsx
```ts
import { Person } from 'my-stencil-components/dist/types/models/person';

const Home: React.FC = () => {
  const pers: Person = {
    email: 'donald.duck@andeby.disney',
    name: 'Donald Duck',
    position: '0',
    photo: ''
  };
  const commonProps = {person: pers};
  return (
      {/* Soon a sln? https://github.com/skatejs/skatejs/issues/1058#issuecomment-275851441 */}
      {/* https://stackoverflow.com/a/49081745/750989 */}
       {pers && <my-component first="External Stencil" last="'Don't call me a framework' JS" {...commonProps}></my-component>}
     {/* {pers && <my-component first="External Stencil" last="'Don't call me a framework' JS" person={pers}></my-component>} */}
  )
```

* [ionic-team/ionic](https://github.com/ionic-team/ionic/blob/master/packages/react/src/components/utils/attachProps.ts)
* [Passing state through the props object in React](https://dev.to/cesareferrari/passing-state-through-the-props-object-in-react-5fmm)
* [Can I use JSX to pass an object to an attribute? · Issue #1058 · skatejs/skatejs](https://github.com/skatejs/skatejs/issues/1058#issuecomment-275851441)
* [Web Components – React](https://reactjs.org/docs/web-components.html)
* [Refs and the DOM – React](https://reactjs.org/docs/refs-and-the-dom.html)
* [Forwarding Refs – React](https://reactjs.org/docs/forwarding-refs.html#forwarding-refs-to-dom-components)
* [How to use Web Components in React](https://vaadin.com/learn/tutorials/using-web-components-in-react)
    * Includes: @webcomponents/webcomponentsjs vendor-copy
    * [@webcomponents/webcomponentsjs](https://www.npmjs.com/package/@webcomponents/webcomponentsjs)
* [Custom Elements Everywhere](https://custom-elements-everywhere.com/)
* [Stencil 4 React](https://stenciljs.com/docs/react)
* [Stencil 4 JS](https://stenciljs.com/docs/javascript)
* [Direflow](https://direflow.io/)

## Ionic React

* [@ionic/react](https://www.npmjs.com/package/@ionic/react)
* [Ionic React - First Look](https://dev.to/dabit3/ionic-react-first-look-104l)
* [Announcing Ionic React Hooks](https://ionicframework.com/blog/announcing-ionic-react-hooks/)

## Links

* React - guide: [React – A JavaScript library for building user interfaces](https://reactjs.org/)
    * [Getting Started – React](https://reactjs.org/docs/getting-started.html)
        * [Getting Started with React - An Overview and Walkthrough Tutorial](https://www.taniarascia.com/getting-started-with-react/)
    * [Tutorial: Intro to React – React](https://reactjs.org/tutorial/tutorial.html)
* Support: [Where To Get Support – React](https://reactjs.org/community/support.html)
    * [Join the Reactiflux Discord Server!](https://discordapp.com/invite/0ZcbPKXt5bZjGY5n)
* React Playground: [Babel · The compiler for next generation JavaScript](https://babeljs.io/repl)
* Create React App (CRA) - guide: [facebook/create-react-app](https://github.com/facebook/create-react-app)
    * User guide: [Create React App · Set up a modern web app by running one command.](https://create-react-app.dev/)
    * [Getting Started · Create React App](https://create-react-app.dev/docs/getting-started)
* TSX:
    * [How to conditionally add attributes to React components?](https://stackoverflow.com/questions/31163693/how-to-conditionally-add-attributes-to-react-components/35428331#35428331)
* TypeScript:
    * 2018-11: [Learn React with TypeScript 3](https://www.packtpub.com/web-development/learn-react-typescript-3)
        * [Online book](https://subscription.packtpub.com/book/web_development/9781789610253)
        * Code: [PacktPublishing/Learn-React-with-TypeScript-3](https://github.com/PacktPublishing/Learn-React-with-TypeScript-3)
* Hooks:
    * Vid 2019-10: [React Hooks](https://subscription.packtpub.com/video/web_development/9781839210075)
    * Why? [Hooks allow you to reuse stateful logic without changing your component hierarchy.](https://reactjs.org/docs/hooks-intro.html#its-hard-to-reuse-stateful-logic-between-components)
        * Removes layers of
            * Providers
            * Consumers
            * [Higher-Order Components (HOC)](https://reactjs.org/docs/higher-order-components.html)
            * [Render Props](https://reactjs.org/docs/render-props.html)
    * [Hooks at a Glance – React](https://reactjs.org/docs/hooks-overview.html)
    * `useLayoutEffect`:
        * [Hooks API Reference](https://reactjs.org/docs/hooks-reference.html#uselayouteffect)
            * Identical to useEffect, but it fires synchronously after all DOM mutations. 
            * Use this to read layout from the DOM and synchronously re-render. 
            * Prefer the standard useEffect when possible to avoid blocking visual updates.
        * `ref.current.setAttribute`: [How to use SVG Icons as React Components?](https://www.robinwieruch.de/react-svg-icon-components)
    * `useRef`:
        * [When?](https://reactjs.org/docs/refs-and-the-dom.html#when-to-use-refs)
            * When can't do it declaratively (**can't use props**) - opposed to **can only call methods** (imperatively)
                * For example, instead of exposing open() and close() methods on a Dialog component, pass an isOpen prop to it (declaratively).
            * Examples:
                * Managing focus, text selection, or media playback.
                * Triggering imperative animations.
                * Integrating with **third-party DOM libraries**.
        * [Hooks API Reference](https://reactjs.org/docs/hooks-reference.html#useref)

        * Using Class: [Refs and the DOM – React](https://reactjs.org/docs/refs-and-the-dom.html#adding-a-ref-to-a-dom-element)
        * [React: Using Refs with the useRef Hook](https://medium.com/@rossbulat/react-using-refs-with-the-useref-hook-884ed25b5c29)
    * `useMemo`: 
        * [Hooks API Reference](https://reactjs.org/docs/hooks-reference.html#usememo)
            * A cache
        * Automatic generation of ids: [Managing ARIA attributes with React hooks](https://medium.com/gronda/managing-aria-attributes-with-react-hooks-a7470d572683)
* Default Props:
    * Blog 2019-01 [Understanding React Default Props](https://blog.bitsrc.io/understanding-react-default-props-5c50401ed37d?gi=ae3da137374d)
    * Blog 2019-07 [React defaultProps is dying, who’s the contender?](https://medium.com/@matanbobi/react-defaultprops-is-dying-whos-the-contender-443c19d9e7f1)
* React and WebComponents:
    * [Web Components – React](https://reactjs.org/docs/web-components.html)
    * [rasor/react-stencil-poc](https://github.com/rasor/react-stencil-poc/blob/master/my-ionic-react-app/src/pages/Home.tsx)
    * [Can I use JSX to pass an object to an attribute?](https://github.com/skatejs/skatejs/issues/1058#issuecomment-275851441)
    * [How Lazy-Loading Web Components Work with Stencil](https://stenciljs.com/blog/how-lazy-loading-web-components-work)
* Lazy Loading:
    * [Lazy Loading React Components (with react.lazy and suspense)](https://blog.bitsrc.io/lazy-loading-react-components-with-react-lazy-and-suspense-f05c4cfde10c)
    * [How Lazy-Loading Web Components Work with Stencil](https://stenciljs.com/blog/how-lazy-loading-web-components-work)
    * [Preloading modules - Google Developers](https://developers.google.com/web/updates/2017/12/modulepreload)
* Authentication:
    * Blog 2019-04 [React (without Redux) - JWT Authentication](https://jasonwatmore.com/post/2019/04/06/react-jwt-authentication-tutorial-example)
    * Blog 2019-02 [How To Implement OIDC Authentication with React Context API and React Router](https://medium.com/@franciscopa91/how-to-implement-oidc-authentication-with-react-context-api-and-react-router-205e13f2d49)
* IFrame Headers:
    * [enriquemorenotent/react-auth-iframe](https://github.com/enriquemorenotent/react-auth-iframe)
    * [Is it possible to add Request Headers to an iframe src request?](https://stackoverflow.com/questions/13432821/is-it-possible-to-add-request-headers-to-an-iframe-src-request/42280739#42280739)
* npm runner (npx): [Introducing npx: an npm package runner](https://blog.npmjs.org/post/162869356040/introducing-npx-an-npm-package-runner)
    * Exec js gist: [npx is cool](https://gist.github.com/zkat/4bc19503fe9e9309e2bfaa2c58074d32)
        * [Building command line tools with Node.js - Atlassian Developer Blog](https://blog.developer.atlassian.com/scripting-with-node/)
    * Depricated: [node-bin](https://www.npmjs.com/package/node-bin)
        * Replaced by engines?[npm-package.json](https://docs.npmjs.com/files/package.json#engines)
            * Probably requires `n`: [How to change to an older version of Node.js | Codementor](https://www.codementor.io/victor-nizeyimana/how-to-change-to-an-older-version-of-node-js-ofs3xt53n)
    * Compile and Exec Babel: [@babel/node · Babel](https://babeljs.io/docs/en/babel-node)

The End