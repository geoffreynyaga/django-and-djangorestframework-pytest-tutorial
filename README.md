# Welcome to Pytest Django and DRF Tutorial 🦄

> This tutorial series is dedicated to exploring the basics of inbuilt Django testing and introduces
> Pytest and its various plugins to help us write better code
>
> Currently we cover the following:
>
> - Code coverage,
> - Generating fixtures using mixer
> - Complex testing of edge-cases using hypothesis
> - Testing Serializers
> - Testing DRF Views
> - DRF authentication testing
> - Github Actions

> ### Additional Resources
>
> - Full Course(FREE): https://geoffreynyaga.com/courses/pytest-django-and-django-rest-framework/
> - YouTube Playlist: https://www.youtube.com/playlist?list=PLP1DxoSC17LZTTzgfq0Dimkm6eWJQC9ki

## Installation 📥

```bash
mkdir <my_project>

cd my_project

git clone https://github.com/geoffreynyaga/django-and-djangorestframework-pytest-tutorial.git .

```

## Testing setup🧪🧪

The projects uses pytest and black as the formatting option. The tests also check for consistencies on code format.

To initiate tests follow the steps below:

1. Its advised to create a virtual environment in the root folder

```bash
virtualenv venv
```

2. Activate the environent. For Linux/MacOS users use the command below

```bash
source venv/bin/activate
```

for windows users

```bash
cd venv/Scripts

activate.bat
```

3. Install the requirements

```shell
pip install -r requirements.txt
```

4. Run the pytest command

```bash
pytest
```

The testing results will be displayed and there will also be a `htmlcov` folder generated inside the project that will contain the code coverage details.

<pre>
├── aerocalc
│   ├── __pycache__
│   └── test
├──  <b>htmlcov</b>
└── venv
</pre>

Open up the folder and open the `index.html` in your browser to see this information.

## Project layout

```
    .
    ├── accounts
    │   ├── api
    │   │   └── tests
    │   └── migrations
    ├── classroom
    ├── htmlcov
    └── venv # after you create the virtualenv
```
