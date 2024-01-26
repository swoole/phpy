from gradio_client import Client

client = Client("http://192.168.1.146:8088/")
result = client.predict(
        "Hello!!",	# str  in 'Input' Textbox component
        api_name="/predict"
    )
print(result)
