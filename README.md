# Intro
This repo serves [wiki.seasalt.ai](https://wiki.seasalt.ai). Wiki is product documentation/user manual for non-technical Seasalt.ai customers. 

## How to Develop?

### Doks
To get started with development, follow [Doks](https://getdoks.org/tutorial/introduction/). To modify and extend components of Doks, go to [detailed documentation](https://getdoks.org/docs/prologue/introduction/).

### Deployment
To deploy your changes, make a PR to merge changes to `main` branch as usual. When your code is merged to `main` branch, Github Actions for deployment (see `.github/workflows/deploy-github.yml`) will be triggered to rebuild and publish static files to `gh-pages` branch. The webpage, [wiki.seasalt.ai](https://wiki.seasalt.ai), serves the static files that are pushed to `gh-pages` directly.
