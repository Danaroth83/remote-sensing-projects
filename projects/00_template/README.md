## Project description

Use this space to give a very high level description of your project including:
- Problem statement
- Available resources
- Employed methods
- Validation protocols

## Starting up

- Setting up your project folder
  - Indicating your project folders depends on your IDE
      - For PyCharm, it is defined through `File -> Open project`
      - For Spyder, go through `Projects -> Open Project...`
  - For thr template project the folder would be: ```.\00_template```. 
  - If your project has not already an assigned folder:
    - Copy the template folder and rename it to your project name.
    - E.g., for the snow project:
      - Copy ```.\00_template``` 
      - Paste it and rename it to: ```.\01_snow_hr```
      - Set ```.\01_snow_hr``` as your project folder. 
    - You are allowed to call local imports such as:
         ```import src.utilities.utils_rasterio```
      - The imports are relative folders to the project folder.

- Locate your terminal:
  - We suggest to use `git bash` for terminal usage.
  - For Pycharm, the terminal is in the tab below, called `terminal`
  - For Spyder, the terminal is directly your command window

- Creating your environment in your terminal:

  - On Linux/Mac:
    ```bash
    cd projectname
    python -m venv .venv --prompt projectname
    source .venv/bin/activate
    pip install pip --upgrade
    pip install -e .
    ```
    or, more briefly, using the provided script:
    ```bash
    cd projectname
    source install.sh
    ```

  - On Windows:
    ```
    cd projectname
    python -m venv .venv --prompt projectname
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    .\.venv\Scripts\activate
    pip install pip --upgrade
    pip install -e .
    ```

## Project Organization

The following folder structure serves as a guideline to standardize the project
structure across different groups and across different academic years.

------------
    xx_project          <- Root folder of your project. Do not add or change any 
    │                      file outside this folder.  
    ├── data            <- Contains a subset of the data, with relatively small  
    │   │                  size (<10 MB), to run a demo of your script.
    │   ├── weights     <- stores trained weights, for machine learning projects 
    │   ├── raw         <- Input data
    │   └── outputs     <- Processed data
    ├── docs            <- Contains the official documentation related to 
    │                      the dataset, methods, etc.  
    ├── notebooks       <- Contains the Jupyter notebooks to present how to use
    ├── reports         <- Contains reports and presentation
    │   ├── presentation_mid.pdf   <- Mid-project presentation slides
    │   ├── presentation.pdf       <- Final presentation slides
    │   ├── report.pdf             <- Final report
    │   └── figures     <- Raw figures that you generated for your reports
    └── project         <- Contains the source code in Python for the
                           specific project. The `project` should be the name
                           of your project
    LOG.md              <- To track the progress at each session
    PROJECT_OVERVIEW.md <- Instructions for the project
    README.md           <- Has to include instructions to run your project.
    pyproject.toml      <- Add here a list of all the libraries you included
    .gitignore          <- List of folders and files not to upload to git
------------
 