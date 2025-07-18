link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

link_len = 11
id_start = "v="
link_id = ""

print(f"link: {link}")
if id_start in link:
    index = link.find(id_start) + 2
    link_id = link[index: index + 12]
    print(f"ID: {link_id}")
else:
    print("Link don't have ID")