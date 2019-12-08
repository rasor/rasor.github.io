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


## Links

* Hooks:
    * Vid 2019-10: [React Hooks](https://subscription.packtpub.com/video/web_development/9781839210075)
    * [Hooks at a Glance – React](https://reactjs.org/docs/hooks-overview.html)
    * `useLayoutEffect`:
        * [Hooks API Reference – React](https://reactjs.org/docs/hooks-reference.html#uselayouteffect)
            * Identical to useEffect, but it fires synchronously after all DOM mutations. 
            * Use this to read layout from the DOM and synchronously re-render. 
            * Prefer the standard useEffect when possible to avoid blocking visual updates.
        * `ref.current.setAttribute`: [How to use SVG Icons as React Components?](https://www.robinwieruch.de/react-svg-icon-components)
    * `useRef`:
        * [Hooks API Reference – React](https://reactjs.org/docs/hooks-reference.html#useref)
        * [React: Using Refs with the useRef Hook](https://medium.com/@rossbulat/react-using-refs-with-the-useref-hook-884ed25b5c29)
    * `useMemo`: 
        * [Hooks API Reference – React](https://reactjs.org/docs/hooks-reference.html#usememo)
            * A cache
        * Automatic generation of ids: [Managing ARIA attributes with React hooks](https://medium.com/gronda/managing-aria-attributes-with-react-hooks-a7470d572683)
* TSX:
    * [How to conditionally add attributes to React components?](https://stackoverflow.com/questions/31163693/how-to-conditionally-add-attributes-to-react-components/35428331#35428331)
* 2018-11: [Learn React with TypeScript 3](https://www.packtpub.com/web-development/learn-react-typescript-3)
    * [Online book](https://subscription.packtpub.com/book/web_development/9781789610253)
    * Code: [PacktPublishing/Learn-React-with-TypeScript-3](https://github.com/PacktPublishing/Learn-React-with-TypeScript-3)
* React Playground: [Babel · The compiler for next generation JavaScript](https://babeljs.io/repl)
* npm runner: [Introducing npx: an npm package runner](https://blog.npmjs.org/post/162869356040/introducing-npx-an-npm-package-runner)
    * Exec js gist: [npx is cool](https://gist.github.com/zkat/4bc19503fe9e9309e2bfaa2c58074d32)
        * [Building command line tools with Node.js - Atlassian Developer Blog](https://blog.developer.atlassian.com/scripting-with-node/)
    * Depricated: [node-bin](https://www.npmjs.com/package/node-bin)
        * Replaced by engines?[npm-package.json](https://docs.npmjs.com/files/package.json#engines)
            * Probably requires `n`: [How to change to an older version of Node.js | Codementor](https://www.codementor.io/victor-nizeyimana/how-to-change-to-an-older-version-of-node-js-ofs3xt53n)
    * Compile and Exec Babel: [@babel/node · Babel](https://babeljs.io/docs/en/babel-node)
* Create React App - guide: [facebook/create-react-app](https://github.com/facebook/create-react-app)
    * User guide: [Create React App · Set up a modern web app by running one command.](https://create-react-app.dev/)
    * [Getting Started · Create React App](https://create-react-app.dev/docs/getting-started)
* React - guide: [React – A JavaScript library for building user interfaces](https://reactjs.org/)
    * [Getting Started – React](https://reactjs.org/docs/getting-started.html)
        * [Getting Started with React - An Overview and Walkthrough Tutorial](https://www.taniarascia.com/getting-started-with-react/)
    * [Tutorial: Intro to React – React](https://reactjs.org/tutorial/tutorial.html)
* Support: [Where To Get Support – React](https://reactjs.org/community/support.html)
    * [Join the Reactiflux Discord Server!](https://discordapp.com/invite/0ZcbPKXt5bZjGY5n)


The End