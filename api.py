import enum
from typing import Annotated
from livekit.agents import llm
import logging

logger = logging.getLogger("nba-stats")
logger.setLevel(logging.INFO)

class Team(enum.Enum):
    CELTICS = "celtics"
    LAKERS = "lakers"
    WARRIORS = "warriors"
    BULLS = "bulls"
    HEAT = "heat"
    BUCKS = "bucks"
    NUGGETS = "nuggets"
    SUNS = "suns"
    SIXERS = "sixers"
    KNICKS = "knicks"
    NETS = "nets"
    CLIPPERS = "clippers"
    JAZZ = "jazz"
    SPURS = "spurs"
    ROCKETS = "rockets"
    PISTONS = "pistons"
    KINGS = "kings"
    MAVERICKS = "mavericks"
    BLAZERS = "blazers"
    PACERS = "pacers"
    HAWKS = "hawks"
    MAGIC = "magic"
    TIMBERWOLVES = "timberwolves"
    WIZARDS = "wizards"
    THUNDER = "thunder"
    GRIZZLIES = "grizzlies"
    PELICANS = "pelicans"
    RAPTORS = "raptors"
    CAVALIERS = "cavaliers"
    HORNETS = "hornets"



class Position(enum.Enum):
    POINT_GUARD = "point guard"
    SHOOTING_GUARD = "shooting guard"
    SMALL_FORWARD = "small forward"
    POWER_FORWARD = "power forward"
    CENTER = "center"

class AssistantFnc(llm.FunctionContext):
    def __init__(self) -> None:
        super().__init__()
        
        self._team_championships = {
            Team.CELTICS: 17,
            Team.LAKERS: 17,
            Team.WARRIORS: 7,
            Team.BULLS: 6,
            Team.HEAT: 3,
            Team.BUCKS: 2,
            Team.NUGGETS: 1,
            Team.SUNS: 0,
            Team.SIXERS: 3,
            Team.KNICKS: 2,
            Team.NETS: 0,
            Team.CLIPPERS: 0,
            Team.JAZZ: 0,
            Team.SPURS: 5,
            Team.ROCKETS: 2,
            Team.PISTONS: 3,
            Team.KINGS: 1,
            Team.MAVERICKS: 1,
            Team.BLAZERS: 1,
            Team.PACERS: 0,
            Team.HAWKS: 1,
            Team.MAGIC: 0,
            Team.TIMBERWOLVES: 0,
            Team.WIZARDS: 1,
            Team.THUNDER: 0,
            Team.GRIZZLIES: 0,
            Team.PELICANS: 0,
            Team.RAPTORS: 1,
            Team.CAVALIERS: 1,
            Team.HORNETS: 0
        }

        self._team_stats = {
            Team.CELTICS: {"wins": 24, "losses": 9},
            Team.LAKERS: {"wins": 18, "losses": 14},
            Team.WARRIORS: {"wins": 18, "losses": 16},
            Team.BULLS: {"wins": 15, "losses": 18},
            Team.HEAT: {"wins": 16, "losses": 14},
            Team.BUCKS: {"wins": 17, "losses": 14},
            Team.NUGGETS: {"wins": 18, "losses": 13},
            Team.SUNS: {"wins": 15, "losses": 17},
            Team.SIXERS: {"wins": 13, "losses": 17},
            Team.KNICKS: {"wins": 23, "losses": 10},
            Team.NETS: {"wins": 12, "losses": 20},
            Team.CLIPPERS: {"wins": 19, "losses": 14},
            Team.JAZZ: {"wins": 7, "losses": 24},
            Team.SPURS: {"wins": 17, "losses": 16},
            Team.ROCKETS: {"wins": 21, "losses": 11},
            Team.PISTONS: {"wins": 14, "losses": 18},
            Team.KINGS: {"wins": 14, "losses": 19},
            Team.MAVERICKS: {"wins": 20, "losses": 13},
            Team.BLAZERS: {"wins": 11, "losses": 21},
            Team.PACERS: {"wins": 16, "losses": 18},
            Team.HAWKS: {"wins": 18, "losses": 15},
            Team.MAGIC: {"wins": 20, "losses": 14},
            Team.TIMBERWOLVES: {"wins": 17, "losses": 15},
            Team.WIZARDS: {"wins": 5, "losses": 25},
            Team.THUNDER: {"wins": 27, "losses": 5},
            Team.GRIZZLIES: {"wins": 23, "losses": 11},
            Team.PELICANS: {"wins": 5, "losses": 28},
            Team.RAPTORS: {"wins": 7, "losses": 26},
            Team.CAVALIERS: {"wins": 29, "losses": 4},
            Team.HORNETS: {"wins": 7, "losses": 25} 
        }

    @llm.ai_callable(description="get the number of championships for a specific team")
    def get_championships(self, team: Annotated[Team, llm.TypeInfo(description="The NBA team")]):
        logger.info("get championships - team %s", team)
        championships = self._team_championships[Team(team)]
        return f"The {team} have won {championships} NBA championships"
    
    @llm.ai_callable(description="get current season record for a team")
    def get_team_record(self, team: Annotated[Team, llm.TypeInfo(description="The NBA team")]):
        logger.info("get team record - team %s", team)
        stats = self._team_stats.get(Team(team))
        if stats:
            return f"The {team} current record is {stats['wins']}-{stats['losses']}"
        return f"Current record not available for {team}"
    
    @llm.ai_callable(description="get information about positions in basketball")
    def get_position_info(self, position: Annotated[Position, llm.TypeInfo(description="The basketball position")]):
        position_info = {
            Position.POINT_GUARD: "The point guard is typically the team's primary ball handler and playmaker, responsible for running the offense.",
            Position.SHOOTING_GUARD: "The shooting guard is usually the team's best perimeter shooter and scorer.",
            Position.SMALL_FORWARD: "The small forward is a versatile position combining outside shooting with inside play.",
            Position.POWER_FORWARD: "The power forward plays near the basket, focusing on rebounding and inside scoring.",
            Position.CENTER: "The center is typically the tallest player, focusing on defense, rebounding, and scoring close to the basket."
        }
        logger.info("get position info - position %s", position)
        return position_info[Position(position)]
    
    @llm.ai_callable(description="get notable players for a specific team")
    def get_team_legends(self, team: Annotated[Team, llm.TypeInfo(description="The NBA team")]):
        team_legends = {
            Team.CELTICS: "Larry Bird, Bill Russell, Paul Pierce",
            Team.LAKERS: "Magic Johnson, Kobe Bryant, Kareem Abdul-Jabbar",
            Team.WARRIORS: "Stephen Curry, Klay Thompson, Wilt Chamberlain",
            Team.BULLS: "Michael Jordan, Scottie Pippen, Dennis Rodman",
            Team.HEAT: "Dwyane Wade, LeBron James, Alonzo Mourning",
            Team.BUCKS: "Kareem Abdul-Jabbar, Giannis Antetokounmpo, Oscar Robertson",
            Team.NUGGETS: "Nikola Jokic, Carmelo Anthony, Alex English",
            Team.SUNS: "Charles Barkley, Steve Nash, Devin Booker",
            Team.SIXERS: "Allen Iverson, Julius Erving, Wilt Chamberlain",
            Team.KNICKS: "Patrick Ewing, Walt Frazier, Willis Reed",
            Team.NETS: "Jason Kidd, Vince Carter, Julius Erving",
            Team.CLIPPERS: "Chris Paul, Blake Griffin, Bob McAdoo",
            Team.JAZZ: "John Stockton, Karl Malone, Adrian Dantley",
            Team.SPURS: "Tim Duncan, David Robinson, George Gervin",
            Team.ROCKETS: "Hakeem Ol, Clyde Drexler, James Harden",
            Team.PISTONS: "Isiah Thomas, Joe Dumars, Ben Wallace",
            Team.KINGS: "Chris Webber, Oscar Robertson, Mitch Richmond",
            Team.MAVERICKS: "Dirk Nowitzki, Steve Nash, Jason Kidd",
            Team.BLAZERS: "Clyde Drexler, Bill Walton, Damian Lillard",
            Team.PACERS: "Reggie Miller, Paul George, Jermaine O'Neal",
            Team.HAWKS: "Dominique Wilkins, Bob Pettit, Dikembe Mutombo",
            Team.MAGIC: "Shaquille O'Neal, Dwight Howard, Tracy McGrady",
            Team.TIMBERWOLVES: "Kevin Garnett, Kevin Love, Karl-Anthony Towns",
            Team.WIZARDS: "Michael Jordan, Wes Unseld, Elvin Hayes",
            Team.THUNDER: "Kevin Durant, Russell Westbrook, Gary Payton",
            Team.GRIZZLIES: "Marc Gasol, Zach Randolph, Mike Conley",
            Team.PELICANS: "Anthony Davis, Chris Paul, Zion Williamson",
            Team.RAPTORS: "Vince Carter, Chris Bosh, Kyle Lowry",
            Team.CAVALIERS: "LeBron James, Kyrie Irving, Mark Price",
            Team.HORNETS: "Larry Johnson, Alonzo Mourning, Kemba Walker"
        }
        logger.info("get team legends - team %s", team)
        return f"Notable {team} legends include: {team_legends[Team(team)]}"