# AI Builders Lab — Class 2

**Sunday 23 August · Build Your First AI**

Everything for today's class is on this page. Click a button, the notebook opens in
Google Colab, and you can run it. Nothing to install.

---

## Today's two projects

| | Notebook | What you build |
|---|---|---|
| **1** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_Aug_23/blob/main/notebooks/01_Crime_Prediction_ANN.ipynb) **01 — Crime Prediction** | A network that predicts a city's crime rate from five facts about it. *Regression: how much?* |
| **2** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_Aug_23/blob/main/notebooks/02_Handwriting_MNIST_ANN.ipynb) **02 — Handwriting** | A network that reads handwritten digits, including one you draw with your mouse. *Classification: which one?* |

## Take home

| | Notebook | What it adds |
|---|---|---|
| **3** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_Aug_23/blob/main/notebooks/03_Handwriting_FULL_selfstudy.ipynb) **03 — Handwriting, full version** | The long self-study version: look at the digits the model gets *wrong*, upload a photo of real pen-on-paper handwriting, and the homework. |

---

## How to use these in class

1. Click **Open in Colab** above.
2. In Colab, click **Copy to Drive** (top of the page) so your changes are saved.
3. Go to **Runtime → Change runtime type** and pick **CPU**. We do not need a GPU today.
4. Run cells with **Shift + Enter**, in order, top to bottom. If you skip one, later cells break.

## Homework

1. Write all ten digits 0–9 by hand and test each one on your model. Find one it gets
   wrong and write down *why* you think it failed — look at "what the model actually sees".
2. Change **one** thing in the model (`Dense(128)` → `Dense(16)`, delete the `Dropout`,
   or set `epochs=1`), re-run, and record what happened to the test accuracy.
   One change at a time. If you change three things at once you learn nothing about any of them.

## Data

`data/crimeSTATS.csv` — 600 US cities, five features plus the crime rate.
The notebook reads it straight off this repository, so you never have to download it.

---

*AI Builders Lab · Dr. Eric Jing Du*
