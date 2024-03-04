#!/bin/bash

#PBS -q par128
#PBS -l nodes=1:ppn=128
#PBS -m abe

CPUS=128
cd $PBS_O_WORKDIR

module load hisat/2.2.1 samtools/1.17
mkdir -p RNASeqmapping/
cd RNASeqmapping/
hisat2-build --large-index -p $CPUS --seed 12345 ../../yahs.PITALB_v0.2.col_scaffolds_final.fa.masked yahs.PITALB_v0.2.col_scaffolds_final.masked

hisat2 --dta -x yahs.PITALB_v0.2.col_scaffolds_final.masked -1 ../../RNA-seq_albiflos/Subsample/CHA742B_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA744_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA745A_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA747_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA749B_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO670_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO674A_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO675_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO677_RNA_1.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO678_RNA_1.fastq.gz -2 ../../RNA-seq_albiflos/Subsample/CHA742B_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA744_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA745A_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA747_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/CHA749B_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO670_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO674A_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO675_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO677_RNA_2.fastq.gz,../../RNA-seq_albiflos/Subsample/PBO678_RNA_2.fastq.gz --rna-strandness RF --time --no-unal --threads $CPUS --seed 12345 | samtools view -Sbh > hisat2_output_coll.bam

samtools sort -o hisat2_output_coll.sorted.bam --threads $CPUS hisat2_output_coll.bam
samtools index hisat2_output_coll.sorted.bam
