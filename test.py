FUNNY_WORDS = [
    "poboy", "dobby", "cuppy", "hobby", "pudgy", "cocky", "bawdy", "miffy", "foamy", "jazzy",
    "caddy", "jaggy", "muddy", "jumpy", "duchy", "poppy", "yucky", "bumpy", "biddy", "choky",
    "fuzzy", "buggy", "byway", "gaudy", "dizzy", "moody", "muggy", "gabby", "dicky", "doggy",
    "wiggy", "hooky", "kiddy", "dumpy", "waddy", "guppy", "woody", "doozy", "giddy", "mummy",
    "gamay", "piggy", "divvy", "gawky", "bobby", "woozy", "ducky", "buddy", "cooky", "mommy",
    "dodgy", "middy", "gummy", "kooky", "jiffy", "humpy", "picky", "comfy", "puppy", "muzzy",
    "copay", "cabby", "gauzy", "booby", "boomy", "mammy", "boody", "pommy", "zappy", "yummy",
    "wacky", "jimmy", "hubby", "bubby", "paddy", "pappy", "goofy", "cubby", "goody", "juicy",
    "hammy", "daffy", "kicky", "zippy", "pawky", "biffy", "hippy", "baggy", "howdy", "cuddy",
    "daddy", "dowdy", "dippy", "happy", "huffy", "dummy", "foggy",
]


def filter_misplaced(wordbank: list[str], target: str, unwanted_positions: list[int]) -> list[str]:
    ans = []
    dic = {}
    ans2 = []
    for i in wordbank:
        if len(unwanted_positions) == 0:
            if target in i:
                ans2.append(i)
        else:
            for j in unwanted_positions:
                if (i[j - 1] != target and target in i):
                    ans.append(i)
    for i in ans:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    if len(dic) == 97:
        ans2 = wordbank
    else:
        for i in dic:
            if dic[i] == 2:
                ans2.append(i)
    return ans2


print(filter_misplaced(FUNNY_WORDS, "y", [3]))
