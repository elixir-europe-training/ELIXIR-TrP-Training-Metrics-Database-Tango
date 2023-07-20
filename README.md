#  Training Metrics Database

The Training Metrics Database was developed in an effort to streamline data collection, storage, and visualisation for the Quality and Impact Subtask of the [ELIXIR Training Platform](https://elixir-europe.org/platforms/training), which aims to:

* Describe the audience demographic being reached by ELIXIR-badged training events,
* Assess the quality of ELIXIR-badged training events directly after they have taken place,
* Evaluate the longer term impact that ELIXIR-badged training events have had on the work of training participants.

In an effort to achieve the above aims, the subtask, in collaboration with the [ELIXIR Training Coordinators](https://elixir-europe.org/platforms/training/how-organised), has compiled a set of core metrics for measuring audience demographics and training quality, in the short term, and training impact, in the longer term. Both sets of metrics are collected via feedback survey. In some cases, the demographic information is collected via registration form. These metrics were developed out of those already collected by ELIXIR training providers as well as from discussions with stakeholders and external training providers. The metrics are listed in the 'References' page under the 'Help' tab.

View and filter all ELIXIR training events on the 'All ELIXIR events' page and create custom reports on the 'Reports' page.

# ELIXIR-TrP-Tango

For the Tango, new Training Metrics Database of the [ELIXIR Training Platform](https://elixir-europe.org/platforms/training).

## Getting started

### Running with Docker

```shell
docker compose up
```

### Installation

```shell
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r utils/requirements.txt
pip3 install -r utils/dev-requirements.txt
```

### Running local development server

```shell
source .venv/bin/activate
python3 manage.py migrate
python3 manage.py runserver
```

### Running local validation checks

```shell
pre-commit run -a
```

## Production

### Environment

The following settings need to be defined in the environment

```
DJANGO_PRODUCTION           # Set to 1 only in production
DJANGO_SECRET_KEY           # A random string of characters - e.g. 3i%9&+g@dux1+bj)d&g=isgtza29tohv$)9zpp8$lg=x6-=bcr
DJANGO_POSTGRESQL_DBNAME    # Name of database
DJANGO_POSTGRESQL_USER
DJANGO_POSTGRESQL_PASSWORD
DJANGO_POSTGRESQL_HOST      # Hostname or IP address
DJANGO_POSTGRESQL_PORT      # Typically 5432
```
