# AI Builders Lab — Class 2

**Sunday 23 August · Build Your First AI**

Everything for today's class is on this page. Click a button, the notebook opens in
Google Colab, and you can run it. Nothing to install.

---

## Today's two projects

Each project comes in **two versions of the same code**. They run identically — pick whichever
suits you.

| | Explained version — diagrams and reasoning | Code only — for following along in class |
|---|---|---|
| **1 · Crime prediction** *(regression: how much?)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_lab1/blob/main/notebooks/01_Crime_Prediction_ANN.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_lab1/blob/main/notebooks/01_Crime_Prediction_CODE_ONLY.ipynb) |
| **2 · Handwriting** *(classification: which one?)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_lab1/blob/main/notebooks/02_Handwriting_MNIST_ANN.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_lab1/blob/main/notebooks/02_Handwriting_CODE_ONLY.ipynb) |

**In class, use the code-only version** — less scrolling, so we all stay on the same cell.
**Afterwards, open the explained version** — same code, plus the diagrams and the reasoning
behind every line. That is the one to read when you want to actually understand it.

## Take home

| | Notebook | What it adds |
|---|---|---|
| **3** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chizelnut/ABL_lab1/blob/main/notebooks/03_Going_Further.ipynb) **03 — Going Further** | Picks up where Project 2 stopped. Find the digits it gets **wrong** and work out why · feed it a **photo** of real pen-and-paper handwriting · break it on purpose. The optional take-it-further challenges are in here. |

---

## How to use these in class

1. Click **Open in Colab** above.
2. In Colab, click **Copy to Drive** (top of the page) so your changes are saved.
3. Go to **Runtime → Change runtime type** and pick **CPU**. We do not need a GPU today.
4. Run cells with **Shift + Enter**, in order, top to bottom. If you skip one, later cells break.

## Optional — take it further on your own

**All optional. Nothing to hand in.** These are for you, not for marks — the questions are
the point, not the code.

1. Write all ten digits 0–9 by hand and test each one on your model. Find one it gets
   wrong and write down *why* you think it failed — look at "what the model actually sees".
2. Change **one** thing in the model (`Dense(128)` → `Dense(16)`, delete the `Dropout`,
   or set `epochs=1`), re-run, and see what happens to the test accuracy.
   One change at a time. If you change three things at once you learn nothing about any of them.
3. Found something surprising? Post it in the class WhatsApp group.

## Data

`data/crimeSTATS.csv` — 600 US cities, five features plus the crime rate.
The notebook reads it straight off this repository, so you never have to download it.

---

*AI Builders Lab · Dr. Eric Jing Du*
