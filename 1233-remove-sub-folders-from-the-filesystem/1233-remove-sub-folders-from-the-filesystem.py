class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderSet = set(folder)
        res = []

        for f in folder:
            isSubFolder = False
            tmp = f

            while f:
                pos = f.rfind('/')
                if pos == -1:
                    break
                f = f[:pos]

                if f in folderSet:
                    isSubFolder = True
                    break

            if not isSubFolder:
                res.append(tmp)

        return res     