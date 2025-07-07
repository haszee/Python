weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}


weather_today = input(
    "What's the weather like today?"
    "\n1. Sunny ☀"
    "\n2. Rainy 🌧"
    "\n3. Cloudy ☁"
    "\n4. Snowy ❄"
    "\nChoose 1, 2, 3 or 4: "
    )

if weather_today == "1":
    print(weather_activities["1"])
if weather_today == "2":
    print(weather_activities["2"])
if weather_today == "3":
    print(weather_activities["3"])
if weather_today == "4":
    print(weather_activities["4"])
