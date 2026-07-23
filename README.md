# Personal Blog


### Theme

Using customized [FLEX](https://github.com/alexandrevicenzi/Flex/tree/b3bd59002a3e85803332c35702d90e1e19ef39b6) theme. 

### Deployment
- [Github actions](https://github.com/marketplace/actions/github-pages-pelican-build-action)

### Analytics

The live site uses [GoatCounter](https://www.goatcounter.com/) — lightweight, privacy-oriented pageview analytics (paths, referrers, browsers, locations). No cookies, no cross-site tracking; bots that identify themselves are ignored.

The tracking script is in `theme_tufte/templates/base.html` and loads on every built page. Dashboard: [casyfill.goatcounter.com](https://casyfill.goatcounter.com/).

Hits are sent on page load; the dashboard aggregates them about every **10 seconds** ([GoatCounter FAQ](https://www.goatcounter.com/help/faq)). Local previews (`make serve`) count too unless the script is blocked (adblockers often block `gc.zgo.at`).

I am thinking of building something around [sidewalklabs](https://sidewalklabs.com/blog/) blog.



### Dev

###### 1. CLone with submodules
In order to pull `ipynb2pelican` submodule, clone with `--recurse-submodules` flag, as:
```bash
git clone --recurse-submodules https://github.com/Casyfill/pyCombo
```

###### 2. Install dependencies

First, create environment (there is no reason to use conda specifically, just easier for me)
```bash
conda create --name blog python=3.7 pip
```

Now, install our dependencies
```
conda activate blog
pip install -r requirements.txt
```

###### 3. Build and serve blog locally

```bash
make html
make serve
```