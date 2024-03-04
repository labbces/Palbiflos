# Genome annotation of __Pitcairnia albiflos__

## Gene prediction with extrinsic evidence

We use two pipelines to predict gene models exploiting extrinsic evidence, BRAKER which can use Protein, RNASeq or both kinds of dataset as extrinsic evidence, and GALBA which only uses proteins as extrinsic evidence.

| Number | Evidence | BRAKER | GALBA |
| --- | --- | --- | --- |
| 1 | Protein Sequences Viridiplantae from OrthoDB v10 | X | X |
| 2 | RNASeq (CHA742B,CHA744,CHA745A,CHA747,CHA749B,PBO670,PBO674A,PBO675,PBO677,PBO678)| X | |
| 3 | Protein Sequences Bromeliaceae from NCBI | | X |

BRAKER was run in three different ways, with only evidence 1, only evidence 2 and with both evidences 1 and 2. GALBA was run two times, onece with evidence 1 and once with evidence 2.
