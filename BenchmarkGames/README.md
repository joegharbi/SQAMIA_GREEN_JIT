# Energy Efficiency in Programming Languages
#### Investigating The Energy Consumption of Erlang Programming Language Using the _Computer Language Benchmark Game_ as a case study.

## How to use this repo:
- Windows 10 or later
- Scaphandre installed [from here](https://hubblo-org.github.io/scaphandre-documentation/)
- Rapl driver for windows [found here](https://github.com/hubblo-org/windows-rapl-driver)
- compile the needed benchmarks(C, Erlang, Java)
- run the the python scripts that will start the measurements and output the results in a CSV file.

### What is this?

This repo contains the source code of 5 distinct benchmarks, implemented in 4 different languages (exactly as taken from the [Computer Language Benchmark Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)).

It also contains tools which provide support, for each benchmark of each language, to 4 operations: *(1)* **compilation**, *(2)* **execution**, *(3)* and **energy measuring**.

#### The Structure
Basically, the directories tree will look something like this:

Taking the `C` language as an example, this is how the folder for the `binary-trees` and `k-nucleotide` benchmarks would look like:

```Java
| ...
| C
	| binary-trees
		| binarytrees.gcc-3.c
		| Makefile
	| k-nucleotide
		| knucleotide.c
		| knucleotide-input25000000.txt
		| Makefile
	| ...
| ...

```


#### IMPORTANT NOTE:
This repo is edited by Youssef Gharbi supervised by Dr. Melinda Tóth. The original work exits here in [The Computer Language Benchmark Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)


### Contacts and References

[Green Software Lab](http://greenlab.di.uminho.pt)

Main contributors: [@Marco Couto](http://github.com/MarcoCouto) and [@Rui Pereira](http://haslab.uminho.pt/ruipereira)


[The Computer Language Benchmark Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)

