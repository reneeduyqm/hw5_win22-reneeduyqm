# Your name: Renee Du
# Your student id: 97626101
# Your email: reneedu@umich.edu
# List who you have worked with on this homework: Loria Sun

import re, os, unittest
from tempfile import tempdir
from xml.etree.ElementPath import find

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')

    # Read the lines from the file object into a list
    lines = infile.readlines()

    # Close the file object
    infile.close()

    # return the list of lines
    return lines

def find_movie_titles(string_list):
    """
    This function returns a dictionary with the keys being numbers, (1 - 8)
    and the values being the names of movies.
    """
    # pass

    dict = {}
    idx = 1
    for value in (string_list):
         
        temp = re.findall("^[Tt]itle: (.+)",value) 
            
        if temp:
            dict[idx] = temp[0]
            idx += 1

    return dict

def find_and_phrases(string_list):
    """
    This function finds all phrases with the word "and"
    and then returns them in a list.
    """
    lst = []
    exp = r'(\w* and \w*)'
    for w in string_list:
        temp = re.findall(exp, w)
        if temp:
            for i in temp:
                lst.append(i)
    return lst   
            

def find_urls(string_list):
    """
    This functions returns a list of valid urls in the list of strings
    """
    lst = []
    exp = r'https?:\/\/www.[a-z]*.com'
    for str in string_list:
        url = re.findall(exp, str)
        if url:
            lst.append(url)
    return lst

def find_valid_release_dates(string_list):
    """
    This function returns a list of valid release dates.
    Sample format:
        mm/dd/yyyy
        mm/dd/yy
        mm-dd-yyyy
        mm-dd-yy
    Please refer to the instructions and be careful about invalid dates!
    """
    lst = []
    exp = r'\b(([0][1-9]|[1][0-2])(\/|-)([0][1-9]|[1][0-9]|[2][0-9]|[3][0-1])(\/|-)\d{2,4})\b'
    for strings in string_list:
        strings = strings.rstrip()
        dates = re.findall(exp, strings)
        for date in dates:
            lst.append(date[0])
    return lst
    
## Extra credit
def count_mid_str(string_list, string):
    """
    This function returns a count of the number of times a specified string appears
    in the text. The matched string should be in the middle of a word (ie: Not at 
    the start of end of a word).
    """
    count = 0
    exp = ''
    pass

#Implement your own tests
class TestAllMethod(unittest.TestCase):
    
    def test_find_movie_titles(self):
        string_list = read_file("best_picture.txt")
        self.assertEqual(len(find_movie_titles(string_list)), 8)
        self.assertEqual(find_movie_titles(string_list)[1], 'Belfast')
        self.assertEqual(find_movie_titles(string_list)[2], 'CODA')

    def test_find_valid_release_dates(self):
        string_list = read_file("best_picture.txt")
        self.assertEqual(len(find_valid_release_dates(string_list)), 5)
        self.assertEqual(find_valid_release_dates(string_list)[0], '08-13-2021')
        self.assertEqual(find_valid_release_dates(string_list)[2], '11/24/21')

    def test_find_and_phrases(self):
        string_list = read_file("best_picture.txt")
        self.assertEqual(len(find_and_phrases(string_list)), 10)
        self.assertEqual(find_and_phrases(string_list)[0], 'boy and his')
        self.assertEqual(find_and_phrases(string_list)[1], 'Music and her')

    def test_find_urls(self):
        string_list = read_file("best_picture.txt")
        self.assertEqual(len(find_urls(string_list)), 7)
        self.assertEqual(find_urls(string_list)[2], ['https://www.netflix.com'])
        self.assertEqual(find_urls(string_list)[3], ['https://www.imdb.com'])

    #Uncomment if working on Extra Credit
    #def test_count_mid_str(self):
    #    pass

    
def main():
    #Feel free run your functions here as well!
    file = read_file("best_picture.txt")
    find_movie_titles(file)
    find_and_phrases(file)
    find_urls(file)
    find_valid_release_dates(file)
    # pass

if __name__ == '__main__':
    main()
    print()
    unittest.main(verbosity=2)