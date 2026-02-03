import datetime
import time # To make the "loading" part feel more dramatic

def display_lana_face():
    # A stylized Lana-inspired ASCII face
    lana = """
         .---.
        /     \\      "I believe in the kindness of strangers.
       (  -  -  )      And when I'm at war with myself...
        )  ▿  (                   I RIDE."
       /   -   \\ 
      / /|   |\\ \\    🥀✨🍒🎀🐎💎🥀✨🍒🎀🐎💎
    """
    print(lana)

def music_manager():
    display_lana_face()
    
    # We will pre-load your favorite Lana songs into the list
    songs = [
        {"title": "Ride", "artist": "Lana Del Rey 🏍️"},
        {"title": "White Mustang", "artist": "Lana Del Rey 🐎"}
    ]
    
    print("Pre-loading your favorites: Ride & White Mustang...")
    
    # Let the user add more if they want
    while True:
        more = input("\nAdd another song? (Type the name or 'no' to save): ")
        if more.lower() == 'no':
            break
        songs.append({"title": more, "artist": "Lana Del Rey 🥀"})

    print("\n--- Revving up the White Mustang... ---")
    for i in range(3):
        print("VROOM... 💨")
        time.sleep(0.5)

    # Saving the file with aesthetic formatting
    file_name = "lana_playlist.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("✨ L A N A   D E L   R E Y   P L A Y L I S T ✨\n")
        file.write(f"Date: {datetime.datetime.now().strftime('%m/%d/%Y')}\n")
        file.write("=" * 45 + "\n")
        file.write("“Summer's meant for loving and leaving.” 🐎\n")
        file.write("“I've got a war in my mind.” 🏍️\n")
        file.write("=" * 45 + "\n\n")

        # Bonus: Numbering and Emojis
        for i, track in enumerate(songs, 1):
            file.write(f"{i:02}. {track['title']} -- {track['artist']}\n")
        
        file.write("\n" + "=" * 45)
        file.write("\nStay wild. Be free. 🍒")

    print(f"\n🎀 Done! Your '{file_name}' is ready to be shared with the class.")

music_manager()
