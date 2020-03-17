# SpringerLink journal parser
A parser designed to get a full archives of a certain academic journal published by SpringerLink

## This project needs a further development!

I have upload the very initial python script to this repo and you could make use of it directly with an established env. I'll spare some other time to compile it to an execute. I'll hurry :D

To directly execute the python script you will need the following env:

- python3
- bs4 | Beautifulsoup the python module
- requests

Attention that `requests` the python module has not been built-in so far and you may have problems importing it. If so, a solution with [Google](http://google.com) may help :)

Once launched, the script will create a folder under the present directory and store all the arhives inside. The articles and citation would be stored in multiple folders, whose index corresponds to the issues or volumes of the original jounal.

## Proxy

I set a proxy by default to `http://127.0.0.1:1087` to speed up the access to web. If you don't want a proxy or you don't use a proxy, please change the assignment of proxy to `proxies=None`, or the access would fail as no server will respond.

## Warning

I wrote this scripts as an extension of the existing [Sci-Hub](http://sci-hub.tw) project, which unlocks most of the copyright journals. It could be a great violence in the name of academic freedom. Please pay attention.
