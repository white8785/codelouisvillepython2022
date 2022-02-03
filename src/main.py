import random

# raw output from Google's BigQuery
# later to be replaced by sqlalchemy query to Big Query
topnfts = [
    {
      "address": "0x06012c8cf97bead5deae237070f9587f8e7a266d",
      "tx_count": "4895135"
    },
    {
      "address": "0x06a6a7af298129e3a2ab396c9c06f91d3c54aba8",
      "tx_count": "646168"
    },
    {
      "address": "0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe",
      "tx_count": "442927"
    },
    {
      "address": "0x1a94fce7ef36bc90959e206ba569a12afbc91ca1",
      "tx_count": "180701"
    },
    {
      "address": "0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d",
      "tx_count": "147728"
    },
    {
      "address": "0x7fdcd2a1e52f10c28cb7732f46393e297ecadda1",
      "tx_count": "119608"
    },
    {
      "address": "0x8c9b261faef3b3c2e64ab5e58e04615f8c788099",
      "tx_count": "108286"
    },
    {
      "address": "0x2a46f2ffd99e19a89476e2f62270e0a35bbf0756",
      "tx_count": "101077"
    },
    {
      "address": "0xf915bbfbb6c097dc327e64eec55e9ef4d110d627",
      "tx_count": "78763"
    },
    {
      "address": "0xd2f81cd7a20d60c0d558496c7169a20968389b40",
      "tx_count": "60858"
    }
  ]


class Project:
    def __init__(self, address):
        self.address = address
        self.tx_count = self.get_tx_count()
        self.rank = self.get_ranking()
        self.name = self.get_name()

    # temp solution to shortcut the evaluation process that will be added later
    def get_ranking(self):
        return random.randint(1, 5)

    def get_tx_count(self):
        for project in topnfts:
            if project["address"] == self.address:
                return project["tx_count"]

    def get_name(self):
        """
        Static mapping until API calls are added

        returns random name for a project
        """
        names = [
          "BoredApes",
          "AlienBoys",
          "MutantApes",
          "Doodles",
          "Azuki",
          "CryptoPunks",
          "SavegeDroids",
          "TheFrontier",
          "TheSandbox",
          "Decentraland"
          ""
        ]
        return random.choice(names)


for project in topnfts:
    current_project = Project(project["address"])
    if current_project.rank >= 3:
        print(f"Above the bar: {current_project.name}")
    else:
        print(f"Below the bar: {current_project.name}")