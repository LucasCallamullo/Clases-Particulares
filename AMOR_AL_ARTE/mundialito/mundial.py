

from pais import Pais
from group import Group
from knockout_stage import KnockoutStage
    
def main(paises):
    groups = (
        'Group A', 
        'Group B',
        'Group C',
        'Group D',
        'Group E',
        'Group F',
        'Group G',
        'Group H'
    )
    
    v_groups = []
    for g in groups:
        group = Group(g)
        v_groups.append(group)
    
    cont = 0
    for p in paises:
        pais = Pais(p['pais'], p['score'], p['pos'])
        group = v_groups[cont]
        group.add_country(pais)
        cont += 1
        if cont == 8:
            cont = 0
    
    # Fecha 1
    for g in v_groups:
        g.make_fixture()
        g.play_next_match()
        g.play_next_match()
        print(g)
        
    # Fecha 2
    print("\n\n\n\n\n\n\n\n\n\n")
    for g in v_groups:
        g.play_next_match()
        g.play_next_match()
        print(g)
        
    # Fecha 3
    print("\n\n\n\n\n\n\n\n\n\n")
    for g in v_groups:
        g.play_next_match()
        g.play_next_match()
        print(g)
        
    
    # Octavos de Final
    octavos = KnockoutStage("Octavos de Final")
    for i in range(0, len(v_groups), 2):
        g1 = v_groups[i]    
        g2 = v_groups[i+1]    
        country1, country2 = g1.get_podium()
        country3, country4 = g2.get_podium()
        octavos.add_match(country1, country4)
        octavos.add_match(country2, country3)
        
    print("\n\n\n\n\n\n\n\n\n\n")
    winners = octavos.play_all()
    
    # Cuartos de Final
    cuartos = KnockoutStage("Cuartos de Final")
    for i in range(0, len(winners), 2):
        country1 = winners[i]
        country2 = winners[i+1]
        cuartos.add_match(country1, country2)
    
    print("\n\n\n\n\n\n\n\n\n\n")
    winners = cuartos.play_all()
    
    # Semi Final
    semis = KnockoutStage("Semifinal")
    for i in range(0, len(winners), 2):
        country1 = winners[i]
        country2 = winners[i+1]
        semis.add_match(country1, country2)
    
    print("\n\n\n\n\n\n\n\n\n\n")
    winners = semis.play_all()
    
    # Semi Final
    final = KnockoutStage("Final")
    for i in range(0, len(winners), 2):
        country1 = winners[i]
        country2 = winners[i+1]
        final.add_match(country1, country2)
    
    print("\n\n\n\n\n\n\n\n\n\n")
    winners = final.play_all()
    
    
if __name__ == "__main__":
    paises = [
        {"pais": "Argentina", "pos": 1, "score": 4},
        {"pais": "France", "pos": 2, "score": 4},
        {"pais": "Croatia", "pos": 3, "score": 4},
        {"pais": "Morocco", "pos": 4, "score": 4},
        {"pais": "Netherlands", "pos": 5, "score": 4},
        {"pais": "England", "pos": 6, "score": 4},
        {"pais": "Brazil", "pos": 7, "score": 4},
        {"pais": "Portugal", "pos": 8, "score": 4},
        {"pais": "Japan", "pos": 9, "score": 3},
        {"pais": "Senegal", "pos": 10, "score": 3},
        {"pais": "Australia", "pos": 11, "score": 3},
        {"pais": "Switzerland", "pos": 12, "score": 3},
        {"pais": "Spain", "pos": 13, "score": 3},
        {"pais": "USA", "pos": 14, "score": 3},
        {"pais": "Poland", "pos": 15, "score": 3},
        {"pais": "South Korea", "pos": 16, "score": 3},
        {"pais": "Germany", "pos": 17, "score": 2},
        {"pais": "Ecuador", "pos": 18, "score": 2},
        {"pais": "Cameroon", "pos": 19, "score": 2},
        {"pais": "Uruguay", "pos": 20, "score": 2},
        {"pais": "Tunisia", "pos": 21, "score": 2},
        {"pais": "Mexico", "pos": 22, "score": 2},
        {"pais": "Belgium", "pos": 23, "score": 2},
        {"pais": "Ghana", "pos": 24, "score": 2},
        {"pais": "Saudi Arabia", "pos": 25, "score": 1},
        {"pais": "Iran", "pos": 26, "score": 1},
        {"pais": "Costa Rica", "pos": 27, "score": 1},
        {"pais": "Serbia", "pos": 28, "score": 1},
        {"pais": "Wales", "pos": 29, "score": 1},
        {"pais": "Canada", "pos": 30, "score": 1},
        {"pais": "Qatar", "pos": 31, "score": 1},
        {"pais": "Denmark", "pos": 32, "score": 1}
    ]
    main(paises)
