'''
Start
1. Ask user for input and convert the string to uppercase for uniformity
2. Allow the program to read long strings
3. Identify specific patterns linked to genetic markers
4. Predict possible traits based on these markers
5. Split the DNA sequence by different markers
6. Replace specific nucleotide patterns
End
'''
trait_marker_dict = {'TA':'blue eyes',
                     'TC':'brown eyes',
                     'TG':'green eyes',
                     'GT':'blonde hair',
                     'GA':'brown hair',
                     'GC':'black hair'
                    }

dna_sequence = input('Enter the DNA sequence: ').upper()
print(dna_sequence)

genetic_marker1 = 'TAGC'
genetic_marker2 = 'TACG'
genetic_marker3 = 'TCAG'
genetic_marker4 = 'TGAC'

if genetic_marker1 in dna_sequence:
    print(f'genetic marker found:',{genetic_marker1})

if genetic_marker2 in dna_sequence:
    print(f'genetic marker found:',{genetic_marker2})

if genetic_marker3 in dna_sequence:
    print(f'genetic marker found:',{genetic_marker3})

if genetic_marker4 in dna_sequence:
    print(f'genetic marker found:',{genetic_marker4})


replace_letter = input('Would you like to replace a letter?: Yes or  No : ').capitalize()

if replace_letter == 'Yes':
    letter1 = input('Which letter would you like to replace? :').upper()
    letter2 = input("What letter would you like to replace it with? :").upper()
    dna_sequence_replace = dna_sequence.replace(letter1,letter2)
    print(dna_sequence_replace)
else:
    print('No letter replaced')

segment = input('What letter would you like to segment the sequence by? :').upper()

try:
    seg_dna_seq = dna_sequence_replace.split(segment)
except:
    seg_dna_seq = dna_sequence.split(segment)

print(seg_dna_seq)

genetic_trait = []
for i in seg_dna_seq:
    if i in trait_marker_dict:
        value = trait_marker_dict.get(i)
        genetic_trait.append(value)
    else:
        continue

print(f'The genetic marker/s for,{genetic_trait} likely exist')

