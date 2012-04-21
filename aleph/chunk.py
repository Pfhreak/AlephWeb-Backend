from utils.bigendian import *

EntryData = { 
  "LINS": {
    "entryLen": 32,
    "packString": '>hhhhhhhhhhxxxxxxxxxxxx',
    # Not entirely sure what all these do, variable names lifted from Aleph One
    "varNames": "p1 p2 flags len highAdjFlr lowAdjCei cwPolyIdx ccwPolyIdx cwPolyOwner ccwPolyOwner"
  }
}
class Chunk:
    def read(self, file):
        self.tag = file.read(4)
        self.next = readInt(file)
        self.length = readInt(file)
        # TODO: Not sure what this int is used for in chunks
        file.seek(4, 1)
        self.entries = []
        
        if self.tag in EntryData:
            info = EntryData[self.tag]
            for i in range(0, self.length / info["entryLen"]):
                record = file.read(info["entryLen"])
                val = {k:v for k,v in zip(info["varNames"].split(), unpack(info["packString"], record))}
                self.entries.append(val)