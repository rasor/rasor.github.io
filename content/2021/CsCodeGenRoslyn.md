Title: Code Generation in C#
Date: 2099-01-01 00:00
Category: Develop
Tags: #csharp, #roslyn, #fsharp

* Compilers - Roslyn
    * .NET compiler provides C# and Visual Basic languages with rich code analysis APIs: [dotnet/roslyn](https://github.com/dotnet/roslyn)
    * F# Wrapper For Roslyn Code Generation: [johnazariah/roslyn-wrapper](https://github.com/johnazariah/roslyn-wrapper)

* Code generators
    * [Best 20 NuGet code-generator Packages](https://nugetmusthaves.com/Tag/code-generator)
        * C#2Typescript[TypeGen](https://nugetmusthaves.com/Package/TypeGen)
        * ServiceModel2Grpc [ServiceModel.Grpc](https://max-ieremenko.github.io/ServiceModel.Grpc/)
            * [ServiceModel.Grpc.SelfHost](https://nugetmusthaves.com/Package/ServiceModel.Grpc.SelfHost)
        * [Bit.Tooling.CodeGenerator.Task](https://nugetmusthaves.com/Package/Bit.Tooling.CodeGenerator.Task)

## 42 C# Source Generators - Write Code that Writes Code  -  David Wengier  
20:30 (PT) | 04:30 (UTC) | 05:30 (Local)

With C# 9 there is finally an officially supported mechanism for generating source code into your .NET projects as part of the compiler pipeline. Lets run through how they work, some of the pros and cons, and play around with ideas to get your mind racing with the possibilities.

* [@davidwengier](https://twitter.com/davidwengier)
* [David Wengier](https://wengier.com/)
* Other generators: 
    * T4 - runs in runtime
    * RoslunSyntaxTree
* This runs in the compiler
* Starter Template: [davidwengier/SourceGeneratorTemplate](https://github.com/davidwengier/SourceGeneratorTemplate)
* SVG2Cs: [wieslawsoltes/SourceGenerators](https://github.com/wieslawsoltes/SourceGenerators)
    * SVG2PNG-PDF: [wieslawsoltes/Svg.Skia](https://github.com/wieslawsoltes/Svg.Skia)
* Sample validator: [davidwengier/EnumValidatorGenerator](https://github.com/davidwengier/EnumValidatorGenerator)
* Adv sample: [chsienki/Kittitas](https://github.com/chsienki/kittitas)
* Davids online generator: [sourcegen.dev - Source Generator Playground - @davidwengier](https://sourcegen.dev/)
    * [davidwengier/SourceGeneratorPlayground](https://github.com/davidwengier/SourceGeneratorPlayground)

The End