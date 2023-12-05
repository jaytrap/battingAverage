# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def batting_average():
    total_score = 0
    number_of_innings = 0

    while True:
        try:
            score = int(input("Enter number of runs scored (-1 to finish) : "))
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

def bat_average():
    total_score = 0
    innings = 0
    status = 'c'
    while status == 'c':
        score = (input("Enter scored run: (q to finish): >>>"))
        if score.isnumeric():
            total_score += int(score)
            innings += 1
        elif score == 'q':
            status = 'q'
        else:
            print("Enter a valid score")
    if innings == 0:
        print("No valid score entered")
    else:
        average = total_score / innings
        print(f"The average runs scored is: {average:.2f}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    batting_average()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
