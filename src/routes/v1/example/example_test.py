from example import ExampleApi
def test_list_examples_OK():
    api = ExampleApi(None)
    
    response = api.list_examples()
    assert response == "list examples route"