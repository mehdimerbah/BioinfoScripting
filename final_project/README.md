## Final Project

### Testing The Scripts

The following is a small gif showing a test of the scripts on the given data.

![Testing](Test.gif)    


### How To Use The Scripts
#### Part One
`./part_one path/to/fasta_file.fasta`

Part One timing with no Sequence prompt:
`real	0m0.184s   
user	0m0.130s   
sys	0m0.013s   
`

Part One timing with Sequence prompt:
`real	0m3.939s   
user	0m0.153s   
sys	0m0.012s   
`


#### Part Two
`./part_two`      
Current timing on 3 amino acid peptide sequence:    

`real	0m0.057s   
user	0m0.051s   
sys		0m0.004s   
`

Current timing for: MSLMVVSMAC    
Number of mRNA Sequences: 27648    

`real	0m0.418s   
user	0m0.218s   
sys	0m0.091s   
`

For the sequence: MSLMVVSMACVGVHRK (16 AA)    

Number of mRNA Sequences: 42,467,328    
Most Probable mRNA Sequence Based on GC content:     
AUGUCUUUAAUGGUUGUUUCUAUGGCUUGCGUCGGCGUCCACCGCAAG   
GC Content: 50.00% (Normally, many sequences have 50% GC content so I just take the first)    

`real	10m32.145s   
user	3m27.942s   
sys	2m23.052s    
`


For the sequence: MEGGGKPNSSSNSRDDGN (18 AA) On the Server     

Number of mRNA Sequences: 1,019,215,872    
Most Probable mRNA Sequence Based on GC content:     
AUGGAAGGUGGUGGUAAACCUAAUUCUUCUUCUAACUCCCGCGACGACGGCAAC    
GC Content: 50.00%   
`Running time ~18 Hours   
real    1105m22.276s   
user    315m4.436s   
sys     484m29.170s   
`
