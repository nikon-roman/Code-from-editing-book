import pokebase as pb


charizard = pb.pokemon("charizard")
print(charizard.name)  # charizard
print(charizard.height)  # 17
types = [t.type.name for t in charizard.types]
print(types)  # ['fire', 'flying']
