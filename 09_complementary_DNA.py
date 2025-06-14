# start: 3:33pm 14/6/2025
# end: 3:53pm 14/6/2025
#  Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)
#
#     "ATTGC" --> "TAACG"
#     "GTAT" --> "CATA"

def complement_DNA(dna):
    output_dna = ''
    convert_dna = {'A' : 'T', #converts A to T and vice versa
                   'T' : 'A',
                   'C' : 'G', #converts C to G and vice versa
                   'G' : 'C'}
    for letter in dna:
        output_dna += convert_dna[letter] #converts and joins dna letters to the output dna
    return output_dna

def assertion_test():
    #test only single letters first
    assert complement_DNA('AAAAA') == 'TTTTT'
    assert complement_DNA('TTTTT') == 'AAAAA'
    assert complement_DNA('CCCCC') == 'GGGGG'
    assert complement_DNA('GGGGG') == 'CCCCC'
    #test conbinations of DNA
    assert complement_DNA('ATTCG') == 'TAAGC'
    assert complement_DNA('GTAT') == 'CATA'
    assert complement_DNA('AACTCCTCCGAAATGGCTAGATT') == 'TTGAGGAGGCTTTACCGATCTAA'

    #test false cases
    assert complement_DNA('ATA') != 'TTT'
    assert complement_DNA('GCC') != 'ATT'
    assert complement_DNA('TCG') != 'AGG'


def main():
    assertion_test()

if __name__ == '__main__':
    main()
