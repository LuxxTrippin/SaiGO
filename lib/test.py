from web_screenshot_module import specificpositionscreenshot, rescalc, webscreenshot

# Webhook URL
webhook_url = "https://discord.com/api/webhooks/1296834621706604648/Nr2sEUXSSWbxfVwzgk52-RBYaKNmBs--UTnRxKMf7IE7A2h-ALq-6ZrYW89fQVX52AFT"

# Take a full screenshot and send it to the webhook
print("Taking full screenshot...")
webscreenshot(webhook_url)

# Input specific coordinates for the region screenshot
coords = input("Enter coordinates for the specific screenshot (format: 'x1, y1, x2, y2'): ")

# Take a screenshot of the specific position and send it to the webhook
print("Taking specific position screenshot...")
specificpositionscreenshot(coords, webhook_url)

# Calculate adjusted coordinates
print("Calculating adjusted coordinates...")
adjusted_coords = rescalc(coords)

# Output the adjusted coordinates
print(f"Adjusted coordinates: {adjusted_coords}")