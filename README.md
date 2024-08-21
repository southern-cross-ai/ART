# Australian Radio Talkback Corpus (ART)

## Overview

**Keywords**: Australian English; Corpus linguistics

Australian Radio Talkback (ART) is a set of **transcribed recordings** of samples of **national, regional and commercial Australian talkback radio** from **2004 to 2006**. It consists of **transcriptions** of **27 audio recordings** of talkback from ABC National Radio (NAT), ABC Radio broadcasts to eastern Australian (ABCE), ABC Radio broadcasts to southern and western Australia (ABCNE), as well as commercial stations broadcasting to eastern Australia (COME) and southern and western Australia (COMNE).

## Data Source

The original dataset is from [Macquarie University Research Data - Australian Radio Talkback Corpus (ART)](https://figshare.mq.edu.au/articles/dataset/Australian_Radio_Talkback_Corpus_ART_/24769434?file=43534011) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). For any data usage concern, please refer to [Fair Self Assessment Summary](https://figshare.com/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418).

## Dataset Structure

After unzipping `ART/ABC.zip`, the dataset under `ABC` contains:

- `ABC`: There are 14 `.txt` transcripts in total, where 4 are from ABCE (e.g., `ABCe1.txt`), 2 are from ABCNE (e.g., `ABCne1.txt`) and 8 are from NAT (e.g., `Nat1.txt`).
- `Commercial`: There are 15 `.txt` transcripts in total, where 8 from COME (e.g., `COMe1.txt`) and 7 are from COMNE (e.g., `COMne1.txt`).
- `ART-corpus-catalogue.xls`: A catalogue of all the transcripts.

`ART_clean/ART_clean.csv` is a cleaned dataset created by [Gillian Law](https://github.com/GillianLaw) and [Yifan Luo](https://github.com/iamyifan). The cleaned dataset can also be downloaded from [Hugging Face - SouthernCrossAI/ART_Australian_Radio_Talkback_Corpus](https://huggingface.co/datasets/SouthernCrossAI/ART_Australian_Radio_Talkback_Corpus).

## Download

You can download it directly from [Macquarie University Research Data - Australian Radio Talkback Corpus (ART)](https://figshare.mq.edu.au/articles/dataset/Australian_Radio_Talkback_Corpus_ART_/24769434?file=43534011).

You can also download it by running `utils/download.py` in your terminal:

```bash
$ python3 download.py --help                       
usage: download.py [-h] [--save_path SAVE_PATH] [--unzip]

Download a file and optionally unzip it.

options:
  -h, --help            show this help message and exit
  --save_path SAVE_PATH
                        Path to save the downloaded file.
  --unzip               Unzip the file if it's a zip archive.
```

For example:

- `python3 download.py --save_path my_data --unzip` will download and unzip the dataset `ACE.zip` under the directory `my_data`.
- `python3 download.py` will only download under the current directory.

## License

This repository is licensed under [MIT](https://opensource.org/license/mit).