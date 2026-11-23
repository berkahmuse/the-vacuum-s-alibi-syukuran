# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

A [make.fun](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) entry: a program that writes one line — at most 200 characters — in which a robot vacuum explains why it missed a spot.

## The line

> Spot status: skipped on purpose. My cliff sensor called it a ledge, and I do not argue with the sensor that has saved my life fourteen times.

141 characters, one line, deadpan all the way down. A status report instead of a denial: the vacuum trusts the sensor that has saved its life over its own eyes.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the line to `/output/entry.txt` (creating `/output` if needed) and asserts it is a single line of 1–200 characters. The output is deterministic: every run produces the same bytes.

## License

MIT — see [LICENSE](LICENSE).
