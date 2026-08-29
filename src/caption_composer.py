def compose_caption(title: str, summary: str, platform: str) -> str:
    # Shared brand voice fragments
    brand_voice = "Exciting news from FlyRank! 🚀"
    
    if platform.lower() == "instagram":
        return f"{brand_voice}\n\n{title}\n\n{summary}\n\n#Tech #AI #Innovation #FlyRank"
    elif platform.lower() == "x":
        # Shorter, punchier for X
        return f"{title}: {summary[:120]}... Read more! 🧵👇 #BuildInPublic"
    else:
        return f"{title}\n\n{summary}"