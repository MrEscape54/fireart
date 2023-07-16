# Django + React blueprint project
### Recipe
#### Back folder
- Run `poetry init` to create the virtual envirenment.
- Run `poetry install` to install the required dependencies.
#### Front folder
- Run `npm create vite@latest`.
- Run `npm install` to install the required dependencies.

It is required to build the frontned to let Django get the **index.html** file

See this settings in **`settings.py`**:
`"DIRS": [FRONT_BASE_DIR / "dist"],`
`STATIC_URL = "assets/" `