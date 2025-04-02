# hello

Coding / algorithm practice.

## INSTALL

```sh
python3 -m venv ~/venv # ONCE
source ~/venv/bin/activate # EACH SESSION
pip install -U -r requirements.txt # ONCE'ish
```

## vim mappings

```
" python
nmap <F10> :w!<Return>:!black %<Return>:!python3 %<Return>
```
