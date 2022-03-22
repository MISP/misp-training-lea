# Additional files for the trainers (to take shortcuts if needed)

- Final MISP event is [available](./files).

# Exporting raw bitcoin addresses 
- the correct `jq` selector is the following: `.[].nodes[0].text`
- to trim quotes, we use `tr`: `tr -d '"'`
- the complete command is:
```bash 
ail@mytraining:~$ python ./ail-framework/tools/extract_cryptocurrency.py -t bitcoin  | jq .[].nodes[0].text | tr -d '"'
```
- Complete list of addresses:
```
12bsh5bc7wkVSRv25Qw6x3JYzuQDpZZ4zi
1LCEGFc6Cwe194B6gavMcZ56o2pbftXqWk
1NqxPMSjDxEfJ2ozbFnGEoumDpL4Z8frKh
32Bg4EsuNjxVJ9ZP2RWHv66ybZRHQotQS4
33i6BL4HGNL7YSdPWDP9x2swdJinNLs5zu
395hQDyiBT16yt8jVVNj7WuZoQ4ouuFJcZ
3CPbvktjKPiWcYu4PM4oVrQhvSQjCKnR59
3ESoHHu87mTrFNSNUaMVEfT3vYwRYGfSHQ
3HrDFf1Yj95PFeSR58kCthga3p9hcz9Nmw
3M9tAMuamLcCpifaCQPSH3Th5F4VwjmyWz
3NAn1bJ49deFB9MmKw1gfBVr5Vwu5KsVzr
3QdNiLEpxKWQ6SoxULAo4xc48d5otumivR
bc1q4hxu7x9jjlx9wqx8sr6pq2gajr786gffgpw3ey
bc1q8qfesjc2slfwe8xv3l0rxwdexms006swf7gcur
bc1qa273a36dgnrdqevnx0lftn99t2we306eu7gm2k
bc1qmdjxd98fnk83l5k8cpvc77f9rljr7942cq0sfz
bc1qptn5qsllcxmrndmwucelazjt0z68zkrgrlumy0
bc1qtn42kyjuz0lc9w9gue72xr9m2a7jgsf3rk2vul
bc1qtnqw53pxxp3j0a7ttuurqzuzxnn66su8svwv6k
bc1qvahawe2w84mgqgspcgx4uyu0vgw6r9y96srcj2
1NVHhVjcPEWdUNpUjb3RaBWPw2WdvZ7JEk
bc1q0q5gsymkvp7vffpuexz0eq5csufxs60npza3ct5
bc1q6gj8ymnjh863gmuvh2nc3462trrvzlxf2atzxn
bc1q7cd8rxvvwuqgeh2ya9vk2ekr9qutthyklzkamf8
bc1qc2gtz9eadvr9mf2xcptyjatajakx93schz35aq7
bc1qc5sn0myjvc8lj7n5xs3qdq6k9t07xn6vtew2ze
bc1qfrmrz7nx6c62qdf6gqk65yajn2k89hfy9cum44
bc1qqp7nt7m7m9fju2uflds93u9n5du78q3mhx6qss
bc1qrkusavjestgd6lud0rjpr47x4vs2udpqesjsn8
bc1qtdyul6azg4lfecpkyaq3gdvpypxgz2ap8cgd5f
1LYiEgq9k3xSAddbqMZcsVTayJVoKbTFub
```