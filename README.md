<p align="center">
  <a href="https://github.com/iamsahebgiri/dinesh">
    <img width="380" alt="dinesh" src="https://github.com/iamsahebgiri/dinesh/assets/47132373/b018f72f-2a52-450f-8539-902e6fac5a6f">
  </a>
</p>
<div align="center">
Augmented DNS server providing useful utilities.
</div>

<br />

<div align="center">
  <a href="https://standardjs.com">
    <img src="https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat-square"
      alt="Standard" />
  </a>
  
  <img src="https://img.shields.io/github/languages/code-size/iamsahebgiri/dinesh?style=flat-square" alt="Code size" />

  <img src="https://img.shields.io/github/license/iamsahebgiri/dinesh?style=flat-square" alt="License" />

  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/iamsahebgiri/dinesh?style=flat-square">

  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/iamsahebgiri/dinesh?style=social">
</div>

## ⚡️ Introduction

Dinesh is an augmented DNS server that provides various useful utilities to enhance your DNS experience. It
allows you to perform tasks beyond traditional DNS lookups.

## ⚙️ Installation

Make sure you have [Python](https://www.python.org/downloads/) installed.
Run this followed commands:

```bash
# Install dependencies (only the first time)
pip install -r requirements.txt

# Run the DNS server at 127.0.0.1:53
python main.py
```

## 💡 Usage

### Help

Show a list of all supported commands with examples.

```sh
dig help @127.0.0.1
```

### Random Number

Generate random number between [min, max] both inclusive.
It is suitable for rolling dice [1-6], flipping coins [0-1], etc. Both the arguments, `min` and `max` are required.

#### Examples

```sh
dig rand.1-100 @127.0.0.1 +short
# "69"

dig rand.1-6 @127.0.0.1 +short
# "3"

dig rand.0-1 @127.0.0.1 +short
# "1"
```

### Password

Generate cryptographically secure password suitable for generating tokens and codes. In this case `length` is optional.

#### Examples

```sh
dig pwd @127.0.0.1 +short
# "7XcFMFO1KV"

dig pwd.32 @127.0.0.1 +short
# "Efe3301RDS7V3bdKHb_zcRBRG_EYnQH_"
```

### IP

Returns Host's IP Address.

#### Examples

```sh
dig ip @127.0.0.1 +short
# "127.0.0.1"
```

### Number to words

Convert number to words.

#### Examples

```sh
dig words.1024 @127.0.0.1 +short
# "one thousand and twenty-four"
```

## ❤️ Acknowledgements

- [dns.toys](https://github.com/knadh/dns.toys)

## ⭐️ Contribute

If you want to say thank you and/or support the active development of dinesh:

1. Add a GitHub Star to the project.
2. Tweet about the project on your Twitter.
3. Write a review or tutorial on Medium, Dev.to or personal blog.
4. Support the project by donating a cup of coffee.

## 🧾 License

MIT License Copyright (c) 2023 [Saheb Giri](https://github.com/iamsahebgiri).
