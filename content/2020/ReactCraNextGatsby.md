Title: React starters: CRA vs Next vs Gatsby
Date: 2099-01-01 00:00
Category: Develop
Tags: #react, #gatsby, #next, #cra, #ssr

Next.js vs Gatsby vs create-react-app

* [Create a New React App – Recommended Toolchains](https://reactjs.org/docs/create-a-new-react-app.html#recommended-toolchains)
* [The Next.js Handbook](https://www.freecodecamp.org/news/the-next-js-handbook/#next-js-vs-gatsby-vs-create-react-app)
    * CRA: CLI When you don't need Server-Side-Rendering (SSR)
    * Gatsby: When you don't deploy a backend (static site), but API is somewhere else
    * CNA - Next: Cli When you do need Node.js backend
    * Neutrino
        * Both for Apps and Libs
        * React, Preact, Vue, Web
    * Parcel - for web
    * Razzle
    * CRL: CLI For creating React component libraries with (or without) TypeScript
* [When to Use Static Generation (Gatsby) v.s. Server-side Rendering (Next)](https://next-learn-starter.now.sh/posts/ssg-ssr)

# Individual starters

* [CRA - Create React App](https://create-react-app.dev/)
    * App CLI: `npx create-react-app my-app --template typescript --use-npm` - [Getting Started](https://create-react-app.dev/docs/getting-started)
* [CRA using Ionic components](https://ionicframework.com/)
    * [App CLI:](https://ionicframework.com/docs/cli/commands/start)
    ```bash
    npm install -g @ionic/cli
    ionic start my-app tabs --type=react --no-deps
    ```
* [GatsbyJS](https://www.gatsbyjs.org/)
    * [App CLI:](https://www.gatsbyjs.org/docs/quick-start/)  
    ```bash
    npm install -g gatsby-cli
    gatsby new my-app
    ```
* [CNA - Next.js](https://nextjs.org/)
    * App CLI: `npm init next-app nextjs-blog --example "https://github.com/zeit/next-learn-starter/tree/master/learn-starter --use-npm"` - [Create a Next.js App](https://nextjs.org/learn/basics/create-nextjs-app/setup)
    * Guide: [The Next.js Handbook](https://www.freecodecamp.org/news/the-next-js-handbook/)
* [CRL - create-react-library](https://www.npmjs.com/package/create-react-library)
    * Lib CLI: `npx create-react-library --template typescript --mananger npm` - [create-react-library](https://www.npmjs.com/package/create-react-library)
* [Neutrino](https://neutrinojs.org/)
    * Lib CLI: `npx @neutrinojs/create-project my-lib`- @neutrinojs/react-components - [React Components - Neutrino](https://neutrinojs.org/packages/react-components/)
    * App CLI: `npx @neutrinojs/create-project my-app` - @neutrinojs/react - [React - Neutrino](https://neutrinojs.org/packages/react/)
* [Parcel](https://parceljs.org/getting_started.html)

# Alternative CLI starting

```bash
# install CLI
npm install -g create-react-app
# and use CLI
create-react-app my-app

# or use npx
npx create-react-app my-app

# or use npm
npm init react-app my-app

# or use yarn
yarn create react-app my-app
```

The end