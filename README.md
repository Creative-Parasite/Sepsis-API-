<!-- TABLE OF CONTENTS -->

# 🔖 Table of Contents

- [📑 Table of Contents](#-table-of-contents)
- [Sepsis-API ](#sepsis-API-)
  - [🛠 Built With ](#-built-with-)
    - [FAST API ](#fastapi-)
    - [Streamlit ](#streamlit-)
    - [Docker ](#docker-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [☑️ Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🤝 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)
  - [🦹‍♀️ Authors ](#-authors-)

# Sepsis-API-
Sepsis *also known as a blood poisioning*
Sepsis is a life threatening condition characterized by a sudden severe and inflammatory change in the blood usually involving circulatory system. It can lead to severe complications such as pneumonia, septic shock or death.
In this repo we will be building an API that detects a patient in the ICU for sepsis.

***Features***
*ID*: number to represent patient ID

*PRG*: Plasma glucose.

*PL*: Blood Work Result-1 (mu U/ml)

*PR*: Blood Pressure (mm Hg)

*SK*: Blood Work Result-2 (mm)

*TS*: Blood Work Result-3 (mu U/ml)

*M11*: Body mass index (weight in kg/(height in m)^2

*BD2*: Blood Work Result-4 (mu U/ml)

*Age*: patients age (years)

*Insurance*: If a patient holds a valid insurance card

*Sepsis*: Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise

## 🛠 Built With <a name="built-with"></a>

<details>
  <summary>FAST API</summary>
  <ul>
    <li><a href="">Fast api</a></li>
  </ul>
</details>

<details>
<summary>Streamlit</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
</details>

<details>
<summary>Docker</summary>
  <ul>
    <li><a href="">Docker</a></li>
  </ul>
</details>

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites
In order to run this project you need:
- Python

### 🏹 Setup
Clone this repository to your desired folder:
```sh
  cd my-folder
  git clone https://github.com/Creative-Parasite/Sepsis-API-.git
```
Change into the cloned repository

```sh
  cd sepsis-api
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    env/Scripts/activate
```

### Install
Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```
### Usage
To run the project, execute the following command:

```sh
    uvicorn main:app --reload

```
- A webpage opens up to view the api
- Test a prediction by clicking on the prediciton page

## ☑️ Contributing <a name="contributing"></a>
Contributions, features and issues are welcome .

## ⭐️ Show your support <a name="support"></a>
If you like this project show some love with a  🌟 **STAR** 🌟

## 🤝 Acknowledgments <a name="acknowledgements"></a>
I would like to extend my appreciations to my team project and Azubi Africa for their immense support in availing all the necessary resources for this project's success.

## 📝 License <a name="license"></a> 
This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 🦹‍♀️ Authors <a name="authors"></a>
🕵🏽‍♀️ **Nyawira Kamuri**

[@Creative-Parasite](https://github.com/Creative-Parasite) 
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/evalyne-kamuri/)
