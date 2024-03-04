SAMPLES=["BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB/braker" ,"BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB/braker" ,"BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyRNASeq/braker" ,"GALBA/galba.february2024.coll.Bromeliaceae_NCBI/augustus.hints" ,"BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB/braker" ,"GALBA/galba.february2024.coll.ViridiplantaeOrthoDB/augustus.hints" ,"BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB/braker" ,"GALBA/galba.february2024.hap1.Bromeliaceae_NCBI/augustus.hints" ,"BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyRNASeq/braker","GALBA/galba.february2024.hap1.ViridiplantaeOrthoDB/augustus.hints"]
#SAMPLES=["test.p1", "test.p2"]

rule all:
    input:
        expand("{sample}.BUSCO_embryophyta_odb10/", sample=SAMPLES),
        expand("{sample}.BUSCO_liliopsida_odb10/", sample=SAMPLES)

rule BUSCO_liliopsida:
    input:
        "{sample}.aa"
    output:
        directory("{sample}.BUSCO_liliopsida_odb10/")
    threads: 10
    shell:
        """
        #module load BUSCO/5.4.4
        busco --offline --download_path /home/lovelace/proj/proj832/diriano/Projects/Sugarcane/busco-data.ezlab.org/v5/data --in  {input} --cpu {threads}  --out {wildcards.sample}.BUSCO_liliopsida_odb10 --mode prot --lineage liliopsida_odb10 
        """

rule BUSCO_embryophyta:
    input:
        "{sample}.aa"
    output:
         directory("{sample}.BUSCO_embryophyta_odb10/")
    threads: 10
    shell:
        """
        #module load BUSCO/5.4.4
        busco --offline --download_path /home/lovelace/proj/proj832/diriano/Projects/Sugarcane/busco-data.ezlab.org/v5/data --in  {input} --cpu {threads}  --out {wildcards.sample}.BUSCO_embryophyta_odb10 --mode prot --lineage embryophyta_odb10
        """
