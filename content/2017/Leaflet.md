Title: Using Leaflet with Angular
Date: 2099-01-01 00:00

 [Leaflet](http://leafletjs.com/) is JavaScript mapping library by [Vladimir Agafonkin (@mourner)](https://twitter.com/mourner).

If you want to use it in Angluar then you can work with it

1. Untyped 
2. Typed
3. Using one of the components build on the types

### 1. Untyped

Ionic sample using untyped leaflet: [dreamhouse-mobile-ionic](https://github.com/dreamhouseapp/dreamhouse-mobile-ionic/blob/master/src/pages/property-list/property-list.ts)

### 2. The types

Leaflet already have a [@types/leaflet](https://www.npmjs.com/package/@types/leaflet)-file.  
You can start working on them.
Then you can use the samples shown on the Leaflet website. 

Package.json

```json
  "dependencies": {
    "leaflet": "^1.2.0",
    "@types/leaflet": "^1.2.0",
```

some-page.html

```html
    <div style="height:100%;" id="map"></div>
```

some-page.ts

```typescript
import leaflet from 'leaflet';
import * as L from 'leaflet';

@Component({})
export class TabMapPage implements OnInit {
  map: L.Map;
  mapDefaults: L.TileLayerOptions = {};

  public ngOnInit() {
      var mapOpts: L.MapOptions = {};
      this.map = L.map("map", mapOpts);
      leaflet.tileLayer(
        'http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
        this.mapDefaults)
      .addTo(this.map);
  };
```
Typed leaflet gives a problem with untyped leaflet plugins extending L. Luckily there is a [fix for that](https://github.com/yagajs/leaflet-ng2#use-standard-leaflet-plugins).

Using an untyped Leaflet plugin  
(in this case [Leaflet.Icon.Glyph](https://www.npmjs.com/package/leaflet.icon.glyph))  
Notice `(L as any).` to make L untyped in this place where we use `glypth()`, that leaflet don't know.

some-page.ts
```typescript
        var markerOpts: L.MarkerOptions = {
          icon: (L as any).icon.glyph({
            prefix: '',
            glyph: 'A'
          })
        };
```

### 3. The Components 

A lot of [solutions are already using the @types](https://www.npmjs.com/browse/depended/@types/leaflet).  

I found two interesting components
A. ngx.leaflet.components
B. leaflet-ng2

#### 3A. [ngx.leaflet.components](https://www.npmjs.com/package/ngx.leaflet.components) 

It has many example sites using code in [Angular.io.MapViewer](https://github.com/elasticrash/Angular.io.MapViewer)

It has a starter template [ngx-leaflet-starter](https://github.com/haoliangyu/ngx-leaflet-starter)

Usage: See [Wiki](https://github.com/elasticrash/ngx.leaflet.component/wiki)

API [ngx.leaflet.components documentation](https://elasticrash.github.io/Angular.io.MapViewer/documentation/components/LeafletElement.html)

#### 3B. [leaflet-ng2](https://www.npmjs.com/package/@yaga/leaflet-ng2)

It seems you can do anything with the leaflet-ng2 component. There is a lot of documentation.  
It is updated to latest leaflet 1.2.0 and latest Angular 4.4.
Perhaps it is best to start off from [github](https://github.com/yagajs/leaflet-ng2)

![Directive structure](https://raw.githubusercontent.com/yagajs/leaflet-ng2/develop/directive-structure.svg "leaflet-ng2 structure")

It has comprehensive [API documentation](https://leaflet-ng2.yagajs.org/1.0.0-rc8/typedoc/).  
Notice - there might be a newer version - check root of url.

It is explained [howto use Leaflet Plugins](https://github.com/yagajs/leaflet-ng2#use-standard-leaflet-plugins)

leaflet-ng2 also has a starter template  [ionic2-starter-leaflet-ng2](https://github.com/yagajs/ionic2-starter-leaflet-ng2)  

And a lot of [Examples](https://leaflet-ng2.yagajs.org/latest/examples/)

# Links

* [Leaflet.VectorGrid](https://github.com/Leaflet/Leaflet.VectorGrid) - used by ngx-leaflet-starter
* [3rd party libs](http://ionicframework.com/docs/developer-resources/third-party-libs/#type-definitions)
* [The Future of Declaration Files](https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/)
* [TypeScript Types Search](http://microsoft.github.io/TypeSearch/)

## Other links

* [Mapbox](https://www.mapbox.com/)
* [Maps for Unity](https://www.mapbox.com/unity/)

The End