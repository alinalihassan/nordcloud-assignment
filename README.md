# Nordcloud Assignment
[![python version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)](https://www.python.org/downloads/)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg)](https://github.com/RichardLitt/standard-readme)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Nordcloud technical assignment. The repository contains both the algorithm requested and the infrastructure/maintainability
standards I would deem necessary and acceptable for collaboration and maintainability.

## 📃 Table of Contents

- [🧑‍🎨 Design decisions](#🧑‍🎨-design-decisions)
- [🛠️ Install](#🛠️-install)
  - [📖 Prerequisites](#📖-prerequisites)
  - [🖥️ Local installation](#🖥️-local-installation)
- [🔬 Usage](#🔬-usage)
- [🧪 Test](#🧪-test)
- [👨‍💻 Deploy](#👨‍💻-deploy)
  - [☁️ Setting up a GCP Account](#☁️-setting-up-a-gcp-account)
  - [⚙️ Configuring](#⚙️-configuring)
  - [⚡ Deploying](#⚡-deploying)
  - [💣 Destroying](#💣-destroying)
  - [🧐 Checking the results](#🧐-Checking-the-results)
- [📐 Problem](#📐-problem)
- [⚖️ License](#⚖️-license)

## 🧑‍🎨 Design decisions

Some arbitrary design decisions have been made, which resulted in an opinionated code repository, as most of them are.
Below is a list of most of them and the reason why.

- Python docstrings are formatted using reST, since it's suggested by [PEP 287](https://www.python.org/dev/peps/pep-0287/)
- The repository does not use any dependencies, thus the testing framework used is unittest, part of the standard Python library
- The minimum Python version is set to 3.6 due to integrated type hints which contributes greatly to maintainability.
- The cloud vendor chosen is Google Cloud mainly because it provides sane defaults, and writing for all three public clouds would have taken too long.
- Infrastructure is written in Terraform, since it's the most popular IaaC tool, especially for multi-cloud setups, [which are becoming more and more common](https://www.hashicorp.com/state-of-the-cloud)

## 🛠️ Install

### 📖 Prerequisites

- [Python](https://www.python.org/): I recommend using the official binaries provided by the Python Software Foundation.
- [Terraform](https://www.terraform.io): Optional, required for deploying to the cloud.
- [Google Cloud Platform](https://cloud.google.com): Optional, cloud vendor of choice, we will need to use some cli operations. You can use the web console instead.

### 🖥️ Local installation

```shell
# Install dependencies
pip install -r requirements.txt
```

## 🔬 Usage

Running the python script with no arguments will prompt the user for either running the it with sample input, or providing the input inline.

```shell
# Run script
python src/main.py
```

If you decide not to run the sample input, you will have to provide data for link stations and devices. You can use Python syntax for comma separated lists or sets.

```shell
# Sample data format
Run sample? (y/n): n
Link Stations (x, y, reach): (0, 0, 10), (20, 20, 5), (10, 0, 12)
Devices (x, y): (0,0), (100,100), (15,10), (18,18)
```

## 🧪 Test

The unit tests are run using Python's built in unittest command.

```shell
# Run all tests
python -m unittest -v
```

## 👨‍💻 Deploy

A cloud configuration is already set up using [Terraform](https://www.terraform.io) and 
[Google Cloud Platform](https://cloud.google.com). The Terraform configuration is under `terraform`.

The cloud infrastructure is minimal, and it consists of a Cloud Function which runs the script with the sample input
and returns the output as a response. 

The steps below show some manual configurations you might need to do set up a Project successfully.


### ☁️ Setting up a GCP Account

If you are using the Google Cloud SDK for the first time, you will need to authenticate with your Google Account.
You can run the following command:

```shell
# Authenticate with GCP
gcloud auth application-default login
```

Now create the project on GCP:
```shell
# Create a GCP project
gcloud projects create PROJECT_ID --name="My App"
```

Set the project you just created as the default one. This will make it easier to run the subsequent commands.

```shell
# Set the project as the default one
gcloud config set project PROJECT_ID
```

Many features on GCP require a billing account linked to the project, Cloud functions is one of them.
For this step, you will need to visit the dashboard:

[Create a billing account on GCP](https://cloud.google.com/billing/docs/how-to/manage-billing-account)

> Note: even though Google asks for your credit card, this tutorial should not cost any money to run.
> 
> The first 2 million invocations of a Cloud Function are free.

### ⚙️ Configuring

The configuration includes an example configuration file named `terraform.tfvars.example`. You need to supply the `PROJECT_ID` from earlier
and a region.

Copy the file and name the copy `terraform.tfvars` in the same directory. Then modify the project with your `PROJECT_ID` and `region`.

```hcl
project = "PROJECT_ID"
region  = "eu-west-2"
```

### ⚡ Deploying

To create the infrastructure, we can do so by using Terraform. Use the following commands:

```shell
# Deploy infrastructure to GCP
terraform apply
```

### 🧐 Checking the results

We can now check the results, go to the link provided in the output or directly in the console in [Cloud Functions](https://console.cloud.google.com/functions/list).

If you open the webpage it should show the sample output we are expecting.

### 💣 Destroying

To delete the infrastructure we deployed, we can do so directly from Terraform and delete the the google project.

```shell
# Delete all infrastructure
terraform destroy

# Optional: delete the project
gcloud projects delete PROJECT_ID
```

## 📐 Problem

Create a function that solves the most suitable (with most power) link station for a device at
given point [x,y].

Please write it in the language you know best, please also make this project as complete as you
think it should be to be maintainable in a long term by more than one maintainer.
This problem can be solved in 2-dimensional space. Link stations have reach and power.

A link station’s power can be calculated:
```
power = (reach - device's distance from link station)^2
if distance > reach, power = 0
```

Function receives list of link stations and the point where the device is located.
Function should output following line:

```
Best link station for point x,y is x,y with power z
```
or:
```
No link station within reach for point x,y
```

Link stations are located at points (x, y) and have reach (r) ([x, y, r]):
```
[[0, 0, 10],
[20, 20, 5],
[10, 0, 12]]
```
Print out function output from points (x, y):
```
(0,0), (100, 100), (15,10) and (18, 18).
```

## ⚖️ License

MIT © [Alin Ali Hassan](LICENSE)