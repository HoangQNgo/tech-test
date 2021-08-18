medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def getScore(position):
    score=0
    if position=="1":
        score=3
    elif position=="2":
        score=2
    elif position=="3":
        score=1
    return score

def createMedalTable(results):
    myResult={}

    for result in results:
        print(result["podium"])
        for position in result["podium"]:
            score=position.split(".")

            points=getScore(score[0])

            if score[1] in myResult:
                myResult[score[1]]=myResult[score[1]]+points
            else:
                myResult[score[1]]=points
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    return myResult


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

def main():
    createMedalTable(medalResults) 

if __name__ == "__main__":
    main()