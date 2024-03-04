#!/bin/bash

#PBS -q par128
#PBS -l nodes=1:ppn=128
#PBS -m abe

module load singularity/3.8.3-gcc-9.4.0

cd $PBS_O_WORKDIR

export BRAKER_SIF=/home/lovelace/proj/proj832/diriano/Projects/Sugarcane/Assemblies/B4/BRAKER3/braker3.sif


#BRAKER RNASeq e Prots
singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Pitcairnia albiflos coll 1" --genome=yahs.PITALB_v0.2.col_scaffolds_final.fa.masked --prot_seq=Viridiplantae.fa --bam=RNASeqmapping/hisat2_output_coll.sorted.bam --softmasking --workingdir=PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB --threads 48
#BRAKER only RNASeq
singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Pitcairnia albiflos coll 2" --genome=yahs.PITALB_v0.2.col_scaffolds_final.fa.masked --bam=RNASeqmapping/hisat2_output_coll.sorted.bam --softmasking --workingdir=PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyRNASeq --threads 48
#BRAKER only Prots
singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Pitcairnia albiflos coll" --genome=yahs.PITALB_v0.2.col_scaffolds_final.fa.masked --prot_seq=Viridiplantae.fa --softmasking --workingdir=PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB --threads 48

