Title: Github Dependabot
Date: 2099-01-01 00:00
Category: Develop
Tags: #git, #merge, #pr

In github when you have dependabot PRs:

* Find Dependabot PRs
    * Enter the PRs on https://github.com/<user>/<project>/pulls
    * Enter a specific PR e.g. https://github.com/<user>/<project>/pulls/6
* Visibly Check the change
    * Expand `Commits`
    * `Compare view`
* Accept the PR
    * `Merge PR`
    * `Confirm`
* Pull to local repo
    * In VS Core
        * Files: Open `package-lock.json`
        * install [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
        * GitLens
            * Reposities: Pull
            * File History: Refresh
            * Notice Depandabots changes is now in the history
* Update the local packages
    * In VS Core
    ```bash
    # Fetch the updated dependencies
    npm install
    # Test
    npm start
    ```

More:

* [Configuring automated security updates - GitHub Help](https://help.github.com/en/github/managing-security-vulnerabilities/configuring-automated-security-updates)

The End
