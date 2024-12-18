import string
import math

# The set of special characters for use in the program
SPECIAL_CHARS = "!@#$%^&*()-_=+<>?{}[]"

def calculate_entropy(password: str) -> float:
    # Calculate password entropy in bits
    char_set_size = 0
    if any(c.isupper() for c in password):
        char_set_size += len(string.ascii_uppercase)
    if any(c.islower() for c in password):
        char_set_size += len(string.ascii_lowercase)
    if any(c.isdigit() for c in password):
        char_set_size += len(string.digits)
    if any(c in SPECIAL_CHARS for c in password):
        char_set_size += len(SPECIAL_CHARS)
        
    return len(password) * math.log2(char_set_size)

def find_sequential_chars(password: str, seq_length: int = 3) -> float:
    """
    Check for and penalize sequential patterns in password.
    Returns a penalty value between 0 and 1, where 1 means no sequences found
    and lower values indicate more/longer sequences.
    """
    # Common sequences to check
    sequences = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "".join(reversed(string.ascii_lowercase)),
        "".join(reversed(string.ascii_uppercase)),
        "".join(reversed(string.digits)),
        "qwerty" + "yuiop" + "asdfg" + "hjkl" + "zxcvb",  # Keyboard patterns
        "!@#$%^&*()",  # Common special char sequences
        "12345678901",
    ]
    
    penalty = 1.0
    password_lower = password.lower()  # For case-insensitive checks
    
    # Check for sequences of different lengths
    for seq_len in range(seq_length, min(len(password) + 1, 7)):
        for sequence in sequences:
            # Look for sequences in forward direction
            for i in range(len(sequence) - seq_len + 1):
                if sequence[i:i+seq_len].lower() in password_lower:
                    # Longer sequences get higher penalties
                    penalty *= (0.93 ** seq_len)
                    
    return max(0.1, penalty)  # Never reduce entropy by more than 90%  

# This function returns true if the password is in the top 500 passwords
def check_top_500_passwords(password: str) -> bool:
    TOP_500_PASSWORDS = [
        "123456",
        "password",
        "12345678",
        "qwerty",
        "123456789",
        "12345",
        "1234",
        "111111",
        "1234567",
        "dragon",
        "123123",
        "baseball",
        "abc123",
        "football",
        "monkey",
        "letmein",
        "696969",
        "shadow",
        "master",
        "666666",
        "qwertyuiop",
        "123321",
        "mustang",
        "1234567890",
        "michael",
        "654321",
        "superman",
        "1qaz2wsx",
        "7777777",
        "121212",
        "000000",
        "qazwsx",
        "123qwe",
        "killer",
        "trustno1",
        "jordan",
        "jennifer",
        "zxcvbnm",
        "asdfgh",
        "hunter",
        "buster",
        "soccer",
        "harley",
        "batman",
        "andrew",
        "tigger",
        "sunshine",
        "iloveyou",
        "2000",
        "charlie",
        "robert",
        "thomas",
        "hockey",
        "ranger",
        "daniel",
        "starwars",
        "klaster",
        "112233",
        "george",
        "computer",
        "michelle",
        "jessica",
        "pepper",
        "1111",
        "zxcvbn",
        "555555",
        "11111111",
        "131313",
        "freedom",
        "777777",
        "pass",
        "maggie",
        "159753",
        "aaaaaa",
        "ginger",
        "princess",
        "joshua",
        "cheese",
        "amanda",
        "summer",
        "love",
        "ashley",
        "6969",
        "nicole",
        "chelsea",
        "biteme",
        "matthew",
        "access",
        "yankees",
        "987654321",
        "dallas",
        "austin",
        "thunder",
        "taylor",
        "matrix",
        "william",
        "corvette",
        "hello",
        "martin",
        "heather",
        "secret",
        "merlin",
        "diamond",
        "1234qwer",
        "gfhjkm",
        "hammer",
        "silver",
        "222222",
        "88888888",
        "anthony",
        "justin",
        "test",
        "bailey",
        "q1w2e3r4t5",
        "patrick",
        "internet",
        "scooter",
        "orange",
        "11111",
        "golfer",
        "cookie",
        "richard",
        "samantha",
        "bigdog",
        "guitar",
        "jackson",
        "whatever",
        "mickey",
        "chicken",
        "sparky",
        "snoopy",
        "maverick",
        "phoenix",
        "camaro",
        "sexy",
        "peanut",
        "morgan",
        "welcome",
        "falcon",
        "cowboy",
        "ferrari",
        "samsung",
        "andrea",
        "smokey",
        "steelers",
        "joseph",
        "mercedes",
        "dakota",
        "arsenal",
        "eagles",
        "melissa",
        "boomer",
        "booboo",
        "spider",
        "nascar",
        "monster",
        "tigers",
        "yellow",
        "xxxxxx",
        "123123123",
        "gateway",
        "marina",
        "diablo",
        "bulldog",
        "qwer1234",
        "compaq",
        "purple",
        "hardcore",
        "banana",
        "junior",
        "hannah",
        "123654",
        "porsche",
        "lakers",
        "iceman",
        "money",
        "cowboys",
        "987654",
        "london",
        "tennis",
        "999999",
        "ncc1701",
        "coffee",
        "scooby",
        "0000",
        "miller",
        "boston",
        "q1w2e3r4",
        "brandon",
        "yamaha",
        "chester",
        "mother",
        "forever",
        "johnny",
        "edward",
        "333333",
        "oliver",
        "redsox",
        "player",
        "nikita",
        "knight",
        "fender",
        "barney",
        "midnight",
        "please",
        "brandy",
        "chicago",
        "badboy",
        "iwantu",
        "slayer",
        "rangers",
        "charles",
        "angel",
        "flower",
        "bigdaddy",
        "rabbit",
        "wizard",
        "jasper",
        "enter",
        "rachel",
        "chris",
        "steven",
        "winner",
        "adidas",
        "victoria",
        "natasha",
        "1q2w3e4r",
        "jasmine",
        "winter",
        "prince",
        "marine",
        "ghbdtn",
        "fishing",
        "cocacola",
        "casper",
        "james",
        "232323",
        "raiders",
        "888888",
        "marlboro",
        "gandalf",
        "asdfasdf",
        "crystal",
        "87654321",
        "12344321",
        "golden",
        "blowme",
        "bigtits",
        "8675309",
        "panther",
        "lauren",
        "angela",
        "bitch",
        "spanky",
        "thx1138",
        "angels",
        "madison",
        "winston",
        "shannon",
        "mike",
        "toyota",
        "jordan23",
        "canada",
        "sophie",
        "Password",
        "apples",
        "dick",
        "tiger",
        "razz",
        "123abc",
        "pokemon",
        "qazxsw",
        "55555",
        "qwaszx",
        "muffin",
        "johnson",
        "murphy",
        "cooper",
        "jonathan",
        "liverpoo",
        "david",
        "danielle",
        "159357",
        "jackie",
        "1990",
        "123456a",
        "789456",
        "turtle",
        "abcd1234",
        "scorpion",
        "qazwsxedc",
        "101010",
        "butter",
        "carlos",
        "password1",
        "dennis",
        "slipknot",
        "qwerty123",
        "booger",
        "asdf",
        "1991",
        "black",
        "startrek",
        "12341234",
        "cameron",
        "newyork",
        "rainbow",
        "nathan",
        "john",
        "1992",
        "rocket",
        "viking",
        "redskins",
        "butthead",
        "asdfghjkl",
        "1212",
        "sierra",
        "peaches",
        "gemini",
        "doctor",
        "wilson",
        "sandra",
        "helpme",
        "qwertyui",
        "victor",
        "florida",
        "dolphin",
        "pookie",
        "captain",
        "tucker",
        "blue",
        "liverpool",
        "theman",
        "bandit",
        "dolphins",
        "maddog",
        "packers",
        "jaguar",
        "lovers",
        "nicholas",
        "united",
        "tiffany",
        "maxwell",
        "zzzzzz",
        "nirvana",
        "jeremy",
        "suckit",
        "stupid",
        "porn",
        "monica",
        "elephant",
        "giants",
        "jackass",
        "hotdog",
        "rosebud",
        "success",
        "debbie",
        "mountain",
        "444444",
        "xxxxxxxx",
        "warrior",
        "1q2w3e4r5t",
        "q1w2e3",
        "123456q",
        "albert",
        "metallic",
        "lucky",
        "azerty",
        "7777",
        "shithead",
        "alex",
        "bond007",
        "alexis",
        "1111111",
        "samson",
        "5150",
        "willie",
        "scorpio",
        "bonnie",
        "gators",
        "benjamin",
        "voodoo",
        "driver",
        "dexter",
        "2112",
        "jason",
        "calvin",
        "freddy",
        "212121",
        "creative",
        "12345a",
        "sydney",
        "rush2112",
        "1989",
        "asdfghjk",
        "red123",
        "bubba",
        "4815162342",
        "passw0rd",
        "trouble",
        "gunner",
        "happy",
        "fucking",
        "gordon",
        "legend",
        "jessie",
        "stella",
        "qwert",
        "eminem",
        "arthur",
        "apple",
        "nissan",
        "bullshit",
        "bear",
        "america",
        "1qazxsw2",
        "nothing",
        "parker",
        "4444",
        "rebecca",
        "qweqwe",
        "garfield",
        "01012011",
        "beavis",
        "69696969",
        "jack",
        "asdasd",
        "december",
        "2222",
        "102030",
        "252525",
        "11223344",
        "magic",
        "apollo",
        "skippy",
        "315475",
        "girls",
        "kitten",
        "golf",
        "copper",
        "braves",
        "shelby",
        "godzilla",
        "beaver",
        "fred",
        "tomcat",
        "august",
        "buddy",
        "airborne",
        "1993",
        "1988",
        "lifehack",
        "qqqqqq",
        "brooklyn",
        "animal",
        "platinum",
        "phantom",
        "online",
        "xavier",
        "darkness",
        "blink182",
        "power",
        "fish",
        "green",
        "789456123",
        "voyager",
        "police",
        "travis",
        "12qwaszx",
        "heaven",
        "snowball",
        "lover",
        "abcdef",
        "00000",
        "pakistan",
        "007007",
        "walter",
        "playboy",
        "blazer",
        "cricket",
        "sniper",
        "hooters",
        "donkey",
        "willow",
        "loveme",
        "saturn",
        "therock",
        "redwings"
    ]

    return password in TOP_500_PASSWORDS 

# This function will return a 0, 1, 2 for low, medium, high strength passwords
def p_strength(password: str) -> int:
    # Return 0 if the length is 0
    if len(password) == 0:
        return 0

    # Check if the password is one of the top 500 passwords
    if check_top_500_passwords(password):
        return 0

    password_entropy = calculate_entropy(password) # Get the entropy of the password

    # If the entropy is less than 35, return 0
    if password_entropy < 35:
        return 0

    # Get the final score of the password by multiplying the entropy by the penalty
    final_score = password_entropy * find_sequential_chars(password)

    # Return the strength of the password. 35 = low (0), 60 = medium (1), anything above 60 is high (2)
    if final_score < 35:
        return 0
    elif final_score < 60:
        return 1
    else:
        return 2
