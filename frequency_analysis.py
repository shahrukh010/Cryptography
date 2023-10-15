
import matplotlib.pyplot as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ';

def frequency_analysis(text):

    text = text.upper();
    letter_frequency = {};

    for letter in LETTERS:

        letter_frequency[letter] = 0;

    for character in text:

        if character in LETTERS:
            letter_frequency[character] +=1;
    return letter_frequency;

def caesar_crack(text):

    frq = frequency_analysis(text);
    frq_sort = sorted(frq.items(),key=lambda x:x[1],reverse=True);
#   print(frq);
    print(frq_sort);
    print('The possible key value: %s' %(LETTERS.find(frq_sort[0][0]) - LETTERS.find('E')));
    


def plot_distribution(frequencies):

    plt.bar(frequencies.keys(),frequencies.values());
    plt.show();



if __name__ == '__main__':

    plain_text = 'This code generates a paragraph by concatenating three random sentences'
#    frq = frequency_analysis(plain_text);
#    print(frq);
#    plot_distribution(frq);

    caesar_crack(plain_text);
