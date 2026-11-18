# World News in One Image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/munnavuyyuru/SUMUP-18NOV-News-As-Image/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/munnavuyyuru/SUMUP-18NOV-News-As-Image/reward.svg)](https://make.fun/bounty/news-image-20261118)

A deterministic Node 22 entry that copies an editorial infographic summarizing eight verified developments reported on Wednesday 18 November 2026.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out node main.ts
```

The grader runs `main.ts` with no network and checks the resulting `entry.png` for valid image bytes, dimensions, size, and deterministic output.
