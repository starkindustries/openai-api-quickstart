from dotenv import load_dotenv
import quickstart


def test_quickstart():
    load_dotenv()
    prompt = "Say this is a test"
    response = quickstart.get_gpt_response(prompt)
    print("GPT-3 response:", response)
    assert "this is a test" in response.lower()