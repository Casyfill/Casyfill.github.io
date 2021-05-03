# blog development readme

### Theme

for now I use customized [FLEX](https://github.com/alexandrevicenzi/Flex/tree/b3bd59002a3e85803332c35702d90e1e19ef39b6) theme. I am thinking of building something around [sidewalklabs](https://sidewalklabs.com/blog/) blog.


### Plugins

- [ipynb2pelican](https://github.com/peijunz/ipynb2pelican)


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
pip install -f requirements.txt
```

###### 3. Build and serve blog locally

```bash
make html
make serve
```