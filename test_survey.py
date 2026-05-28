from survey import AnonymousSurvey

def test_store_single_response():
    question = "What is your native language? "
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('english')
    assert 'english' in language_survey.responses

def test_store_three_response():
    question = "What is your native language? "
    language_survey = AnonymousSurvey(question)
    responses = ['French','English','German']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses