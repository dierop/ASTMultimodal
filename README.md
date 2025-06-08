# ✨  ASTMultimodal

Source code for Automatic speech Translation using Multimodal models. 

Using the [dataset](https://github.com/mllpresearch/ESO-dataset) created in the article [Speech translation for multilingual medical education leveraged by large language models](https://www.sciencedirect.com/science/article/pii/S093336572500082X?via%3Dihub#sec3) that has for presentations related to oncology: audio, pdfs, transcriptions and translations.

Using the model [phi4-multimodal](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) I will check the baseline and basic finetune performance of the model and see if using the pdfs and other related data can help improve the performance

## ⚙️ Setup

This project is being developed and run in Google colab to use the T4 and A100 GPUs.

In particular, I will use the T4 Gpus for only inference notebooks: Baseline and data analysis.
The A100 GPUs are used for finetune


## 💻 Notebooks and Metrics

### Data

- _data_exploration_: First exploration to open the data. I created two small zips for dev and test to use in the later experiments

### Baseline

- _transcription_baseline_: First transcription using presegmented phrases.
    - Test: WER 13.86%, CER 7.19%
