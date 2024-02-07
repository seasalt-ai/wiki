# Intro
This repo serves [wiki.seasalt.ai](https://wiki.seasalt.ai). Wiki is product documentation/user manual for non-technical Seasalt.ai customers. 

## How to Develop?

### Doks
To get started with development, follow [Doks](https://getdoks.org/tutorial/introduction/). To modify and extend components of Doks, go to [detailed documentation](https://getdoks.org/docs/prologue/introduction/).

### Develop Locally

1. Run `npm install` to install all required npm packages. 
2. Run `npm run start`. Doks will start the Hugo development webserver accessible by default at http://localhost:1313. Saved changes will live reload in the browser.

To preview the static files that will be generated, run `hugo` and check `/public`. Open `/public/index.html` to see result.


### Deployment
To deploy your changes, make a PR to merge changes to `main` branch as usual. When your code is merged to `main` branch, Github Actions for deployment (see `.github/workflows/deploy-github.yml`) will be triggered to rebuild and publish static files to `gh-pages` branch. The webpage, [wiki.seasalt.ai](https://wiki.seasalt.ai), serves the static files that are pushed to `gh-pages` directly.


### API Documentation 
To add a new API documentation page:
1. Add a navigation button to the main menu in `menus.en.toml` and `menus.zh.toml`.
2. Add a new page under `content/en/seasaltApi/seasalt-api` and `content/zh/seasaltApi/seasalt-api` by copying any existing page and replace the `specUrl` with your OpenAPI specification URL.

