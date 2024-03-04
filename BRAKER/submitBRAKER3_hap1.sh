#!/bin/bash

#PBS -q par128
#PBS -l nodes=1:ppn=128
#PBS -m abe

module load singularity/3.8.3-gcc-9.4.0

cd $PBS_O_WORKDIR

export BRAKER_SIF=/home/lovelace/proj/proj832/diriano/Projects/Sugarcane/Assemblies/B4/BRAKER3/braker3.sif

#singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Saccharum SP80-3280" --genome=B2.asm.hic.p_utg_mask.soft.fasta --prot_seq=external_prots.fasta --bam=hisat2_output.sorted.bam --softmasking --workingdir=braker3.junhe23 --threads 16
#BRAKER RNASeq e Prots
#singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Pitcairnia albiflos hap1" --genome=yahs.PITALB_v0.2.hap1_scaffolds_final_mod.fa.masked --prot_seq=Viridiplantae.fa --bam=RNASeqmapping/hisat2_output_hap1.sorted.bam --softmasking --workingdir=PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB --threads 128
#BRAKER only RNASeq
singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Pitcairnia albiflos hap1 2" --genome=yahs.PITALB_v0.2.hap1_scaffolds_final_mod.fa.masked --bam=RNASeqmapping/hisat2_output_hap1.sorted.bam --softmasking --workingdir=PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyRNASeq --threads 128
#BRAKER only Prots
singularity exec -B ${PWD}:${PWD} ${BRAKER_SIF} braker.pl --species "Pitcairnia albiflos hap1 3" --genome=yahs.PITALB_v0.2.hap1_scaffolds_final_mod.fa.masked --prot_seq=Viridiplantae.fa --softmasking --workingdir=PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB --threads 128
