from survey import AnonymousSurvey

question = "What is your native language?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Type 'q' to finish program")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\n Thank you for answers")
language_survey.show_results()