% fact name game with 1 argument

game('The legend of Zelda: Tears of the kingdom').
game('PUBG').
game('Black myth wukong').
game('Silent hill').
game('The scourge').
game('Subnautica').
game('League of legends').
game('Arena of valor').
game('Elden ring').
game('It take two').
game('Sea of Thieves').
game('Rush royal').

% game genre

genre(action).
genre(adventure).
genre(horro).
genre(shooter).
genre(funny).
genre(strategy).
genre(role_playing).

% game platform

platform(pc).
platform(plastation).
platform(xbox).
platform(switch).
platform(mobile).

% Тип игры

type(online).
type(offline).

% fact with 2 arguments
% game and genre

genre_game('The legend of Zelda: Tears of the kingdom',adventure).
genre_game('The legend of Zelda: Tears of the kingdom',action).
genre_game('The legend of Zelda: Tears of the kingdom',role_playing).

genre_game('PUBG',shooter).
genre_game('PUBG',action).

genre_game('Black myth wukong',action).
genre_game('Black myth wukong',role_playing).
genre_game('Black myth wukong',adventure).

genre_game('Silent hill',horro).
genre_game('Silent hill',adventure).
genre_game('Silent hill',role_playing).


genre_game('The scourge',horro).
genre_game('The scourge',action).
genre_game('The scourge',role_playing).

genre_game('Subnautica',adventure).
genre_game('Subnautica',horro).
genre_game('Subanutica',action).

genre_game('League of legends',strategy).
genre_game('League of legends',role_playing).
genre_game('League of legends',action).

genre_game('Arena of valor',strategy).
genre_game('Arena of valor',action).
genre_game('Arena of valor',role_playing).

genre_game('Elden ring',horro).
genre_game('Elden ring',action).
genre_game('Elden ring',adventure).

genre_game('It take two',funny).
genre_game('It take two',adventure).

genre_game('Sea of Thieves',adventure).
genre_game('Sea of Thieves',action).
genre_game('Sea of Thieves',strategy).

% game in platform

platform_game('The legend of Zelda: Tears of the kingdom', switch).

platform_game('PUBG', pc).
platform_game('PUBG', xbox).
platform_game('PUBG', mobile).

platform_game('Black myth wukong', pc).
platform_game('Black myth wukong', playstation).
platform_game('Black myth wukong', xbox).

platform_game('Silent hill', playstation).
platform_game('Silent hill', pc).

platform_game('The scourge', pc).
platform_game('The scourge', playstation).

platform_game('Subnautica', pc).
platform_game('Subnautica', xbox).
platform_game('Subnautica', playstation).

platform_game('League of legends', pc).

platform_game('Arena of valor', mobile).

platform_game('Elden ring', pc).
platform_game('Elden ring', playstation).
platform_game('Elden ring', xbox).

platform_game('It take two', pc).
platform_game('It take two', playstation).
platform_game('It take two', xbox).

platform_game('Sea of Thieves', pc).
platform_game('Sea of Thieves', xbox).

% game and Тип игры

type_game('The legend of Zelda: Tears of the kingdom', offline).

type_game('PUBG', online).

type_game('Black myth wukong', offline).

type_game('Silent hill', offline).

type_game('The scourge', offline).

type_game('Subnautica', offline).

type_game('League of legends', online).

type_game('Arena of valor', online).

type_game('Elden ring', offline).
type_game('Elden ring', online).

type_game('It take two', online).

type_game('Sea of Thieves', online).

% Правила
% Правило для поиска игры на платформе с определенным жанром

game_on_platform_with_genre(Game, Platform, Genre):-
    platform_game(Game, Platform),
    genre_game(Game, Genre).

% Правило для поиска игр одного жанра

same_game_genre(Game1, Game2):-
    genre_game(Game1, Genre),
    genre_game(Game2, Genre),
    \+(Game1 = Game2).

find_game_same_genre(Game1, Genre, Game2):-
    genre_game(Game1, Genre),
    genre_game(Game2, Genre),
    \+(Game1 = Game2).

% Правило для поиска игр на платформе

game_in_platform(Game, Platform):- platform_game(Game, Platform).


% Правила поиска игр одного жанра и типа

game_same_genre_and_type(Game1, Game2, Genre, Type):-
    genre_game(Game1, Genre),
    genre_game(Game2, Genre),
    type_game(Game1, Type),
    type_game(Game2, Type),
    Game1 \= Game2.
