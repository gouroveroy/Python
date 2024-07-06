import time
import random


def testScript():
    with open("paragraphs.txt", "r") as file:
        paragraphs = file.read()
        list_of_paragraphs = paragraphs.split("\n")
        paragraphList = []
        for paragraph in list_of_paragraphs:
            if paragraph != "":
                para = paragraph[3 : len(paragraph)]
                paragraphList.append(para)

        return random.choice(paragraphList)


def typingTest(start, end, user_input, paragraph):
    time_taken = end - start
    words = user_input.split(" ")
    correct_words = 0
    for word in words:
        if word in paragraph:
            correct_words += 1
    accuracy = (correct_words / len(words)) * 100
    print(f"Time taken: {round(time_taken)} seconds")
    print(f"Accuracy: {round(accuracy)}%")
    words_per_minute = len(words) / time_taken * 60
    print(f"Typing speed is: {round(words_per_minute)} wpm")
    print(f"Net speed is: {round(words_per_minute * accuracy / 100)} wpm")


def main():
    print("welcome to the typing test".upper())
    print("You will be given a paragraph to type out")
    print("You will be timed and your accuracy will be measured")
    print("Good luck")
    while True:
        print("Would you like to start the test? (yes/no)")
        response = input()
        if "n" in response.lower():
            return

        else:
            paragraph = testScript()
            print(paragraph)
            print("\n\n")
            start = time.time()
            user_input = input()
            end = time.time()
            typingTest(start, end, user_input, paragraph)
            print("\n\n")


if __name__ == "__main__":
    main()
