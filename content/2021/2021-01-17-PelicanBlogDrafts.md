Title: Setting Pelican blogs in "draft" - 4 review. HowTo
Status: published
Date: 2021-01-17 00:00
Modified: 2021-01-17 17:00
Category: DevOps
Tags: #blog, #pelican, #cms, #python

This blog is part of a serie:

1. [Using Pelican blog on Github pages]({filename}/2017/2017-09-23B-PelicanBlogOnGithubPages.md)
2. [Using Pelican Themes]({filename}/2017/2017-09-30A-PelicanThemes.md)
3. [Setting Pelican blogs in "draft"]({filename}/2021/2021-01-17-PelicanBlogDrafts.md) (this blog)

Sometimes you want your pelican blog to be set into draft for review.  
I always forget some part of howto do.  
So here is a small HowTo.  

First you need the top metadata of your blog. For this blog it is:  

```text
Title: Setting Pelican blogs in draft - 4 review. HowTo
Status: draft
```

From the title you transform it into an url: 

```txt
Metadata: Setting Pelican blogs in "draft" - 4 review. HowTo
Url     : setting-pelican-blogs-in-draft-4-review-howto.html
```

From cmd run 

```
.\serve
```

and browse to
http://localhost:8000/drafts/setting-pelican-blogs-in-draft-4-review-howto.html

Tip: After running `serve` you will also find the file in `\output\drafts\`, if you don´t want to do this manual transform.  

When you then decide to deploy using

```
.\publish "commit msg"
```

then you can find your blog on  
https://rasor.github.io/drafts/setting-pelican-blogs-in-draft-4-review-howto.html

The blog wil not be visible in any of the lists in this mode.  
First when you change the blogs state to

```text
Status: published
```

Then you will find it  on  
https://rasor.github.io/setting-pelican-blogs-in-draft-4-review-howto.html

Notice: 

* The commands `serve` and `publish` are two small scrips I created in [Using Pelican blog on Github pages]({filename}/2017/2017-09-23B-PelicanBlogOnGithubPages.md)  
* After `publish` has run it will take 1 - 2 minutes before you see it deployed to Github pages

The End  
