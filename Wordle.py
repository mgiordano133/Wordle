# Import modules
import pandas as pd
from datetime import date

class program:


    @staticmethod
    def wordle():

        # Read Excel file of wordle answers by date
        df = pd.read_excel('tmpTextData.xlsx',sheet_name='Sheet1')

        # Get today's date
        today = date.today().strftime("%b %d %Y")

        # Get answer for day and store in variable
        word = df.loc[df['Date']==today]['Word']
        word = str(word.item())

        # Index each letter of answer
        indexedAnswer = pd.DataFrame([x for x in word])
        # Initialize counter for number of tries
        q = 0
    
        while True:
            # Initialize list for 'squares' (so far just visualized as letters)
            # G: Green  Y: Yellow   X: Grey
            output = []

            # Get input for guess
            guess = str(input())
            guess = guess.upper()

            # Index each letter of guess
            indexedGuess = pd.DataFrame([x for x in guess])

            # If the word is a possible solution, take the answer.  If not, allow for repeat attempts.
            if df['Word'].str.contains(guess).sum() != 0 and len(guess) == 5:

                # If correct print G's and end program
                if guess == word:
                    print(['G' for x in range(0,5)])
                    print('Congrats!')
                    break
                
                # If incorrect, print appropriate response
                else:
                    # Loop through letters to determine 'color' of squares for game
                    for index in range(0,5):
                        # If correct letter and placement, 'G'
                        if indexedAnswer.iloc[index][0] == indexedGuess.iloc[index][0]:
                            output.append('G')
                        else:
                            # If incorrect placement but letter is in word, 'Y'
                            if str(indexedGuess.iloc[index][0]) in word:
                                output.append('Y')
                            # Else 'X'
                            else:
                                output.append('X')

                    # Print 'squares'
                    print(output)
                    q += 1

                    # If six tries, end game
                    if q == 6:
                        print('You lost!')
                        break

                
            else:
                # Error message allows for unlimited 'Invalid' attempts
                print('Invalid guess')




def main():
    
    program.wordle()
    

if __name__ == '__main__':
    main()