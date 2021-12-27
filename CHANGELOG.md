# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [1.0.0](https://github.com/Rubenrod18/pypotter_books/compare/v0.3.0...v1.0.0) (2021-12-27)


### ⚠ BREAKING CHANGES

* **pip:** Flask package version has been updated from 1.1.2 to 2.0.1 version

### Features

* **swagger:** update Swagger UI and add persist authorization when reload the brow ([6af1607](https://github.com/Rubenrod18/pypotter_books/commit/6af160701d51c3aee760ed4e530a104543b240ec))
* add Flask-Caching integration ([96c934b](https://github.com/Rubenrod18/pypotter_books/commit/96c934bd29394cfb37f7e09a088ec69d758a8eea))
* add support for running tests in parallel ([3104332](https://github.com/Rubenrod18/pypotter_books/commit/31043325f3e6ca1b4f82d3a599063c771a489900))
* **book-prices:** add new price field ([59fb176](https://github.com/Rubenrod18/pypotter_books/commit/59fb1766d6af7748df13d566b9203b10d96c18ec))
* **books:** add smart hyperlinks to serializer ([ab93477](https://github.com/Rubenrod18/pypotter_books/commit/ab93477445be503bb0349fa68aa21f330d5a68f4))
* **pip:** upgrade Python packages version ([5ea1a4e](https://github.com/Rubenrod18/pypotter_books/commit/5ea1a4ed147d3a3432c59d122bafc740a34ed6fd))


### Bug Fixes

* **swagger:** add custom Swagger UI ([981e83a](https://github.com/Rubenrod18/pypotter_books/commit/981e83a21090f20149ee761a34a7649caa073b67))


### Build System

* **cli:** add new migration command ([fb50c91](https://github.com/Rubenrod18/pypotter_books/commit/fb50c916220ed24153a9ea3cca091c52914a9d7d))
* **docker:** add Docker integration ([6d189df](https://github.com/Rubenrod18/pypotter_books/commit/6d189df651c8fa97a797d01e19aeb7b9f25a4be7))
* **npm:** upgrade standard-version package version ([0fe1082](https://github.com/Rubenrod18/pypotter_books/commit/0fe1082461f189e17639583e82697d00bdd6b763))
* **pip:** update packages version ([85694f9](https://github.com/Rubenrod18/pypotter_books/commit/85694f9bda161e09613cb29610bc3d1b56c7eca2))
* **pre-commit:** update hook versions ([0c5b58b](https://github.com/Rubenrod18/pypotter_books/commit/0c5b58bfaf6386d6842e2178aa2891aea92694c9))
* **pre-commit:** update package versions ([12e829f](https://github.com/Rubenrod18/pypotter_books/commit/12e829f10fef2ffd466f6b234efb9d11943d1134))
* add new way to run options from Makefile based on FLASK_CONFIG argument ([fa10325](https://github.com/Rubenrod18/pypotter_books/commit/fa10325ded9230aad2d826dbf24bd7c0e6b6dfde))

## [0.3.0](https://github.com/Rubenrod18/flask_api_alchemy/compare/v0.2.0...v0.3.0) (2021-07-22)


### Features

* **book-price:** add book price calculation logic ([8026d93](https://github.com/Rubenrod18/flask_api_alchemy/commit/8026d93fbbb2fa23472adfec8e8cab91dfa2db05))
* **book-prices:** add model, factory and seeder ([2d383fb](https://github.com/Rubenrod18/flask_api_alchemy/commit/2d383fbd71df9a5060b05ca4d377a8e745cb858f))
* **cli:** add new component cli version ([2f2a12f](https://github.com/Rubenrod18/flask_api_alchemy/commit/2f2a12f885e8d7e1e6f5e5eababd80fddcc9b7e3))
* **components:** add bill component ([0a8f9e5](https://github.com/Rubenrod18/flask_api_alchemy/commit/0a8f9e5f9a4db7d7b7343125b15b913327ab7246))
* **components:** add book component ([93099e7](https://github.com/Rubenrod18/flask_api_alchemy/commit/93099e792386814f14b406fbeb04e31306e93884))
* **components:** add book price component ([d196367](https://github.com/Rubenrod18/flask_api_alchemy/commit/d196367885b17db5db1e2accf5f033c5d66bf398))
* **components:** add book stock component ([0288b25](https://github.com/Rubenrod18/flask_api_alchemy/commit/0288b2556d24d3be49ae8a887e4c02fde097a2b0))
* **components:** add country component ([2e16572](https://github.com/Rubenrod18/flask_api_alchemy/commit/2e165720d9ae421e7f1209ee091bd02073c0db3c))
* **components:** add currency component ([4ee9b80](https://github.com/Rubenrod18/flask_api_alchemy/commit/4ee9b802fb7903261899cade871df55df87e5322))
* **components:** add shopping cart book component ([8eeb4c0](https://github.com/Rubenrod18/flask_api_alchemy/commit/8eeb4c059ec05f417519e4a2a527b195453938f3))
* **components:** add shopping cart component ([5e98ea0](https://github.com/Rubenrod18/flask_api_alchemy/commit/5e98ea0ea740c241a8bbdd20dd5a889144438464))
* **db:** add database migration for allowing image column to be nullable ([cd70291](https://github.com/Rubenrod18/flask_api_alchemy/commit/cd702912a384ff278e6a18c12e435b24afbb88bf))
* **db:** add potter books models ([bf5663b](https://github.com/Rubenrod18/flask_api_alchemy/commit/bf5663b681357c7df657d3dfbcad97058c1151b4))
* **exceptions:** add exceptions module for managing application exceptions ([36b22d4](https://github.com/Rubenrod18/flask_api_alchemy/commit/36b22d4fb6e3a62f1b080ca1796ef42bae0ec3e2))
* **seeders:** add attribute for sorting by priority of execution ([7e73609](https://github.com/Rubenrod18/flask_api_alchemy/commit/7e73609b9a512c72b9b429704858f43068b04a4c))


### Bug Fixes

* **cli:** correct component CLI ([9d92767](https://github.com/Rubenrod18/flask_api_alchemy/commit/9d927677c510413e22faa850a8e799c910142de4))


### Build System

* **services:** remove app.services directory ([e6ecd73](https://github.com/Rubenrod18/flask_api_alchemy/commit/e6ecd738ac7b201aae8f231d40c89b16f3838835))
* **services:** the files are inside to components ([aa15e33](https://github.com/Rubenrod18/flask_api_alchemy/commit/aa15e33ecd3e81a542e62e4917339a865bc8a6a2))

## [0.2.0](https://github.com/Rubenrod18/flask_api_alchemy/compare/v0.1.0...v0.2.0) (2021-04-18)


### Features

* **cli:** add new cli to generate a component structure files ([432e899](https://github.com/Rubenrod18/flask_api_alchemy/commit/432e899bcd36aa849f11ec9069b414aeed4a3ad9))
* **roles:** add roles search endpoint ([ee25c56](https://github.com/Rubenrod18/flask_api_alchemy/commit/ee25c566f681057811f10006b940e77877d10b4d))


### Build System

* **cli:** add new cli module that contains flask shell configurations ([7c78a95](https://github.com/Rubenrod18/flask_api_alchemy/commit/7c78a9581742097f0460e6dabe8cd59aba42c979))
* **decorators:** move decorators from app.utils to app ([8b560cb](https://github.com/Rubenrod18/flask_api_alchemy/commit/8b560cbf09a18c407a93668f1b92dc5f025342f7))
* **linter:** add flake8 config file ([2e6b522](https://github.com/Rubenrod18/flask_api_alchemy/commit/2e6b522179cab47f4a3ebeec00f44d423d7af5a8))
* **linter:** add flake8 linter integration ([0395759](https://github.com/Rubenrod18/flask_api_alchemy/commit/03957598a13ff475faf06082d67315486c6f90f4))
* **makefile:** add new flask shell command ([946bcc3](https://github.com/Rubenrod18/flask_api_alchemy/commit/946bcc338f04eb42e5b14ef9b494df37bbb324e3))
* **makefile:** provides commands to run the application tools ([978aa03](https://github.com/Rubenrod18/flask_api_alchemy/commit/978aa03c0c435104273eda731c66cb2af49274af))
* **makefile:** update linter command ([3a29cd2](https://github.com/Rubenrod18/flask_api_alchemy/commit/3a29cd2dd3911cddaea0637f23100e2cd0deb36d))
* **makefile:** update linter command ([32d881b](https://github.com/Rubenrod18/flask_api_alchemy/commit/32d881b102e1f404b7bcb7d582f83386bd3f1c3f))
* **pip:** update packages version ([04ed2e9](https://github.com/Rubenrod18/flask_api_alchemy/commit/04ed2e9d86b681f64690c30156527ef992fd9e18))
* **pip:** upgrade python packages ([592006b](https://github.com/Rubenrod18/flask_api_alchemy/commit/592006b4f4f02ac30de06fd593960952d5f0178c))
* **pre-commit:** add git hook scripts ([c341e4d](https://github.com/Rubenrod18/flask_api_alchemy/commit/c341e4d50fa1d93eaeb48c860ba53daa03c0059c))
* **pre-commit:** add lint to git commit message ([686f93d](https://github.com/Rubenrod18/flask_api_alchemy/commit/686f93d1439fbd9a7cdb4e59627397f288ea16fe))
* **pre-commit:** add local hooks ([45088e0](https://github.com/Rubenrod18/flask_api_alchemy/commit/45088e07fefda4baa897768d740a1935458c722f))
* **pre-commit:** disable black string normalization config ([da42623](https://github.com/Rubenrod18/flask_api_alchemy/commit/da42623c407f43e728e6be64c3b3d1805412e5ce))
* **pre-commit:** update flake8 hook configuration ([1d610e5](https://github.com/Rubenrod18/flask_api_alchemy/commit/1d610e58a7d387696cc6b2069e6e0c106ccd3118))
* remove useless files ([4bff2e9](https://github.com/Rubenrod18/flask_api_alchemy/commit/4bff2e91d9753f27c48561ab50e15f9c10ff7c7a))

## [0.1.0](https://github.com/Rubenrod18/flask_api_alchemy/compare/v0.0.1...v0.1.0) (2021-03-19)


## Features

* **db:** add command for filling fake data in database ([7b53fc6](https://github.com/Rubenrod18/flask_api_alchemy/commit/7b53fc62343e34c10b0cb58227883f7e5eb53b9a))
* **security:** users need to login before to use api ([98de276](https://github.com/Rubenrod18/flask_api_alchemy/commit/98de2768fa96f50e24bf30015cb9c8a4ccaddfac))


### Build System

* update blueprints structure ([eb9bb92](https://github.com/Rubenrod18/flask_api_alchemy/commit/eb9bb92903edd4b254d638742530102496117b65))

## 0.0.1 (2021-02-28)


### Features

* **changelog:** add node packages for generating a changelog file ([c97b501](https://github.com/Rubenrod18/flask_api_alchemy/commit/c97b5017308de45d2fe1754acf50d3af4ffc8942))
* **roles:** add crud for managing roles ([3e82426](https://github.com/Rubenrod18/flask_api_alchemy/commit/3e82426dba09dd90ec591deaba0182d74dc638cd))
* **users:** add crud for managing users ([f00ebcd](https://github.com/Rubenrod18/flask_api_alchemy/commit/f00ebcd18d8dbaae8af57e7fbdc96251cb0bb426))
