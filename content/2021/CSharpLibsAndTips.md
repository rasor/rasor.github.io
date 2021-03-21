Title:  C# libs and tips
Date: 2099-01-01 00:00
Category: Develop
Tags: #csharp, #nuget, #fsm, #valuetype, #heap, #stack, #featureswitch

## C# librarie and Nuget packages

* [mexx/FeatureSwitcher](https://github.com/mexx/FeatureSwitcher)
    * [FeatureSwitcher](https://slides.com/mexx/featureswitcher#/)
    * [emardini/FeatureSwitcherDemo](https://github.com/emardini/FeatureSwitcherDemo)

## C# tips

* Articles
    * Readonly structs: [Write safe and efficient C# code](https://docs.microsoft.com/en-us/dotnet/csharp/write-safe-efficient-code#conclusions)
    * Convert ValueTypes
        * Case ValueType: [How to safely cast by using pattern matching and the is and as operators](https://docs.microsoft.com/en-us/dotnet/csharp/how-to/safely-cast-using-pattern-matching-is-and-as-operators)
        * Object to value: [Tutorial: Build algorithms with pattern matching](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/pattern-matching#implement-the-basic-toll-calculations)
        * State checking: [Implement the commands with patterns](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/exploration/patterns-objects#implement-the-commands-with-patterns)
    * Serialization
        * [Custom serialization](https://docs.microsoft.com/en-us/dotnet/standard/serialization/custom-serialization)
            * [BinaryWriter Class (System.IO)](https://docs.microsoft.com/en-us/dotnet/api/system.io.binarywriter?view=net-5.0#examples)
        * [Define custom integer-based type?](https://stackoverflow.com/questions/7615113/define-custom-integer-based-type)
        * Custom BinaryFormatter: [A High Performance Binary Serializer using Microsoft Common Intermediate Language](https://www.codeproject.com/articles/151946/a-high-performance-binary-serializer-using-microso)
        * Custom Serializer using Attributes: [Writing and reading of a custom binary protocol](https://codereview.stackexchange.com/questions/44625/writing-and-reading-of-a-custom-binary-protocol)
        * [BufferedStream Class (System.IO)](https://docs.microsoft.com/en-us/dotnet/api/system.io.bufferedstream?view=net-5.0#examples)
        * Warning on deserialization: [BinaryFormatter security guide](https://docs.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-security-guide)
    * Webservice streams
        * Async streams: [Generate and consume async streams](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/generate-consume-asynchronous-stream#async-streams-provide-a-better-way) // #github-GraphQl, #JObject, #JArray
        * [Create a REST client using .NET Core](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/console-webapiclient) // #JsonSerializer.DeserializeAsync, #JsonPropertyName
    * Array: [Explore ranges of data using indices and ranges](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/ranges-indexes) // #`arr[..]`
    * Capabilities with Interfaces: [Create mixin types using default interface methods](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/mixins-with-default-interface-methods#mix-and-match-capabilities)
    * "Multiple inheritace" / Interface methods: [Safely update interfaces using default interface methods in C#](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/default-interface-methods-versions)
    * Authentication
        * [Cutting Edge - Cookies, Claims and Authentication in ASP.NET Core](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/september/cutting-edge-cookies-claims-and-authentication-in-asp-net-core)
            * Flow:
                * `User` -> 
                * `Claims` -> 
                * `ClaimsIdentity` (which claim is userid? which is role? use cookies (authscheme) or?) -> 
                * `ClaimsPrincipal` (1 principal can have many identities - think cards) -> 
                * Authenticate
                    * Can be challenge to e.g. Twitter
                    * Can optionally inspect and edit external principal: 
                    ```csharp
                    app.UseXxxAuthentication(new Options(){
                        AuthenticationScheme = "Xxx", //where to do auth - e.g. Twitter
                        SingInScheme = "NextAuthScheme" //next auth after twitter
                    });
                    app.UseYyyyAuthentication(new Options(){
                        AuthenticationScheme = "NextAuthScheme", //where to do auth - e.g. cookie from Twitter
                        AutomaticAuthenticate = false
                    });
                    // where to manual do auth
                    var props = new AuthenticationProperties(){
                        RedirectUri = "/account/external"  
                    };
                    // Controller
                    public async Task<IActionResult> External(){
                        var principal = await HttpContext
                            .Authentication()
                            .AuthenticateAsync("ExternalCookie");
                        // Edit the principal
                        // ...
                        await HttpContext.Authentication.SignInAsync("Cookies", principal);
                        await HttpContext.Authentication.SignOutAsync("ExternalCookie "); // remove temp twitter cookie
                    }
                    ```
                * Endpoint (can require cookies, roles or other)  
                ```csharp
                [Authorize(ActiveAuthenticationSchemes = "Bearer")]
                public class ApiController : Controller
                {
                    // Your API action methods here
                }
                ```
    * dotnet/standard
        * [So devs understand](https://github.com/dotnet/standard/blob/master/docs/metaphor.md)
        * [FAQ](https://github.com/dotnet/standard/blob/master/docs/faq.md)
        * [.NET Standard - Demystifying .NET Core and .NET Standard](https://docs.microsoft.com/en-us/archive/msdn-magazine/2017/september/net-standard-demystifying-net-core-and-net-standard)

The End