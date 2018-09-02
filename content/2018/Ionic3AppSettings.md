Title:Ionic 3 AppSettings
Date: 2099-01-01 00:00
Tags: #ionic, #config, #webpack

Ionic3 app-scripts has since version 3.2.0 support of [dotenv-webpack](https://github.com/mrsteele/dotenv-webpack) for supplying config setting for dev and prod.  
This means you can do like this:

```bash
# Build for dev using settings in .env.dev
ionic build --dev
# Build for prod using settings in .env.prod
ionic build --prod --aot
```

Howto do that? See `Setup with dev and prod settings`.  
If you need more environments, then you could use the app-scripts copy script for having more .env files and copy them to root before build.  
Howto do that? Continue in `Setup with more environments`  

# Setup with dev and prod settings

* First create a Ionic3 project

```bash
# Verify if you have latest ionic3 installed
ionic help
# Install latest ionic3, if it is not already installed
npm install -g ionic@3.20.0
# Create a blank project
ionic start ionic3-appsettings blank
# enter project folder
cd .\ionic3-appsettings
# open in VSCode
code .

# Optionally add a readme.md file and a licence file to the project

# Test drive
ionic serve

# Create a project in github with the same name
# Upload your code to github
git remote add origin https://github.com/rasor/ionic3-appsettings.git
git push -u origin master

# Update app-scripts to at least "3.2.0" - but less than 4.0.0
npm update @ionic/app-scripts@3.2.0

```

* Add to file `src/declarations.d.ts`

```typescript
// src/declarations.d.ts
// https://github.com/ionic-team/ionic-app-scripts/pull/1471#issue-210604229
declare var process: { env: { [key: string]: string | undefined; } };
```

* Add a dev file `.env.dev`

```text
// .env.dev
// https://github.com/ionic-team/ionic-app-scripts/pull/1471#issue-210604229

ENVIR_NAME=Development
SOME_KEY=abc-dev
```

* Add a prod file `.env.prod`

```text
// .env.prod
// https://github.com/ionic-team/ionic-app-scripts/pull/1471#issue-210604229

ENVIR_NAME=Production
SOME_KEY=def-prod
```

* Add a property to Home page logic `src/pages/home/home.ts`

```typescript
export class HomePage {

  envirName: string;

  constructor(public navCtrl: NavController) {
    this.envirName = process.env.ENVIR_NAME;
  }
}
```

* Show property in Home page `src/pages/home/home.html`

```html
<ion-content padding>
  <p>You are viewing environment <strong>{{envirName}}</strong></p>
</ion-content>
```

```bash
# Test drive
ionic serve
# It will write 'Development' for envirName
```

```bash
# Build for prod
npm run build --prod --aot
# Now you can drop your /www folder to your prod web server
```

# Setup with more environments

With more environments than dev and prod you need to use the app-scripts copy script.

```bash
# Optionally - to keep the two ways to use .env files separated - create a new branch
# In git create a new branch copy-envs and then switch to it
git checkout -b copy-envs
```

* Move config files from root to /config/

Recommended:  
Add `.env.*` to your `.gitignore` file

### Links 

* [feature(environment configuration) by nphyatt](https://github.com/ionic-team/ionic-app-scripts/pull/1471)
* [dotenv-webpack](https://github.com/mrsteele/dotenv-webpack)
* Modify [app-scripts](https://www.npmjs.com/package/@ionic/app-scripts#command-line-flags)
* [Adding Environment for Ionic 2/3 Projects](https://scotch.io/@chaitanyamankala/adding-environment-for-ionic-23-projects)
* [ionic](https://www.npmjs.com/package/ionic) versions
* [Deploying Ionic to Azure](https://rasor.github.io/deploying-ionic-to-azure.html)

/**
   * [rasor/awesome-tables](https://github.com/rasor/awesome-tables/blob/master/awesome-cli-js.md#nvm-sets-of-tools)
   * https://forum.ionicframework.com/t/configuration-file/46275/7
   * https://ionicframework.com/docs/api/config/Config/
   * https://blogs.msdn.microsoft.com/premier_developer/2018/03/01/angular-how-to-editable-config-files/
   * https://stackoverflow.com/questions/39576991/ionic2-angular2-read-a-custom-config-file
   * https://stackoverflow.com/questions/34986922/define-global-constants-in-angular-2/40287063?noredirect=1#comment72196008_40287063
   *
   * https://www.npmjs.com/package/@ionic/app-scripts
   * https://github.com/ionic-team/ionic-app-scripts/tree/master/config
   * https://github.com/ionic-team/ionic-cli/issues/1205
   * https://github.com/ionic-team/ionic-app-scripts/issues/760#issuecomment-280375208
   * https://github.com/ionic-team/ionic-app-scripts#environments
   * -> https://scotch.io/@chaitanyamankala/adding-environment-for-ionic-23-projects
   * https://github.com/ionic-team/ionic-app-scripts/issues/760#issuecomment-280375203
   * https://www.twilio.com/blog/2017/08/working-with-environment-variables-in-node-js.html
   * https://stackoverflow.com/a/39769388/750989
   * https://www.google.dk/search?q=declare+var+process%3A+%7B+env&rlz=1C1GCEA_enDK784DK784&oq=declare+var+process%3A+%7B+env&aqs=chrome..69i57.543j0j7&sourceid=chrome&ie=UTF-8
   *
   * https://github.com/rasor/angularattack2018-dongir/blob/master/config/copy.config.js
   *
   * https://ionicframework.com/docs/theming/platform-specific-styles/
   *
   * https://www.javascripttuts.com/understanding-the-manifest-of-an-ionic-pwa-in-one-go/
   *
   * https://blog.ionicframework.com/announcing-ionic-4-beta/
   * https://github.com/ionic-team/ionic-cli/issues/1205#issuecomment-408987182
   */

The End