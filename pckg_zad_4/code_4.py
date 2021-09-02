def checking_input_sentence(user_input_lst):
    defined_marks = {",", ".", ":", "?", "!"}
    clear_sentence = []
    for word in user_input_lst:
        if word.isalpha():
            print("OK-no action: ", word)
            clear_sentence.append(word)
        else:
            print("---------------------------------------------------")
            print("YES - action is needed: ", word)
            not_marks = []
            marks_in = []
            for chr in word:
                if chr in defined_marks:
                    marks_in.append(chr)
                else:
                    not_marks.append(chr)
            print("Marks: ", marks_in)
            print("Characters: ", not_marks)
            word = "".join(not_marks)
            print(f"NOW - word is: {word}")
            final_wrd = word + marks_in[0]
            print("Final word -> ", final_wrd)
            clear_sentence.append(final_wrd)
    return clear_sentence

