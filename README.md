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

- _images_to_text_: Create descriptions of the slides for later ussage. the description created follow a structured order.

### Baseline

- _transcription_baseline_: First transcription using presegmented phrases.
    - Test: WER 13.86%, CER 7.19%

- _esp_trad_baseline_: First translation to spanish. 0 Shot
    - Test: Bleu: 11.61, comet22 : 0.68

- _esp_cot_baseline_: Translation to spanish using chain of thougths. 0 Shot
    - Test: Bleu: 25.75, comet22 : 0.76

- _esp_image_text_baseline: Translation using the description of the slides to help. 0 Shot
    - Test: Bleu: 0.17, comet22 : 0.22

- _esp_image_baseline: Translation using slides as context. 0 Shot
    - Test: Bleu: 4.86, comet22 : 0.60


### Finetune
 - _lora_esp_base_: First basic finetunning with Query and Keys projections
    - Test: BLEU: 10.95, COMET-22: 0.674

 - _lora_esp_validacion_: Add validation 
    - Test: BLEU: 17.30, COMET-22: 0.7028

 - _lora_esp_full_attention_: Finetune over full attention projections 
    - Test: BLEU: 21.48, COMET-22: 0.7236

 - _lora_esp_cot_: Finetune using CoT
    - Test: BLEU: 37.49, COMET-22: 0.8080

 - _lora_esp_images_: Finetune using slides as context
    - Test: BLEU: 9.84, COMET-22: 0.7155

 - _lora_esp_images_: Finetune using slides as context
    - Test: BLEU: 20.87, COMET-22: 0.6869


## Notas personales

### Version transformers

- Inicialmente usando 4.47 porque en pruebas previas (fine-tune) me habia dado problemas (no seguro de que sea necesario)
- Versiones incomatibles con comet/bleu: 4.47 y 4.53
- Vesiones compatibles: 4.48 y 4.49 (4.49 necesita incluir en generate logits=0)