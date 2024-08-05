# animefvl.py

class AnimeFVL:
    def __init__(self):
        self.anime_data = {
            "Full Metal Alchemist": {
                "title": "Full Metal Alchemist",
                "synopsis": "Two brothers search for a Philosopher's Stone...",
                "episodes": 64,
                "status": "Completed",
                "score": 8.5,
                "episodes_list": list(range(1, 65))
            }
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def search_anime(self, title):
        return self.anime_data.get(title)

    def search(self, query):
        results = []
        for title, data in self.anime_data.items():
            if query.lower() in title.lower():
                results.append(AnimeElement(data))
        return results

    def get_anime_info(self, anime_id):
        for title, data in self.anime_data.items():
            if anime_id == title:
                return AnimeInfo(data)
        return None

    def get_links(self, serie, capitulo):
        # Simulate fetching links
        return [AnimeLink("Server1"), AnimeLink("Server2")]


class AnimeElement:
    def __init__(self, data):
        self.id = data["title"]
        self.title = data["title"]
        self.synopsis = data["synopsis"]
        self.episodes = data["episodes"]
        self.status = data["status"]
        self.score = data["score"]


class AnimeInfo:
    def __init__(self, data):
        self.episodes = [AnimeEpisode(e) for e in data["episodes_list"]]


class AnimeEpisode:
    def __init__(self, id):
        self.id = id


class AnimeLink:
    def __init__(self, server):
        self.server = server
