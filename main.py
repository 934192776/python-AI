import requests
# from rich import print
# from rich.markdown import Markdown
from http.server import BaseHTTPRequestHandler

api_key = "2046c535afeb092fo82f1d306d8a2b2t"


def display_current_weather(location):
  api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}&units=metric"

  response = requests.get(api_url)
  response_data = response.json()

  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']

  print(f"The current temperature in [bold]{location}[/bold] is [bold]{temperature}°C[/bold], {condition}.\n")

def generate_itinerary(origin, destination, duration):
  """ Generate travel itinerary between 2 places using AI """
  print(f"\n\nGenerating itinerary from {origin} to {destination}..\n")
  prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. This is a road, keep it short, less than 15 lines, add some emojis (not more than 5) to make readable. Add an estimated price of each day in euros"

  context = "You a travel specialist and know the best tourist spots around the world"
  api_key = "2046c535afeb092fo82f1d306d8a2b2t"
  api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

  response = requests.get(api_url)
  response_data = response.json()
  itinerary = response_data['answer']

  print(itinerary)

def welcome():
  """ Welcome message """
  print("[bold green]Welcome to the AI Travel Itinerary Planner[/bold green]")

def credit():
  """ Credit message """
  print("[green]The AI Travel Itinerary Planner was built by [bold]Jing Hui[/bold], thank you for using it 💖[/green]")

welcome()

origin = input("What city does your trip start from?\n")
destination = input("What city is your trip going to?\m")
duration = input("How many days will your trip last? (enter a number only, i.e 5)\n")

if origin and destination and duration.isdigit():
  display_current_weather(origin)
  display_current_weather(destination)
  generate_itinerary(origin, destination, duration)
  credit()
else:
  print("Please try again. Make sure you enter valid information")