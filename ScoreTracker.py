class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "C":
                scores.pop()
            elif op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(scores[- 1] * 2)
            else: # Number case, convert to numeric
                scores.append(int(op))
        return self.listadd(scores)
    
    # Helper just for some complexity
    def listadd(self, int_list: List[int]) -> int:
        total = 0
        for i in range(len(int_list)):
            total += int_list[i]
        return total
