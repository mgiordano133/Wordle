
import pandas as pd
from datetime import date

class program:


    @staticmethod
    def wordle():


        df = pd.read_excel('tmpTextData.xlsx',sheet_name='Sheet1')
        today = date.today().strftime("%b %d %Y")
        word = df.loc[df['Date']==today]['Word']
        word = str(word.item())
        indexedAnswer = pd.DataFrame([x for x in word])
        q = 0
        while True:
            output = []
            guess = str(input())
            guess = guess.upper()
            indexedGuess = pd.DataFrame([x for x in guess])
            if df['Word'].str.contains(guess).sum() != 0:
                print(' ')
                if guess == word:
                    print(['G' for x in range(0,5)])
                    print('Congrats!')
                    break
                else:
                    for index in range(0,5):
                        if indexedAnswer.iloc[index][0] == indexedGuess.iloc[index][0]:
                            output.append('G')
                        else:
                            if str(indexedGuess.iloc[index][0]) in word:
                                output.append('Y')
                            else:
                                output.append('X')

                    print(output)
                    q += 1
                    if q == 6:
                        print('You lost!')
                        break

                
            else:
                print('Invalid guess')




def main():
    
    program.wordle()
    

if __name__ == '__main__':
    main()