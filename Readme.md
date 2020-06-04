# Repetitive DNA comparison of different primitive cultivated potato species. 
### Gurina A., Divashuk M.

Big part of plant genome refers to repetitive genome fraction, include tandem repeats (satellites), LTR-elements and transposones. <br>
These part generally difficult in assambly and analysing. To identify these elements specific tools, such RepeatExplorer, could be used.
__So aim of these work is to compare repetitive DNA fraction of primitive potato species__
<br> <br>
To perform it, the following tasks were set:
- select samples with SRA data available in NCBI
- find repetitive elements using TAREAN
- compare repetitive DNA fraction of different primitive cultured potato species




#### __Requirements__
*Tested on UBUNTU 19.10*
<ol>
    <li> RepeatExplorer [1] with TAndem REpeats ANaliser (Tarean) tool[2]
    <li> Python3.6 or higher with packages:</li>
    - pandas 0.25.3<br>
    - numpy 1.18.1<br>
    - scikitlearn 0.23.0 <br>
    - matplotlib 3.2.0<br>
    - seaborn 0.10.0<br>
    - folium 0.11.0<br>
    - os <br>
    - argparse 1.1<br>
    <li> FastQC v0.11.8 [3] </li>
    <li> Preprocession of FASTQ paired-end reads on Galaxy 19.09 [4] </li>
    <li> NCBI SRA toolkit 2.9.3 [5] </li>
    <li> BLAST Command line Applications [6] </li>
</ol>

#### __Pipeline__
<ol>
    <li> Collecting SRA data from NCBI using SRA toolkit [5] </li>
    <li> Checking reads quality using FastQC [3] </li>
    <li> Preprocessing data on Galaxy server, including trimming, quality filtering, cutadapt filtering and interlacing. Broken pairs are discarded [4] </li>
    <li> randomly selecting paired-reads from library using 
        [reads_random_selection.py] (https://github.com/Alena-Gurina/Potato_repeats/blob/master/scripts/reads_random_selection.py) </li>
    <li> run RepeatExplorer [1] with Tarean [2]. 
        [We get such files] (https://github.com/Alena-Gurina/Potato_repeats/tree/master/tarean_report_files_example)</li>
    <li> repeat steps 4,5 5 times for each sample </li>
    <li> collecting data from Tarean reports using 
        [report_parsing.ipunb] (https://github.com/Alena-Gurina/Potato_repeats/blob/master/scripts/report_parsing.ipynb) </li>
    <li> creating local database of primitive cultivated potato repeats using BLAST Command line Application [6] <br> </li>
        `makeblastdb -in sequences_repeats.fasta -parse_seqids -blastdb_version 5 -title sequences_repeats -dbtype nucl`
    <li> run local BLAST <br> </li>
        'blastn -db sequence_repeats -query sequence_repeats.fasta -perc_identity 50 -max hsps 200 -outfmt 6 -out blast_results.txt`
    <li> analysis of blast and tarean results 
        [Blast_results_analysis.ipunb] (https://github.com/Alena-Gurina/Potato_repeats/blob/master/scripts/Blast_results_analysis.ipynb) </li> 
</ol>

#### Examples

Comparison compositions of repetitive DNA fration between species
![alt text][logo]

[logo]: https://github.com/Alena-Gurina/Potato_repeats/blob/master/illustarions/comparison_amount_repeats.png "Comparison compositions of repetitive DNA fration between species"


Local BLAST results
![alt text][logo1]

[logo1]:  https://github.com/Alena-Gurina/Potato_repeats/blob/master/illustarions/local_blast.png "Local BLAST results"

Cluster distribution of repetitive elements 
![alt text][logo2]

[logo2]:  https://github.com/Alena-Gurina/Potato_repeats/blob/master/illustarions/cluster_country.png "Cluster distribution of repetitive elements"

Map with points colored by presence of one of clusters (number 4) in sample
![alt text][logo3]

[logo3]: https://github.com/Alena-Gurina/Potato_repeats/tree/master/illustarions   "Map with points colored by presence of one of clusters (number 4) in sample"

[It's interactive view available on](https://github.com/Alena-Gurina/Potato_repeats/blob/master/illustarions/map_kl_4.html)


#### Liturature
<ol>
    <li>Novák, P., Neumann, P., Pech, J., Steinhaisl, J. & Macas, J. RepeatExplorer: a Galaxy-based web server for genome-wide characterization of eukaryotic repetitive elements from next-generation sequence reads. Bioinformatics 29, 792–793 (2013).</li>
    <li>Novak, P., Avila Robledillo, L., Koblizkova, A., Vrbova, I., Neumann, P., Macas, J. (2017) – TAREAN: a computational tool for identification and characterization of satellite DNA from unassembled short reads. Nucleic Acids Res., doi:10.1093/nar/gkx257</li>
    <li> FastQC: A Quality Control Tool for High Throughput Sequence Data [Online]. Available online at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ (2015), "FastQC," https://qubeshub.org/resources/fastqc.</li>
    <li> [Galaxy] (http://repeatexplorer-elixir.cerit-sc.cz/galaxy) </li>
    <li> Sequence Read Archive Submissions Staff. Using the SRA Toolkit to convert .sra files into other formats. In: SRA Knowledge Base [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2011-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK158900/ </li>
    <li> BLAST® Command Line Applications User Manual [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2008-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK279690/ </li>
    
</ol>
