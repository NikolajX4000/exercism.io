def to_rna(dna_strand):
    transcription = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    rna_strand = ''
    for c in dna_strand:
        rna_strand += transcription[c]
    return rna_strand
