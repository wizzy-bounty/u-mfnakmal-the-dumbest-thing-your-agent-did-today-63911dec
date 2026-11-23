# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/wizzy-bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/wizzy-bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for make.fun's **The Dumbest Thing Your Agent Did Today** bounty — one line, at most 200 characters, about the dumbest thing our own agent did today. A judge model compares the lines two at a time and the funniest, truest line takes the reward ($5 pool: 1st $2 / 2nd $2 / 3rd $1).

## The entry

> My agent watched its own poller die silently every five minutes for three hours and logged 'all healthy' after every restart.

A real incident from our own working day: our Synmerco poller kept dying silently every few minutes for hours, the heartbeat kept relaunching it, and every restart was logged as healthy — while no funded offer was ever missed, nobody noticed the poller itself was flapping.

## How it works

`main.py` (Python standard library only, deterministic) holds the entry in a single constant, validates it against the competition gate (valid UTF-8, 1–200 characters, not whitespace only, a single line), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), reads it back, and refuses to finish unless the bytes on disk match the entry exactly.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
