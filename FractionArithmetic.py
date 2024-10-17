class Solution:
    def fractionAddition(self, expression: str) -> str:
        # All fractions in this returned list are signed
        # So we can add them all together
        def split_into_fracs(expr):
            terms = []
            l = 0
            r = 1
            while r < len(expr): # l < r always by construction
                if expr[r] == "+": # ...a/b+x/y
                    terms.append(expr[l:r]) # append a/b to terms
                    l = r + 1 # l = x, r = y
                    r += 3 # since a fraction is guaranteed to at least have 2 
                            # digits and a slash
                elif expr[r] == "-":
                    terms.append(expr[l:r]) # ...a/b-x/y
                    l = r # l = -, r = y
                    r += 3 # Can always guarantee that if we just encountered a -
                            # there are 3 characters that must follow it, at minimum
                            # since a fraction is guaranteed to at least have 2 
                            # digits and a slash
                else:
                    r += 1 # Have no information so check next character
                
            terms.append(expr[l:r]) # This final append gets missed since r reached the end
            # And we only append terms while we're in the loop.
            return terms

        # Least common multiple of two integers
        def lcm(a, b):
            return abs(a * b) // math.gcd(a, b) 

        def frac_to_ints(frac):
            i = 0
            while i < len(frac):
                if frac[i] == "/":
                    break
                i += 1
            return (int(frac[:i]), int(frac[i+1:]))

        # Add fraction exp2 to accumulator, exp1
        def frac_add(f1, f2):
            n1, d1 = frac_to_ints(f1)
            n2, d2 = frac_to_ints(f2)

            # Formula for adding two fractions, valid for negative numerator too
            # First we treat them like coprime: a/b + c/d = (ad + bc)/bd
            # Then we factor out the greatest common divisor of the numerator and denominator
            # Note gcd must be between b and d.  A and c
            num = str(n1*d2 + n2*d1)
            denom = str(1 if num == "0" else d1*d2) # simplify a net 0 fraction, edge case
            return simplify(num + "/" + denom)

        # To ensure the final fraction is in simplest form
        def simplify(frac):
            n, d = frac_to_ints(frac) # Extract the GCD from numerator, denominator
            return str(n // math.gcd(n, d)) + "/" + str(d // math.gcd(n, d))

        
        terms = split_into_fracs(expression)
        
        sum = "0/1" # Start with simplest representation of 0 as an addable fraction
        for frac in terms: # Accumulate all our terms
            sum = frac_add(sum, frac)
        return sum # This should be our final result in proper format, simplified fully
