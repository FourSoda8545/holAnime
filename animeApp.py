## app para ver animes 

from animefvl import AnimeFVL
with AnimeFVL() as api:
    anime = api.search_anime("FUll Metal Alchemist")
    elements = api.search(input("Escribe la serie: "))

    for i, element in enumerate(elements):
        print(f"{i}, {element.title}")
        print(f"{i}, {element.synopsis}")
        print(f"{i}, {element.episodes}")
        print(f"{i}, {element.status}")
        print(f"{i}, {element.score}")
        
        try:
            selection = int(input("select option:"))
            info = api.get_anime_info(elements[selection].id)
            info.episodes.reverse()
            
            for j, episode in enumerate(info.episodes):
                print(f"{j} | Episode - {episode.id}")
            index_episode = int(input("Select episode"))
            serie = elements[selection].id
            capitulo = info.episodes[index_episode].id
            results = api.get_links(Serie, capitulo)
            for result in results:
                print(f"{result.server} - ********")
                
        except Exception as e:
            print(e)
