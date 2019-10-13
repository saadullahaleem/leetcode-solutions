class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        o = c = n
        result = ''
        results_list = list()

        def generate_parentheses(o, c, result, results_list):

            if o == 0 and c == 0:
                results_list.append(result)
                return

            if o > 0:
                generate_parentheses(o - 1, c, result + '(', results_list)

            if c > o:
                generate_parentheses(o, c - 1, result + ')', results_list)

        generate_parentheses(o, c, '', results_list)

        return results_list