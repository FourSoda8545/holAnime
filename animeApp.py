from animefvl import AnimeFVL

with AnimeFVL() as api:
    anime_name = input("Escribe el nombre del anime: ")
    anime = api.search_anime(anime_name)
    elements = api.search(anime_name)

    for i, element in enumerate(elements):
        print(f"{i}, {element.title}")
        print(f"{i}, {element.synopsis}")
        print(f"{i}, {element.episodes}")
        print(f"{i}, {element.status}")
        print(f"{i}, {element.score}")
        
        try:
            selection = int(input("Selecciona una opción: "))
            info = api.get_anime_info(elements[selection].id)
            info.episodes.reverse()
            
            for j, episode in enumerate(info.episodes):
                print(f"{j} | Episode - {episode.id}")
            index_episode = int(input("Selecciona el episodio: "))
            serie = elements[selection].id
            capitulo = info.episodes[index_episode].id
            results = api.get_links(serie, capitulo)
            for result in results:
                print(f"{result.server} - ********")
                
        except Exception as e:
            print(e)
