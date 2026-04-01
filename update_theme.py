import os

files = ['style.css', 'index.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace('#ffcc00', '#ffffff')
    content = content.replace('255, 204, 0', '255, 255, 255')
    content = content.replace('#ff6600', '#aa0000')
    content = content.replace('255, 102, 0', '170, 0, 0')
    content = content.replace('Black-Yellow-Red', 'Black-White-Red')

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Theme updated to Black-White-Red successfully.")
