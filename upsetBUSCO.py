import sys
import pandas as pd
from upsetplot import from_contents, plot
from matplotlib import pyplot

pd.set_option('future.no_silent_downcasting', True)

df1 = pd.read_table("BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
print(df1.head().values.tolist())
df2 = pd.read_table("BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyRNASeq__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df3 = pd.read_table("BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df4 = pd.read_table("BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df5 = pd.read_table("BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyRNASeq__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df6 = pd.read_table("BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)


df17 = pd.read_table("BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB__braker.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df18 = pd.read_table("BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyRNASeq__braker.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df19 = pd.read_table("BRAKER/PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB__braker.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df20 = pd.read_table("BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB__braker.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df21 = pd.read_table("BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyRNASeq__braker.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df22 = pd.read_table("BRAKER/PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB__braker.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)


df7 = pd.read_table("universe.BUSCO_embryophyta_odb10.gz",header=None)
df8 = pd.read_table("universe.BUSCO_liliopsida_odb10.gz",header=None)

df9 = pd.read_table("GALBA/galba.february2024.coll.Bromeliaceae_NCBI__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df10 = pd.read_table("GALBA/galba.february2024.coll.Bromeliaceae_NCBI__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df11 = pd.read_table("GALBA/galba.february2024.coll.ViridiplantaeOrthoDB__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df12 = pd.read_table("GALBA/galba.february2024.coll.ViridiplantaeOrthoDB__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df13 = pd.read_table("GALBA/galba.february2024.hap1.Bromeliaceae_NCBI__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df14 = pd.read_table("GALBA/galba.february2024.hap1.Bromeliaceae_NCBI__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df15 = pd.read_table("GALBA/galba.february2024.hap1.ViridiplantaeOrthoDB__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df16 = pd.read_table("GALBA/galba.february2024.hap1.ViridiplantaeOrthoDB__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)

df23 = pd.read_table("GALBA/galba.march2024.coll.Bromeliaceae_NCBI__galba.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df24 = pd.read_table("GALBA/galba.march2024.coll.Bromeliaceae_NCBI__galba.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df25 = pd.read_table("GALBA/galba.march2024.coll.ViridiplantaeOrthoDB__galba.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df26 = pd.read_table("GALBA/galba.march2024.coll.ViridiplantaeOrthoDB__galba.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df27 = pd.read_table("GALBA/galba.march2024.hap1.Bromeliaceae_NCBI__galba.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df28 = pd.read_table("GALBA/galba.march2024.hap1.Bromeliaceae_NCBI__galba.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df29 = pd.read_table("GALBA/galba.march2024.hap1.ViridiplantaeOrthoDB__galba.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df30 = pd.read_table("GALBA/galba.march2024.hap1.ViridiplantaeOrthoDB__galba.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)

dataBRAKEREmbryophytaColl = {
 'ProtsViridiplantae' : df1.values.flatten().tolist(),
 'RNASeq' : df2.values.flatten().tolist(),
 'RNASeqProtsViridiplantae' : df3.values.flatten().tolist(),
 'universe' : df7.values.flatten().tolist() 
}
dataBRAKEREmbryophytaHap1 = {
 'ProtsViridiplantae' : df4.values.flatten().tolist(),
 'RNASeq' : df5.values.flatten().tolist(),
 'RNASeqProtsViridiplantae' : df6.values.flatten().tolist(),
 'universe' :  df7.values.flatten().tolist()
}

dataBRAKERLiliopsidaColl = {
 'ProtsViridiplantae' : df17.values.flatten().tolist(),
 'RNASeq' : df18.values.flatten().tolist(),
 'RNASeqProtsViridiplantae' : df19.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}
dataBRAKERLiliopsidaHap1 = {
 'ProtsViridiplantae' : df20.values.flatten().tolist(),
 'RNASeq' : df21.values.flatten().tolist(),
 'RNASeqProtsViridiplantae' : df22.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}

dataGALBALiliopsidaHap1 = {
 'Viridiplantae' : df16.values.flatten().tolist(),
 'Bromeliaceae' : df14.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}

dataGALBALiliopsidaColl = {
 'Viridiplantae' : df12.values.flatten().tolist(),
 'Bromeliaceae' : df10.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}

dataGALBAEmbryophytaHap1 = {
 'Viridiplantae' : df15.values.flatten().tolist(),
 'Bromeliaceae' : df13.values.flatten().tolist(),
 'universe' :  df7.values.flatten().tolist()
}

dataGALBAEmbryophytaColl = {
 'Viridiplantae' : df11.values.flatten().tolist(),
 'Bromeliaceae' : df9.values.flatten().tolist(),
 'universe' :  df7.values.flatten().tolist()
}

dataGALBABRAKEREmbryophytaColl = {
 'BRAKER_Prots' : df1.values.flatten().tolist(),
 'BRAKER_RNASeq' : df2.values.flatten().tolist(),
 'BRAKER_Both' : df3.values.flatten().tolist(),
 'GALBA_ViridiplantaeIncomplete' : df11.values.flatten().tolist(),
 'GALBA_BromeliaceaeIncomplete' : df9.values.flatten().tolist(),
 'GALBA_ViridiplantaeComplete' : df25.values.flatten().tolist(),
 'GALBA_BromeliaceaeComplete' : df23.values.flatten().tolist(),
 'universe' : df7.values.flatten().tolist()
}

dataGALBABRAKEREmbryophytaHap1 = {
 'BRAKER_Prots' : df4.values.flatten().tolist(),
 'BRAKER_RNASeq' : df5.values.flatten().tolist(),
 'BRAKER_Both' : df6.values.flatten().tolist(),
 'GALBA_ViridiplantaeIncomplete' : df15.values.flatten().tolist(),
 'GALBA_BromeliaceaeIncomplete' : df13.values.flatten().tolist(),
 'GALBA_ViridiplantaeComplete' : df29.values.flatten().tolist(),
 'GALBA_BromeliaceaeComplete' : df27.values.flatten().tolist(),
 'universe' :  df7.values.flatten().tolist()
}

dataGALBABRAKERLiliopsidaColl = {
 'BRAKER_Prots' : df17.values.flatten().tolist(),
 'BRAKER_RNASeq' : df18.values.flatten().tolist(),
 'BRAKER_Both' : df19.values.flatten().tolist(),
 'GALBA_ViridiplantaeIncomplete' : df12.values.flatten().tolist(),
 'GALBA_BromeliaceaeIncomplete' : df10.values.flatten().tolist(),
 'GALBA_ViridiplantaeComplete' : df26.values.flatten().tolist(),
 'GALBA_BromeliaceaeComplete' : df24.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}

dataGALBABRAKERLiliopsidaHap1 = {
 'BRAKER_Prots' : df20.values.flatten().tolist(),
 'BRAKER_RNASeq' : df21.values.flatten().tolist(),
 'BRAKER_Both' : df22.values.flatten().tolist(),
 'GALBA_ViridiplantaeIncomplete' : df16.values.flatten().tolist(),
 'GALBA_BromeliaceaeIncomplete' : df14.values.flatten().tolist(),
 'GALBA_ViridiplantaeComplete' : df30.values.flatten().tolist(),
 'GALBA_BromeliaceaeComplete' : df28.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}

fig1 = pyplot.figure(figsize=(14,6))
#Forcing to plot empty sybsets
#plot(from_contents(dataBRAKEREmbryophytaColl),fig=fig1, show_counts="{:d}", show_percentages=True, element_size=None,include_empty_subsets=True)
plot(from_contents(dataBRAKEREmbryophytaColl),fig=fig1, show_counts="{:d}", show_percentages=True, element_size=None,include_empty_subsets=False)
pyplot.suptitle("BRAKER PITALB_v0.2.coll Embryophyta")
pyplot.savefig("BRAKER/BRAKER.PITALB_v0.2.coll.Embryophyta.png",dpi=300,format='png')


fig2 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKEREmbryophytaHap1),fig=fig2, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.hap1 Embryophyta")
pyplot.savefig("BRAKER/BRAKER.PITALB_v0.2.hap1.Embryophyta.png",dpi=300,format='png')

fig3 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKERLiliopsidaColl),fig=fig3, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.coll Liliopsida")
pyplot.savefig("BRAKER/BRAKER.PITALB_v0.2.coll.Liliopsida.png",dpi=300,format='png')


fig4 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKERLiliopsidaHap1),fig=fig4, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.hap1 Liliopsida")
pyplot.savefig("BRAKER/BRAKER.PITALB_v0.2.hap1.Liliopsida.png",dpi=300,format='png')


fig5 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBALiliopsidaHap1),fig=fig5, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.hap1 Liliopsida")
pyplot.savefig("GALBA/GALBA.PITALB_v0.2.hap1.Liliopsida.png",dpi=300,format='png')

fig6 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBALiliopsidaColl),fig=fig6, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.coll Liliopsida")
pyplot.savefig("GALBA/GALBA.PITALB_v0.2.coll.Liliopsida.png",dpi=300,format='png')

fig7 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBAEmbryophytaHap1),fig=fig7, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.hap1 Embryophyta")
pyplot.savefig("GALBA/GALBA.PITALB_v0.2.hap1.Embryophyta.png",dpi=300,format='png')

fig8 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBAEmbryophytaColl),fig=fig8, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.coll Embryophyta")
pyplot.savefig("GALBA/GALBA.PITALB_v0.2.coll.Embryophyta.png",dpi=300,format='png')

fig9 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBABRAKEREmbryophytaColl),fig=fig9, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA and BRAKER PITALB_v0.2.coll Embryophyta")
pyplot.savefig("GALBA.BRAKER.PITALB_v0.2.coll.Embryophyta.png",dpi=300,format='png')

fig10 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBABRAKEREmbryophytaHap1),fig=fig10, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA and BRAKER PITALB_v0.2.hap1 Embryophyta")
pyplot.savefig("GALBA.BRAKER.PITALB_v0.2.hap1.Embryophyta.png",dpi=300,format='png')

fig11 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBABRAKERLiliopsidaColl),fig=fig11, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA and BRAKER PITALB_v0.2.coll Liliopsida")
pyplot.savefig("GALBA.BRAKER.PITALB_v0.2.coll.Liliopsida.png",dpi=300,format='png')

fig12 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBABRAKERLiliopsidaHap1),fig=fig12, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA and BRAKER PITALB_v0.2.hap1 Liliopsida")
pyplot.savefig("GALBA.BRAKER.PITALB_v0.2.hap1.Liliopsida.png",dpi=300,format='png')


