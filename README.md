# Australian Radio Talkback Corpus (ART)

## Overview

Australian Radio Talkback (ART) is a set of **transcribed recordings** of samples of **national, regional and commercial Australian talkback radio** from **2004 to 2006**. It consists of **transcriptions** of **27 audio recordings** of talkback from ABC National Radio (NAT), ABC Radio broadcasts to eastern Australian (ABCE), ABC Radio broadcasts to southern and western Australia (ABCNE), as well as commercial stations broadcasting to eastern Australia (COME) and southern and western Australia (COMNE).

**Keywords**: Australian English, Corpus linguistics.

## Data Source

The original dataset is from [Macquarie University Research Data - Australian Radio Talkback Corpus (ART)](https://figshare.mq.edu.au/articles/dataset/Australian_Radio_Talkback_Corpus_ART_/24769434?file=43534011) and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Dataset Structure

After unzipping `ABC.zip`, the dataset under `ABC` contains:

- `ABC` contains 14 transcripts from NAT, ABCE and ABCNE in `.txt` format.
- `Commercial` contains 15 transcripts from COME and COMNE in `.txt` format.
- `ART-corpus-catalogue.xls` contains a catalogue of the details for each transcript.

## Download

You can download it directly from [Macquarie University Research Data - Australian Radio Talkback Corpus (ART)](https://figshare.mq.edu.au/articles/dataset/Australian_Radio_Talkback_Corpus_ART_/24769434?file=43534011).

You can also download it by running `download.py` in your terminal:

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