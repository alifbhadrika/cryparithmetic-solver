import re
import itertools
import time

def main():
    ''' 
    main function of this program
    handle file I/O and whole function 
    '''

    print("--- CRYPARITHMETIC PUZZLEZ ---")

    print()
    inputfile = input("ENTER inputFilename.txt: ")
    print()

    print("----- PROBLEM: -----\n")
    with open('../test/'+inputfile,'r') as file:
        listInput = []
        for line in file:
            print(line.rstrip('\n'))
            if line.startswith('-'):
                continue
            else:
                listInput.append(line.replace('+','').rstrip('\n').lower())

    print("\n----- SOLUTION: -----\n")
    start = time.time()

    solve(listInput)

    end = time.time()
    print("EXECUTION TIME: {:.6f} seconds".format(end-start))

def wordValue(word, letterValue):
    ''' 
    wordValue menerima parameter string word yaitu kata inputan,
    letterValue yaitu dictionary yang menyimpan nilai dari setiap huruf,
    menghasilkan nilai dari satu kata.
    Contoh:
    SEND dengan { S : 1, E : 2, N : 3, D : 4 }
    SEND = 1*1000 + 2*100 + 3*10 + 4*1
    '''

    wordValue = 0
    n = len(word) 
    factor = 1
    for _ in range (n-1):
        factor *= 10
    for letter in word:
        wordValue += factor * letterValue[letter]
        factor = int (factor/10)
    return wordValue

def printSolution(operands,value,letterValue):
    '''
    Mencetak solusi dengan format:
    9821
    1213+
    -----
    17830
    '''

    operands_letter = list('/'.join(operands))
    value_letter = list(''.join(value))
    for op_letter in operands_letter:
        if op_letter == '/':
            print()
            continue
        print("{}".format(letterValue[op_letter]),end="")
    print("+")
    print("-----")
    for val_letter in value_letter:
        print("{}".format(letterValue[val_letter]),end="")

def solve(words):
    '''
    solve akan memproses persamaan penjumlahan dan mengembalikan
    solusi crypariitmetic puzzle
    Algoritma:
    1. membuat list letters yang terdiri setiap huruf unique yang ada pada persamaan
    2. mengidentifikasi kata pada operan dan hasil penjumlahan
    3. melakukan permutasi, yaitu menyusun digit 0-9 pada n buah huruf pada list letter
       dengan syarat huruf pertama pada hasil penjumlahan tidak boleh bernilai 0
    4. Substitusi setiap hasil permutasi pada persamaan, cek apakah jumlah operan sama 
       dengan hasil persamaan
    5. Jika tidak sama, ulangi langkah 3
    6. Jika sesuai, maka solusi ditemukan
    '''

    letters_from_words = ''.join(words)
    letters = []                            # ordered list of letters
    for letter in letters_from_words:       # pake ini karena kalo pake set() gaberaturan jadi gakonsisten waktunya
        if letter not in letters:
            letters.append(letter)

    value = words[-1]                       # hasil penjumlahan
    words.pop()                 
    operands = words                        # operand penjumlahan
    first_letter = value[0]                 # character pertama dari value (hasil penjumlahan)

    tescount = 0
    for perm in itertools.permutations(range(10), len(letters)):
        letterValue = dict(zip(letters, perm))
        tescount += 1

        if letterValue[first_letter] == 0:  # huruf pertama pada value tidak boleh bernilai 0
            continue            

        sum_of_operands = 0
        for word in operands:
            sum_of_operands += wordValue(word,letterValue)
        
        if sum_of_operands == wordValue(value, letterValue):
            break
    
    printSolution(operands,value,letterValue)
    
    print("\n\nNUMBER OF TEST: {}".format(tescount))

if __name__ == '__main__':
    main()