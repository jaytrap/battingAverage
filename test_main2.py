from unittest import TestCase
from unittest.mock import patch
from io import StringIO

def bat_average():
    total_score = 0
    innings = 0
    status = 'c'
    while status == 'c':
        score = input("Enter score run: ")
        if score.isnumeric():
            total_score += int(score)
            innings += 1
        elif score == 'q':
            status = 'q'
    if innings == 0:
        print("No valid score entered")
    else:
        average = total_score / innings
        print(f"The average runs scored is: {average:.2f}")


class Test(TestCase):
    @patch('builtins.input', side_effect=['10', '20', '30', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_basic_input(self, mock_stdout, mock_input):
        bat_average()
        self.assertEqual(mock_stdout.getvalue().strip(), "The average runs scored is: 20.00")

    @patch('builtins.input', side_effect=['q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_no_scores_entered(self, mock_stdout, mock_input):
        bat_average()
        self.assertEqual(mock_stdout.getvalue().strip(), "No valid score entered")

