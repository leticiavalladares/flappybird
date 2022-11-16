# flappy setup

Create environment
```sh
pyenv virtualenv venvflappy 
pyenv activate venvflappy  
pyenv install requirements.txt
```

Activate the environment and run the script
```sh
pyenv activate venvflappy  
pgzrun flappybird.py   
pyenv deactivate
```

### flappy-bird-tutorial

To generate the html go to [stackedit](stackedit.io) and past the MD file, adjust any formatting and export
as a html with TOC.

From parent directory run to build a zip

```bash
zip -r flappy-bird-tutorial.zip flappy-bird-tutorial -x flappy-bird-tutorial/.idea/\* flappy-bird-tutorial/.git/\* flappy-bird-tutorial/.github/\* flappy-bird-tutorial/cloudformation/\* flappy-bird-tutorial/*.md flappy-bird-tutorial/.DS_Store
```
