# 🎵🐍 Python Music Downloader

Hey! I made an music downloader with python ( for your lazy days... ).

![Automation view](https://media.giphy.com/media/cNU1dHMjkeqSNZvQFO/giphy.gif)

> It's automatic! You can see my cursor is always at the _top of the screen_.

---

## Content

- [Why](#why)
- [Usage](#usage)
  - [Examples](#examples)
    - [URL Example](#url-example)
    - [Code Examples](#code-examples)
    - [How to Run](#how-to-run)
- [Installation](#installation)
- [Made With](#made-with)
- [Thank You](#thank-you)

<br />

## Why?

It's always a bad feeling when you **need** to download **a bunch** of musics you love but you have no time, isn't it?

So, thinking this way, i made this **music downloader**! it's as easy as it seems.

## Usage

To use it is pretty simple!

First of all, just clone this repository and go into the created folder:

```
git clone https://github.com/gasampaiosouza/python-music-downloader
cd python-music-downloader
```

Inside `songs.py` you have a list called `SONGS_LIST`. That's where you're going to put all of your songs' URLs ( must be from youtube ).

> A valid URL is **everything after** `yt.com/watch?v=`.

### Examples

#### URL Example

- **Full URL:** `https://www.youtube.com/watch?v=68ugkg9RePc`

- **Valid URL:** `68ugkg9RePc`

> This url regex if you need: `/\?v=(.*)/`

#### Code Examples

```python
# valid list example
SONGS_LIST = ['8mCCMhuKEYw', 'PMivT7MJ41M', 'bnVUHWCynig']
```

```python
# you can also download only one music, if you want to, but it must always be an array.
SONGS_LIST = ['8mCCMhuKEYw']

# obs: there's no length limit.
```

### How to Run

To run, you can type `python main.py` in your terminal, or run it inside your favorite IDE.

## Installation

Everything you need to install is [selenium](https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium) with `python -m pip install selenium` or just `pip install selenium`.

## Made With

- Python - [selenium](https://selenium-python.readthedocs.io/)

## Thank you

That's my project, i hope you liked it, there's a bunch more coming! 💜

[⬆️ Back to top](#)
