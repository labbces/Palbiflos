#!/bin/bash

#PBS -q par128
#PBS -l nodes=1:ppn=128
#PBS -m abe

module load singularity/3.8.3-gcc-9.4.0

cd $PBS_O_WORKDIR

#singularity exec -B ${PWD}:${PWD} galba.sif galba.pl --genome=B2.asm.hic.p_utg_mask.soft.fasta --prot_seq=sorghum_prots_NCBI.nr90.fasta --workingdir=galba.junhe23 --threads 128
#singularity exec -B ${PWD}:${PWD}  ~/Projects/Sugarcane/Assemblies/B4/GALBA/galba.sif galba.pl --genome=yahs.PITALB_v0.2.hap1_scaffolds_final_mod.fa.masked --prot_seq=Bromeliaceae_NCBI.fasta --workingdir=galba.february2024.Bromeliaceae_NCBI --threads 128
#singularity exec -B ${PWD}:${PWD}  ~/Projects/Sugarcane/Assemblies/B4/GALBA/galba.sif galba.pl --genome=yahs.PITALB_v0.2.hap1_scaffolds_final_mod.fa.masked --prot_seq=Viridiplantae.fa  --workingdir=galba.hap1.february2024.ViridiplantaeOrthoDB  --threads 128
singularity exec -B ${PWD}:${PWD}  ~/Projects/Sugarcane/Assemblies/B4/GALBA/galba.sif galba.pl --genome=yahs.PITALB_v0.2.col_scaffolds_final.fa.masked --prot_seq=Bromeliaceae_NCBI.fasta --workingdir=galba.february2024.coll.Bromeliaceae_NCBI --threads 128
singularity exec -B ${PWD}:${PWD}  ~/Projects/Sugarcane/Assemblies/B4/GALBA/galba.sif galba.pl --genome=yahs.PITALB_v0.2.col_scaffolds_final.fa.masked --prot_seq=Viridiplantae.fa  --workingdir=galba.february2024.coll.ViridiplantaeOrthoDB  --threads 128
