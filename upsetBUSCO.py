import sys
import pandas as pd
from upsetplot import from_contents, plot
from matplotlib import pyplot

pd.set_option('future.no_silent_downcasting', True)

df1 = pd.read_table("PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
print(df1.head().values.tolist())
df2 = pd.read_table("PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.onlyRNASeq__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df3 = pd.read_table("PITALB_v0.2.coll_scaffolds_final.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df4 = pd.read_table("PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df5 = pd.read_table("PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.onlyRNASeq__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df6 = pd.read_table("PITALB_v0.2.hap1_scaffolds_final_mod.masked.braker3.feb2024.RNASeqProtsViridiplantaeOrthoDB__braker.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df7 = pd.read_table("universe.BUSCO_embryophyta_odb10",header=None)
df8 = pd.read_table("universe.BUSCO_liliopsida_odb10",header=None)

df9 = pd.read_table("galba.february2024.coll.Bromeliaceae_NCBI__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df10 = pd.read_table("galba.february2024.coll.Bromeliaceae_NCBI__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df11 = pd.read_table("galba.february2024.coll.ViridiplantaeOrthoDB__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df12 = pd.read_table("galba.february2024.coll.ViridiplantaeOrthoDB__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df13 = pd.read_table("galba.february2024.hap1.Bromeliaceae_NCBI__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df14 = pd.read_table("galba.february2024.hap1.Bromeliaceae_NCBI__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)
df15 = pd.read_table("galba.february2024.hap1.ViridiplantaeOrthoDB__augustus.hints.BUSCO_embryophyta_odb10__run_embryophyta_odb10__full_table.found.gz",header=None)
df16 = pd.read_table("galba.february2024.hap1.ViridiplantaeOrthoDB__augustus.hints.BUSCO_liliopsida_odb10__run_liliopsida_odb10__full_table.found.gz",header=None)

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
 'ProtsViridiplantae' : df1.values.flatten().tolist(),
 'RNASeq' : df2.values.flatten().tolist(),
 'RNASeqProtsViridiplantae' : df3.values.flatten().tolist(),
 'universe' :  df8.values.flatten().tolist()
}
dataBRAKERLiliopsidaHap1 = {
 'ProtsViridiplantae' : df4.values.flatten().tolist(),
 'RNASeq' : df5.values.flatten().tolist(),
 'RNASeqProtsViridiplantae' : df6.values.flatten().tolist(),
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
fig1 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKEREmbryophytaColl),fig=fig1, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.coll Embryophyta")
pyplot.savefig("BRAKER.PITALB_v0.2.coll.Embryophyta.png",dpi=300,format='png')


fig2 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKEREmbryophytaHap1),fig=fig2, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.hap1 Embryophyta")
pyplot.savefig("BRAKER.PITALB_v0.2.hap1.Embryophyta.png",dpi=300,format='png')

fig3 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKERLiliopsidaColl),fig=fig3, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.coll Liliopsida")
pyplot.savefig("BRAKER.PITALB_v0.2.coll.Liliopsida.png",dpi=300,format='png')


fig4 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataBRAKERLiliopsidaHap1),fig=fig4, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("BRAKER PITALB_v0.2.hap1 Liliopsida")
pyplot.savefig("BRAKER.PITALB_v0.2.hap1.Liliopsida.png",dpi=300,format='png')


fig5 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBALiliopsidaHap1),fig=fig5, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.hap1 Liliopsida")
pyplot.savefig("GALBA.PITALB_v0.2.hap1.Liliopsida.png",dpi=300,format='png')

fig6 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBALiliopsidaColl),fig=fig6, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.coll Liliopsida")
pyplot.savefig("GALBA.PITALB_v0.2.coll.Liliopsida.png",dpi=300,format='png')

fig7 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBAEmbryophytaHap1),fig=fig7, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.hap1 Embryophyta")
pyplot.savefig("GALBA.PITALB_v0.2.hap1.Embryophyta.png",dpi=300,format='png')

fig8 = pyplot.figure(figsize=(14,6))
plot(from_contents(dataGALBAEmbryophytaColl),fig=fig8, show_counts="{:d}", show_percentages=True, element_size=None)
pyplot.suptitle("GALBA PITALB_v0.2.coll Embryophyta")
pyplot.savefig("GALBA.PITALB_v0.2.coll.Embryophyta.png",dpi=300,format='png')

