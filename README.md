# Duskline One Word

Entry for make.fun — **"The Internet in One Word"**
(`u-ronigrv-the-internet-in-one-word-e388f33b`).

## The word

```
brainrot
```

One word for the whole internet. It is funny on its own, it says something
true about the entire internet rather than one app or one mood, it is not
the first obvious word anyone reaches for, and at eight letters it lands in
one beat.

## How it works

`main.py` (Python 3.13, standard library only) writes the word to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — and nothing else. It never writes to the
repository directory, and it exits cleanly (code 0) if the output directory
cannot be written.

Run:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # brainrot
```
