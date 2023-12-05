from io import StringIO
from unittest import TestCase
from unittest.mock import patch


def calculate_average_score():
    total_score = 0
    number_of_innings = 0

    while True:
        try:
            score = int(input("Enter number of runs scored (q to finish) : "))
        except ValueError:
            print("Invalid input")
            continue

        if score == -1:
            break
        else:
            number_of_innings += 1
            total_score += score

    if number_of_innings == 0:
        print("No valid score entered")
    else:
        average_score = total_score / number_of_innings
        print(f"The average runs scored is: {average_score:.2f}")


class Test(TestCase):
    @patch("builtins.input", side_effect=["10", "20", "-1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_batting_average(self, mock_stdout, mock_input):
        calculate_average_score()
        self.assertEqual(mock_stdout.getvalue().strip(), "The average runs scored is: 15.00")

    @patch("builtins.input", side_effect=["abc", "15", "25", "-1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_calculate_average_score_invalid_input(self, mock_stdout, mock_input):
        calculate_average_score()
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid input\nThe average runs scored is: 20.00")
