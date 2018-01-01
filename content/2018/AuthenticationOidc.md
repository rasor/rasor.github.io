Title: OIdC Authentication
Date: 2099-01-01 00:00

![SPA host](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-reference-spa "SPA host")

![WebApp host](https://docs.microsoft.com/en-us/azure/media/active-directory-v2-flows/convergence_scenarios_webapp.png "WebApp host")

## Articles

* [When To Use Which (OAuth2) Grants and (OIDC) Flows](https://medium.com/@robert.broeckelmann/when-to-use-which-oauth2-grants-and-oidc-flows-ec6a5c00d864)
* [Which OpenID Connect/OAuth 2.0 Flow is the right One?](https://leastprivilege.com/2016/01/17/which-openid-connectoauth-2-o-flow-is-the-right-one/)

## Code

### SPA

* [ng CLI sample](https://github.com/rasor/angular-cli-auth-oidc-sample-google-openid)
* [SPA built on MSAL.js with Azure AD B2C](https://github.com/Azure-Samples/active-directory-b2c-javascript-msal-singlepageapp)
* [SPA CLI & ASP.NET Core WebAPI](https://github.com/robisim74/AngularCliAspNetCore)

### REST

* [WebApp/WebAPI with Microsoft.Owin.Security.OpenIdConnect](https://auth0.com/docs/protocols/oidc/openid-connect-discovery)

# Identity Providers

* <https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration>
* <https://login.microsoftonline.com/common/.well-known/openid-configuration>
* <https://auth.login.yahoo.co.jp/yconnect/v2/.well-known/openid-configuration>
* <https://www.paypalobjects.com/.well-known/openid-configuration>

----

https://github.com/rasor/rasor.github.io/blob/pelican/content/2017/AzureMBaaSforIonic.md 

https://connect2id.com/learn/openid-connect 
http://kevinchalet.com/2016/07/13/creating-your-own-openid-connect-server-with-asos-choosing-the-right-flows/ 

http://openid.net/add-openid/add-getting-started/ 
http://openid.net/developers/certified/ 
http://openid.net/specs/openid-connect-core-1_0.html#rfc.section.3

"response_type" value
Flow
code 
Authorization Code Flow
id_token 
Implicit Flow
id_token token 
Implicit Flow
code id_token 
Hybrid Flow
code token 
Hybrid Flow
code id_token token 
Hybrid Flow


https://leastprivilege.com/2016/01/17/which-openid-connectoauth-2-o-flow-is-the-right-one/
https://nordicapis.com/api-security-oauth-openid-connect-depth/ 
## Code flow
### Sandbox
https://openidconnect.net/ 
## Implicit flow
http://openid.net/specs/openid-connect-core-1_0.html#rfc.section.3.2 
https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-dev-understanding-oauth2-implicit-grant#is-the-implicit-grant-suitable-for-my-app 

2016 Oidc implicit - cUrl
http://nzpcmad.blogspot.dk/2016/08/postman-using-curl-to-send-openid.html 

Problem with Oidc - AAD: Cannot use “id_token token” (Implicit flow) to return bearer token to SPA CLI. Code flow is possible to use to get bearer token.

2016 AAD - only asking for (bearer) token
http://nzpcmad.blogspot.dk/2016/08/postman-azure-ad-and-implicit-flow.html 

2016 OAuth implicit for Swashbuckle to AAD
http://nzpcmad.blogspot.dk/2016/12/swagger-using-swagger-for-implicit_21.html 
Client
https://damienbod.com/2017/09/26/auto-redirect-to-an-sts-server-in-an-angular-app-using-oidc-implicit-flow/ 
## Social Providers on Core, OWIN or Express
### Social Providers on Core
https://github.com/aspnet-contrib/AspNet.Security.OAuth.Providers 
### Social Providers on OWIN
https://github.com/TerribleDev/OwinOAuthProviders 
## REST on Core, OWIN or Express
### WebAPI on Core

2017 Oidc implicit - Ngx CLI - Asos+SQLids - Webapi Core2 - EF - Good separated WebAPI sample
https://damienbod.com/2017/04/11/implementing-openid-implicit-flow-using-openiddict-and-angular/ 

2017 WebAPI Core2 bearer tokens - HowTo test
https://jonhilton.net/security/apis/secure-your-asp.net-core-2.0-api-part-2---jwt-bearer-authentication/ 

2017 Oidc implicit - ngx - keycloak - webapi core2 (dotnet new angular)
https://medium.com/@xavier.hahn/asp-net-core-angular-openid-connect-using-keycloak-6437948c008 
https://medium.com/@xavier.hahn/adding-authorization-to-asp-net-core-app-using-keycloak-c6c96ee0e655 

2017 Oidc implicit - ngx - identityserver - webapi core2
https://github.com/damienbod/AspNet5IdentityServerAngularImplicitFlow 
### WebAPI on OWIN
About OWIN
https://github.com/aspnet/AspNetKatana/wiki/Roadmap 
http://johnatten.com/2015/01/04/asp-net-understanding-owin-katana-and-the-middleware-pipeline/ 
https://brockallen.com/2013/08/07/owin-authentication-middleware-architecture/ 
https://brockallen.com/2013/10/27/host-authentication-and-web-api-with-owin-and-active-vs-passive-authentication-middleware/ 
https://brockallen.com/2014/01/09/a-primer-on-external-login-providers-social-logins-with-owinkatana-authentication-middleware/ 
https://gkulshrestha.wordpress.com/2014/01/19/oauth-implicit-grant-flow-with-owinkatana/ 

OWIN packages
https://github.com/aspnet/AspNetKatana/wiki/Packages 
https://www.nuget.org/packages/Microsoft.Owin.Security.OpenIdConnect/4.0.0-preview1 
https://www.nuget.org/packages/Microsoft.AspNet.WebApi.Owin/ 
https://docs.microsoft.com/en-us/aspnet/aspnet/overview/owin-and-katana/an-overview-of-project-katana 

Tweak message in OWIN middleware
http://www.cloudidentity.com/blog/2017/03/20/tweak-sign-in-messages-with-the-asp-net-owin-middleware/ 

2017 Oidc - OWIN - AAD - WebAPI
https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-devquickstarts-webapi-dotnet 

2016 5 pages
Oidc - OWIN - install
https://www.microsoftpressstore.com/articles/article.aspx?p=2473126

2014 Oidc - OWIN
http://appetere.com/post/getting-started-with-openid-connect 

2014 Oidc - OWIN - Console CLI - AAD - WebAPI
http://www.cloudidentity.com/blog/2014/04/28/use-owin-azure-ad-to-secure-both-mvc-ux-and-web-api-in-the-same-project/
2014 Oidc - OWIN - WebAPI - Ext ID
https://blogs.msdn.microsoft.com/webdev/2014/03/28/owin-security-components-in-asp-net-openid-connect/ 

2015 OWIN - WebAPI
http://johnatten.com/2015/01/19/asp-net-web-api-understanding-owinkatana-authenticationauthorization-part-i-concepts/ 

2017 Oidc implicit - OWIN - WebAPI as client
https://docs.sitefinity.com/request-access-token-for-calling-web-services 

2014 OAuth Implicit - OWIN
https://gkulshrestha.wordpress.com/2014/01/19/oauth-implicit-grant-flow-with-owinkatana/ 
### REST on Express
2017 Oidc - keycloak - express
https://codeburst.io/keycloak-and-express-7c71693d507a
## ID Server (OpenidDict/ASOS)
Oidc - IDServer -  Core2 or OWIN
https://github.com/openiddict/openiddict-samples 
2016 Oidc implicit/code - Core - ASOS
http://kevinchalet.com/2016/07/13/creating-your-own-openid-connect-server-with-asos-implementing-the-authorization-code-and-implicit-flows/ 
http://kevinchalet.com/2017/01/30/implementing-simple-token-authentication-in-aspnet-core-with-openiddict/ 
-> http://kevinchalet.com/2017/10/20/the-new-asos-and-openiddict-packages-are-now-on-nuget-org/ 

Oidc implicit - OWIN - ASOS - WinAuth
https://www.howtucode.com/angularjs-webapi-jwt-with-integrated-windows-authentication-221727.html 

## Authorization
https://leastprivilege.com/2017/07/10/authorization-is-hard-slides-and-video-from-ndc-oslo-2017/ 
https://speakerdeck.com/leastprivilege/implementing-authorization-for-applications-and-apis?slide=5


The End