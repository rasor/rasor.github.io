Title: YAML tables in Markdown
Status: published
Category: Develop
Date: 2018-09-07 17:00
Tags: #github, #yaml, #markdown

If you put YAML in your github markdown, you can use it for creating **nested** tables  
[![Nested tables with yaml](https://f.cloud.github.com/assets/64050/1228267/e049d0c6-27a0-11e3-9dd8-a1cd22599344.png)](https://blog.github.com/2013-09-27-viewing-yaml-metadata-in-your-documents/)
  
This is opposed to using [normal markdown tables](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables) as here:  

| Normal        | Markdown      | Tables|
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

## Cool usage sample

CryptoZombies is a code teaching webapp that uses data from Yaml tables as persistence for their content. Here is how their markup shows in github:  
[![cryptozombie markdown](img/2018/2018-09-07-YamlTable1.PNG)](https://github.com/loomnetwork/cryptozombie-lessons/blob/master/en/3/02-ownable.md)  

The corresponding yaml markdown:

```yaml
---
title: Ownable Contracts
actions: ['checkAnswer', 'hints']
requireLogin: true
material:
  editor:
    language: sol
    startingCode:
      "zombiefactory.sol": |
        pragma solidity ^0.4.19;
        // 1. Import here
      "zombiefeeding.sol": |
        pragma solidity ^0.4.19;
        // other sol code here 
      "ownable.sol": |
        // other sol code here 
    answer: >
      pragma solidity ^0.4.19;
      // other sol code here 
---
Did you spot ....
```

What is really cool is how their webapp formats the .md
[![cryptozombie markdown](img/2018/2018-09-07-YamlTable2.PNG)](https://cryptozombies.io/en/lesson/3/chapter/2)

# Links

* [github/markup](https://github.com/github/markup)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [CryptoZombies - Learn to code games on Ethereum.](https://cryptozombies.io/en/course)
* [CryptoZombies lessons webapp on github](https://github.com/loomnetwork/cryptozombie-lessons)

The End
