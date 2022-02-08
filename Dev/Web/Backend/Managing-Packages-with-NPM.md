# [Managing Packages with NPM](https://www.freecodecamp.org/learn/back-end-development-and-apis#managing-packages-with-npm)
- *npm (Node Package Manager)* is command line tool to install, create and share packages of JavaScript code written for Node.js


## How to Use package.json, the Core of Any Node.js Project and npm Package
- The `package.json` file is the center of any Node.js project or npm package. It stores information about our project.
- The `package.json` consists of a singe *JSON* object with two required fields *name* and *version*. it's good practice to provide additional information that could be useful to future users and maintainers.


## Add a Description to your package.json
- `description` should be short and informative.
- `description` is a great way to summarize what this project does and help other developers, future maintainers and myself understand project quickly.
- When the project publishes to npm, `description` is the string that show off the idea behind this project.


## Add Keywords to Your package.json
- The `keywords` field is where we describe our project using related keywords


## Add a License to Your package.json
- The `license` filed is where we inform users of what they are allowed to do with our project.


## Add a Version to Your package.json
- A `version` is one of the required fields of your project. This fields describes the current version of the project.


## Expand Your Project with External Packages from npm
- One of the biggest reasons to use a package manager is their powerful dependency management.
- Instead of manually having to make sure that we get all dependencies whenever we set up a project on a new computer, *npm* automatically installs everything for you.
- `dependencies` section in `packages.json` help *npm* know exactly what packages that our project need?
```json
"dependencies": {
	"package-name": "version",
	"express": "4.14.0"
}
```


## Manage npm Dependencies By Understanding Semantic Versioning
- Libraries, frameworks or other tools published on *npm* should use *Sematic Versioning* in order to clearly communicate what kind of changes projects can expect if they update.
```json
"package": "MAJOR.MINOR.PATCH"
```
- The MAJOR version should increment when you make incompatible API changes. The MINOR version should increment when you add functionality in a backwards-compatible manner. The PATCH version should increment when you make backwards-compatible bug fixes. This means that PATCHes are bug fixes and MINORs add new features but neither of them break what worked before. Finally, MAJORs add changes that won’t work with earlier versions.


## Use the Tilde-Character to Always Use the Latest Patch Version of a Dependency
- Including a specific version of a package is a useful way to freeze our dependencies if we need to make sure that our project still stay compatible.
- But, is most use cases, we don't want to miss bug fixes that hopefully don't break our projects.
- To allow *npm* dependency to update to the latest PATH version, we use tilde character `~` before the version.
```json
"package": "~1.3.8"
```
- *npm* can install the version of 1.3.x


## Use the Caret-Character to Use the Latest Minor Version of a Dependency
- To allow *npm* dependency to update the the latest MINOR version, we use caret character `^` before the version
```json
"package": "^1.3.8"
```
- *npm* can install the version of 1.x.x


# Remove a Package from Your Dependencies
- To remove a external package that we no longer need, just remove the corresponding key-value pair of that package from our dependencies.