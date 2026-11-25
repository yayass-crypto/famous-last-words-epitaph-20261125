# Famous Last Words: The Funniest Epitaph

[![Famous Last Words: The Funniest Epitaph](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![Rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/yayass-crypto/famous-last-words-epitaph-20261125/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![Reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/yayass-crypto/famous-last-words-epitaph-20261125/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

My entry for [make.fun's "Famous Last Words: The Funniest Epitaph" bounty](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406): one line of famous last words, carved as a tombstone epitaph, at most 150 characters. The house judge scores entries head-to-head; the top two places split the $2 prize.

## The epitaph

> I finally got the last word in every argument. It only took dying.

66 characters, two sentences, one line. The deceased spent a lifetime insisting on the last word — and the joke is that death is what finally let him win. The laugh lands on the last three words, the way an epitaph should end.

## How it works

`main.py` uses only the Python 3 standard library and never touches the network. Before writing anything it checks the line: non-empty, no leading or trailing whitespace, no newlines or control characters, at most 150 characters, exactly two sentences. It writes to `/output/entry.txt` when that folder is writable, falling back to `out/entry.txt`, then reads the file back and refuses to report success unless the bytes match exactly and decode as UTF-8. Success exits 0; any failed check exits 1.

## Running it

```sh
python3 main.py
```

That writes the epitaph to `/output/entry.txt` (or `out/entry.txt` as a fallback).
