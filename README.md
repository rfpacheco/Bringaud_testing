#  Bringaud testing data

## Needed files:

### L. major genome

We'll get the data from [TryTrypDB](https://tritrypdb.org/tritrypdb/app/record/dataset/NCBITAXON_347515), based on the
primary publication of [Ivens et al. (2005)](https://pubmed.ncbi.nlm.nih.gov/16020728/).

Information about [_L. major_ file](./data/TriTrypDB-68_LmajorFriedlin_Genome.fasta):
- Primary contact: Pathogen Sequencing Unit, Wellcome Sanger Institute
- Source version(s): GCA_000002725.2, May 28, 2016, Sep 01, 2022
- Release # / date: TriTrypDB rel. 60, 2022-NOV-09
- Summary: Genome sequence and annotation for Leishmania major Friedlin.
- Megabase Pairs: 32.86

Following this table, seems there were no modification to the genome fasta file, only the annotation

| VEuPathDB Build | Release Date | Release | Genome Source | Genome Version  | Structural Annotation Source | Structural Annotation Version | Functional Annotation Source | Functional Annotation Version | Note                                                              |
|-----------------|--------------|---------|---------------|-----------------|------------------------------|-------------------------------|------------------------------|-------------------------------|-------------------------------------------------------------------|
| 0               | 2005-01-01   | 1.0     | GeneDB        | Oct 20, 2010    | GeneDB                       | Oct 20, 2010                  |                              |                               |                                                                   |
| 18              | 2013-05-31   | 5.0     | GeneDB        | Jan 16, 2013    | GeneDB                       | Jan 16, 2013                  |                              |                               | re-annotated                                                      |
| 27              | 2016-02-20   | 27      | GeneDB        | Jan 16, 2013    | GeneDB                       | Jan 16, 2013                  | GeneDB                       | Oct 5, 2015                   | functional annotation updated                                     |
| 29              | 2016-10-12   | 29      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Aug 07, 2016                  | re-annotated, functional annotation updated                       |
| 32              | 2017-04-20   | 32      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Mar 11, 2017                  | functional annotation updated                                     |
| 33              | 2017-06-30   | 33      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | May 20, 2017                  | functional annotation updated                                     |
| 37              | 2018-04-25   | 37      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Feb 25, 2018                  | functional annotation updated                                     |
| 41              | 2018-12-13   | 41      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Oct 22, 2018                  | functional annotation updated                                     |
| 43              | 2019-04-25   | 43      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Mar 30, 2019                  | functional annotation updated                                     |
| 44              | 2019-07-02   | 44      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | May 24, 2019                  | functional annotation updated                                     |
| 48              | 2020-08-27   | 48      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | May 06, 2020                  | functional annotation updated                                     |
| 49              | 2020-11-05   | 49      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Sep 01, 2020                  | functional annotation updated                                     |
| 51              | 2021-03-16   | 51      | GeneDB        | May 28, 2016    | GeneDB                       | May 28, 2016                  | GeneDB                       | Jan 01, 2021                  | functional annotation updated                                     |
| 52              | 2021-05-20   | 52      | GenBank       | GCA_000002725.2 | GeneDB                       | May 28, 2016                  | GeneDB                       | Apr 01, 2021                  | rebuild with INSDC accession added, functional annotation updated |
| 54              | 2021-09-08   | 54      | GenBank       | GCA_000002725.2 | GeneDB                       | May 28, 2016                  | GeneDB                       | Aug 03, 2021                  | functional annotation updated                                     |
| 60              | 2022-11-09   | 60      | GenBank       | GCA_000002725.2 | GeneDB                       | May 28, 2016                  | GeneDB                       | Sep 01, 2022                  | functional annotation updated                                     |
	
functional annotation updated

### Hallmark 79 from T. brucei ingi/RIME

>ingi_1 Trypanosoma brucei ingi element
CCCTGGCGATGCCGGCCACCTCAACGTGGTGCCAGGGTCCAGTACCCCGTATCATCGGGG
GAAGCCAAGAGCCAGCAGC

Which is the same as in RIME

### SIDERs from Bringaud to compare

The [SIDERs list from Bringaud](./data/Bringaud_SIDERs.pdf)
