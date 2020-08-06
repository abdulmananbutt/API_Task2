# This is the class we want to test. So, we need to import it
from Tests import given_program

# test case function to check the Weather.get_public_data function

expected = "It works!!!"
url = "https://opendata.sz.gov.cn/api/29200_01503673/1/service.xhtml"
payload = {
        'page': 1,
        'rows': 1,
        'appKey': '46ee202a8eea4292868562710c12ac85'
}


def test_public_data():
    test_obj = given_program.GivenProgram()
    print("Start get_public_data test\n")
    result = test_obj.public_data(url, payload)
    # check if get_public_data return 'It works!!!'
    assert result != None  # null result will fail the test
    assert expected == result

    #print("\nFinish get_public_data test\n")