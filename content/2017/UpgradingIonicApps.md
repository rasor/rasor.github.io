Title: Ionic upgrade check-list
Date: 2099-01-01 00:00

* [Update.Ionic.Zone](https://update.ionic.zone/)

* From v3.4.2
* To v3.7.1


1. Create newest template and test
```ps1
ionic start newesttemplate blank --type=ionic-angular
cd newesttemplate
ionic serve
```

2. Diff the template with your old version

3. Git updates

* In `.gitignore` add lines
```ps1
.sourcemaps/
www/
```

If you have committed files in `www\` you need to remove tracked files
`git rm -r --cached`

4. Dependencies - `package.json`

* Replace `dependencies` and `devDependencies`
* Extra added (project specific) dependencies you need to move and upgrade version manually

5. `src/service-worker.js`

* After main.js add
```
    './build/vendor.js',
```

... or just replace the whole file.

6. `src/index.html`

* Before cordova.js add
```
  <!-- add to homescreen for ios -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
```

* Before main.js add
```
  <!-- The vendor js is generated during the build process
       It contains all of the dependencies in node_modules -->
  <script src="build/vendor.js"></script>
```

--------------

# Links

* [Compare](https://github.com/rasor/ionDogMap/commit/0a292fa2b5cd73594c233cad382abcaef08c213c)
* <https://rasor.wordpress.com/2017/06/29/update-ionic1-poject-to-new-ioniccli-plugin-ionic1-2-0-0/>

The End
