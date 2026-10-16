from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbours = defaultdict(list)

        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbours[pattern].append(word)
        
        visit = {beginWord}
        q = deque([beginWord])
        output = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return output
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in neighbours[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            output += 1
        
        return 0